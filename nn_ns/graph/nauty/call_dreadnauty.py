
import argparse
import subprocess
import sys, re
import io


path_to_nauty = r'D:\software\programming\library\graph\nauty24r2\dreadnaut'

def to_str(bs):
    return io.TextIOWrapper(io.BytesIO(bs)).read()

class ArgumentParserTypeChecker:
    def __init__(self, check_f):
        self.check_f = check_f
    def __call__(self, s):
        succ, msg = check_f(s)
        if succ:
            return msg
        raise argparse.ArgumentTypeError(msg.format(s))

def check_positive_f(s):pass
    
def build_nauty_argparser():
    epilog = '''
The canonical labellings produced by dreadnaut can depend on the values of \
many of the options. If you are testing two or more graphs for isomorphism, \
it is important that you use the same values of these options for all your \
graphs. In general, h is a function of all these:
(a) option digraph (d command)
(b) all the vertex-invariant options (*, k and K commands)
(c) the value of tc level (y command)
(d) the use of userrefproc (u command)
(e) the version of nauty used
'''
    parser = argparse.ArgumentParser(description='set nauty options',
                                     prefix_chars='-+',
                                     epilog = epilog)


    parser.add_argument('n', type=int,
                        help='graph order, number of vertices')
    parser.add_argument('-f', '--partition', type=str,
                        default = None,
                        help='specify an initial partition, like: [3:6|0,1]')
    parser.add_argument('-l', '--linelength', type=int,
                        default = 0,
                        help='set value of option linelength')
    
    parser.add_argument('-y', '--tc_level', type=int,
                        default = 100,
                        help='set value of option tc_level; be larger for harder graph')

    
    parser.add_argument('+d', '++digraph', action='store_const',
                        default = '-d', const = '+d',
                        help='set option digraph to TRUE')
    parser.add_argument('+p', '++cartesian', action='store_const',
                        default = '-p', const = '+p',
                        help='set option cartesian to TRUE')    
    parser.add_argument('-d', '--digraph', action='store_const',
                        const = '-d',
                        help='set option digraph to FALSE')
    parser.add_argument('-p', '--cartesian', action='store_const',
                        const = '-p',
                        help='set option cartesian to FALSE')

    
    parser.add_argument('-c', '--getcanon', action='store_const',
                        default = '+c', const = '-c',
                        help='set option getcanon to FALSE')
    parser.add_argument('-a', '--writeautoms', action='store_const',
                        default = '+a', const = '-a',
                        help='set option writeautoms to FALSE')
    parser.add_argument('-m', '--writemarkers', action='store_const',
                        default = '+m', const = '-m',
                        help='set option writemarkers to FALSE')    
    parser.add_argument('+c', '++getcanon', action='store_const',
                        const = '+c',
                        help='set option getcanon to TRUE')
    parser.add_argument('+a', '++writeautoms', action='store_const',
                        const = '+a',
                        help='set option writeautoms to TRUE')
    parser.add_argument('+m', '++writemarkers', action='store_const',
                        const = '+m',
                        help='set option writemarkers to TRUE')

    return parser



def call_nauty(args = None, stdin = None, path_to_nauty=path_to_nauty):
    exe = 'x'
    output_graph = 'T'
    output_options = '?'
    output_partition = '&'
    output_orbits_after_exe = 'o'
    output_if_getcanon_after_exe = 'b'
    qut = 'q'

    parser = build_nauty_argparser()
    args = parser.parse_args(args)

    assert args.n > 0
    n = 'n={}'.format(args.n)
    f = '-f' if args.partition is None else 'f={}'.format(args.partition)
    
    l = 'l={}'.format(args.linelength)
    y = 'y={}'.format(args.tc_level)
    d = args.digraph
    p = args.cartesian
    c = args.getcanon
    a = args.writeautoms
    m = args.writemarkers
    in_ls = [n, f, l, y, d, p, c, a, m, output_options, output_partition,]
    out_ls = [output_graph, exe, 
              output_orbits_after_exe,]

    if c == '+c':
        out_ls.append(output_if_getcanon_after_exe)
    out_ls.append(qut)

    if stdin == None:
        stdin = sys.stdin
    if isinstance(stdin, str):
        g = stdin
    else:
        g = stdin.read()
    
    in_str = ' '.join(in_ls) + '\ng\n{!s}\n'.format(g) + ' '.join(out_ls)


    in_bytes = in_str.encode()
    is_timeout, outs, errs = call([path_to_nauty], in_bytes)
    # outs = outs.decode() # \n\n on windows!!
    # errs = errs.decode()
    outs = to_str(outs)
    errs = to_str(errs)

    if is_timeout:
        raise RuntimeError('call nauty timeout',
                           dict(is_timeout=is_timeout, outs=outs, errs=errs))
    if errs:
        raise RuntimeError('nauty errors:\n'+errs,
                     dict(is_timeout=is_timeout, outs=outs, errs=errs))
    return outs


