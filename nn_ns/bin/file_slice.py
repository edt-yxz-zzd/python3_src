
import os

r"""
class FileSlice:
	def __init__(self, fin, to_open, to_close):
		self.__to_close = bool(to_close)
		if to_open:
			ifname = fin
			self.__fin = open(ifname, 'rb')
		else:
			self.__fin = fin
		self.__sz = None
__del__
to_close
close
__len__
__getitem__

#"""


#__unsafe
def get_file_size__unsafe(fin):
	fin.seek(0, os.SEEK_END)
	return fin.tell()
def file_slice(fin, *, begin, end, file_size):
	if begin is None:
		begin = 0
	if begin < 0 or end is None or end < 0:
		sz = get_file_size__unsafe(fin) if file_size is None else file_size
		r = range(sz)[begin:end]
		begin, end = r.start, r.stop
	if end <= begin:
		return b''
	fin.seek(begin)
	return fin.read(end-begin)





def main(args=None):
	import argparse
	import sys
	#from seed.io.may_open import may_open_stdin, may_open_stdout

	parser = argparse.ArgumentParser(
		description="file slice, get bytes of file at offset"
		, epilog=""
		, formatter_class=argparse.RawDescriptionHelpFormatter
		)
	parser.add_argument('-i', '--input', type=str, default=None
						, help='input file path')
	parser.add_argument('-o', '--output', type=str, default=None
						, help='output file path')
	parser.add_argument('--begin', type=int, default=None
						, help='begin of slice')
	parser.add_argument('--end', type=int, default=None
						, help='end of slice')
	parser.add_argument('-sz', '--end_as_slice_size', action='store_true'
						, default = False
						, help='the "end" option used as "slice_size"')
	parser.add_argument('-oe', '--output_encoding', type=str
						, default='utf8'
						, help='output file encoding')
	parser.add_argument('-opy', '--output_as_py_bytes_repr', action='store_true'
						, default = False
						, help='output style')
	parser.add_argument('-f', '--force', action='store_true'
						, default = False
						, help='open mode for output file')

	args = parser.parse_args(args)
	oencoding = args.output_encoding
	omode_t = 'wt' if args.force else 'xt'
	omode_b = 'wb' if args.force else 'xb'
	may_ifname = args.input
	may_ofname = args.output
	begin = args.begin
	end = args.end

	if args.end_as_slice_size and end is not None:
		if begin is None:
			begin = 0
		end += begin
		if begin < 0 <= end:
			end = None

	file_size = None
	if may_ifname is None:
		fin = sys.stdin.buffer
		bs = file_slice(fin, begin=begin, end=end, file_size=file_size)
	else:
		with open(may_ifname, 'rb') as fin:
			bs = file_slice(fin, begin=begin, end=end, file_size=file_size)
	
	def f(fout_t, bs):
		if args.output_as_py_bytes_repr:
			#text
			s = repr(bs)
			print(s, file=fout_t)
		else:
			#bytes
			fout_b = fout_t.buffer
			fout_b.write(bs)
	if may_ofname is None:
		fout_t = sys.stdout
		f(fout_t, bs)
	else:
		with open(may_ofname, omode_t, encoding=oencoding) as fout_t:
			f(fout_t, bs)


	r"""
	with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:

	with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
	#"""
if __name__ == "__main__":
	main()
