
from chars_of import *
from sand import all_encodings, gb18030

e1 = 'mbcs'  # no std enc matched
e2 = 'cp936' # gbk


diff_chars = chars_encoded_bytes_mbcs_not_the_same_as_gb18030 = \
    '€\ue76c\ue7c8\ue7e7\ue7e8\ue7e9\ue7ea\ue7eb\ue7ec\ue7ed\ue7ee\ue7ef\ue7f0\ue7f1\ue7f2\ue7f3\ue815\ue819\ue81a\ue81b\ue81c\ue81d\ue81f\ue820\ue821\ue822\ue823\ue824\ue825\ue827\ue828\ue829\ue82a\ue82d\ue82e\ue82f\ue830\ue833\ue834\ue835\ue836\ue837\ue838\ue839\ue83a\ue83c\ue83d\ue83e\ue83f\ue840\ue841\ue842\ue844\ue845\ue846\ue847\ue848\ue849\ue84a\ue84b\ue84c\ue84d\ue84e\ue84f\ue850\ue851\ue852\ue853\ue856\ue857\ue858\ue859\ue85a\ue85b\ue85c\ue85d\ue85e\ue85f\ue860\ue861\ue862\ue863'
assert len(diff_chars) == 82
assert '\u20ac' == '€'


assert [ch.encode(e1) for ch in diff_chars] == \
       [b'\x80', b'\xa2\xe3', b'\xa8\xbf', b'\xa9\x89', b'\xa9\x8a', b'\xa9\x8b', b'\xa9\x8c', b'\xa9\x8d', b'\xa9\x8e', b'\xa9\x8f', b'\xa9\x90', b'\xa9\x91', b'\xa9\x92', b'\xa9\x93', b'\xa9\x94', b'\xa9\x95', b'\xfeP', b'\xfeT', b'\xfeU', b'\xfeV', b'\xfeW', b'\xfeX', b'\xfeZ', b'\xfe[', b'\xfe\\', b'\xfe]', b'\xfe^', b'\xfe_', b'\xfe`', b'\xfeb', b'\xfec', b'\xfed', b'\xfee', b'\xfeh', b'\xfei', b'\xfej', b'\xfek', b'\xfen', b'\xfeo', b'\xfep', b'\xfeq', b'\xfer', b'\xfes', b'\xfet', b'\xfeu', b'\xfew', b'\xfex', b'\xfey', b'\xfez', b'\xfe{', b'\xfe|', b'\xfe}', b'\xfe\x80', b'\xfe\x81', b'\xfe\x82', b'\xfe\x83', b'\xfe\x84', b'\xfe\x85', b'\xfe\x86', b'\xfe\x87', b'\xfe\x88', b'\xfe\x89', b'\xfe\x8a', b'\xfe\x8b', b'\xfe\x8c', b'\xfe\x8d', b'\xfe\x8e', b'\xfe\x8f', b'\xfe\x92', b'\xfe\x93', b'\xfe\x94', b'\xfe\x95', b'\xfe\x96', b'\xfe\x97', b'\xfe\x98', b'\xfe\x99', b'\xfe\x9a', b'\xfe\x9b', b'\xfe\x9c', b'\xfe\x9d', b'\xfe\x9e', b'\xfe\x9f']
assert b'\x80' == '€'.encode(e1)


raise

cs1 = ''.join(chars_of(e1))
#cs2 = ''.join(chars_of(e2))



print(len(cs1)) # 24069
#print(len(cs2)) # 21919

# which encoding of chars are diff in mbcs with in gb18030??
cs = []
for c in cs1:
    bs = c.encode(e1)
    x = False
    try:
        c2 = bs.decode(gb18030)
        if c2 == c:
            x = True
    except:pass
    if not x:
        cs.append(c)
print(len(cs)) # 82
assert ''.join(cs) == diff_chars


# no std enc matched
if 0:
    assert len(set(cs1)) == len(cs1)
    bs1 = cs1.encode(e1)
    assert len(set(bs1.decode(e1))) == len(cs1)


    es = []
    for e in all_encodings:
        try:
            s = bs1.decode(e)
        except:pass
        else:
            s = set(s)
            if not len(s) <= 256:
                print(e)
            if len(s) == len(cs1):
                print(e)
                es.append(e)

    assert not es






