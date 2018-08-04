
r'''
Java Concepts (5ed)(Cay Horstmann)
    ::Chapter 12 Object-Oriented Design Page 13 of 77
    ::[page 538]

CRC_cards :: Map Class [(Responsibility, [(Class, [Responsibility])])]
       or :: Map Class (Map Responsibility (Map Class [Responsibility]))

    # first layer map is filename(i.e. classname) to filecontent

e.g.
    # in XXX.crc file
    XXX:
        handle yyy:
            YYY:
                get value
            OUT:
                output data
        get size
    # in YYY.crc file
    YYY:
        get value
    # in OUT.crc file
    OUT:
        out data

'''


CRC_card_Grammar = r'''
CRCR = ClassName ':' newline indent RCR+ dedent
RCR = Responsibility (newline | ':' newline indent CR+ dedent)
CR = ClassName ':' newline indent R+ dedent
R = Responsibility newline
Responsibility = word+
# word = regex"\w+"
'''








