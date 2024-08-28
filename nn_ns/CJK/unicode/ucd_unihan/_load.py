def _load__literal_eval(ipath, encoding, /):
    from ast import literal_eval
    from pathlib import Path
    ipath = Path(ipath)
    txt = ipath.read_text(encoding)
    r = literal_eval(txt)
    return r
from nn_ns.CJK.unicode.ucd_unihan._load import _load__literal_eval
