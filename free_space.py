# -*- coding: utf-8 -*-
# HKD OBFUSCATE v4 - portable source payload, no marshal/code-object dependency.
# Protection is import-time only; protected functions have no per-call wrapper.
def _hkd_v4_bootstrap(_g):
    import binascii as _hb
    import hashlib as _hh
    import struct as _hs
    import zlib as _hz

    _b = (
        _hb.unhexlify('fe8b22f57a3834552949d8fa307df8517751b28f075b43852d9dc3e586134b49ca69976cbf7fa1efa1c959182c1871c09c1b56b9943b42f89e3d40fbbac79bec462c371da56535ca68091ccd41a3f9ce11c797f3bbe5c718f1e59d5ff292e0d3944a42d331cbccc0d6e4120d10e8395e2ddb3e49be257ead24ad5e2da008ef19'),
        _hb.unhexlify('22ce7652f63c44624713934313f774ea40830a210986e57c55abd7476701bf8f49146bfc6fdcf584dab356012918d4a4f5bd3cefaf75efa5f68dc1050bf3d9dd9b2bfc01f401a8587a83154bde8afd1c8a12efe5f12a6c15a20dc5ae1f1b475bda6b3e0b505d2991883be8a8c47e6ec865339ad12f0cd2b4cb4e619ae59b8c4a'),
        _hb.unhexlify('55df3cd99d8818d73c04fff8d1c6188a4d00981ee79b6724919012cd21188e8ac5a3e8cd41ff822e23533693dd3614dd4ecf86978c4a791c9df0daa97478fcf7e6f2491c63854acad41451ac70c4da544d04ed5d09b78abe3b77cc77575bb87ffa570974db33f65bc1062fb47d4d1f4fafc86291e49c827bc6cc245b291eea0e'),
        _hb.unhexlify('33f49cd8bcae4585920e1f14f7494d2fbca0088828d9d5fc0aa12a84f014e21a3e65a9a1d3bf5e2c80d4162667c2a1590a56005db6a8e9a5b3246723e635f7a2d229c24409e9f41878223787186116841d80badb384562ac19ceb583b3f0173dc40f044755532d9077fbf12fc6595aa478e5c63c1e668d3a0582689bce6ef110'),
        _hb.unhexlify('3730e54adac23bb26164f358ed522d5218c245c3c5cef241169d7f35903821f1c36d5723cc7361518a06f6b6d119f7bdfc7980c5d5bd6e0e573eb088776b78dffb3b880ba8a5a4caa1c8577fa3a18266d37621ef955e1376ef568f23aefd2584deac17db3cb0b308c27fdd4a4212fbde24642597a32170c857d8f808b6944304'),
        _hb.unhexlify('7e9273838f31c96bfdf57ee0927ddef4ad1bc29bfdf56ae30bd3de064580187b4f15c03edb41cfc737f241fe8e5acb6e9d0c30a710ae7b57ee302c2067a4cb515be0f4882eb453ec38fe71d8720c96fa38f0058a10559d72da41506a17d6fb3d6a77b5fb6939baf27bd5a3b6dffe9c50096d0caabcbf65e52ab4d196544f457b'),
        _hb.unhexlify('b5648e91f5a3902dd69f5a830c6163cc7f6890529280ff9bc78f184faa6b520da511eed79ec27932a564409531de51099ac5d44e8563ce3602ee13871ec80f00fb16876eac0fe0f8916fd8781668e53c2cebd0b83f2ec99916c50d0880632da65df1269e4cbfcfbce81fe6f7f0bfd526acdd0efea9255f8800ce5135b33ca5cf'),
        _hb.unhexlify('3b13ea345dca88ebddee8b0303412592180bd8b70038f666a36d50fcc701d5726e4459f908575f629d1a2f9f70e81732eb84634f9f35aa5d7e395d61753d889276616357d54b4973b6742f296dc7eb1b993267be507e7e4178288059b3cd6f818f7f72470a6886a7ab4e43c8dedf720746d03c8fbf4c37167781f64b7ecbbc31'),
        _hb.unhexlify('d1fe9a91654a1d4c15dc3eb88f8f8d9cbe1f4ba2a3aaf28992c4e945a60bef873fd7d3eeca61c6e2717b37ee41c08db6e38749b2a3760534c8f9c60f74483df167a117d381e18cc1c1b1edb4959c0c4a25eeb0db0e608ab81fbb75e5a0caeea38dc69cd353f69e8782bd283d32be163fe32966a26e62b1629c77acf32b355c79'),
        _hb.unhexlify('da64d1e3ddb620cbfcc0770140b7737128df306030db0f4cdd2029dc1fa3ac00b40f01409867cf0c29e406c7fffa7df768cfe699e645f04ef93ae20694f3646dedba6a3ba8442fe4e7257542627ad18d1fee8c852e5b9b12d8b3d160aded217077a9906b007a59217ebb91dbc59651d95d3818fb5673157f2e09b0a9a2b00eba'),
        _hb.unhexlify('85819629e33ec02efd4c61d0e66b203a2124eeac13d92a72917a5ea44d3601f240967e776a5c1fad05975d21eb2d9e65bc8a42245d26c48b7aa776d0769d98ccbf83a5818f919c5cf6b19407def69d3405b909c8e44b38e6ef791fb442ebe5cfeba4f6b113321bfff0ca83f66af2efda5d2e6e4e0bb393f4795b96c47a90ea7a'),
        _hb.unhexlify('37e7d1e4977a790a21bfb9d11a508e5ed39e73a00a9ded0bb251067209fd977265673651f3c2789d8a19ea993520bf26c60b83bba233bd43502ee99f4c8c3031fcb9d5116fb65aacbf876dca4a10229caae098d58647978bcf663984fa228df6339a06cd479d7d4d1a4ddaac0ff2fe0c2488af0f7d52037a1aa9c1bf6beca2df'),
        _hb.unhexlify('548fb3f2966271c366d15d4cc067ed28a89e9bfa38f67e99d6ff0fca7a9de4a18529238e0044aabaafd2382f65720788cd365235ace2b853a73a385de2744452b16ec5588427f521cafa68aab990ba0fc75f3be3690b22bb5913237a4638b88e86658b75938858fb388f3b9dcec6167de9326ca8594d9f0db53d57e4d9d375ac'),
        _hb.unhexlify('7878cea59c63fe72b21a2cca4371052b95f92f842ec42907a680e62f097bef760ace187618d66a38cbb9b69dc84c4031f59338afa6373bd486682ebf5e624e5f0df7082875e7db63016d3e87e30c30f430b763696b69491d2400e5ef94f369a67e28ab76423c7a0838334b58d0be1afc2679edfb87b35edbb3a32236c40e1278'),
        _hb.unhexlify('9480437d8e129a26a669bb8bf7cb557f2a2e49dc95ed7dcb6a63bc0b0c70765b2b18dcaab78bd8b375d907b4ba3ab79565c9a80bb8a0adba186c8e8107c20cffaef1fceafa927e441b913e40bba05ad5142f477b779ffb3ee7c6e80c4b9e313d832ff5ae9bf802fa1621bf22b1a4b719a38e41df4aa7253a4ca19164a4f6be7a'),
        _hb.unhexlify('21113afa213a87d6b2b614d95b'),
        _hb.unhexlify('3e4b96c3a7687f449f2cfc50c1f87d9f93e60a79e65add507dfa7e867821751efb41570ae83abce635ca19726748ff32174b255152b7f5c6050e25f408fa4d028ee4b80fee905bf0c2ee3f3debea76cba4bf85ed5cedfeeb63495041aff23d2c9860d35f7ecb73f88e80b3e268bab915e71bab353803eae272fba931a707c530'),
        _hb.unhexlify('8d4bdac25729c3636f942de550911c2997b5f3726e49af3baebe71867a12236c431514752e37b017606644038410429a9f066f22bb73269dbc64ace9174301ecd01bcf052baaa1819397293b3368e05cf7fdd78db9e2e69a486508f5fd82e197dcdee7dd78300001de02a56e62d5bf22a93691f0e51e7c607848598ad6c96801'),
        _hb.unhexlify('aa722564d08bdfc979b21d81a59a7d2f89ea8f5f74d38faf23081299af64624d675304aeddf48898a2109977c025434b1eed81be4c196a8cd9be11d1f966c8479e63444ab88eb5c4b3f63977edad682fafdda2111e4020214b50d8534179836d11c67df79c4ff1bda9789ad30ac95fa95104e5519705961a7ece783b5384fb1c'),
        _hb.unhexlify('d258411d7e18aa483054993c2c44f18c2f3e79264c7a20becefcc306e576b207a5a1bf7ab0f4364d8f622f169180f7f943d75b0912d3e1c603eb0829c082b383d4d338e31b08836ba3584c534a809248f487024ed9d57f5f379a81276e19df06185c8767908545a501d10c26a82d5e9a1ede4d9c9bd3291bfecc9bbd42abff13'),
        _hb.unhexlify('b1224e80c8009b1d5234c912a1a07edca564627eb449d6bec3cc81afee242328b70a6d5aa0727659d5f5d131cf15c97a934db5a11a62ac868cd92cacdc4ae51c288249b999e11a8ccbfae56991a42f1e116c5cb837eb9d0c9181ce3b43c307e41101559e56aa6226c15df74eb6e0eb42942908f3e126f2ad6a2b2f63fa13b6f6'),
        _hb.unhexlify('657e3373133df261b73202c695c1860fedf66175e690ed582f1a09bbd6a0a868e7aa2e72516840ccce1b0070558c855380d8ed1cfe67dc2681f07c2e4fc46cbe3485c09e74443edcc5b81df9edaccbc2d7f77a1c3f9f4da56a091ec447847921d5f9dfacc09bf41652bdc0a75dce733867fce153195825791dd7301577d7e02c'),
        _hb.unhexlify('b41ce3c3c96a19768fa2324f7d6035cb2948555fc49a7084273308f16cfb4b4e522b969632ce3bbb6525737f8c8e6c20fa95778265c1ba0fca44c46c03b71c2b4692923d552315c5da2cde2d64a464357b993b589a83d9941fca5ea95a9f4973fa5001fe0a35567bc91670747384f4c03c85da504d0fa2188cce1c042015487f'),
    )
    _inv = (18, 4, 8, 13, 12, 20, 0, 21, 7, 17, 10, 6, 2, 9, 19, 1, 22, 5, 14, 11, 3, 16, 15)
    _leaves = (
        _hb.unhexlify('ad924e06dfd4024edd77a587900d9a2993ed57230f6c84f79236e7a377191c62'),
        _hb.unhexlify('71960331968adac6e5cebc8794989c170b346a79f8b2af1fe8ff82c6c7d77372'),
        _hb.unhexlify('2adf093c6793e56501b05c439da601f504c1aa6498813d30a4755209646e5544'),
        _hb.unhexlify('c8d22c5de87f3c64cfbe18db0ef1c3c797498d0afd3080697998cc3c1534f16f'),
        _hb.unhexlify('0ef1076645ba90ee46f05f8690a60ad472cd9e8ef2d41d75f87a49384a388e31'),
        _hb.unhexlify('0bb59b6f1b647ba31156880b64a111538f972a458b9b8d040b1d7dd5a84d8255'),
        _hb.unhexlify('2f7b7dcb5a1bd4f552d8eb072606f980a48d377a76b950b88733548c4ffd2135'),
        _hb.unhexlify('1e610012d19de6c65bf40789f70f1c483da995943e8c3dcb63783280b3bd48f8'),
        _hb.unhexlify('c12ffb9ba02be7fe193c5aa25c383374487a7149fcfe447ece21c3410e6a0739'),
        _hb.unhexlify('7e842ca566d44dfa8ae1f165f286acd6bcdcfff00a2f44a8e6f2dff393d06d4b'),
        _hb.unhexlify('4849d18942026340f8e2e6703988a6c473a14cf262eaea29b17214c1fb50cde8'),
        _hb.unhexlify('bf8551ebe3fd1d245d60a3f8442eab283921c74c8f48d7c5c540825a05a0b57b'),
        _hb.unhexlify('6d853d735dac7d9597f022c8df5c148b5fb7314b6df67b3c98d4ade4a0e1d265'),
        _hb.unhexlify('f786961a91b0e579d041769b503c1242501f90e3520962a9039ba346e7833422'),
        _hb.unhexlify('c27a413087167f6e91b2c5d6b7c4ead474719f2879b88b02dea8bbb5e65e7e0c'),
        _hb.unhexlify('cbbb5a214af9832678fded2f30b788b5a098a2bc88548c20cb872907d16fa299'),
        _hb.unhexlify('824109bdde7f06ab1542cc58a66388c882d7174f116e0771df97fe7f4acdc476'),
        _hb.unhexlify('6e98e9aa384d656128a381a6bf1c0d302fe1dfdf9f463b6855f9890a6d232507'),
        _hb.unhexlify('469c88631b3603e21182f64decc125f51be99ccc58a02b88c7fb37dfe63585be'),
        _hb.unhexlify('f3c40966185457c0a8e0212cf4d146d2a8e773493ce4694c570d0fad92dbf84c'),
        _hb.unhexlify('f1333a9c8fe05df25cc04324556fce3d281771512f9217cd68557af92c72a9ae'),
        _hb.unhexlify('75786dd6e335b205f8c3f65d1d9228fd697779cc9692642e0e9685e861836c16'),
        _hb.unhexlify('0bb24370e444b11e8c2b6853833649be837a3380a46c0e69e23977b76299ae9e'),
    )
    _root = _hb.unhexlify('36030bdd2ec2894d63114665c2f78d58c624233c113a16bee3ccd7572c575d04')
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
