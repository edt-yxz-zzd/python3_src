r"""
pi cf count by bit_len; [3]++[...]
output:
	txt_phone/txt/others/数学pi_cf_counter.txt



continued_fraction_pi_100term_per_line_omit_zeroth_term.txt
	file_regex
	file
		= continued_fraction_pi_100term_per_line_omit_zeroth_term.txt
		= cf(1/(pi-3))[0:1_8000_0000]
		= cf(pi)[1:1_8000_0001]
	begin with 7

	file_regex = r"((\d+[;,] ){100}[\n\r]){180_0000}"

#"""


def split_seps(seps, bs):
	sep = seps[0:1]
	for i in range(1, len(seps)):
		bs = bs.replace(seps[i:i+1], sep)
	return bs.split(sep)
	return [*iter_split_seps(seps, bs)]
def iter_split_seps(seps, bs):
	begin = 0
	end = -1
	for end, x in enumerate(bs):
		if x in seps:
			yield bs[begin:end]
			begin = end+1
	else:
		end += 1
		yield bs[begin:end]
	assert end == len(bs)

def iter_read__by_sep__1B(fin, *, block_size, seps):
	if block_size is None:
		block_size = 1<<8
	if seps is None:
		seps = b','
	if type(block_size) is not int: raise TypeError
	if block_size <= 0: raise ValueError
	seps = memoryview(seps)
	#if len(sep) != 1: raise ValueError
	#if not all(len(sep) == 1 for sep in seps): raise ValueError

	bss0_ = []
	while 1:
		bk = fin.read(block_size)
		# len(sep)==1
		#i = bk.find(sep)
		#_bss_ = bk.split(sep)
		_bss_ = split_seps(seps, bk)
		nn = len(_bss_)
		assert(nn)
		bss0_.append(_bss_[0])
		if nn >= 2:
			#assert len(_bss_) >= 2
			bss0 = b''.join(bss0_)
			_bss_[0] = bss0
			bss0_ = [_bss_.pop()]
			for bs in _bss_:
				yield bs
		else:
			pass

		if not bk: break
	#end while
	bss0 = b''.join(bss0_)
	#bug:yield bs
	yield bss0
	return

def iter_read__pint_in_cf_without_head(fin, *, block_size):
	it = iter_read__by_sep__1B(fin, block_size=block_size, seps=b',;')
	for bs in it:
		bs = bs.strip()
		if not bs:
			#end with ','
			for _ in it:
				raise Exception(fr'format error: regex",\s*,"')
				
			break
		p = int(bs)
		if p <= 0: raise Exception(fr"format error: {bs!r}")
		yield p
	else:
		#not end with ','
		pass
	return
	

from collections import Counter
from itertools import chain, islice
from pathlib import Path
import os


def main_i(fin, nn, *, head, block_size):
	if type(head) is not int: raise TypeError
	it = iter_read__pint_in_cf_without_head(fin, block_size=block_size)
	it = chain([head], it)
	us = set()
	us = Counter()
	i = -1
	while 1:
		if nn < len(us):
			s = input(fr"num_diff_terms >= {len(us)} to continue (q/*/=):")
			if s == 'q': break
			elif s in ('', '*', '='):
				if s == '=':
					nn = len(us)
				else:
					nn *= 2
				print(fr"num_diff_terms := {nn}")
			else:
				try:
					m = int(s)
				except:
					pass
				else:
					if m >= len(us):
						nn = m
						print(fr"num_diff_terms := {nn}")
			continue
		for i,u in enumerate(it, 1+i):
			us[u]+=1
			if nn < len(us):
				#print(fr"cf[0..{i}] -> num_diff_terms {len(us)}")
				print(fr"len(set(cf[0:{i+1}])) == {len(us)}")
				break
		else:
			break
	sz = 1+i
	us = {**us}
	#print(fr"cf[0:{sz}] -> num_diff_terms {len(us)}")
	print(fr"len(set(cf[0:{sz}])) == {len(us)}")
	assert sz == sum(us.values())
	return sz, us

def main_i__f(ifname, nn, block_size):
	#with open(ifname, "rt", encoding='ascii') as fin:
	with open(ifname, "rb") as fin:
		sz, us = main_i(fin, nn, head=3, block_size=block_size)
	print(us)
	print(fr"len(set(cf[0:{sz}])) == {len(us)}")
	assert sz == sum(us.values())

class Globals:
	my_home = Path(os.environ["my_home"])
	this_file = Path(__file__)
	this_dir = this_file.parent
	small = this_dir / (this_file.name+r".example_cf.txt")
	big = my_home/ r"unzip/e_book/连分数/continued_fraction_pi/continued_fraction_pi_100term_per_line_omit_zeroth_term.txt"

#main_i__f(Globals.small, 8, 3)






