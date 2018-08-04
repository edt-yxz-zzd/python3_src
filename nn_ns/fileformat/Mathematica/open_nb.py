

'''
to use in find...
    find %mathematica_home% -path *%1.nb | py -m nn_ns.fileformat.Mathematica.open_nb %mathematica_home%
'''

import sys, subprocess, os.path
def open_nb(exe_path, nb_fname):
    subprocess.call([exe_path, '"{}"'.format(nb_fname)])

exe_fname = 'Mathematica.exe'
def home2exe_path(home):
    return os.path.join(home, exe_fname)
def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser(
        description='open Mathematica *.nb files.',
        epilog='input fnames from stdin')
    parser.add_argument('Mathematica_home', type=str,
                        help='for Mathematica_home/{}'.format(exe_fname))


    args = parser.parse_args()
    exe_path = home2exe_path(args.Mathematica_home)
    if not os.path.isfile(exe_path):
        raise ValueError('cannot find Mathematica.exe under {!r}'
                         .format(exe_path))
    
    for nb_fname in sys.stdin:
        # bug: nb_fname contain \n!!!
        if nb_fname[-1:] == '\n':
            nb_fname = nb_fname[:-1]
        print('open: ', nb_fname)
##        print('calling: ', exe_path)
##        print('open: ', nb)
##        assert nb == nb_fname
##        assert exe == exe_path
        open_nb(exe_path, nb_fname)

if __name__ == "__main__":
    home = r'C:\Program Files\Wolfram Research\Mathematica\9.0'
    nb = home + r'\Documentation\English\System\ReferencePages\Programs\math.nb'
    exe = home2exe_path(home)
    if 0:
        open_nb(exe, nb)
    else:
        main()