def call(path_args, input=None, timeout=None):
    PIPE = subprocess.PIPE
    if input is not None:
        stdin = PIPE
    else:
        stdin = None

    is_timeout = False
    with subprocess.Popen(path_args, stdin=stdin, stdout=PIPE, stderr=PIPE) as proc:
        try:
            outs, errs = proc.communicate(input=input, timeout=timeout)
        except subprocess.TimeoutExpired:
            is_timeout = True
            proc.kill()
            outs, errs = proc.communicate()
        except:
            proc.kill()
            outs, errs = proc.communicate()
            raise
        retcode = proc.poll()
        if not is_timeout and retcode:
            raise subprocess.CalledProcessError(retcode, proc.args)
    
    return is_timeout, outs, errs


nauty_options_pattern = re.compile(
    r'm=(?P<M>\d+)\s+n=(?P<N>\d+)\s+labelorg=0\s+g=undef\s+'
    r'options=\((?P<c>[+-])c(?P<a>[+-])a(?P<m>[+-])m(?P<p>[+-])p(?P<d>[+-])d\s+'
    r'y=(?P<y>\d+)\s+k=\(0,1\)\)\s+'
    r'linelen=(?P<linelen>\d+)\s+worksize=(?P<worksize>\d+)\s+input_depth=0;\s+'
    r'(?P<Ncells>\d+)\s+cells?\s+'
    )

nauty_partition_pattern = re.compile(
    r'((unit partition)|\[[\d| ,:]+\])\s*?\n')

nauty_graph_basic_pattern = re.compile(
    r'(\s+\d+\s*:(\s+\d+)*\s*;\s*?\n)+')

nauty_graph_pattern = re.compile(
    r'n=(?P<n>\d+)\s+\$=0\s+g\s*?\n'
    r'(?P<original_graph>{original_graph})'
    r'\s*\$\$\s*?\n'
    .format(
        original_graph = nauty_graph_basic_pattern.pattern
        )
    )

nauty_exe_opt_output_using_usr_partition_pattern = re.compile(
    r'\[fixing partition\]\s*?\n')

nauty_exe_basic_output_pattern = re.compile(
    r'(?P<Norbits>\d+)\s+orbits?;\s+grpsize=(?P<grpsize>\d+);\s+'
    r'(?P<Ngen>\d+)\s+gens?;\s+(?P<Nnodes>\d+)\s+nodes?'
    r'(?P<opt_Nbadleaves>(\(\s*(?P<Nbadleaves>\d+)\s+bad\s+(leaf|leaves)\))?);\s+'
    r'maxlev=(?P<maxlev>\d+)\s*?\n'
    r'tctotal=(?P<tctotal>\d+);\s+'
    r'(?P<opt_Ncanupdates>(canupdates=(?P<Ncanupdates>\d+);\s+)?)'
    r'cpu\s+time\s*=\s*(?P<cpu_time>[\.\d]+)\s+seconds?\s*?\n'
    )



nauty_exe_optional_writeautoms_pattern = re.compile(
    r'(\(\d+(\s+\d+)*\))+\s*?\n|(\s+\d+)+\s*?\n')
