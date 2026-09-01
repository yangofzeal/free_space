# HKD Space Reclaimer

## SYNOPSIS

`free_space.py` is a fast, conservative disk-space reclamation utility using persistent HKD-style filesystem state where available.

```bash
python3 free_space.py
python3 free_space.py --min-mb 100 --top 10
```

The program:

- Finds up to **10 of the largest reclaim-safe files**.
- Uses `~/.cache` on Linux and `~/Library/Caches` on macOS.
- Also recognizes HKD ffmpeg `.partial` cache files.
- Never automatically targets arbitrary project, source, archive, or media files.
- Refuses symlinks and revalidates each candidate before deletion.
- Displays the total reclaimable space before making any change.
- Requires an explicit `y` or `yes` before deleting the displayed files.
- Any other response, including the default `N`, deletes nothing.

### Obfuscated build

```bash
python3 obfuscate.py free_space.py.src.py free_space.py
python3 free_space.py
```

Designed to remain compatible with older HKD Linux/Python 3.x deployments, including the Python 3.4-compatible source path.
