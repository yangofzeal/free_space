#!/usr/bin/env python3
"""HKD Space Reclaimer 3 — bounded-memory, dry-run-first cache cleanup."""

from __future__ import annotations

import argparse
import heapq
import os
import shutil
import stat
import sys
import time
from dataclasses import dataclass
from pathlib import Path

VERSION = "3.0"
MIB = 1024 * 1024


@dataclass(frozen=True)
class Root:
    path: Path
    label: str
    confidence: int


@dataclass
class Candidate:
    path: Path
    root: Path
    label: str
    logical: int
    allocated: int
    mtime: float
    confidence: int

    @property
    def age_days(self) -> float:
        return max(0.0, (time.time() - self.mtime) / 86400.0)

    @property
    def score(self) -> float:
        # Polynomial ranking: allocated bytes dominate, age and confidence break ties.
        age = min(self.age_days, 365.0) / 365.0
        return self.allocated * (1.0 + age) ** 2 * (self.confidence / 100.0) ** 2


def human(n: int) -> str:
    value = float(n)
    for unit in ("B", "KiB", "MiB", "GiB", "TiB"):
        if value < 1024 or unit == "TiB":
            return f"{value:.1f} {unit}"
        value /= 1024
    raise AssertionError


def roots(home: Path) -> list[Root]:
    if sys.platform == "darwin":
        specs = [
            ("Library/Caches", "app caches", 98),
            ("Library/Developer/Xcode/DerivedData", "Xcode derived data", 96),
            (".Trash", "Trash", 100),
        ]
    else:
        specs = [(".cache", "app caches", 98), (".local/share/Trash/files", "Trash", 100)]
    specs += [
        ("Downloads/.hkd_inf_ffmpeg_cache_v2", "HKD partial cache", 100),
        (".npm/_cacache", "npm cache", 99),
        (".cache/pip", "pip cache", 99),
        (".cache/huggingface", "model cache", 90),
        (".cache/torch", "model cache", 90),
    ]
    result, seen = [], set()
    for rel, label, confidence in specs:
        p = home / rel
        try:
            rp = p.resolve(strict=True)
        except (OSError, RuntimeError):
            continue
        if not rp.is_dir() or rp in seen:
            continue
        # Avoid nested roots: the broad cache root already includes them.
        if any(rp == old or old in rp.parents for old in seen):
            continue
        seen.add(rp)
        result.append(Root(rp, label, confidence))
    return result


def inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def scan(scan_roots: list[Root], top: int, min_age: float, same_device: bool) -> tuple[list[Candidate], dict]:
    heap: list[tuple[float, int, Candidate]] = []
    stats = {"files": 0, "dirs": 0, "errors": 0, "logical": 0, "allocated": 0}
    serial = 0
    cutoff = time.time() - min_age * 86400

    for spec in scan_roots:
        try:
            root_dev = spec.path.stat().st_dev
        except OSError:
            stats["errors"] += 1
            continue
        for dirpath, dirnames, filenames in os.walk(spec.path, topdown=True, followlinks=False):
            stats["dirs"] += 1
            safe_dirs = []
            for name in dirnames:
                p = Path(dirpath) / name
                try:
                    st = p.lstat()
                    if stat.S_ISLNK(st.st_mode) or (same_device and st.st_dev != root_dev):
                        continue
                    safe_dirs.append(name)
                except OSError:
                    stats["errors"] += 1
            dirnames[:] = safe_dirs
            for name in filenames:
                p = Path(dirpath) / name
                try:
                    st = p.lstat()
                    if not stat.S_ISREG(st.st_mode) or st.st_nlink > 1 or st.st_mtime > cutoff:
                        continue
                    allocated = getattr(st, "st_blocks", 0) * 512 or st.st_size
                except OSError:
                    stats["errors"] += 1
                    continue
                stats["files"] += 1
                stats["logical"] += st.st_size
                stats["allocated"] += allocated
                c = Candidate(p, spec.path, spec.label, st.st_size, allocated, st.st_mtime, spec.confidence)
                serial += 1
                item = (c.score, serial, c)
                if len(heap) < top:
                    heapq.heappush(heap, item)
                elif item[0] > heap[0][0]:
                    heapq.heapreplace(heap, item)
    return [x[2] for x in sorted(heap, reverse=True)], stats


def available(path: Path) -> int:
    return shutil.disk_usage(path).free


def still_safe(c: Candidate, home: Path) -> bool:
    try:
        if c.path.is_symlink():
            return False
        resolved = c.path.resolve(strict=True)
        st = resolved.stat()
        return (inside(resolved, c.root) and inside(resolved, home.resolve()) and
                stat.S_ISREG(st.st_mode) and st.st_nlink == 1)
    except (OSError, RuntimeError):
        return False


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--top", type=int, default=5000, help="bounded candidate count (default: 5000)")
    ap.add_argument("--min-age-days", type=float, default=0, help="only files at least this old")
    ap.add_argument("--target-free-gb", type=float, default=5, help="stop applying after this much free space")
    ap.add_argument("--apply", action="store_true", help="enable deletion after exact confirmation")
    ap.add_argument("--yes", action="store_true", help="noninteractive apply; requires --apply")
    args = ap.parse_args()
    if args.top < 1 or args.top > 100000 or args.min_age_days < 0 or args.target_free_gb < 0:
        ap.error("invalid numeric option")

    home = Path.home().resolve()
    before = available(home)
    scan_roots = roots(home)
    candidates, stats = scan(scan_roots, args.top, args.min_age_days, same_device=True)
    selected = []
    projected = before
    goal = int(args.target_free_gb * 1024 ** 3)
    for c in candidates:
        if projected >= goal:
            break
        selected.append(c)
        projected += c.allocated

    print(f"HKD Space Reclaimer {VERSION} | mode={'APPLY' if args.apply else 'DRY RUN'}")
    print(f"free_before={human(before)} scanned_files={stats['files']} errors={stats['errors']}")
    print(f"eligible_allocated={human(stats['allocated'])} bounded_candidates={len(candidates)}")
    print(f"plan_files={len(selected)} projected_free<={human(projected)}")
    for i, c in enumerate(selected, 1):
        print(f"{i:4d}. {human(c.allocated):>11} age={c.age_days:7.1f}d {c.label}: {c.path}")

    if not args.apply:
        print("DRY RUN: nothing deleted. Re-run with --apply after reviewing the paths.")
        return 0
    if not selected:
        print("Nothing selected; nothing deleted.")
        return 0
    if not args.yes:
        answer = input(f"Type DELETE {len(selected)} FILES to continue: ").strip()
        if answer != f"DELETE {len(selected)} FILES":
            print("ABORTED: nothing deleted.")
            return 2

    reclaimed = deleted = failures = 0
    for c in selected:
        if available(home) >= goal:
            break
        if not still_safe(c, home):
            print(f"SKIP changed/unsafe: {c.path}")
            failures += 1
            continue
        try:
            size = c.path.stat().st_blocks * 512 or c.path.stat().st_size
            c.path.unlink()
            reclaimed += size
            deleted += 1
        except OSError as exc:
            print(f"FAILED {c.path}: {exc}")
            failures += 1
    after = available(home)
    print(f"deleted={deleted} measured_gain={human(max(0, after-before))} accounted={human(reclaimed)} failures={failures}")
    print(f"free_after={human(after)}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