nauty_exe_optional_writemarkers_pattern = re.compile(
    r'level\s+(?P<level>\d+):(\s*(?P<ncells>\d+)\s+cells?;)?'
    r'\s*(?P<norbits>\d+)\s+orbits?;\s*(?P<nfixed>\d+)\s+fixed;'
    r'\s*index\s+(?P<equivalent_size>\d+)\s*(\/\s*(?P<curr_cell_size>\d+))?\s*?\n'
    )
nauty_orbits_pattern = re.compile(
    r'((\s+\d+)+;)+\s*?\n'
    )
nauty_optional_getcanon_pattern = re.compile(
    r'(?P<canon_label>(\s+\d+)+)\s*?\n'
    r'(?P<relabel_graph>{relabel_graph})'
    .format(
        relabel_graph = nauty_graph_basic_pattern.pattern
        )
    )


nauty_output_pattern = re.compile(
    r'(?P<options>{options})(?P<partition>{partition})(?P<graph>{graph})'
    r'(?P<opt_using_usr_partition>(?P<using_usr_partition>{using_usr_partition})?)'
    r'(?P<opt_automNmarker>((?P<autom>{autom})?(?P<marker>{marker})?)+)'
    r'(?P<exe_basic>{exe_basic})(?P<orbits>{orbits})'
    r'(?P<opt_canon>(?P<canon>{canon})?)\s*'
    .format(
        options = nauty_options_pattern.pattern,
        partition = nauty_partition_pattern.pattern,
        graph = nauty_graph_pattern.pattern,
        using_usr_partition = nauty_exe_opt_output_using_usr_partition_pattern.pattern,
        autom = nauty_exe_optional_writeautoms_pattern.pattern,
        marker = nauty_exe_optional_writemarkers_pattern.pattern,
        exe_basic = nauty_exe_basic_output_pattern.pattern,
        orbits = nauty_orbits_pattern.pattern,
        canon = nauty_optional_getcanon_pattern.pattern
        )
    )
    
def parse_nauty_output(nauty_outs):
    '''

>>
m=1 n=5 labelorg=0 g=undef options=(+c+a+m-p-d y=100 k=(0,1))

linelen=0 worksize=120 input_depth=0; 1 cell

unit partition

n=5 $=0 g

  0 :  1 2;

  1 :  0 4;

  2 :  0;

  3 : ;

  4 :  1;

$$

(0 1)(2 4)

level 1:  3 orbits; 2 fixed; index 2

3 orbits; grpsize=2; 1 gen; 3 nodes; maxlev=2

tctotal=2; canupdates=1; cpu time = 0.00 seconds

 0 1; 2 4; 3;

 3 2 4 0 1

  0 : ;

  1 :  3;

  2 :  4;

  3 :  1 4;

  4 :  2 3;


>>
m=1 n=5 labelorg=0 g=undef options=(-c+a+m-p-d y=100 k=(0,1))

linelen=0 worksize=120 input_depth=0; 3 cells

[ 2 3 | 1 4 | 0 ]

n=5 $=0 g

  0 :  1 2 4;

  1 :  0 4;

  2 :  0;

  3 : ;

  4 :  0 1;

$$

[fixing partition]

(1 4)

level 1:  4 orbits; 1 fixed; index 2

4 orbits; grpsize=2; 1 gen; 3 nodes; maxlev=2

tctotal=2; cpu time = 0.00 seconds

 0; 1 4; 2; 3;


>>
m=1 n=5 labelorg=0 g=undef options=(-c-a-m-p+d y=100 k=(0,1))

linelen=0 worksize=120 input_depth=0; 1 cell

unit partition

n=5 $=0 g

  0 :  1 2 4;

  1 :  4;

  2 : ;

  3 : ;

  4 : ;

$$

5 orbits; grpsize=1; 0 gens; 1 node; maxlev=1

tctotal=0; cpu time = 0.00 seconds

 0; 1; 2; 3; 4;


m=1 n=5 labelorg=0 g=undef options=(-c+a-m+p-d y=100 k=(0,1))

linelen=0 worksize=120 input_depth=0; 1 cell

unit partition

n=5 $=0 g

  0 :  1 2 4;

  1 :  0 4;

  2 :  0;

  3 : ;

  4 :  0 1;

$$

 0 4 2 3 1

4 orbits; grpsize=2; 1 gen; 3 nodes; maxlev=2

tctotal=2; cpu time = 0.00 seconds

 0; 1 4; 2; 3;

 

m=1 n=5 labelorg=0 g=undef options=(-c-a-m-p-d y=100 k=(0,1))

linelen=0 worksize=120 input_depth=0; 1 cell

unit partition

n=5 $=0 g

  0 :  1 2 4;

  1 :  0 4;

  2 :  0;

  3 : ;

  4 :  0 1;

$$

4 orbits; grpsize=2; 1 gen; 3 nodes; maxlev=2

tctotal=2; cpu time = 0.00 seconds

 0; 1 4; 2; 3;

 
'''
    # output_options, output_partition, output_graph, output_orbits_after_exe,
    # output_if_getcanon_after_exe

    m = nauty_output_pattern.match(nauty_outs)
    if not m or m.end() != len(nauty_outs) or m.start() != 0:
        print(m)
        if m:
            print(m.start())
            print(m.end())
            print(nauty_outs[:m.end()])
        print(nauty_outs)
        print(repr(nauty_outs))
        raise ValueError('not nauty output')

    keys = ['options', 'partition', 'graph', 'opt_using_usr_partition',
            'opt_automNmarker', 'exe_basic', 'orbits', 'opt_canon']
    d = {key: m.group(key) for key in keys}
    for key in keys:
        if not d[key]:
            del d[key]


    
    return d
    
    
    pass

