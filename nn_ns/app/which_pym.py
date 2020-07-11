r"""
which_pym
	like "which" but for py module
py -m nn_ns.app.which_pym nn_ns
...[show paths]...
#"""

import importlib
def which_pym(name):
	m =  importlib.import_module(name, package=__package__)
	[*paths] = m.__path__
	may_fname = m.__file__
	return may_fname, paths



def main(args=None):
	import argparse

	parser = argparse.ArgumentParser(
		description="find out where is the module/package"
		, epilog=""
		, formatter_class=argparse.RawDescriptionHelpFormatter
		)
	parser.add_argument('module_name', type=str, default=None
						, help='python module/package name')

	args = parser.parse_args(args)
	name = args.module_name
	may_fname, paths = which_pym(name)
	print(f"{may_fname!r}")
	print(f"{paths!r}")
if __name__ == "__main__":
	main()

