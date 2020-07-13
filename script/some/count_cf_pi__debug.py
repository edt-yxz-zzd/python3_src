r"""
* 1
	it says there 1_8000_0000 terms
	but I count 1_8000_0002 (include head "3")
* 2
	it seems to use ','
	but I found ';'
	only one at 316350278
* 3
	newline = \n | \r
	no \n
	only \r

#"""

from .count_cf_pi import Globals

def iter_search_1B(fin, byte, *, block_size):
	[byte] = byte
	b = bytes([byte])
	while 1:
		bk = fin.read(block_size)
		if not bk: break
		bss = bk.split(b)
		if len(bss) >= 2:
			bss.pop()
			i = fin.tell()-len(bk)
			for d in map(len, bss):
				i += d
				yield i
				i += 1

def search_1B_with_context__i(ifname, byte, *, block_size, file_begin, context_begin, context_end):
	sz = context_end-context_begin
	#assert sz >= 0
	with open(ifname, "rb") as fin:
		fin.seek(file_begin)
		it = iter_search_1B(fin, byte, block_size=block_size)
		for loc in it:
			#print(loc)
			if sz > 0:
				save = fin.tell()
				fin.seek(loc)
				assert byte == fin.read(1)
				#bug: i0 = save + context_begin
				i0 = loc + context_begin
				if i0 < 0:
					_i0 = 0
					_sz = max(0, i0+sz)
					#print(_i0, _sz)
					fin.seek(_i0)
					context = fin.read(_sz)
				else:
					#print(i0, sz)
					fin.seek(i0)
					context = fin.read(sz)
				print(f"{context!r}")
				fin.seek(save)
			input(loc)


def read_util(fin, byte):
	assert len(byte)==1
	block_size = 1<<8
	begin = fin.tell()
	bss = []
	while 1:
		bs = fin.read(block_size)
		if not bs: break
		i = bs.find(byte)
		if i >= 0:
			end = fin.tell()-(len(bs)-i-1)
			fin.seek(end)
			bss.append(bs[:i+1])
			break
		bss.append(bs)
	bs = b''.join(bss)
	assert len(bs) == fin.tell()-begin
	return bs