def make_nauty_graph_args(graph):
    n = len(graph)
    if not n > 0:
        raise ValueError('not 0 < order(G)')

    ls = []
    for i, vtc in enumerate(graph):
        for v in vtc:
            if not isinstance(v, int):
                raise ValueError('vertex should be an integer')
            if not 0 <= v < n:
                raise ValueError('not 0 <= vertex < order(G)')
        s = set(vtc)
        if len(s) < len(vtc):
            raise ValueError('not allow multiedges')
        if i in s:
            raise ValueError('not allow loop')

        ls.append(' '.join(str(v) for v in vtc))
    return [str(n)], ';\n'.join(ls) + '.\n'
            
outs = '''m=1 n=5 labelorg=0 g=undef options=(-c+a+m-p-d y=100 k=(0,1))
linelen=0 worksize=120 input_depth=0; 3 cells
[ 2 3 | 1 4 | 0 ]
n=5 $=0 g
  0 :  1 2 4;
  1 :  0 4;
  2 :  0;
  3 : ;
  4 :  0 1;
$$
[fixing partition]
(1 4)
level 1:  4 orbits; 1 fixed; index 2
4 orbits; grpsize=2; 1 gen; 3 nodes; maxlev=2
tctotal=2; cpu time = 0.00 seconds
 0; 1 4; 2; 3;

'''

parse_nauty_output(outs)

outs = call_nauty(['5'], '''1 2 3;
4;
.''')
parse_nauty_output(outs)


args, gs = make_nauty_graph_args([[1,2,4], [4], [], [], []])
outs = call_nauty(args+['-c', '-f', '[2 3 | 1 4]'], gs)
parse_nauty_output(outs)
#nfly dpcam

_options = 'dpcma'
for i,p in enumerate(_options):
    ls = ['-'+o for o in _options]
    ls.append('+'+p)
    outs = call_nauty(args+ls, gs)
    parse_nauty_output(outs)
else:
    ls.append('+p')
    outs = call_nauty(args+ls, gs)
    parse_nauty_output(outs)
    
    ls.pop()
    ls.pop()
    outs = call_nauty(args+ls, gs)
    parse_nauty_output(outs)

