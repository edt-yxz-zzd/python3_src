
r'''
Encryption
strings and streams in body except encryption_dict
    [page115][from Errata::page4]
        Encryption applies to all strings and streams in the document's PDF file, with the following exceptions:
            * The values for the ID entry in the file trailer
                -- since optional direct obj, not in objID2val, I donot care it
            * Any strings in an Encrypt dictionary
                -- since I will remove /Encrypt, so I donot care, too
            * Any strings that are inside streams such as content streams and compressed object streams, which themselves are encrypted
                -- not to support
        Encryption is not applied to other object types such as integers and boolean values, which are used primarily to convey information about the document's structure rather than its contents.
    [page 120]
        Stream data is encrypted after applying all stream encoding filters and is decrypted before applying any stream decoding filters. The number of bytes to be encrypted or decrypted is given by the Length entry in the stream dictionary.
        Decryption of strings (other than those in the encryption dictionary) is done after escape-sequence processing and hexadecimal decoding as appropriate to the string representation described in Section 3.2.3, "String Objects".

    [page120][from Errata::page4]
        If a user attempts to open an encrypted document that has a user password, the application shall first try to authenticate the encrypted document using the padding string defined in "Encryption Key Algorithm" (default user password) on page 124
        -- PADDING_BYTES == b'' after padding

encryption_dict = trailer_dict[/Encrypt] -- exist ==>> pdf is encrypted
    -- [not encrypted] [direct objects]: all key-values [page 118]
    -- Security handlers are responsible for encrypting any data in the encryption dictionary that they need to protect. 
security_handler = encryption_dict[/Filter]
    /Standard standard password-based security handler
        -- TABLE 3.19
        /O byte[32] <<== owner password + user password
        /U byte[32] <<== user password
            -- see "Encryption Key Algorithm" on page 124 and "Password Algorithms" on page 126
        /P -- permission flags
format_syntax_name = encryption_dict[/SubFilter]


access permission
    owner password
    user password

#3.2 user_password+/O+/P+/ID_0+(/R+/Length) ==>> encryption_key
#3.3[1-4] owner_password+/R ==>> keyRC4
#3.3 keyRC4(owner_password+/R)+user_password+/R ==>> /O
#3.5[/R>=3] user_password+/O+/P+/ID_0+(/R+/Length) ==>> encryption_key
#       encryption_key+/ID_0==>> /U[:16]
'''
pads_str = \
    '28  BF  4E  5E  4E  75  8A  41  64  00  4E  56  FF  FA  01  08\
     2E  2E  00  B6  D0  68  3E  80  2F  0C  A9  FE  64  53  69  7A'
pads_hex_str = ''.join(pads_str.split())
PADDING_STRING = ''.join(map(lambda x:chr(int(x, base=16)), pads_str.split()))
_PADDING_BYTES = bytes(map(lambda x:(int(x, base=16)), pads_str.split()))
PADDING_BYTES = bytes.fromhex(pads_str)
PASSWORD_LEN = 32
assert len(PADDING_BYTES) == PASSWORD_LEN
assert _PADDING_BYTES == PADDING_BYTES

from abc import abstractmethod, ABCMeta
import hashlib, random

class MD5:
    def __init__(self):
        self.worker = hashlib.md5()
    def __call__(self, *bytess)->None:
        try:
            for bs in bytess:
                self.worker.update(bs)
            return self
        except:
            print(type(bs))
            raise
    def finish(self)->bytes:
        return self.worker.digest()
class RC4:
    def __init__(self, key:bytes, *, decrypt:bool):
        self.key = key
        self.data_ls = []
        self.decrypt_flag = decrypt
    def __call__(self, *bytess)->None:
        self.data_ls.extend(bytess)
        return self
    def finish(self)->bytes:
        key = self.key
        bs = b''.join(self.data_ls)
        from nn_ns.app.rc4 import rc4
        #print('begin rc4: key={!r}, len(data)={}'.format(key, len(bs)))
        print('begin rc4: len(data)={}'.format(len(bs)))
        r = rc4(key, bs, self.decrypt_flag)
        print('end rc4')
        return r
        return rc4(key, bs)