def output_counter(fout, d):
	num_diff_terms = len(d)
	num_terms = sum(d.values())
	def f(s):
		#fout.write(s)
		print(s, file=fout)

	f(f'#begin: total={num_terms}; diff={num_diff_terms};')

	for k,v in sorted(d.items()):
		f(f',{k}:{v}')

	f(f'#end: total={num_terms}; diff={num_diff_terms};')
	#print(fr"len(set(cf[0:{sz}])) == {len(us)}")


def main(args=None):
	import argparse
	import sys

	parser = argparse.ArgumentParser(
		description="count terms of continued_fraction_of_pi"
		, epilog=""
		, formatter_class=argparse.RawDescriptionHelpFormatter
		)
	parser.add_argument('-i', '--input', type=str, default=None
						, help='input file path')
	parser.add_argument('-ic', '--input_choice', type=str, default=None
						, choices='big small'.split()
						, help='choose builtin input file path')
	parser.add_argument('-o', '--output', type=str, default=None
						, help='output file path')
	parser.add_argument('-b', '--block_size', type=int, default=1<<8
						, help='input file read as blocks #block_size')
	parser.add_argument('-n', '--num_diff_terms', type=int, default=1<<8
						, help='read num_diff_terms "diff terms"')
	parser.add_argument('-hd', '--head', type=int, default=3
						, help='leading term of continued_fraction_of_pi')


	args = parser.parse_args(args)
	nn = args.num_diff_terms
	head = args.head
	block_size = args.block_size
	may_ifname = args.input
	if may_ifname is None:
		if args.input_choice is not None:
			may_ifname = getattr(Globals, args.input_choice)

	if may_ifname is None:
		fin = sys.stdin.buffer
		sz, us = main_i(fin, nn, head=head, block_size=block_size)
	else:
		ifname = may_ifname
		with open(ifname, "rb") as fin:
			sz, us = main_i(fin, nn, head=head, block_size=block_size)

	assert sz == sum(us.values())
	if args.output is None:
		fout = sys.stdout
		output_counter(fout, us)
		print(fr"len(set(cf[0:{sz}])) == {len(us)}")
	else:
		ofname = args.output
		try:
			with open(ofname, "xt", encoding='ascii') as fout:
				output_counter(fout, us)
		except FileExistsError:
			while 1:
				yn = input(fr"overwrite {ofname!r} ? (y/n):")
				if yn in ('y', 'n'):
					break
			if yn == 'y':
				with open(ofname, "wt", encoding='ascii') as fout:
					output_counter(fout, us)



	return
	main_i__f(ifname
				, args.num_diff_terms
				, block_size=args.block_size
				)


if __name__ == "__main__":
	main()


r"""
>>> 1<<20
1048576

$ py  ~/python3_src/script/some/count_cf_pi.py -ic big -o ~/tmp/pi.txt -n 1 -b 1048576
len(set(cf[0:2])) == 2
num_diff_terms >= 2 to continue (q/*/=):
num_diff_terms := 2
len(set(cf[0:3])) == 3
num_diff_terms >= 3 to continue (q/*/=):
num_diff_terms := 4
len(set(cf[0:5])) == 5
num_diff_terms >= 5 to continue (q/*/=):
num_diff_terms := 8
len(set(cf[0:28])) == 9
num_diff_terms >= 9 to continue (q/*/=):
num_diff_terms := 16
len(set(cf[0:80])) == 17
num_diff_terms >= 17 to continue (q/*/=):
num_diff_terms := 32
len(set(cf[0:214])) == 33
num_diff_terms >= 33 to continue (q/*/=):
num_diff_terms := 64
len(set(cf[0:884])) == 65
num_diff_terms >= 65 to continue (q/*/=):
num_diff_terms := 128
len(set(cf[0:3867])) == 129
num_diff_terms >= 129 to continue (q/*/=):
num_diff_terms := 256
len(set(cf[0:15316])) == 257
num_diff_terms >= 257 to continue (q/*/=):
num_diff_terms := 512
len(set(cf[0:60671])) == 513
num_diff_terms >= 513 to continue (q/*/=):
num_diff_terms := 1024
len(set(cf[0:254130])) == 1025
num_diff_terms >= 1025 to continue (q/*/=):
num_diff_terms := 2048
len(set(cf[0:961567])) == 2049
num_diff_terms >= 2049 to continue (q/*/=):
num_diff_terms := 4096
len(set(cf[0:3679301])) == 4097
num_diff_terms >= 4097 to continue (q/*/=):
num_diff_terms := 8192
len(set(cf[0:14745051])) == 8193
num_diff_terms >= 8193 to continue (q/*/=):
num_diff_terms := 16384
len(set(cf[0:58369369])) == 16385
num_diff_terms >= 16385 to continue (q/*/=):
num_diff_terms := 32768
len(set(cf[0:180000001])) == 28555



===============================
len(set(cf[0:180000002])) == 28555
bug!!!!!!!!
	1_8000_0001 < 180000002
	caused by bug, corrected
def iter_read__by_sep__1B(fin, *, block_size, seps):
	#bug:yield bs
3c3
< ,2:30592283
---
> ,2:30592284
28557c28557



#"""