'''
MTOOBIG = 'm is too big'
NTOOBIG = 'n is too big'
CANONGNIL = 'canong = NULL, but options.getcanon = TRUE'


class Stats:
    def __init__(self, grpsize1:'double', grpsize2:'int', numorbits, numgenerators,
                 errstatus:'MTOOBIG|NTOOBIG|CANONGNIL',
                 numnodes, numbadleaves, maxlevel, tctotal, canupdates, invapplics,
                 invsuccesses, invarsuclevel, , ):pass

class Options:
##options for nauty
##
##Some of the fields in the options argument may change the canonical labelling
##produced by nauty. These fields are digraph, defaultptn, tc level, userrefproc,
##invarproc, mininvarlevel, maxinvarlevel, invararg and dispatch.
##The canonical labelling also depends on whether the graph is in packed
##or sparse form. If nauty is used to test two graphs for isomorphism,
##it is important that the same values of these options be used for both graphs.



    def __init__(self, 
                 dispatch:'dispatch_graph | dispatch_sparse',
                 defaultptn = True, digraph = False,
##                Two rules are available to choose target cells.
##                On levels up to level tc_level, inclusive, an expensive but (empirically)
##                highly effective rule is used. (The root of the search tree is at level one.)
##                At deeper levels, a cheaper rule is used.
##                For difficult graphs, a large value is recommended.
                 tc_level = 100,
                 # A value of 0 indicates no limit.
                 linelength = 0,
                 writeautoms = False, writemarkers = False, cartesian = False,
                 getcanon = True,

                 # only writeautoms and writemarkers 
                 outfile_fd = None,

                 
                 mininvarlevel = 0,
                 maxinvarlevel = 1,
                 invararg = 0,
                 userrefproc = None, userautomproc = None, userlevelproc = None,
                 usernodeproc = None, invarproc = None,
                 extra_options = None):pass

def nauty(graph, coloring, options, workspace, worksize, m, n, *, active_set=None):
    assert n >= 1 # required by nauty.c !!!
    assert n == len(graph)
    assert options.linelength >= 0

    g = graph

    if options.getcanon == False:
        assert type(options.mininvarlevel) == int
        assert type(options.maxinvarlevel) == int
    else:
        options.mininvarlevel = abs(options.mininvarlevel)
        options.maxinvarlevel = abs(options.maxinvarlevel)
        
    if options.defaultptn == True or active_set == None:
        active = None
    else:
##        The most common places where this feature may save a little time are:
##        (a) If the initial colouring is known to be already equitable, active can be the empty set.
##        (Don't confuse this with NULL, which causes nauty to set the active set to include every
##        cell.)
##        (b) If the graph is regular and the colouring has exactly two cells, active can indicate
##        just one of them (the smallest for best efficiency).
##        If nauty is used to test two graphs for isomorphism, it is essential that exactly the same
##        value of active be used for each of them.
        active = 

    # begin set (lab, ptn) # labels, partition
    if coloring is None or options.defaultptn == True:
        coloring = [list(range(n))]

    # vtc may be []
    lab = list(v for vtc in coloring for v in vtc)
    assert list(range(n)) == sorted(lab)
    ptn = [1] * n
    _s = set(itertools.accumulate(len(vtc) for vtc in coloring))
    _s.discard(0)
    for i in _s:
        ptn[i-1] = 0
    del i, _s
    # end set (lab, ptn) # labels, partition

    WORDSIZE = 8 * sizeof int;
    typedef setword[m] set;
    assert 1 <= n <= m * WORDSIZE
    if MAXN != 0:
        MAXM = ceil(MAXN/WORDSIZE)
        assert n <= MAXN
        assert m <= MAXM
    if not worksize >= 50*m:
        warnings.warn('the efficiency may suffer', ResourceWarning)
    workspace = new char[worksize * sizeof setword];

    # options
    DEFAULTOPTIONS GRAPH(options); - for packed graphs # options.dispatch = dispatch_graph
    DEFAULTOPTIONS SPARSEGRAPH(options); - for sparse graphs # options.dispatch = dispatch_sparse
    if options.linelength < 100 and options.linelength != 0:
        warnings.warn(
            '"options.linelength >= 100" to protect your code from breaking \
if additional fields are added to options in future editions of nauty, \
which is quite likely. ', FutureWarning)
        
    
    return lab, ptn, orbits, stats, canong
    
    
def _nauty(g, lab, ptn, active, orbits, options, stats, workspace, worksize, m, n, canong):pass



'''
