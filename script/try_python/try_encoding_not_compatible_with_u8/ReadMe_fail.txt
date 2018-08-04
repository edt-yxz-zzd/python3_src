
1) encoding declaration is decoded by utf8
2) encoding the whole file using one encoding
==>> encoding should be compatible with u8









# open from module tokenize
# encoding the whole file
#    buffer.seek(0)
#    text = TextIOWrapper(buffer, encoding, line_buffering=True)
def open(filename):
    """Open a file in read only mode using the encoding detected by
    detect_encoding().
    """
    buffer = builtins.open(filename, 'rb')
    encoding, lines = detect_encoding(buffer.readline)
    buffer.seek(0)
    text = TextIOWrapper(buffer, encoding, line_buffering=True)
    text.mode = 'r'
    return text


# encoding declaration is decoded by utf8
def detect_encoding(readline):
    ...
    def find_cookie(line):
        try:
            # Decode as UTF-8. Either the line is an encoding declaration,
            # in which case it should be pure ASCII, or it must be UTF-8
            # per default encoding.
            line_string = line.decode('utf-8')
        except UnicodeDecodeError:
            msg = "invalid or missing encoding declaration"
            ...
        ...
    ...

