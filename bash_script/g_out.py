#
#
#g_out: \ddd+ --> cjk

import sys
import re

def f(m):
	s = m.group(1)
	if s is None:
		return m.group(0)
	else:
		it = iter(s.split("\\"))
		for c in it:
			assert not c
			break
		else:
			raise logic-error
		bs = bytes(int(x, 8) for x in it)
		r = bs.decode('u8')
		return r
for ln in sys.stdin:
	x = re.sub(r"\\\D|((?:\\[0-7]{1,3})+)", f, ln)
	print(x, end='')