class DecryptPDF1_4(metaclass=ABCMeta):
    # for pdf < 1.6, no AES, only RC4
    # password : from user input ; ascii bytes ==>> bytes
    #   but to avoid confusion with key, I use str intead bytes for psw
    def __init__(self, encryption_dict, trailer_dict):
        self.encryption_dict = encryption_dict
        self.trailer_dict = trailer_dict
        self.n = self.calc_n(encryption_dict)
    @classmethod
    def _authenticating_user_password(cls, O, P, ID_0, R, Length, U, user_password):
        print({'/O':O, '/P':P, 'ID_0':ID_0, '/R':R, '/Length':Length, '/U':U, 'user_password':user_password})
        encryption_dict = {b'/O':O, b'/P':P
                            , b'/R':R, b'/Length':Length
                            , b'/U':U

                            # will delete
                            , b'/V':2
                            }
        trailer_dict = {b'/ID': [ID_0], b'/Encrypt':encryption_dict}
        assert type(O.get()) == type(ID_0.get()) == bytes
        assert len(O.get()) == 32
        assert type(P) == type(R) == type(Length) == int
        assert P < 0
        assert Length > 0
        assert R >= 0
        #if R <= 2: raise NotImplementedError
        self = cls(encryption_dict, trailer_dict)
        del self.n
        del encryption_dict[b'/V']
        return self.authenticating_user_password(user_password)
