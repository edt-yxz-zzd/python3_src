#__all__:goto
r'''[[[
e ../../python3_src/seed/math/constants/lnN.py

seed.math.constants.lnN
py -m nn_ns.app.debug_cmd   seed.math.constants.lnN -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.constants.lnN:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/math/prime_pint/generate_primes.py
to eval:_gt_ln2
]]


'#'; __doc__ = r'#'

>>> (A_lt_ln2, A_gt_ln2) = interval5lnN__via_floor_numerator4denominator_(2**64, 2)
>>> (A_lt_ln2, A_gt_ln2)
(Fraction(12786308645202655659, 18446744073709551616), Fraction(3196577161300663915, 4611686018427387904))

>>> (B_lt_ln2, B_gt_ln2) = interval5lnN__via_limit_denominator_(2**64, 2)
>>> (B_lt_ln2, B_gt_ln2)
(Fraction(3052446177238342414, 4403748962482230453), Fraction(1385328996563313413, 1998607273341576092))

>>> (A_lt_ln2 < B_lt_ln2 < B_gt_ln2 < A_gt_ln2) # B better
True



>>> from math import log as ln_
>>> for n in range(1, 1+1024):
...     if not lt_ln_(n) < ln_(n) < gt_ln_(n):
...         # since "float" has only 53bits
...         assert n*2 == 2**n.bit_length()
...         xs = (n, (a:=lt_ln_(n), b:=ln_(n), c:=gt_ln_(n)), (a<=b, b<=c), (A:=float(a), b, C:=float(c)))
...         if not A == b < C:print(*xs, sep=':')



>>> # [n:=1] => [fn==1>=1] as above
>>> for n in range(1, 1+1024):
...     fn = 1/Fraction(n)
...     if not lt_ln_(fn) < ln_(fn) < gt_ln_(fn):
...         # since "float" has only 53bits
...         assert n*2 == 2**n.bit_length()
...         xs = (n, (a:=lt_ln_(fn), b:=ln_(fn), c:=gt_ln_(fn)), (a<=b, b<=c), (A:=float(a), b, C:=float(c)))
...         if not A < b == C:print(*xs, sep=':')
1:(Fraction(0, 1), 0.0, Fraction(1385328996563313413, 1998607273341576092)):(True, True):(0.0, 0.0, 0.6931471805599453)




















[[

py_adhoc_call   seed.math.constants.lnN   @interval5lnX__via_floor_numerator4denominator_ ='2**64'  :2 +str_ok
py_adhoc_call   seed.math.constants.lnN   @interval5lnN__via_floor_numerator4denominator_ ='2**64'  =2
(Fraction(12786308645202655659, 18446744073709551616), Fraction(3196577161300663915, 4611686018427387904))

===
vs:
===
py_adhoc_call   seed.math.constants.lnN   @interval5lnX__via_limit_denominator_ ='2**64'  :2 +str_ok
py_adhoc_call   seed.math.constants.lnN   @interval5lnN__via_limit_denominator_ ='2**64'  =2
(Fraction(3052446177238342414, 4403748962482230453), Fraction(1385328996563313413, 1998607273341576092))

]]
[[
py_adhoc_call { +lineno }  seed.math.constants.lnN   ,iter_intervals5lnNs__via_limit_denominator_ ='2**64'  ='range(1,101)'
1:(Fraction(0, 1), Fraction(0, 1))
2:(Fraction(3052446177238342414, 4403748962482230453), Fraction(1385328996563313413, 1998607273341576092))
3:(Fraction(9516124465995262291, 8661949774412253525), Fraction(18367491259745028463, 16718811039345510014))
4:(Fraction(6104892354476684828, 4403748962482230453), Fraction(1385328996563313413, 999303636670788046))
5:(Fraction(3174935142468085078, 1972698118976419443), Fraction(4432711515015872125, 2754198519104024633))
6:(Fraction(9484881574221498541, 5293613198153140933), Fraction(16317458115362895553, 9106946772488919828))
7:(Fraction(3612028256345838800, 1856215333528827489), Fraction(9172422087621737809, 4713692506344499207))
8:(Fraction(3052446177238342414, 1467916320827410151), Fraction(1103540812451597825, 530690952514165941))
9:(Fraction(664757672245496119, 302544254739498518), Fraction(18367491259745028463, 8359405519672755007))
10:(Fraction(7013186985772460987, 3045788408476679291), Fraction(9948944967727459672, 4320771900243161573))
11:(Fraction(14365547793331778696, 5990898750372456467), Fraction(20760283098622622803, 8657710507262955125))
12:(Fraction(21366254519296871648, 8598413353322440749), Fraction(16076396907246199109, 6469618047268599055))
13:(Fraction(13286697514340779647, 5180101305193127288), Fraction(4649197926607704086, 1812588585066214961))
14:(Fraction(4377692568071680707, 1658809196354174411), Fraction(10425188855046262160, 3950345730672748837))
15:(Fraction(1476747238062685239, 545317526780571044), Fraction(34286534896474386167, 12660967245924518173))
16:(Fraction(12209784708953369656, 4403748962482230453), Fraction(50224467832376792037, 18114647668264315835))
17:(Fraction(449908031573953433, 158797794919967186), Fraction(475161048900857764, 167711002031560991))
18:(Fraction(26351160502239904885, 9116875858702795454), Fraction(9420738558729229684, 3259351857764611291))
19:(Fraction(35137937491361937845, 11933661298462145433), Fraction(32871804329029726587, 11164029739320870586))
20:(Fraction(18525684430345776207, 6184025386343288174), Fraction(41976694291943943740, 14012164792731907337))
21:(Fraction(39108226588967843519, 12845438780280914614), Fraction(46849015404665514521, 15387968511638695547))
22:(Fraction(13346313753125857508, 4317738741706872075), Fraction(49374041076386124587, 15973265272608227878))
23:(Fraction(6550303803277730935, 2089081768992088941), Fraction(30486113839922056446, 9722905462572515651))
24:(Fraction(8139598239323136451, 2561189543611972667), Fraction(4527823020496463449, 1424715647437834582))
25:(Fraction(34203915747579189953, 10626043876352295937), Fraction(8865423030031744250, 2754198519104024633))
26:(Fraction(7977134499179129810, 2448403356403717801), Fraction(5944243701769631361, 1824452907518616436))
27:(Fraction(9516124465995262291, 2887316591470751175), Fraction(7521851449258773934, 2282228081991754139))
28:(Fraction(11674042832763741479, 3503399265295974340), Fraction(10782439797422631587, 3235827742414195901))
29:(Fraction(5887311149960847383, 1748379544658093173), Fraction(39820375111402260425, 11825624216557834628))
30:(Fraction(24532967786200521621, 7213038537096406573), Fraction(17666745275016672130, 5194272279012217909))
31:(Fraction(14728511021578003371, 4289040740262814141), Fraction(61712796970110983419, 17971178485903389418))
32:(Fraction(15262230886191712070, 4403748962482230453), Fraction(50224467832376792037, 14491718134611452668))
33:(Fraction(62647940225005964133, 17917290074079122645), Fraction(38026644039335606357, 10875607551492536408))
34:(Fraction(55493743720558282117, 15736832162559069568), Fraction(52472017484782821895, 14879935593225912627))
35:(Fraction(33894731992526881669, 9533449723155271396), Fraction(16379195777107447574, 4606917661458394987))
36:(Fraction(2652305033080101529, 740139811908681019), Fraction(16317458115362895553, 4553473386244459914))
37:(Fraction(64647403028553925677, 17903315609081110600), Fraction(5786117659856316238, 1602395235736395787))
38:(Fraction(5878249395949155527, 1615975302806658294), Fraction(4567918097065076543, 1255755299390260783))
39:(Fraction(4721969523237015201, 1288901342284090979), Fraction(43982048692726607549, 12005270537535856470))
40:(Fraction(63141453753882366835, 17116702928165717444), Fraction(40419190271142386299, 10957037434786824553))
41:(Fraction(18580116516141962875, 5003300375595322936), Fraction(6102369492385408166, 1643261362045167421))
42:(Fraction(29089648991681496904, 7782830469923061407), Fraction(23777427158381403263, 6361564714567219260))
43:(Fraction(8018376363150852007, 2131866456585033243), Fraction(6742729072817855741, 1792706813095080866))
44:(Fraction(27104641265464879284, 7162601213882597401), Fraction(33964342476155808301, 8975327814369632925))
45:(Fraction(38008433455416241045, 9984713264587198118), Fraction(64119534084194325527, 16844029187379589893))
46:(Fraction(22379490351272532227, 5845282447135102179), Fraction(9573748380369543526, 2500560222001666939))
47:(Fraction(27028441711520113582, 7020105332978746627), Fraction(16212754512487043901, 4210943628573118493))
48:(Fraction(25413493972343933948, 6564757009707395847), Fraction(56915966176955464235, 14702405278512593653))
49:(Fraction(67818982869698003463, 17426031438970160969), Fraction(18344844175243475618, 4713692506344499207))
50:(Fraction(51695838318479771060, 13214604885183181601), Fraction(21295889774232027501, 5443702591902658735))
51:(Fraction(1304966052013178619, 331898251324278503), Fraction(60573468074758952, 15405939564209045))
52:(Fraction(63767376993120924003, 16138558270461393178), Fraction(71169534368888851180, 18011932302277746013))
53:(Fraction(6068444688530149631, 1528463100613894780), Fraction(44704622158288408881, 11259782185207709509))
54:(Fraction(61541256440982875665, 15427802097626479739), Fraction(5765459375992111124, 1445345308151312619))
55:(Fraction(15479557971839912710, 3862807821641594353), Fraction(26262761717731992187, 6553675600150640631))
56:(Fraction(18201651060250698767, 4521754236317804720), Fraction(27217969060520796749, 6761637529253992737))
57:(Fraction(12157214748527081202, 3006940536531573623), Fraction(18371440317854061887, 4543954330733423300))
58:(Fraction(17620757192315411853, 4339614457473733291), Fraction(38707513459586383477, 9532830126921904702))
59:(Fraction(61572464672159138194, 15100404476771939761), Fraction(14505866606235511413, 3557506658317989218))
60:(Fraction(29540661759442237989, 7214991633095432530), Fraction(69771764257885529929, 17041009421058273421))
61:(Fraction(32501914401909137432, 7906327334722348457), Fraction(32439871992149187185, 7891235066798329617))
62:(Fraction(45066502378460764041, 10919562624798897596), Fraction(27848655936878619227, 6747697879136144251))
63:(Fraction(16881772702344018902, 4074637639661603675), Fraction(19593224776381846815, 4729082221626566662))
64:(Fraction(6104892354476684828, 1467916320827410151), Fraction(4155986989689940239, 999303636670788046))
65:(Fraction(26285395545064572123, 6296827257649654343), Fraction(5680990617922358270, 1360916046024734883))
66:(Fraction(22946389173034949342, 5476916496927473753), Fraction(76956946534296002385, 18368326574106666412))
67:(Fraction(15759206183631332187, 3748004339473926643), Fraction(29111220558990895777, 6923507422335083030))
68:(Fraction(5461782341036726680, 1294412221202182167), Fraction(1745766283604241623, 413736958333479278))
69:(Fraction(13886772314088640393, 3279740908503558125), Fraction(36183216754236637115, 8545655787106451118))
70:(Fraction(10560539203462203923, 2485712846972163715), Fraction(42665293626140404888, 10042448254116397053))
71:(Fraction(9556664985823592435, 2241938231696812407), Fraction(30638273746907700393, 7187561494337085370))
72:(Fraction(25878108577118557785, 6051000442155724687), Fraction(25879367043406808788, 6051294705549973603))
73:(Fraction(22473544785348153691, 5238027557098372036), Fraction(26480504663891399766, 6171950819514934325))
74:(Fraction(11270028711432812290, 2618461493351351053), Fraction(52883125085818832097, 12286785617930765366))
75:(Fraction(9309103170196774309, 2156138691154843399), Fraction(9510707674181891078, 2202833551379945269))
76:(Fraction(19995211641018704128, 4617049831956797245), Fraction(45291195631137805333, 10458089213163914028))
77:(Fraction(28301245102952465881, 6515311427295732394), Fraction(6518901125873644339, 1500735068167891365))
78:(Fraction(50181152243498197183, 11518133122894035645), Fraction(6132578939974324300, 1407617351521311653))
79:(Fraction(49154089952171842037, 11249496872795744994), Fraction(4032964553022754692, 922991803356965131))
80:(Fraction(8928243034511870989, 2037468910815127226), Fraction(24172528321104166835, 5516289684282836481))
81:(Fraction(37399740191735553045, 8510677647042504266), Fraction(74134722711225609971, 16870083166715259273))
82:(Fraction(22947401805525510263, 5207366414316398014), Fraction(58818120931113229271, 13347371963309952311))
83:(Fraction(46660209182464754393, 10559378199824073366), Fraction(13306414314368406274, 3011290855544909731))
84:(Fraction(995988579607956371, 224786675871582878), Fraction(54788699201169168570, 12365372275259050729))
85:(Fraction(17603353355887538493, 3962353184974988171), Fraction(25188229441586983742, 5669639138293655517))
86:(Fraction(2959878622997800883, 664492107628723837), Fraction(65749801183244805514, 14760816077036940699))
87:(Fraction(42352433257189159151, 9483498570039639000), Fraction(15183800603117672313, 3399935735286018649))
88:(Fraction(18836598839986258561, 4207098911807352055), Fraction(2555141759577275617, 570683391813366294))
89:(Fraction(41773393949024551799, 9306477626637727930), Fraction(75004520304041887207, 16709867791878582291))
90:(Fraction(11486821109471436648, 2552734882368559711), Fraction(17106254624564244271, 3801550704989867910))
91:(Fraction(773638351653432466, 171505751960519985), Fraction(837164685200510361, 185588729596001924))
92:(Fraction(34614020387070660656, 7654940030314305433), Fraction(53081888970665633993, 11739135535900563878))
93:(Fraction(73870474913354479892, 16297595899425913949), Fraction(47365950377138860793, 10450063026457062393))
94:(Fraction(44895191320355113495, 9881637329709818709), Fraction(62922077458139557494, 13849437571977506651))
95:(Fraction(1246630063133425088, 273751375543943357), Fraction(2228725401587939733, 489412747564331860))
96:(Fraction(79359628221133790984, 17386847999344402649), Fraction(9434290184262822825, 2066952342044894536))
97:(Fraction(30934856066572114311, 6762144365389495213), Fraction(38130287444850811375, 8335015616073988334))
98:(Fraction(6104767181338866189, 1331474478224426959), Fraction(4415490493273992496, 963036382224085067))
99:(Fraction(76400481266733092992, 16626439300488613315), Fraction(54286282132482832491, 11813899071836570417))
100:(Fraction(16962131953499920659, 3683280154359920432), Fraction(19897889935454919344, 4320771900243161573))
===
]]

]]]'''#'''
__all__ = r'''
lt_ln_
gt_ln_


interval5lnN__via_limit_denominator_
    interval5lnX__via_limit_denominator_
    iter_intervals5lnNs__via_limit_denominator_
        iter_intervals5lnXs__via_limit_denominator_











interval5lnN__via_floor_numerator4denominator_
    interval5lnX__via_floor_numerator4denominator_
        floor_DlnX_
            floor_D_times_cf_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_int_ge
    from seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_ import cf_ln_
    from seed.math.continued_fraction.continued_fraction_fold import calc_ND5finite_continued_fraction_, calc_Fraction5finite_continued_fraction_
    from seed.math.continued_fraction.convert_to_ContinuedFraction_ import convert_to_ContinuedFraction_

    from fractions import Fraction
    from math import floor, ceil

#.#################################
___end_mark_of_excluded_global_names__0___ = ...


def floor_D_times_cf_(D, cf, /):
    'D/int -> cf/ContinuedFraction -> (floor(D*cf))/int'
    check_type_is(int, D)
    return (floor(D*cf))
def floor_DlnX_(D, x, /, *, str_ok:bool):
    'D/int -> x/cf_like{>0} -> (floor(D*ln_(X)))/int'
    check_type_is(int, D)
    cf__X = convert_to_ContinuedFraction_(x, str_ok=str_ok)
    cf__lnX = cf_ln_(cf__X)
    return floor_D_times_cf_(D, cf__lnX)
def interval5lnX__via_floor_numerator4denominator_(D, x, /, *, str_ok:bool):
    'D/int{>=1} -> x/cf_like{>0} -> (a/Fraction, b/Fraction) # [a <= ln_(x) < b == a+1/D][a:=(floor(D*ln_(x))/D)]'
    check_int_ge(1, D)
    #numerator
    na = floor_DlnX_(D, x, str_ok=str_ok)
    nb = 1+na
    a = Fraction(na, D)
    b = Fraction(nb, D)
    return (a, b)
def interval5lnN__via_floor_numerator4denominator_(D, N, /):
    'D/int{>=1} -> N/int{>=1} -> (a/Fraction, b/Fraction) # [a <= ln_(N) < b == a+1/D][a:=(floor(D*ln_(N))/D)]'
    check_int_ge(1, N)
    return interval5lnX__via_floor_numerator4denominator_(D, N, str_ok=False)




def interval5lnN__via_limit_denominator_(max_denominator, N, /):
    'max_denominator/int{>=1} -> N/int{>=1} -> (a/Fraction, b/Fraction) # [a <= ln_(N) <= b][a.numerator <= max_denominator][b.numerator <= max_denominator]'
    check_int_ge(1, N)
    return interval5lnX__via_limit_denominator_(max_denominator, N, str_ok=False)

def interval5lnX__via_limit_denominator_(max_denominator, x, /, *, str_ok:bool):
    'max_denominator/int{>=1} -> x/cf_like{>0} -> (a/Fraction, b/Fraction) # [a <= ln_(x) <= b][a.numerator <= max_denominator][b.numerator <= max_denominator]'
    check_int_ge(1, max_denominator)
    cf__X = convert_to_ContinuedFraction_(x, str_ok=str_ok)
    cf__lnX = cf_ln_(cf__X)
    (a, b) = (lower_approximate_fraction4lnX, upper_approximate_fraction4lnX) = cf__lnX.to_Fraction__via_limit_denominator_(max_denominator, case=3)
    return (a, b)

def iter_intervals5lnXs__via_limit_denominator_(max_denominator, xs, /, *, str_ok:bool):
    'max_denominator/int{>=1} -> Iter x/cf_like{>0} -> Iter (a/Fraction, b/Fraction) # [a <= ln_(x) <= b][a.numerator <= max_denominator][b.numerator <= max_denominator]'
    return (interval5lnX__via_limit_denominator_(max_denominator, x, str_ok=str_ok) for x in xs)

def iter_intervals5lnNs__via_limit_denominator_(max_denominator, Ns, /):
    'max_denominator/int{>=1} -> Iter N/int{>=1} -> Iter (a/Fraction, b/Fraction) # [a <= ln_(N) <= b][a.numerator <= max_denominator][b.numerator <= max_denominator]'
    return (interval5lnN__via_limit_denominator_(max_denominator, N) for N in Ns)










if 0:
    (_lt_ln2, _gt_ln2) = ...
    # [_lt_ln2 < ln2 < _gt_ln2]
def _gmk_lt_ln2():
    try:
        return _lt_ln2
    except NameError:
        pass
    _mk_bounds4ln2()
    return _gmk_lt_ln2()
def _gmk_gt_ln2():
    try:
        return _gt_ln2
    except NameError:
        pass
    _mk_bounds4ln2()
    return _gmk_gt_ln2()


def _mk_bounds4ln2():
    global _lt_ln2, _gt_ln2
    (_lt_ln2, _gt_ln2) = (Fraction(3052446177238342414, 4403748962482230453), Fraction(1385328996563313413, 1998607273341576092))
    return (_lt_ln2, _gt_ln2)
    from seed.math.constants.lnN import interval5lnN__via_limit_denominator_
    (_lt_ln2, _gt_ln2) = interval5lnN__via_limit_denominator_(2**64, 2)
    return (_lt_ln2, _gt_ln2)



def lt_ln_(n, /):
    'n/Rational{>0} -> lower_bound{ln_(n)} # [lower_bound{ln_(n)} <= floor(ln_(n))] # for roughly fast calc'
    if n < 1:
        if not n > 0:raise TypeError
        n = 1/Fraction(n)
        assert n >= 1
        return -gt_ln_(n)
    assert n >= 1
    n = floor(n)
    le_lbN = -1+n.bit_length()
    # [le_lbN == floor_log2(floor(n)) <= log2(n)]
    _lt_ln2 = _gmk_lt_ln2()
    # !! [_lt_ln2 < ln2 < _gt_ln2]
    lt_lnN = _lt_ln2*le_lbN
    # [lt_lnN < ln(2)*log2(n) == ln(n)]
    return lt_lnN
def gt_ln_(n, /):
    'n/Rational{>0} -> upper_bound{ln_(n)} # [upper_bound{ln_(n)} >= ceil(ln_(n))] # for roughly fast calc'
    if n < 1:
        if not n > 0:raise TypeError
        n = 1/Fraction(n)
        assert n >= 1
        return -lt_ln_(n)
    assert n >= 1
    n = ceil(n)
    gt_lbN = n.bit_length()
    # [gt_lbN == 1+floor_log2(floor(n)) > log2(n)]
    _gt_ln2 = _gmk_gt_ln2()
    # !! [_lt_ln2 < ln2 < _gt_ln2]
    gt_lnN = _gt_ln2*gt_lbN
    # [gt_lnN  > ln(2)*log2(n) == ln(n)]
    return gt_lnN











__all__
if 1:
    #sometimes can be useful:
    from seed.math.constants.lnN import interval5lnN__via_floor_numerator4denominator_, interval5lnX__via_floor_numerator4denominator_
    from seed.math.constants.lnN import floor_DlnX_, floor_D_times_cf_




from seed.math.constants.lnN import interval5lnN__via_limit_denominator_, interval5lnX__via_limit_denominator_
from seed.math.constants.lnN import iter_intervals5lnNs__via_limit_denominator_, iter_intervals5lnXs__via_limit_denominator_
from seed.math.constants.lnN import lt_ln_, gt_ln_
from seed.math.constants.lnN import *
