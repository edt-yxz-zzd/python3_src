
import subprocess
import os.path as path
import io

    
#plantri -a [-u] [-V] -d -v -<c2x|c3>m3 <cubic_graph_order>d [output_file]

exe = './plantri45'
outputpath = './adc3m3'
args = '-adc3m3'
nv_ls = list(range(4, 9, 2))
def gen(exe, outputpath, args, nv_ls):
    nv_ls = list(nv_ls)
    fname = args + repr(nv_ls) + '.txt'
    fpath = path.join(outputpath, fname)
    if path.exists(fpath):
        raise ValueError('file exists: {!r}'.format(fpath))

    outs = []
    for n in nv_ls:
        out = subprocess.check_output([exe, args, '{}d'.format(n)])
        outs.append(out)
    outs = b''.join(outs)
    outs = outs.decode(encoding='ascii')
    outs = outs.splitlines()
    outs = '\n'.join(outs) + '\n'
    with open(fpath, 'x', encoding='ascii') as fout:
        fout.write(outs)
    return
    
        
        
# about 38 MB; about 40,0000 graphs? exactly:398438
nv_ls = list(range(4, 25, 2)) 
gen(exe, outputpath, args, nv_ls)










def t(n_c3 = 18, n_c2 = 4): # 16, 16; 20, 18;
    argv2 = [\
        ('a', 'V', 'd', 'c2xm3'),\
        ('a', 'd', 'c2xm3'),\
        ]
    argv3 = [\
        ('a', 'V', 'd', 'c3m3'),\
        ('a', 'd', 'c3m3'),\
        ]
    '''
    argv3 = [\
        ('a', 'V', 'c3m3'),\
        ('a', 'c3m3'),\
        ]'''
    path = 'txt/'
    suffix = '.txt'

    
    def fn_core(argv): return '{}' + ''.join(argv) + '_{}d{}'
    def filename_for_rng(argv, rng, suffix, path):
        fn = fn_core(argv)
        rd = 'from{}to{}'.format(*rng)
        return fn.format(path, rd, suffix)
    def filename_for_int(argv, i, suffix, path):
        fn = fn_core(argv)
        return fn.format(path, i, suffix)

    
    def argv_build(i, argv):
        #fn = filename_for_int(argv, i, suffix, path)
        nd = str(i)+'d'
        return ['plantri45'] + ['-' + a for a in argv] + [nd] #[nd, fn]

    def _call_to_multifiles(n_cx, argvx):
        for i in range(4, n_cx, 2):
            for argv in argvx:
                fn = filename_for_int(argv, i, suffix, path)
                a = argv_build(i, argv)
                with open(fn, 'x') as out:
                    subprocess.check_call(a, stdout=out)
    def _call_to_singlefile(n_cx, argvx):
        
        for argv in argvx:
            fn = filename_for_rng(argv, (4, n_cx), suffix, path)
            with open(fn, 'x') as out:
                for i in range(4, n_cx, 2):
                    a = argv_build(i, argv)
                    subprocess.check_call(a, stdout=out)

    _call = _call_to_singlefile
    _call(n_c3, argv3)
    #_call(n_c2, argv2)


def t1():
    dir_w = ''
    lsa = ['c2', 'd', 'a']
    lsg = ['c2', 'd', 'g']
    ls3g = ['c3', 'd', 'g']
    suf = '_.g6'
    def argv_build(i, ls, suffix = suf):
        fn = ''.join(ls)
        return ['plantri45'] + ['-' + a for a in ls] + [str(i), dir_w + fn + '_' + str(i) + suffix]
        
    for i in range(4, 10):
        #subprocess.check_call(argv_build(i, lsa, '.asc'))
        subprocess.check_call(argv_build(i, lsg))
        subprocess.check_call(argv_build(i, ls3g))
