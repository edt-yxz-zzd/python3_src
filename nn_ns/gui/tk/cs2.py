import Tools.pynche.ColorDB as db

fname = r'C:\Python33\Tools\pynche\X\rgb.txt'
cs = db.get_colordb(fname)
cs = cs._ColorDB__byname
cs = {n:db.triplet_to_rrggbb(rgb).upper() for n, rgb in cs.items()}

import pprint
p = pprint.PrettyPrinter(4)
p.pprint(cs)