#3.5[/R>=3] user_password+/O+/P+/ID_0+(/R+/Length) ==>> encryption_key
#       encryption_key+/ID_0==>> /U[:16]

    #@abstractmethod
    def MD5(self):
        return MD5()
        raise NotImplementedError
        class I_MD5:
            def __init__(self):...
            def __call__(self, *bytess)->'self':...
            def finish(self)->bytes:...
        return MD5()
    def RC4_decrypt(self, key):
        return self.RC4(key, decrypt = True)
    def RC4_encrypt(self, key):
        return self.RC4(key, decrypt = False)
    #@abstractmethod
    def RC4(self, key, *, decrypt:bool):
        return RC4(key, decrypt = decrypt)
        raise NotImplementedError
        class I_RC4:
            def __init__(self, key):...
            def __call__(self, *bytess)->'self':...
            def finish(self)->bytes:...
        return RC4(key)

    def key_for_RC4orAES(self, algo:str, key:bytes, objID:(int, int)):
        # Algorithm 3.1  Encryption of data using the RC4 or AES algorithms
        # objID is id of the indirect obj contains the data
        # key from computing_encryption_key
        # I call the input key "the whole file encryption_key"
        #        the output key "an object key"
        n = len(key)
        encryption_dict = self.encryption_dict
        assert encryption_dict[b'/V'] in [1, 2]
        assert len(key) == self.calc_n(encryption_dict) == n
        assert len(key) == 5 or encryption_dict[b'/V'] == 2
        assert algo in {'RC4', 'AES'}
        objNum, genNum = objID
        assert objNum > 0
        assert genNum >= 0
        key = key + objNum.to_bytes(3, 'little') + genNum.to_bytes(2, 'little')
        if algo == 'AES':
            key = key + 'sAlT'
        key = self.MD5()(key).finish()[:max(n+5, 16)]
        return key
    def encrypt_using_RC4orAES(self, algo, mode, key, data):
        # key : from key_for_RC4orAES
        # data is from string/stream obj
        # AES (Advanced Encryption Standard) algorithm (beginning with PDF 1.6)
        assert algo == 'RC4' or PdfVersion >= "1.6"
        if algo == 'AES' and mode == 'CRC':
            # Cipher Block Chaining (CBC) [page 120]
            init_vec = random_bytes_of_len(16)
            args = (init_vec,)
            data = init_vec + encrypt(algo, key, data, mode=mode, args=args)
        else:
            args = ()
            data = encrypt(algo, key, data, mode=mode, args=args)
        return data
    def decrypt_using_RC4orAES(self, algo, mode, key, data):
        # key : from key_for_RC4orAES
        # data: data of obj
        # AES (Advanced Encryption Standard) algorithm (beginning with PDF 1.6)
        assert algo == 'RC4' or PdfVersion >= "1.6"
        if algo == 'AES' and mode == 'CRC':
            # Cipher Block Chaining (CBC) [page 120]
            init_vec, data = data[:16], data[16:]
        return decrypt(algo, key, data, mode=mode, args=(init_vec,))

    def decrypt_Filter_Standard_ltPDF1_6(self, user_password, objID, data):
        return self.decrypt_Filter_Standard(user_password, objID, data, 'RC4', None)
    def decrypt_Filter_Standard(self, user_password, objID, data, algo, mode):
        # if owner_password given, then call owner_password2user_password
        # user_password pass authenticating_user_password test
        key = computing_encryption_key(user_password)
        key = key_for_RC4orAES(algo, key, objID)
        return decrypt_using_RC4orAES(algo, mode, key, data)

    @classmethod
    def calc_n(cls, encryption_dict):# ??? from /Length
        # Algorithm 3.1::2 [page 119]
        # (n is 5 unless the value of V in the encryption dictionary is greater than 1, in which case n is the value of Length divided by 8.)
        # encryption_dict[b'/R'] == 2 ==>> n == 5


        # encryption_dict[b'/V'] in [1, 2, 3]
        if encryption_dict[b'/V'] <= 1:
            return 5

        L = encryption_dict[b'/Length']
        n = L // 8
        assert n * 8 == L
        assert n == 5 or encryption_dict[b'/R'] != 2
        return n
    @classmethod
    def padded_password(cls, password:'bytes as str'):
        # password - user/owner password string
        return (password + PADDING_BYTES)[:PASSWORD_LEN]
        return (password.encode('ascii') + PADDING_BYTES)[:PASSWORD_LEN]
    def computing_encryption_key(self, user_password:'ascii str'):
        # Algorithm 3.2  Computing an encryption key [page 125]
        # password - user password string
        # user_password+/O+/P+/ID_0+(/R+/Length) ==>> encryption_key
        encryption_dict = self.encryption_dict
        trailer_dict = self.trailer_dict
        #calc_n = self.calc_n
        n = self.n
        padded_password = self.padded_password
        MD5 = self.MD5
        int2uint32le_encode =\
            lambda i: i.to_bytes(4, byteorder='little', signed=True)
            # neg int

        padded = padded_password(user_password)
        O = (encryption_dict[b'/O']).get()
        ID_0 = (trailer_dict[b'/ID'][0]).get()
        P = int2uint32le_encode(encryption_dict[b'/P'])
        if not (len(padded) == 32 == len(O)):# == len(ID_0)):
            raise Exception(
                    'len != 32): len(padded)={}; len(O)={}'
                    .format(len(padded), len(O))
                    )
        assert len(P) == 4
        assert type(O) == type(ID_0) == type(P) == type(padded) == bytes
        f = MD5()\
            ( padded
            , O
            # input negative number!
            , P
            , ID_0
            )
        if encryption_dict[b'/R'] >= 4:
            raise NotImplementedError
        md5 = f.finish()
        #n = calc_n(encryption_dict)
        Length = encryption_dict[b'/Length'] # or n???
        if encryption_dict[b'/R'] >= 3:
            for _ in range(50):
                # Length or n???
                md5 = MD5()(md5[:n]).finish() # in spec; but diff below
                #md5 = MD5()(md5[:Length]).finish() # fix me
                #md5 = MD5()(md5).finish() # I try this, fix me

                # tried:
                #   above     below
                #   [:n]      [:]
                #   [:n]      [:n]
                #   [:]      [:n]
                #   [:]      [:]
                #   [:Length]      [:]
                #   [:Length]      [:n]
                #
        encryption_key = md5[:n]
        return encryption_key

    @classmethod
    def create_RC4_key(cls, bs:bytes):
        # Algorithm 3.3::4
        return bs # assume id??
        raise NotImplementedError # ???
    @classmethod
    def xor_with_same_byte(cls, i, bs):
        return cls.xor(bytes([i])*len(bs), bs)
    @classmethod
    def xor(cls, bs1, bs2):
        assert len(bs1) == len(bs2)
        L = len(bs1)
        encode = lambda bs: int.from_bytes(bs, byteorder='little')
        decode = lambda i: i.to_bytes(L, byteorder='little')
        return decode(encode(bs1) ^ encode(bs2))

    def _algorithm3_3__step1to4__computing_keyRC4(self, owner_password):
        # Algorithm 3.3 :: step 1,2,3,4
        # "If there is no owner password, use the user password instead."
        # owner_password+/R ==>> keyRC4
        encryption_dict = self.encryption_dict
        padded_password = self.padded_password
        create_RC4_key = self.create_RC4_key
        MD5 = self.MD5
        n = self.n

        padded = padded_password(owner_password)
        md5 = MD5()(padded).finish()
        if encryption_dict[b'/R'] >= 3:
            for _ in range(50):
                md5 = MD5()(md5).finish() # in spec; but diff above
                #md5 = MD5()(md5[:n]).finish() # I try with n; fix me
        # n = calc_n(encryption_dict)
        keyRC4 = create_RC4_key(md5[:n])
        # now step4 end
        return keyRC4

    def computing_encryption_dict_O(self, owner_password, user_password):
        # Algorithm 3.3  Computing the encryption dictionary's O (owner password) value [page 126]
        # keyRC4(owner_password+/R)+user_password+/R ==>> /O

        #calc_n = self.calc_n
        encryption_dict = self.encryption_dict
        padded_password = self.padded_password
        RC4_encrypt = self.RC4_encrypt
        xor_with_same_byte = self.xor_with_same_byte


        if user_password is None:
            # I add this line which not in Algorithm 3.3
            user_password = b'' # as-if PADDING_BYTES
        if owner_password is None:
            # "If there is no owner password, use the user password instead."
            owner_password = user_password
        keyRC4 = self._algorithm3_3__step1to4__computing_keyRC4(owner_password)

        # step5:
        padded = padded_password(user_password)
        rc4 = RC4_encrypt(keyRC4)(padded).finish()
        assert len(padded) == len(rc4) == 32
        if encryption_dict[b'/R'] >= 3:
            # 19 times from 1 to 19
            bs = (range(1, 20))
            for b in bs:
                # bug: key = xor_with_same_byte(b, rc4)
                key = xor_with_same_byte(b, keyRC4)
                rc4 = RC4_encrypt(key)(rc4).finish()
        O = rc4
        assert len(O) == 32
        # encryption_dict[b'/O'] := O # output
        return O

    def computing_encryption_dict_U_ifReq2(self, user_password):
        # Algorithm 3.4  Computing the encryption dictionary's U (user password) value (Revision 2) [page 126]
        # user_password+/O+/P+/ID_0+(/R+/Length) ==>> encryption_key ==>> /U
        assert self.encryption_dict[b'/R'] == 2
        encryption_key = self.computing_encryption_key(user_password)
        U = self.RC4_encrypt(encryption_key)(PADDING_BYTES).finish()
        assert len(U) == 32
        # encryption_dict[b'/U'] := U
        return U
    @classmethod
    def random_bytes_of_len(cls, L):
        return bytes(random.randrange(0x100) for _ in range(L))
    def computing_encryption_dict_U_ifRge3(self, user_password):
        # Algorithm 3.5  Computing the encryption dictionary's U (user password) value (Revision 3 or greater) [page 127]
        # user_password+/O+/P+/ID_0+(/R+/Length) ==>> encryption_key
        #       encryption_key+/ID_0==>> /U[:16]
        encryption_dict = self.encryption_dict
        trailer_dict = self.trailer_dict
        MD5 = self.MD5
        RC4_encrypt = self.RC4_encrypt
        xor_with_same_byte = self.xor_with_same_byte
        random_bytes_of_len = self.random_bytes_of_len
        computing_encryption_key = self.computing_encryption_key


        assert encryption_dict[b'/R'] >= 3
        encryption_key = computing_encryption_key(user_password)
        md5 = MD5()\
                ( PADDING_BYTES
                , (trailer_dict[b'/ID'][0]).get()
                ).finish()
        assert len(md5) == 16 # why?? or md5 = md5[:16]?? @step 4
        rc4 = RC4_encrypt(encryption_key)(md5).finish() # len(rc4) == 16
        if True:
            # 19 times from 1 to 19
            bs = (range(1, 20))
            for b in bs:
                # bug: key = xor_with_same_byte(b, rc4)
                key = xor_with_same_byte(b, encryption_key)
                rc4 = RC4_encrypt(key)(rc4).finish()

        assert len(rc4) == 16
        U = rc4 + random_bytes_of_len(16)
        assert len(U) == 32
        # encryption_dict[b'/U'] := U
        return U

    def authenticating_user_password(self, user_password):
        # Algorithm 3.6  Authenticating the user password [page 127]
        # if authenticating_user_password(user_password):
        #   then we can use computing_encryption_key(user_password) as
        #       the key to decrypt the pdf doc
        # if authenticating_user_password(''):
        #   then suppress prompting for a password
        #
        # default user_password is PADDING_BYTES (not b''?)
        R = self.encryption_dict[b'/R']
        U = (self.encryption_dict[b'/U'].get())
        assert len(U) == 32
        if R >= 3:
            _U = self.computing_encryption_dict_U_ifRge3(user_password)
            assert len(_U) == 32
            print('authenticating_user_password:\n'
                    'user_password:{!r}\n'
                    '/U:{!r}\n'
                    '_U:{!r}'.format(user_password, U, _U))
            return U[:16] == _U[:16]
        elif R == 2:
            _U = self.computing_encryption_dict_U_ifReq2(user_password)
            assert len(_U) == 32
            return U == _U


    def authenticating_owner_password(self, owner_password):
        # Algorithm 3.7  Authenticating the owner password [page 128]
        _user_password = self.owner_password2user_password(owner_password)
        return self.authenticating_user_password(_user_password)
    def owner_password2user_password(self, owner_password):
        # Algorithm 3.7 :: step 1, 2 [page 128]
        encryption_dict = self.encryption_dict
        RC4_decrypt = self.RC4_decrypt
        xor_with_same_byte = self.xor_with_same_byte

        keyRC4 = self._algorithm3_3__step1to4__computing_keyRC4(owner_password)

        R = encryption_dict[b'/R']
        O = (encryption_dict[b'/O'].get())
        assert len(O) == 32
        if R == 2:
            _user_password = RC4_decrypt(keyRC4)(O).finish()
        elif R >= 3:
            rc4 = O
            # 20 times from 19 to 0
            bs = (range(19, -1, -1))
            for b in bs:
                # bug: key = xor_with_same_byte(b, rc4)
                key = xor_with_same_byte(b, keyRC4)
                rc4 = RC4_decrypt(key)(rc4).finish()
            _user_password = rc4
        _O = self.computing_encryption_dict_O(owner_password, _user_password)
        assert O == _O
        print('owner_password2user_password success')
        return _user_password

