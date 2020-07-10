r"""
src/xxx.sh
	mk:
		bin/xxx.sh
			bash src/xxx.sh "$@"


#"""

from pathlib import Path

def _show(d):
	for k,v in sorted(d.items()):
		print(f"{k!s}={v!r}")
def generate_forwarding_shell_script(*
		, otemplate, force
		, idir, odir
		, iencoding, oencoding
		):
	force = bool(force)
	omode = 'wt' if force else 'xt'
	if 0:
		print(otemplate)
		print(omode)
		print(idir)
		print(iencoding)
		print(odir)
		print(oencoding)
	_show({**locals()})
	print("="*25)

	ipath = Path(idir)
	opath = Path(odir)
	if not ipath.is_dir(): raise TypeError
	if not opath.is_dir(): raise TypeError
	if opath.samefile(ipath): raise Exception('samefile: {ipath!r}=={opath!r}')

	for ifname in ipath.iterdir():
		if ifname.is_file():
			ofname = opath/ifname.name
			if ofname.exists():
				if not force:
					print(f"-skip: {str(ofname)!r}")
					continue
				if ofname.samefile(ifname): raise Exception('samefile: {ifname!r}=={ofname!r}')

			#s = ifname.read_text(encoding=iencoding)
			s = otemplate.format(ifname.name)
			print(f"+open: {str(ofname)!r}")
			with open(ofname, omode, encoding=oencoding) as fout:
				fout.write(s)






def main(args=None):
	import argparse
	#os.environ

	parser = argparse.ArgumentParser(
		description="generate_forwarding_shell_script"
		, epilog=""
		, formatter_class=argparse.RawDescriptionHelpFormatter
		)
	parser.add_argument('-t', '--output_file_template', type=str, default=None
						, required=True
						, help='output_file_template: python format string, eg: "bash $my_sh/{}"')
	parser.add_argument('-i', '--input_dir', type=str, default=None
						, required=True
						, help='input directory')
	parser.add_argument('-o', '--output_dir', type=str, default=None
						, required=True
						, help='output directory')
	parser.add_argument('-ie', '--input_encoding', type=str
						, default='utf8'
						, help='input file encoding')
	parser.add_argument('-oe', '--output_encoding', type=str
						, default='utf8'
						, help='output file encoding')
	parser.add_argument('-f', '--force', action='store_true'
						, default = False
						, help='open mode for output file')

	args = parser.parse_args(args)
	otemplate = args.output_file_template
	iencoding = args.input_encoding
	oencoding = args.output_encoding
	idir = args.input_dir
	odir = args.output_dir
	omode = 'wt' if args.force else 'xt'

	generate_forwarding_shell_script(
			otemplate=otemplate
			,force=args.force
			,idir=idir
			,odir=odir
			,iencoding=iencoding
			,oencoding=oencoding
			)
"""
	ifname 
	with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:

	may_ofname = args.output
	with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
"""
if __name__ == "__main__":
	main()