def search_rng_not_mn_terms_per_line(fin, m, *, file_begin, file_end, block_size):
	_recur = search_rng_not_mn_terms_per_line
	######
	fin.seek(file_begin)
	sz = block_size
	kkk = 0
	while 1:
		i = fin.tell()     #txt-file non-simple!!
		if not i < file_end: break
		j = i + block_size
		if j > file_end:
			sz = file_end - i

		assert sz
		bk = fin.read(sz)
		if not bk: break
		#print('xxxxx')
		#t = fin.readline() #bin-file b'\n' !!!
		t = read_util(fin, b'\r')
		#print('yyyyy')
		#print(len(t))
		#bk = b''.join([b'(', bk, t, b')'])
		#bk = ''.join(['(', bk, t, ')'])
		#ls = eval(bk); kk = len(ls)
		bk += t
		kk = bk.count(b',')
		#kk = bk.count(',')
		kk += i <= 316350278 < fin.tell()
		print(kk)
		kkk += kk
		assert fin.tell() == i + len(bk)
		if kk%m:
			_beg, _end = (i, fin.tell())
			print(_beg, _end)
			assert _end == _beg + len(bk)
			if kk > m or block_size <= m:
				return search_rng_not_mn_terms_per_line(fin, m, file_begin=_beg, file_end=_end, block_size=block_size//2)
			print(kk)
			return (_beg, _end)
			break
	print(kkk)




oo = float("inf")
def main__search_rng_not_mn_terms_per_line(ifname, m, *, file_begin, file_end, block_size):
	#with open(ifname, "rt", encoding='ascii') as fin:
	with open(ifname, "rb") as fin:
		#t = fin.readline() #bin-file b'\n' !!!
		#i = fin.tell()     #txt-file non-simple!!
		return search_rng_not_mn_terms_per_line(fin, m, file_begin=file_begin, file_end=file_end, block_size=block_size)



def main(args=None):
	import argparse
	from seed.io.may_open import may_open_stdin, may_open_stdout

	parser = argparse.ArgumentParser(
		description="count_cf_pi debug the pi_cf file"
		, epilog=""
		, formatter_class=argparse.RawDescriptionHelpFormatter
		)
	parser.add_argument('-i', '--input', type=str, default=None
						, help='input hfile path')
	parser.add_argument('-o', '--output', type=str, default=None
						, help='output file path')
	parser.add_argument('-e', '--encoding', type=str
						, default='utf8'
						, help='input/output file encoding')
	parser.add_argument('-f', '--force', action='store_true'
						, default = False
						, help='open mode for output file')

	args = parser.parse_args(args)
	encoding = args.encoding
	omode = 'wt' if args.force else 'xt'

	r"""
	may_ifname = args.input
	with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:

	may_ofname = args.output
	with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
py -m script.some.count_cf_pi__debug
	#"""

if __name__ == "__main__":
	#search_1B_with_context__i(Globals.small, b',', block_size=1<<20, file_begin=0, context_begin=-15, context_end=15)
	#search_1B_with_context__i(Globals.big, b';', block_size=1<<20, file_begin=316350278, context_begin=-311, context_end=320)
	#main__search_rng_not_mn_terms_per_line(Globals.small, 100, file_begin=0, file_end=oo, block_size=1<<20)
	main__search_rng_not_mn_terms_per_line(Globals.big, 100, file_begin=0, file_end=oo, block_size=1<<20)
	#main()

r"""
$ py -m script.some.count_cf_pi__debug

>>> search_1B_with_context__i(Globals.big, b'\n', block_size=1<<20, file_begin=0, context_begin=-15, context_end=15)
<EMPTY>



>>> search_1B_with_context__i(Globals.big, b';', block_size=1<<20, file_begin=0, context_begin=-15, context_end=15)
b', 3, 1, 1, 3, 1; \r4, 180, 539,'
316350278




>>> search_1B_with_context__i(Globals.big, b';', block_size=1<<20, file_begin=316350278, context_begin=-311, context_end=320)
b'\r1, 62, 1, 32, 1, 5, 1, 1, 95, 1, 2, 3, 1, 5, 1, 76, 1, 1, 2, 2, 8, 1, 6, 9, 2, 6, 1, 1, 3, 1, 1, 4, 2, 1, 73, 5, 1, 1, 4, 1, 5, 1, 10, 1, 1, 1, 2, 2, 2, 3, 1, 1, 1, 7, 1, 2, 3, 5, 3, 9, 9, 44, 1, 9, 1, 376, 1, 5, 1, 3, 6, 6, 1, 2, 4, 2, 35, 2, 1, 2, 2, 1, 4, 1, 20, 2, 1, 4, 1, 1, 1, 1, 7, 26, 1, 3, 1, 1, 3, 1; \r4, 180, 539, 1, 27, 3, 6, 7, 1, 13, 1, 2, 50, 3, 2, 1, 1, 6, 2, 1, 1, 5, 5, 1, 1, 2, 12, 1, 2, 1, 24, 12, 1, 2, 1, 1, 2, 3, 2, 4, 7, 1, 6, 1, 1, 1, 2, 5, 1, 2, 1, 2, 1, 1, 1, 3, 1, 28, 1, 7, 1, 2, 3, 13, 1, 2, 17, 1, 6, 6, 1, 6, 1, 27, 1, 10, 1, 7, 3, 2, 1, 1, 3, 2, 2, 1, 1, 5, 4, 1, 8, 1, 2, 9, 1, 1, 3, 32, 2, 4, \r'
316350278


##正常？？？
>>> main__search_rng_not_mn_terms_per_line(Globals.big, 100, file_begin=0, file_end=oo, block_size=1<<20)
...
180000000



#"""


