
CHAR_ORD_UPPER = 0x110000
MAX_CHAR_ORD = CHAR_ORD_UPPER-1

chr(MAX_CHAR_ORD)

try:
    chr(CHAR_ORD_UPPER)
except ValueError:
    #ValueError: chr() arg not in range(0x110000)
    pass
else:
    raise 000



from seed.text.unicode.constant import CHAR_ORD_UPPER, MAX_CHAR_ORD
from seed.text.unicode.constant import *



