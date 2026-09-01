# -*- coding: utf-8 -*-
# HKD OBFUSCATE v4 - portable source payload, no marshal/code-object dependency.
# Protection is import-time only; protected functions have no per-call wrapper.
def _hkd_v4_bootstrap(_g):
    import binascii as _hb
    import hashlib as _hh
    import struct as _hs
    import zlib as _hz

    _b = (
        _hb.unhexlify('83a7385f502810354461b457a557d8ed0ebb7be13ed4fa66754349ee795b242bb7c74c605b85c97c54d4cea92a2982919a9f2f6ee99cd08850d04ef486565ac270781b1a12c36dc678b037b0d7a350323063d9b5e309fa9bec68e40363dce5835b925053961a3b4d0b1a657fc977fae80e22a6a527582b851ad95696d0e0571d'),
        _hb.unhexlify('287aaa7854fc85de7a793862e4fb9fb79b77e666e0eed50f8e382c36f4840a3e8e400f17aab675610ac9efea4b252ae36c75172e5a08fc6f5e0ffa6fc28aa9217302f2a92b70559bfcab2a0820e9fe05633a160570609151b85952f3ce52aba9282a3711773350fbc7030255bf4e4ccb7da8f7dc30c48f4140b6c33e4493c59a'),
        _hb.unhexlify('23a05683aaf5aacc5a9452567220febdc0465eba0ccc9221637c71f6ee6ca6a5e13fe779f6a7099b89583176966be632b20739bcbc62ebf958fe8c04fa7499ebf226680490413e0809032acbb5169ebbf579161d5ed8c63f5fd8f1eff187b02942536d5337a6caea90c1840fe7f3243fff9fbcc7a2b30b8a4d576a5025467731'),
        _hb.unhexlify('778083388cb5d9e05bcb50257952a79e979e1d8dc947efd341dafbcd9f68c91bf24b8056695c644d0a18cfa35867616e39b9a65f2776272139a3722ce0c05bdf2ad63d482a93736a1f345c8400ebfbcfb207b7187288a46ea0164f5a0d44071ef3aceaa4af354f41e18700a2e705f4b40ef64831e112d7a783820d342b616f21'),
        _hb.unhexlify('0d90d8006dae41b13e70eedd6c4ec4dc31c4b2efddbb3a71917e4f4121f9320ba4f2b53a72eb5fd573c6bec6cd63fcaad4805e9754a7e79b8cacfa0bf158ab73953c09ca5b8f56802b668e0979132f2f191aca4cc95864ef6cbb3b25641d76416bc99feac01bee2224658b37c738956f6a6abbbdcd84a76426318f2009572727'),
        _hb.unhexlify('0186ed87d0be656c057ace886374004bbef753d240bbfc9f71390c0f2532d6113785f5ed9b440f81eeee3490720af6057d0d7f713f9db7d5a76d4dd94da548527877e6af8c19111980f9ecbda5418129b5ee4169c8a86b9d41b2eab89a35df2841e637d8d0a5cf18beba05f583b679dd42b935e9eca1243fd3d5cdec0a0186aa'),
        _hb.unhexlify('c211ff14347d2eef27c6dbbca05fccf228dc7476142b8a76179f566128bbdbe1657b381d586b5dd2f684ab36c98f309427df8075a0c275723de2a625778c98930cf3cb1494ab512bb16316d77efeca57f08595884abf844cfa0515fda1f28609b52f1daedd2376bd418e57dfc3bd14dfb2d94c5a978a6f99eb0c04085fcd9079'),
        _hb.unhexlify('6aeb7155c0c9e3db200aa443d919fdd49bcaa05c4f878c4012e391636d1db6376328b99c5bc7c70da19af1b952e7e2b69074bb5a724643bbf3f7fe9b69393f1a3167d3ed4eb45089f301b3f19976addc55efda3ed7c521dfedd8f4ef616af8adfab7edd4387ccfc7dcc02a247b2857d7f97894d16406c0a9515a727a86dfd3d9'),
        _hb.unhexlify('3e52299043af22af320dda3f51777d19b553518e414c980ee4ca70f70aa0b2d1ec3bd1f339ba3d3b5e8b6b680b5eaa0962d6b30cdb8ce4d6847c2c4ca548024b0e5e7faa4bc55b92723e2cf16c6c90eeb599e7be62a6ed603b8e111a742821f800a3009dd14d5c92204111a8c2b8e44bf7c913c6238fdbb93e40fb3aeb43543f'),
        _hb.unhexlify('4294655ba02f2b277513bb60cd7786dfcd0326559bbea23400220dc59e3fc0a569c4f74069c4c124c76b3d598fc138c54fa10aafc2605d4b25a043142c7e30bc07d426605d8d5b6225713bfe64c906c8ca56155d78e53483e12c898542e2d036db7e54db0e2704fba5d6de65854dbaf72f5e20ad1d9d163f7b458b05e94b5ddb'),
        _hb.unhexlify('6f3fb8701fab1061a9b59553da09399eee22a63f900289bd388f48f114b7fddb98454469b5fceeca422c0aa8a02c5b17a0b49165e6fff4037fec52595bf2f7ff1cf03e5855b03cb6856d83ee2b7fc62ed906d2aee45e3a7de69d8921308fb9bc4222a638addf27ee51ac6f97520dc7fbc6f9689f7aae4f8501309088efe87397'),
        _hb.unhexlify('aff056b3ba09c4a31d53198060e00326b923e80d625d07d2d4a974e8a9f1b548de930efa56f7568f0014cf74136f7605671ed57299c7a468f9cbb462f47c3b5d467caa47de3ecf190ab2e900792651b598f020ce65433c628c85d94591768c142de49a4434b1d2db68e8a8c1c4d56b9b128df78e7579a48e202a9dc1ace7a508'),
        _hb.unhexlify('67189472f138ffe023a586fb108c6dd564a0236602c28c5a148310f929f7e24f93b6e87f86f6f6fae4a2a246c2a28b38160d18762d88c10a1e575456fba91a1fa5b80e082653e608e59ed69af849b0db21d74039067f86d3d765d67df043c25bab8a6c9ea68d3da7660d4f87b1acb4ed6c750743f55b565e4175f5b426a7b8c6'),
        _hb.unhexlify('3e3220e89510c193ab57a2c796986ca3c298ced5193dc914e8676cd4a1406f1ac60e21b34820ccd65f9c56cd99285bff7242da6aad415fd0bba975cd55dce4dfbd9bb0b2999a11aa63472b7179b33bed00cbcd6b094834356048f66151618da7212b99bdae311daaae1c570e823658031c1b9f608526b8537539eca9a2e132c2'),
        _hb.unhexlify('074c88ffe673bb96b8997e7d46a8a215856ed2a45553fc65de0160696f75a351e6a95a4847392cec65936c0d298930fcbbb42d18676e980e3db4b27fbb91c24ffbe2851ff0e681259321f6f03f93f40788a2bf56e59d57f659a645b7e41ee266b910c4b2d3782b8dfff8f571321ad340c4d4271c75867b655a3e9b2a89711d2f'),
        _hb.unhexlify('982229bba3c64a59db6a1c22eec5bcd1c0dd012b16899138ad4a901bbd960f12c8f2786ecd1675555d351ce07d1437cba1ce0bf3c1cfd12df3c5af66bd3eb42f31668c64cd4b1cef85273ed45bcb0f63d0f7d8'),
        _hb.unhexlify('7fe14f36793314bd9acaed5708d369dbb81e9306159e09bd525126691a4b36c943b640e5f76947ded1d4e3267cd21cde874003af7542cf8c4a4dd072f0575bff90f2e2abbcabacb7b2dd6b81f47ddd6ff3fcf123c2f0cd894aeb9cd0a1e7e61196b53a7064d1051d60683d0309b0de9521c847b464c2122b37a3f739cca09859'),
        _hb.unhexlify('5a0d2346782170b69a847419a95b5ae71fc18b64b77e8a1e6b3d1e66e99f66070e174d0514be6ac3308ffd7d1c90322b104b03e92b22d9c9b7d14160b8ec7ea8f7aa2045f823715673028573e200a316149417ef8e9b792e4bb226f1ab72ed9214cbb412c7d8325188f0ca6e1227348a68252875a240cc1d56e3b18c5ba8d270'),
        _hb.unhexlify('167dcbbf4bfb9165aa2240d7461ac8d0cbd467c71adfdeb9b7e96365c8a7b4056cece179c210a44afe0de585c6970556b983ec91057bd5c930bb17972403cc41b2b4fa0275e5a02789e74845aa0afbdfc7c6e28f66446c83154d1e8984fe3a92279fe865486b52985485285fd0cfa5b1e275a89735d9e629215b90f46f6c7a7b'),
        _hb.unhexlify('cf5c15c7b5028f61cf31f67d1fc5bb14eb91c94b9a71beb3f89577200efc1e621adfa13a38ac89b0f099faf90acf13591f785d146401bed6ec90f52a53db5017a9ba25de1d95b22dd7beeb4c12cfc1cd13a1302e15995280ae1f63060923e96ca4623918c02de9bb908261c7e5f51478f8f460b94e9f341fed3841a46ff8f5ac'),
        _hb.unhexlify('aa727d647296dfc9653215698466adf5ca416e7bfd7f87617a220b84b2bbff39d060898499b04a423ee605c2bb93849d264b7e7889347e7e8260d2fd8266682151e385607d7e5cb82764600c78cd4e5e2d18ac3f19c357e6150655ab7c8f05ccd00f5668852744ecef19310caa41476849701336bc80cc2a6acb33478958827c'),
        _hb.unhexlify('a9634806cd50631309dc0dadc52097599874437997b3509eccdc6711132ae4fe8dd1242e9a11b1cb78b8d64d21aba8c7eddc56534ec09ab83d81b222a80608c69e705bbaa9afee6bde0d22ae0499642c6f0a6163aee40a4aeb0ac6e9a662fc4d4af76a4b37404a30bcc15007f1caee668b82787aeb530880d27a6f193bac2615'),
    )
    _inv = (20, 21, 3, 10, 14, 16, 2, 12, 8, 11, 6, 4, 0, 13, 18, 19, 5, 7, 1, 9, 17, 15)
    _leaves = (
        _hb.unhexlify('061d3baee689ce6a79cbfbe160d73e48f88f0ddf0847936d91c8946e9e6a0b8a'),
        _hb.unhexlify('1c38a672369dc8c0b3db274084e66a6c07a9780e3fb42915d4f8e6e8d66b7b39'),
        _hb.unhexlify('51efaf3049c6be477c709f7073d26467d2ff4bf9ca9f16c4fab206c3fcb5601e'),
        _hb.unhexlify('f7d8526396f57c80695c963dd757ec84f010842723d660b0f3e69d686d158fbb'),
        _hb.unhexlify('1049c74947e407b53e6dcbfd527410de6050676e3c8506cd7b295355b9fb2b08'),
        _hb.unhexlify('52d725f33c5e69457116299d55cc5be4ac2dd03173821f319f31f65a720e9dc6'),
        _hb.unhexlify('efa6d6e15ba53bcc77a30b7265f10c98df954bcf74e51f033f02e2ddca648d89'),
        _hb.unhexlify('e8538cb0806c138bc817152a63ebd810531796675c760cd32dc48c4fdff03da6'),
        _hb.unhexlify('34ec9b9501bd4a8ac7a372ed2f88f0a55adf1f219c1dd56458d341ad8529e61a'),
        _hb.unhexlify('a754be3e60080982e722656a963ea86837f0a17da0fac1cf469ff76f7c5eac0a'),
        _hb.unhexlify('ce20b575f5c919075000267b9e5d208c17208060c8f854e09f8116c6c52aa997'),
        _hb.unhexlify('c50a8e2333359b16e09845d38e6a243be9a4294a4806c63093834e435eed78f7'),
        _hb.unhexlify('8473369e79eb8b3b81f92988fa6a1920111b07120bcb89be1a2d285ae3e638d1'),
        _hb.unhexlify('4506d3edde79aa9b34edc38d6c8a83fc9d995bd625022ef41062cf005f22a7a4'),
        _hb.unhexlify('86f90a11b6617d2a6c40c4189e51c368c9a40121566b092a65e969eeae5a9c32'),
        _hb.unhexlify('89c26f66551580176baea8ccea8a6819a8a7227f11258cd0a493612a95fde6a1'),
        _hb.unhexlify('3aee9459d01eeb0479960eecabdb26d62952cc2d08f1b4e95ff2c46776299d10'),
        _hb.unhexlify('5cbeeacd47dc4c456d041a611f7edbc0402c70c0d110b2970dc198379e5f7c77'),
        _hb.unhexlify('91728ffa6cc2e79ef38d5711a2a577a65fb8d350af4c6bd02c4e1563dfc8a928'),
        _hb.unhexlify('c2c67c587711549caf9a526085d67420ebbae9965934b4f1113ac2fba82db322'),
        _hb.unhexlify('45a70d244cb7c434befe6ff7eafded839698a0450a3c8f465bca3b2d14dcc6d2'),
        _hb.unhexlify('28ce58af1173d60e2e4b324933b623a45c654ed72aa74b54f1a4c32ccf20ef9e'),
    )
    _root = _hb.unhexlify('3a17a9c15a567c1daa06b9781a3ffdc223c13ce4c068fbfbc5402852807b9eca')
    _share1 = _hb.unhexlify('55eda5f163d89abc0fa9ee2f50360fb8a1798cbdee89b7724aa601d666ef165c')
    _share2 = _hb.unhexlify('9f79c9c5af812421529d38fa0edc11dc26853438e917cd18eb1ba098b56c4e3b')

    def _u32(_n):
        return _hs.pack('>I', _n)


    def _xor(_a, _c):
        _o = bytearray(len(_a))
        _i = 0
        while _i < len(_a):
            _o[_i] = _a[_i] ^ _c[_i]
            _i += 1
        return bytes(_o)

    def _ks(_key, _index, _length):
        _o = bytearray()
        _counter = 0
        _seed = _key + _u32(_index)
        while len(_o) < _length:
            _o.extend(_hh.sha256(_seed + _u32(_counter)).digest())
            _counter += 1
        return bytes(_o[:_length])

    def _merkle(_values):
        if not _values:
            return _hh.sha256(b'').digest()
        _level = list(_values)
        while len(_level) > 1:
            if len(_level) & 1:
                _level.append(_level[-1])
            _next = []
            _i = 0
            while _i < len(_level):
                _next.append(_hh.sha256(_level[_i] + _level[_i + 1]).digest())
                _i += 2
            _level = _next
        return _level[0]

    _key = _xor(_share1, _share2)
    _parts = []
    _verify = []
    _i = 0
    while _i < len(_inv):
        _masked = _b[_inv[_i]]
        _raw = _xor(_masked, _ks(_key, _i, len(_masked)))
        _parts.append(_raw)
        _verify.append(_hh.sha256(_u32(_i) + _raw).digest())
        _i += 1

    if tuple(_verify) != _leaves or _merkle(_verify) != _root:
        raise ImportError('HKD protected payload integrity verification failed')

    try:
        _source = _hz.decompress(b''.join(_parts)).decode('utf-8')
    except Exception as _exc:
        raise ImportError('HKD protected payload reconstruction failed: %s' % (_exc,))

    _filename = _g.get('__file__') or '<HKD-obfuscated>'
    _code = compile(_source, _filename, 'exec', 0, True, 0)

    # Discard the plaintext string before running user code.  CPython may reclaim
    # it immediately; no plaintext source is retained as a module global.
    del _source

    # Return the compiled payload.  Keep exec out of this function: older
    # CPython parsers reject an exec statement in a function that also contains
    # nested functions/free variables.  Execution happens at module scope below.
    return _code

_hkd_v4_code = _hkd_v4_bootstrap(globals())
del _hkd_v4_bootstrap

# Exact module semantics: execute in the real module globals.
exec(_hkd_v4_code, globals(), globals())
del _hkd_v4_code
