/*
__all__:goto
TODO:goto
precomputation4genetate_data:goto
genetate_data__7all_per_deg:goto
genetate_data__7one_per_deg:goto

*/


/*
__all__:here
is_primitive_polynomial_mod_
  is_primitive_root_
    list_accumulate_L2R_
    impl4is_primitive_root__7recur_

show_all_trinomial_binary_primitive_polynomial__7deg_ge_le_
  list_all_trinomial_binary_primitive_polynomial__7deg_eq_

list_all_monic_primitive_polynomial_mod__7deg_eq_
  list_all_binary_primitive_polynomial__7deg_eq_

show_one_binary_primitive_polynomial_per_deg_ge_le_
  find_one_binary_primitive_polynomial__7deg_eq_
    zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_
      inplace_inc_exp_vec_

show_may_pentanomial_binary_primitive_polynomial_per_deg_ge_le_
  show_may_binary_primitive_polynomial_per_deg_ge_le__7bit_count_eq_

mk_one_random_irreducible_binary_polynomial_mod_
  exps5binary_polynomial__7descend_
  coeffs5polynomial__7little_endian_

===
print_methods6my_fmt7gp ../../python3_src/pari_gp_script/polynomial7primitive7finite_field.gp
  \\ total:25
  list_accumulate_L2R_
  is_primitive_root_
  impl4is_primitive_root__7recur_
  is_primitive_polynomial_mod_
  list_all_trinomial_binary_primitive_polynomial__7deg_eq_
  show_all_trinomial_binary_primitive_polynomial__7deg_ge_le_
  list_all_binary_primitive_polynomial__7deg_eq_
  list_all_monic_primitive_polynomial_mod__7deg_eq_
  show_may_pentanomial_binary_primitive_polynomial_per_deg_ge_le_
  show_one_pentanomial_binary_primitive_polynomial_per_deg_ge_le_
  show_one_binary_primitive_polynomial_per_deg_ge_le_
  find_one_binary_primitive_polynomial__7deg_eq_
  show_may_binary_primitive_polynomial_per_deg_ge_le__7bit_count_eq_
  zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_
  advance_exp_vec_
  inplace_inc_exp_vec_
  inplace_inc_exp_vec__7mode_eq0_
  inplace_inc_exp_vec__7mode_eq1_
  inplace_inc_exp_vec__7mode_eq2_
  listassign_
  auto_sleep_
  auto_sleep7finer_
  mk_one_random_irreducible_binary_polynomial_mod_
  exps5binary_polynomial__7descend_
  coeffs5polynomial__7little_endian_

*/

/*
__doc__:here

e ../../python3_src/pari_gp_script/polynomial7primitive7finite_field.gp
gp7my
  read("polynomial7primitive7finite_field.gp");
gp
  read("../../python3_src/pari_gp_script/polynomial7primitive7finite_field.gp");


output:move_to:
view ../../python3_src/pari_gp_script/polynomial7primitive7finite_field.gp.out.txt
    precomputation4genetate_data:here
    genetate_data__7all_per_deg:here
    genetate_data__7one_per_deg:here




===
output format mimic:
view ../../fxt/_ignore__unzip/fxt/data/all-primpoly.txt
view ../../fxt/_ignore__unzip/fxt/data/all-trinomial-primpoly.txt
===

TODO:
  * half-DONE:trinomial:symmetry-copy
  * window limit lowbits in byte #=>mode
  * addhelp

DONE:
  * Mersenne_prime
    [[deg :: exponent{Mersenne_prime}][f :: polynomial{deg}]-> [[is_irreducible_polynomial_mod_(2;f)] <-> [[is_primitive_polynomial_mod_(2;f)]]]]
    view ../../python3_src/nn_ns/math_nn/numbers/Mersenne_exponents.py
    ==>>:
    ++kw:known_be_mulorder





*/



/*
trials6init:
===
polisirreducible
Mod(x,modulus)

x='x \\t_POL
f7bug=(x^127+1)*Mod(1,2) \\t_POL
polisirreducible(f7bug)
  0
f0=(x^127+x+1)*Mod(1,2) \\t_POL
polisirreducible(f0)
  1
f1=Mod(x,(x^127+1)*Mod(1,2)) \\t_POLMOD
x0=ffgen(f0) \\t_FFELT
  x
  \\未必是乘法群生成元
type(x0)
  "t_FFELT"
type(x)
  "t_POL"
type(f0)
  "t_POL"
type(f1)
  "t_POLMOD"
fforder(x0) == -1+2^127
  1
x0.mod \\t_POL \\ == f0
  x^127+x+1
x0.pol \\t_POL \\ == x
  x
x0.p
  2

f3=ffprimroot(ffgen(f0)) \\t_FFELT
  ...很长
  \\ 乘法群生成元
f4=minpoly(f3) \\t_POL
x4=ffgen(f4) \\t_FFELT
  x
  \\ minpoly=>[f4::primpoly]
  \\ => [x4::乘法群生成元]
fforder(x4) == -1+2^127
  1


ff=ffinit(2, 127)
f2=ffgen(ff)
  x
  \\未必是乘法群生成元
fforder(f2) == -1+2^127
  1


ffinit(2,5)
  Mod(1,2)*x^5+Mod(1,2)*x^4+Mod(1,2)*x^2+Mod(1,2)*x+Mod(1,2)
ffgen(ffinit(2,5))
  x
ffgen(ffinit(2,5)).mod
  x^5+x^4+x^2+x+1
ffgen([2,5]).mod
  x^5+x^4+x^2+x+1
ffgen(2^5).mod
  x^5+x^4+x^2+x+1

ffgen('x^2*Mod(1,2))
  *** ffgen: not an irreducible polynomial in ffgen: x^2.
iferr(ffgen('x^2*Mod(1,2)), E, print([type(E),Str(E),E]))
  ["t_ERROR","error(\"not an irreducible polynomial in ffgen: x^2.\")",error("not an irreducible polynomial in ffgen: x^2.")]







\\ order4ff-->order4multiplicative_group4ff-->mulorder4ff

view ../../python3_src/pari_gp_script/factorization4order4multiplicative_group4finite_field.gp
read("../../python3_src/pari_gp_script/factorization4order4multiplicative_group4finite_field.gp");



*/








{list_accumulate_L2R_(op, r0, xs)=
  ;my(rs=List(), r=r0)
  ;foreach(xs, x, r=op(r,x);listput(~rs,r))
  ;return(Vec(rs))
  ;
}
/*

list_accumulate_L2R_((r,x)->r+x, 0, [])
  []
list_accumulate_L2R_((r,x)->r+x, 0, [1])
  [1]
list_accumulate_L2R_((r,x)->r+x, 0, [1,2])
  [1,3]
list_accumulate_L2R_((r,x)->r+x, 0, [1,2,3,4])
  [1,3,6,10]

*/


{is_primitive_root_(factorization4order,x,not_mulorder_ok=0,known_be_mulorder=0)=
  \\;my(L=matsize(factorization4order)[1])
  ;my([L,num_cols]=matsize(factorization4order))
  ;if(2 <> num_cols, error("bad factorization4order"))
  ;my(base=x^prod(j=1,L, factorization4order[j,1]^(-1+factorization4order[j,2])))
  \\ ;my(ps=factorization4order~[1], exp=prod(j=1,L, ps[j]))
  ;my(ps=factorization4order[,1]~, exp=vecprod(ps))
  ;if(!known_be_mulorder && 1 <> base^exp, if(not_mulorder_ok, return(0), error("bad order")))
  \\ [1 == base^II(ps)]
  \\ [1 =?= base]
  ;if(0 == #ps, return(1))
  \\ [0 < len(ps)]
  \\ [1 == base^II(ps)]
  \\ [1 =?= base]

  \\ new_version:ver2.2:
  ;ps=vecsort(ps,,4) \\ reversed_sorted
  ;my(j2ez4p=vector(#ps, j, 1+logint(ps[j],2)))
  ;my(offset4sum_ez=0,j2sum_ez=list_accumulate_L2R_((r,x)->r+x, 0, j2ez4p))
  ;return(impl4is_primitive_root__7recur_(offset4sum_ez,j2sum_ez,ps,base))
  \\ new_version:ver2.1:
  ;return(impl4is_primitive_root__7recur_(ps,base))
  \\ old_version:ver1:
  ;for(j=1,L, if(0==-1+base^(exp/factorization4order[j,1]), return(0)))
  ;return(1)
}
{impl4is_primitive_root__7recur_(offset4sum_ez,j2sum_ez,ps,base)=
  \\ precodition:
  \\    [1 =?= base]
  \\    [0 < len(ps)]
  \\    [1 < II(ps)]
  \\    [1 == base^II(ps)]

  \\    [ps ::  reversed_sorted]

  ;if(#j2sum_ez <> #ps, error("bug:not satisfy precodition"))
  ;if(0 == #ps, error("bug:not satisfy precodition"))
  ;if(ps[1] < 2, error("bug:not satisfy precodition"))
  ;if(1 == base, return(0))
  \\ [1 =!= base]
  \\ [1 <= #ps]
  ;if(1 == #ps, return(1))
  \\ [2 <= #ps]
  \\ [1 =!= base]


  \\ new_version:ver2.2:
  \\ [1 =!= base]
  \\ [2 <= #ps]
  ;my(j=-1, double_mean=offset4sum_ez+j2sum_ez[#ps])
  ;vecmin(vector(#ps, k, abs(j2sum_ez[k]*2-double_mean)), &j)
  ;if(j==#ps, error("bug:", [offset4sum_ez, j2sum_ez, j]))
  ;my(psL=ps[1..j],psR=ps[1+j..#ps])
  ;my(j2sum_ezL=j2sum_ez[1..j],j2sum_ezR=j2sum_ez[1+j..#ps])
  ;my(offset4sum_ezL=offset4sum_ez,offset4sum_ezR=j2sum_ezL[j])
  ;return(impl4is_primitive_root__7recur_(offset4sum_ezL,j2sum_ezL,psL,base^vecprod(psR)) && impl4is_primitive_root__7recur_(offset4sum_ezR,j2sum_ezR,psR,base^vecprod(psL)))

  \\ new_version:ver2.1:
  \\ [1 =!= base]
  \\ [2 <= #ps]
  ;my(j= #ps \2)
  \\ [1 <= j]
  \\ [j < #ps]
  ;my(psL=ps[1..j],psR=ps[1+j..#ps])
  ;return(impl4is_primitive_root__7recur_(psL,base^vecprod(psR)) && impl4is_primitive_root__7recur_(psR,base^vecprod(psL)))
  ;
}
/*

===
for(j=1,-1+11,  print([j, is_primitive_root_(factorint(-1+11), Mod(j,11))]))
  [1,0]
  [2,1]
  [3,0]
  [4,0]
  [5,0]
  [6,1]
  [7,1]
  [8,1]
  [9,0]
  [10,0]

eulerphi(-1+11)
  4

for(j=1,-1+11,  print([j, is_primitive_root_(factorint(5), Mod(j,11))]))
  [1,0]
  ***   error("bad order")));

\\ [not_mulorder_ok := True]
for(j=1,-1+11,  print([j, is_primitive_root_(factorint(5), Mod(j,11), 1)]))
  [1,0]
  [2,0]
  [3,1]
  [4,1]
  [5,1]
  [6,0]
  [7,0]
  [8,0]
  [9,1]
  [10,0]


===
is_primitive_root_(factorint(-1+2^127), ffgen(Mod(1,2)*('x^127+'x+1)))
  1
is_primitive_root_(factorint(-1+2^127), 1+ffgen(Mod(1,2)*('x^127+'x+1)))
  1
is_primitive_root_(factorint(-1+2^127), (ffgen(Mod(1,2)*('x^127+'x+1)))^2)
  1
  \\ !! [is_prime_((-1+2^127))]
is_primitive_root_(factorint(-1+2^127), (ffgen(Mod(1,2)*('x^127+'x+1)))^0)
  0

is_primitive_root_(factorint(-1+2^4), ffgen(Mod(1,2)*('x^4+'x+1)))
  1
is_primitive_root_(factorint(-1+2^4), 1+ffgen(Mod(1,2)*('x^4+'x+1)))
  1
is_primitive_root_(factorint(-1+2^4), (ffgen(Mod(1,2)*('x^4+'x+1)))^2)
  1
is_primitive_root_(factorint(-1+2^4), (ffgen(Mod(1,2)*('x^4+'x+1)))^3)
  0
    \\ x
is_primitive_root_(factorint(-1+2^4), (ffgen(Mod(1,2)*('x^4+'x+1)))^5)
  0
    \\ (x^2+x)
is_primitive_root_(factorint(-1+2^4), (ffgen(Mod(1,2)*('x^4+'x+1)))^15)
  0
    \\ 1

===

*/








{is_primitive_polynomial_mod_(p, f, factorization4mulorder4ff=-1,using_ff_only=1,using_fforder_only=0)=
  ;fp=f*Mod(1,p)
  \\ ;return(polisirreducible(fp) && fforder(ffgen(fp)) == -1+p^poldegree(fp))
  \\ neednot: ;if(!polisirreducible(fp), return(0))
  \\    {but fforder(),ffgen() required}
  ;if(!ispseudoprime(p), error("[not ispseudoprime(p)] : ", p))
  ;my(known_be_mulorder=0)
  ;my(not_mulorder_ok=1)
  ;my(mulorder4ff=-1+p^poldegree(fp))
  ;if(-1==factorization4mulorder4ff,
    ;if(!polisirreducible(fp), return(0))
    ;known_be_mulorder=1
    ;my(x=ffgen(fp))
      \\ *** ffgen: not an irreducible polynomial in ffgen: x^1798+x^2+1.
    ;return(mulorder4ff == fforder(x)
  ))
  ;if(mulorder4ff <> factorback(factorization4mulorder4ff), error("bad factorization4mulorder4ff: [-1+", p, "^", poldegree(fp), "=!=", factorback(factorization4mulorder4ff), "]"))
  ;my(x=0)
  ;if(using_ff_only,
  \\ then:
      ;if(!polisirreducible(fp), return(0))
      ;known_be_mulorder=1
      ;x=ffgen(fp)
        \\ DONE: addprimes(),removeprimes() to use fforder() directly
      ;if(using_fforder_only,
        ;ps7old=addprimes()
        ;ps7new=addprimes(factorization4mulorder4ff[,1]~)
        ;my(order4x=fforder(x))
        ;removeprimes(ps7new)
        ;ps7now=addprimes(ps7old)
        ;if(ps7now <> ps7old, error("bug: [fail to restore addprimes()] : ", [ps7old, ps7now]))
        ;return(mulorder4ff == order4x)
        )
  , \\ else:
      ;x=Mod(variable(fp),fp)
        \\ slow if without:polisirreducible()
      ;known_be_mulorder=0
    )
  ;return(is_primitive_root_(factorization4mulorder4ff,x,not_mulorder_ok,known_be_mulorder)) \\ [not_mulorder_ok := True]
}
/*

is_primitive_polynomial_mod_(2,x^127+1,factorint(-1+2^127))
  0
    \\ test:[not_mulorder_ok := True]
is_primitive_polynomial_mod_(2,x^127+x+1,factorint(-1+2^127))
  1
    \\ test:[not_mulorder_ok := True]

is_primitive_polynomial_mod_(2,x^127+1)
  0
    \\ test:[not_mulorder_ok := False]
    \\ found:fforder() required precodition polisirreducible()
is_primitive_polynomial_mod_(2,x^127+x+1)
  1

is_primitive_polynomial_mod_(2,x^2+x+1)
  1
is_primitive_polynomial_mod_(2,x^2+1)
  0

is_primitive_polynomial_mod_(2,x^2+x+1, Mat([3,1]))
  1
is_primitive_polynomial_mod_(2,x^4+x+1, Mat([3,1]))
  ***   user error: bad factorization4mulorder4ff: [-1+2^4=!=3]

is_primitive_polynomial_mod_(2,x^4+x+1, [3,1;5,1])
  1

===
show_one_binary_primitive_polynomial_per_deg_ge_le_(1798,1798,~deg2factorization4mulorder4ff)
  [1798,685,0]
    \\ *** ffgen: not an irreducible polynomial in ffgen: x^1798+x^2+1.
    \\ slow if without:polisirreducible()
? ##
  ***   last result computed in 2,783 ms.
    \\ @[using_ff_only:=True]
===
is_primitive_polynomial_mod_(2,x^1798+x+1, deg2factorization4mulorder4ff[1798])
is_primitive_polynomial_mod_(2,x^1798+x+1, deg2factorization4mulorder4ff[1798], 1)
  0
    time = 35 ms.
is_primitive_polynomial_mod_(2,x^1798+x+1, deg2factorization4mulorder4ff[1798], 0)
  0
    time = 221 ms.

===
is_primitive_polynomial_mod_(2,x^1798+x^685+1, deg2factorization4mulorder4ff[1798])
  1
    time = 390 ms.
is_primitive_polynomial_mod_(2,x^1798+x^685+1, deg2factorization4mulorder4ff[1798], 0)
  1
    time = 2,087 ms.
      !!! so slow !!!


===
addprimes
++kw:using_fforder_only
factorization4mulorder4ff_7deg_eq_1798 =  [3,1;59,1;233,1;1103,1;2089,1;21577,1;460289,1;3033169,1;715827883,1;2147483647,1;69948188740643,1;110521633444549751,1;127802493095470979,1;575087607870890436346963910799123377,1;796968797719178740820037379973406834314737633,1;8108424985322948112652050655268837686882616590590466226649600910045900760018177829156763489,1;11150918718415813369807615536191314163147736142782825658372748219968216409029220386076329433977,1;99139504899592123218571326920209287051904818120646295979069650582652538073517990541282602213757949844086988744149244472725291477036327962245493467124164012720108873878287197285587107,1]
is_primitive_polynomial_mod_(2,x^1798+x^685+1, factorization4mulorder4ff_7deg_eq_1798,1,0)
  1
    time = 273 ms.
is_primitive_polynomial_mod_(2,x^1798+x^685+1, factorization4mulorder4ff_7deg_eq_1798,1,1)
  1
    time = 900 ms.
      why slower using fforder()???
or:
is_primitive_polynomial_mod_(2,x^1798+x^685+1, deg2factorization4mulorder4ff[1798],1,0)
is_primitive_polynomial_mod_(2,x^1798+x^685+1, deg2factorization4mulorder4ff[1798],1,1)


===

*/





{list_all_trinomial_binary_primitive_polynomial__7deg_eq_(deg, factorization4mulorder4ff=-1,max4sz4output=+oo,min4mid_deg=1)=
  ;if(deg < 2, error("[deg<2]"))
  ;my(ls=List(),half=deg\2)
  ;if(!(1<=half && half <= -1+deg), error("bug:[half:=deg\2]"))
  ;if(!(2*half <= deg && deg <= 2*half+1), error("bug:[half:=deg\2]"))
  ;if(!(1<=min4mid_deg && min4mid_deg <= half), error("bug:[not$[1 <= min4mid_deg <= half]]", [deg, half, min4mid_deg]))
  \\old: ;for(j=1,-1+deg, ...)
    \\ ;if(2*j > deg, break())
  \\ ;for(j=1,half, ...)
  ;for(j=min4mid_deg,half,
    \\ half{trinomial} --> reciprocal_polynomial
    ;if(#ls >= max4sz4output, break())
    ;my(x='x, f2=x^deg +x^j +1)
    ;if(is_primitive_polynomial_mod_(2,f2, factorization4mulorder4ff), listput(~ls, [deg,j,0]))
    )
  \\ append reciprocal_polynomial
  ;my(hsz=#ls)
  ;for(k=1,hsz,
    ;if(#ls >= max4sz4output, break())
    ;my(j=ls[hsz+1-k][2])
    ;listput(~ls, [deg,deg-j,0])
    )
  ;return(ls)
}
/*

===
? list_all_trinomial_binary_primitive_polynomial__7deg_eq_(2)
  List([[2,1,0]])
? list_all_trinomial_binary_primitive_polynomial__7deg_eq_(3)
  List([[3,1,0],[3,2,0]])
? list_all_trinomial_binary_primitive_polynomial__7deg_eq_(4)
  List([[4,1,0],[4,3,0]])
? list_all_trinomial_binary_primitive_polynomial__7deg_eq_(5)
  List([[5,2,0],[5,3,0]])

? list_all_trinomial_binary_primitive_polynomial__7deg_eq_(127)
  List([[127,1,0],[127,7,0],[127,15,0],[127,30,0],[127,63,0],[127,64,0],[127,97,0],[127,112,0],[127,120,0],[127,126,0]])

list_all_trinomial_binary_primitive_polynomial__7deg_eq_(4, [3,1;5,1])
  List([[4,1,0],[4,3,0]])


===
++kw:max4sz4output
list_all_trinomial_binary_primitive_polynomial__7deg_eq_(4, ,0)
  List([])
list_all_trinomial_binary_primitive_polynomial__7deg_eq_(4, ,1)
  List([[4,1,0]])
list_all_trinomial_binary_primitive_polynomial__7deg_eq_(4, ,2)
  List([[4,1,0],[4,3,0]])
list_all_trinomial_binary_primitive_polynomial__7deg_eq_(4)
  List([[4,1,0],[4,3,0]])

list_all_trinomial_binary_primitive_polynomial__7deg_eq_(5, ,0)
  List([])
list_all_trinomial_binary_primitive_polynomial__7deg_eq_(5, ,1)
  List([[5,2,0]])
list_all_trinomial_binary_primitive_polynomial__7deg_eq_(5, ,2)
  List([[5,2,0],[5,3,0]])
list_all_trinomial_binary_primitive_polynomial__7deg_eq_(5)
  List([[5,2,0],[5,3,0]])


===
++kw:min4mid_deg
list_all_trinomial_binary_primitive_polynomial__7deg_eq_(5, , ,2)
  List([[5,2,0],[5,3,0]])
list_all_trinomial_binary_primitive_polynomial__7deg_eq_(4, , ,2)
  List([])
list_all_trinomial_binary_primitive_polynomial__7deg_eq_(4, , ,1)
  List([[4,1,0],[4,3,0]])
list_all_trinomial_binary_primitive_polynomial__7deg_eq_(127, , ,63)
  List([[127,63,0],[127,64,0]])


===
*/


/*
\\ fail: show_all_trinomial_binary_primitive_polynomial__7deg_ge_le_(min4deg,max4deg, ~deg2factorization4mulorder4ff=-1)=
? f(a,~b)=0
  (a,~b)->0
? f(a,~b=4)=0
  ***   variable name expected: f(a,
  ***   ~b=4)=0
  ***   ^-------

*/
{show_all_trinomial_binary_primitive_polynomial__7deg_ge_le_(min4deg,max4deg, ~deg2factorization4mulorder4ff,max4sz4output=+oo,auto_sleep=0,min4mid_deg=1)=
  \\ [deg2factorization4mulorder4ff :: (-1 | [(-1 | Mat{?,2})])]
  ;my(t0=0)
  ;if(auto_sleep, t0=getabstime())
  ;
  ;my(j0=min4deg,j1=max4deg,degs=0,deg=-1)
  ;if(min4deg==-1, degs=max4deg;j0=1;j1=#degs)
  \\ ;for(deg=min4deg,max4deg, ...)
  ;for(j=j0,j1,
    ;deg=if(min4deg==-1, degs[j], j)
    ;my(factorization4mulorder4ff=if(-1==deg2factorization4mulorder4ff, -1, deg2factorization4mulorder4ff[deg]))
    ;if(-1 == factorization4mulorder4ff && -1 <> deg2factorization4mulorder4ff, print("skip deg:", deg); next())
    ;my(ls=list_all_trinomial_binary_primitive_polynomial__7deg_eq_(deg, factorization4mulorder4ff,max4sz4output,min4mid_deg))
    ;foreach(ls, es4f2, print(es4f2))
    ;if(0 == #ls, print("empty@deg:", deg))
    ;if(auto_sleep, t0=auto_sleep_(auto_sleep, t0))
  )
}
/*

deg2factorization4mulorder4ff=vector(5,deg,factorint(-1+2^deg))
  [matrix(0,2),Mat([3,1]),Mat([7,1]),[3,1;5,1],Mat([31,1])]
show_all_trinomial_binary_primitive_polynomial__7deg_ge_le_(2,5,~deg2factorization4mulorder4ff)
  ...ok

show_all_trinomial_binary_primitive_polynomial__7deg_ge_le_(2,5,-1)
  [2,1,0]
  [3,1,0]
  [3,2,0]
  [4,1,0]
  [4,3,0]
  [5,2,0]
  [5,3,0]

show_all_trinomial_binary_primitive_polynomial__7deg_ge_le_(6,8,-1)
  [6,1,0]
  [6,5,0]
  [7,1,0]
  [7,3,0]
  [7,4,0]
  [7,6,0]

++kw:max4sz4output
show_all_trinomial_binary_primitive_polynomial__7deg_ge_le_(6,8,-1,1)
  [6,1,0]
  [7,1,0]

++kw:auto_sleep
show_all_trinomial_binary_primitive_polynomial__7deg_ge_le_(6,8,-1,,1)
  [6,1,0]
  [6,5,0]
  [7,1,0]
  [7,3,0]
  [7,4,0]
  [7,6,0]
  empty@deg:8
  time = 4 ms.

show_all_trinomial_binary_primitive_polynomial__7deg_ge_le_(6,8,-1,,-1)
  [6,1,0]
  [6,5,0]
  cmd: sleep 1
  [7,1,0]
  [7,3,0]
  [7,4,0]
  [7,6,0]
  cmd: sleep 1
  empty@deg:8
  cmd: sleep 1
  time = 4 ms.

*/




{list_all_binary_primitive_polynomial__7deg_eq_(deg, factorization4mulorder4ff=-1,max4sz4output=+oo)=list_all_monic_primitive_polynomial_mod__7deg_eq_(2, deg, factorization4mulorder4ff,max4sz4output)}
/*

? list_all_binary_primitive_polynomial__7deg_eq_(3)
  List([[1,0,1,1],[1,1,0,1]])

list_all_binary_primitive_polynomial__7deg_eq_(4,[3,1;5,1])
  List([[1,0,0,1,1],[1,1,0,0,1]])

++kw:max4sz4output
list_all_binary_primitive_polynomial__7deg_eq_(2,,0)
  List([])
list_all_binary_primitive_polynomial__7deg_eq_(2,,1)
  List([[1,1,1]])
list_all_binary_primitive_polynomial__7deg_eq_(2)
  List([[1,1,1]])

list_all_binary_primitive_polynomial__7deg_eq_(3,,0)
  List([])
list_all_binary_primitive_polynomial__7deg_eq_(3,,1)
  List([[1,0,1,1]])
list_all_binary_primitive_polynomial__7deg_eq_(3,,2)
  List([[1,0,1,1],[1,1,0,1]])
list_all_binary_primitive_polynomial__7deg_eq_(3)
  List([[1,0,1,1],[1,1,0,1]])

*/






{list_all_monic_primitive_polynomial_mod__7deg_eq_(p, deg, factorization4mulorder4ff=-1,max4sz4output=+oo)=
  ;ls=List()
  ;if(p < 2, error("[p<2]"))
  ;if(deg < 2, error("[deg<2]"))
  ;\\digits=vector(deg, j, Mod(0,p))
  ;for(u=p^deg, -1+2*p^deg,
    \\ TODO: half{symmetry} --> reciprocal_polynomial
    \\  only: [[u%p > 1]or[Vecrev(digits(u,p)) <= u]]
    ;if(#ls >= max4sz4output, break())
    ;my(ds=digits(u,p), L=#ds)
    ;if(L <> 1+deg, error("bug:[L <> 1+deg]"))
    ;if(ds[1] <> 1, error("bug:[lead_coef <> 1]"))
    ;if(ds[L]==0,next())
    ;my(fp=sum(j=1,L, ds[j]*'x^(L-j)))
    ;if(is_primitive_polynomial_mod_(p,fp, factorization4mulorder4ff), listput(~ls, ds))
    )
  ;return(ls)
}

/*

? list_all_monic_primitive_polynomial_mod__7deg_eq_(2, 2)
  List([[1,1,1]])
? list_all_monic_primitive_polynomial_mod__7deg_eq_(2, 3)
  List([[1,0,1,1],[1,1,0,1]])
? list_all_monic_primitive_polynomial_mod__7deg_eq_(2, 4)
  List([[1,0,0,1,1],[1,1,0,0,1]])
? list_all_monic_primitive_polynomial_mod__7deg_eq_(2, 5)
  List([[1,0,0,1,0,1],[1,0,1,0,0,1],[1,0,1,1,1,1],[1,1,0,1,1,1],[1,1,1,0,1,1],[1,1,1,1,0,1]])

? list_all_monic_primitive_polynomial_mod__7deg_eq_(3, 2)
  List([[1,1,2],[1,2,2]])
? list_all_monic_primitive_polynomial_mod__7deg_eq_(3, 3)
  List([[1,0,2,1],[1,1,2,1],[1,2,0,1],[1,2,1,1]])

list_all_monic_primitive_polynomial_mod__7deg_eq_(2, 4, [3,1;5,1])
  List([[1,0,0,1,1],[1,1,0,0,1]])

++kw:max4sz4output
list_all_monic_primitive_polynomial_mod__7deg_eq_(2, 3,,1)
  List([[1,0,1,1]])

*/


\\ pentanomial
{show_may_pentanomial_binary_primitive_polynomial_per_deg_ge_le_(min4deg,max4deg, ~deg2factorization4mulorder4ff,auto_sleep=0,auto_sleep7deeper=0)=
  \\ [min4deg==-1] => [max4deg be degs :: [deg]]
  \\ new_version:
  ;return(show_may_binary_primitive_polynomial_per_deg_ge_le__7bit_count_eq_(5, min4deg,max4deg, ~deg2factorization4mulorder4ff,auto_sleep,auto_sleep7deeper))
}
\\ pentanomial
{show_one_pentanomial_binary_primitive_polynomial_per_deg_ge_le_(min4deg,max4deg, ~deg2factorization4mulorder4ff,auto_sleep=0,auto_sleep7deeper=0)=
  \\ [min4deg==-1] => [max4deg be degs :: [deg]]
  ;warning("show_one_pentanomial_binary_primitive_polynomial_per_deg_ge_le_() is deprecated by show_may_pentanomial_binary_primitive_polynomial_per_deg_ge_le_()")
  \\ old_version:
  ;if(min4deg==-1,
    ;my(degs=max4deg)
    ;if(vecmin(degs) < 4, error("[min4deg < 4]"))
  ,\\else:
    ;if(min4deg < 4, error("[min4deg < 4]"))
    )
  \\ {#let it fail#}: ;if(min4deg < 5, error("[min4deg < 5]"))
  ;show_one_binary_primitive_polynomial_per_deg_ge_le_(min4deg,max4deg, ~deg2factorization4mulorder4ff,2,auto_sleep,5,auto_sleep7deeper)
  \\ [mode:=2][min4weight:=5]
}
/*
show_one_pentanomial_binary_primitive_polynomial_per_deg_ge_le_(3,4,-1)
  ***   user error: [min4deg < 4]
show_one_pentanomial_binary_primitive_polynomial_per_deg_ge_le_(4,5,-1)
  ***   user error: fail:[deg:=4][bit_count:=5] : there are no pentanomial binary primitive polynomial of degree 4
    view ../../fxt/_ignore__unzip/fxt/data/all-primpoly.txt
      [deg:=4] => only trinomial

show_may_pentanomial_binary_primitive_polynomial_per_deg_ge_le_(3,4,-1)
  null@(bit_count,deg)::5:3
  null@(bit_count,deg)::5:4

show_one_pentanomial_binary_primitive_polynomial_per_deg_ge_le_(5,6,-1)
show_may_pentanomial_binary_primitive_polynomial_per_deg_ge_le_(5,6,-1)
  [5,3,2,1,0]
  [6,4,3,1,0]

show_one_pentanomial_binary_primitive_polynomial_per_deg_ge_le_(7,9,-1)
show_may_pentanomial_binary_primitive_polynomial_per_deg_ge_le_(7,9,-1)
  [7,3,2,1,0]
  [8,4,3,2,0]
  [9,4,3,1,0]

show_one_pentanomial_binary_primitive_polynomial_per_deg_ge_le_(-1,[5,8,30],-1,-1)
show_may_pentanomial_binary_primitive_polynomial_per_deg_ge_le_(-1,[5,8,30],-1,-1)
  [5,3,2,1,0]
  cmd: sleep 1
  [8,4,3,2,0]
  cmd: sleep 1
  [30,6,4,1,0]
  cmd: sleep 1
    time = 15 ms.

*/

{show_one_binary_primitive_polynomial_per_deg_ge_le_(min4deg,max4deg, ~deg2factorization4mulorder4ff, mode=0,auto_sleep=0,min4weight=3,auto_sleep7deeper=0)=
  \\ [min4deg==-1] => [max4deg be degs :: [deg]]
  \\ [deg2factorization4mulorder4ff :: (-1 | [(-1 | Mat{?,2})])]
  \\ ++kw:min4weight:mainly for pentanomial[#weight==5#] by skip trinomial[#weight==3#]
  ;my(t0=0)
  ;if(auto_sleep, t0=getabstime())
  ;
  ;my(j0=min4deg,j1=max4deg,degs=0,deg=-1)
  ;if(min4deg==-1, degs=max4deg;j0=1;j1=#degs)
  \\ ;for(deg=min4deg,max4deg, ...)
  ;for(j=j0,j1,
    ;deg=if(min4deg==-1, degs[j], j)
    ;my(factorization4mulorder4ff=if(-1==deg2factorization4mulorder4ff, -1, deg2factorization4mulorder4ff[deg]))
    ;if(-1 == factorization4mulorder4ff && -1 <> deg2factorization4mulorder4ff, print("skip deg:"  deg); next())
    ;my(es4f2=find_one_binary_primitive_polynomial__7deg_eq_(deg, factorization4mulorder4ff, mode,min4weight,auto_sleep7deeper))
    ;print(es4f2)
    ;if(auto_sleep, t0=auto_sleep_(auto_sleep, t0))
  )
}
/*

===
same{mode}:
show_one_binary_primitive_polynomial_per_deg_ge_le_(2,10,-1,1)
show_one_binary_primitive_polynomial_per_deg_ge_le_(2,10,-1,0)
show_one_binary_primitive_polynomial_per_deg_ge_le_(2,10,-1)
  [2,1,0]
  [3,1,0]
  [4,1,0]
  [5,2,0]
  [6,1,0]
  [7,1,0]
  [8,4,3,2,0]
  [9,4,0]
  [10,3,0]

===
diff{mode}:
show_one_binary_primitive_polynomial_per_deg_ge_le_(17,22,-1)
show_one_binary_primitive_polynomial_per_deg_ge_le_(17,22,-1,0)
  [17,3,0]
  [18,7,0]
  [19,5,2,1,0]
  [20,3,0]
  [21,2,0]
  [22,1,0]
show_one_binary_primitive_polynomial_per_deg_ge_le_(17,22,-1,1)
  [17,3,0]
  [18,5,2,1,0]
  [19,5,2,1,0]
  [20,3,0]
  [21,2,0]
  [22,1,0]

===
diff{mode}:
show_one_binary_primitive_polynomial_per_deg_ge_le_(32,34,-1,1)
  [32,7,5,3,2,1,0]
  [33,6,4,1,0]
  [34,7,6,5,2,1,0]
show_one_binary_primitive_polynomial_per_deg_ge_le_(32,34,-1,2)
  [32,7,6,2,0]
  [33,6,4,1,0]
  [34,8,4,3,0]

===
++kw:auto_sleep
show_one_binary_primitive_polynomial_per_deg_ge_le_(2,3,-1,,1)
  [2,1,0]
  [3,1,0]

show_one_binary_primitive_polynomial_per_deg_ge_le_(2,3,-1,,-1)
  [2,1,0]
  cmd: sleep 1
  [3,1,0]
  cmd: sleep 1

===
API changed:
  \\ [min4deg==-1] => [max4deg be degs :: [deg]]

show_one_binary_primitive_polynomial_per_deg_ge_le_(-1,[2,8,30],-1,,-1)
  [2,1,0]
  cmd: sleep 1
  [8,4,3,2,0]
  cmd: sleep 1
  [30,6,4,1,0]
  cmd: sleep 1
    time = 7 ms.

===
++kw:auto_sleep7deeper
show_one_binary_primitive_polynomial_per_deg_ge_le_(min4deg,max4deg, ~deg2factorization4mulorder4ff, mode=0,auto_sleep=0,min4weight=3,auto_sleep7deeper=0)=
show_one_binary_primitive_polynomial_per_deg_ge_le_(-1,[255],-1,,,,-1)
  [255,52,0]
  time = 56 ms.
show_one_binary_primitive_polynomial_per_deg_ge_le_(-1,[1798],vector(1798, j, if(j==1798,factorization4mulorder4ff_7deg_eq_1798,-1)),,,,-1)
  !:!.!:!.!:!.
  [1798,685,0]
  time = 3,303 ms.

*/


{find_one_binary_primitive_polynomial__7deg_eq_(deg, factorization4mulorder4ff=-1, mode=0,min4weight=3,auto_sleep7deeper=0)=
  \\ -> [exp]
  \\ ++kw:min4weight:mainly for pentanomial[#weight==5#] by skip trinomial[#weight==3#]
  ;if(mode < 0, error("[mode < 0]"))
  ;if(mode > 2, error("[mode > 2]"))
  ;if(deg < 2, error("[deg<2]"))
  ;if(min4weight < 0, error("[min4weight < 0]"))
  ;if(min4weight > 1+deg, error("[min4weight > 1+deg]", [deg, min4weight]))
  ;min4weight = max(3, min4weight)
  ;if(0 == min4weight%2, min4weight+=1)
  \\ [3 <= min4weight][1 == min4weight%2]
  ;if(0==mode,
    \\ ;forstep(bit_count=3,1+deg,2, ...)
    ;forstep(bit_count=min4weight,1+deg,2,
      ;my(zm=zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(bit_count, deg, factorization4mulorder4ff,  ,auto_sleep7deeper))
      ;if(0 <> zm, return(zm))
      )
    \\ ;error("bug:[impossible:no primitive polynomial]", [deg,mode])
      \\ xxx: !! [min4weight <= half]
    ;if(3==min4weight, error("bug:[impossible:no primitive polynomial]", [deg,mode]))
    ;error("too big min4weight@deg", [deg,mode, min4weight])
    )
  ;if(1==mode,
      ;my(bit_count=-1)
      ;my(zm=zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(bit_count, deg, factorization4mulorder4ff,min4weight,auto_sleep7deeper))
      ;if(0 <> zm, return(zm),
        \\ ;error("bug:[impossible:no primitive polynomial]", [deg,mode])
        ;if(3==min4weight, error("bug:[impossible:no primitive polynomial]", [deg,mode]))
        ;error("too big min4weight@deg", [deg,mode, min4weight])
        )
    )
  ;if(2==mode,
      ;if(5 < min4weight, error("[mode:=2][min4weight > 5]", [deg,mode,min4weight]))
      ;my(bit_count=-2)
      ;my(zm=zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(bit_count, deg, factorization4mulorder4ff,min4weight,auto_sleep7deeper))
      ;if(0 <> zm, return(zm),
        ;if(4==deg, error("fail:[deg:=4][bit_count:=5] : there are no pentanomial binary primitive polynomial of degree 4"))
        ;error("bug:[fail:hypothesis:[always succ@[bit_count:=5]]]", [deg,mode])
        )
    )
  ;
  ;error("bug:", [deg,mode,min4weight])
  ;error("bug:", [deg,mode])
  ;error("bug:", deg)
}
/*

find_one_binary_primitive_polynomial__7deg_eq_(7, -1)
  [7,1,0]
find_one_binary_primitive_polynomial__7deg_eq_(8, -1)
  [8,4,3,2,0]

find_one_binary_primitive_polynomial__7deg_eq_(8, -1, 1)
find_one_binary_primitive_polynomial__7deg_eq_(8, -1, 2)
  [8,4,3,2,0]

{\\testing{find_one_binary_primitive_polynomial__7deg_eq_}{vs:mode:0,1}
for(deg=2,20,
  ;my(es0=find_one_binary_primitive_polynomial__7deg_eq_(deg, -1, 0))
  ;my(es1=find_one_binary_primitive_polynomial__7deg_eq_(deg, -1, 1))
  ;if(es0 <> es1,
    ;print(es0)
    ;print(es1)
    ;break()
    )
  )
}
  [18,7,0]
  [18,5,2,1,0]

{\\testing{find_one_binary_primitive_polynomial__7deg_eq_}{vs:mode:1,2}
for(deg=2,200,
  ;my(es0=find_one_binary_primitive_polynomial__7deg_eq_(deg, -1, 1))
  ;my(es1=find_one_binary_primitive_polynomial__7deg_eq_(deg, -1, 2))
  ;if(es0 <> es1,
    ;print(es0)
    ;print(es1)
    ;break()
    )
  )
}
  [32,7,5,3,2,1,0]
  [32,7,6,2,0]

*/

\\ show_one_pentanomial_binary_primitive_polynomial_per_deg_ge_le_
{show_may_binary_primitive_polynomial_per_deg_ge_le__7bit_count_eq_(bit_count, min4deg,max4deg, ~deg2factorization4mulorder4ff,auto_sleep=0,auto_sleep7deeper=0)=
  \\ [min4deg==-1] => [max4deg be degs :: [deg]]
  \\ [deg2factorization4mulorder4ff :: (-1 | [(-1 | Mat{?,2})])]
  ;if(bit_count < 1, error("[bit_count < 1] : ", bit_count)) \\ avoid to be mode

  ;my(t0=0)
  ;if(auto_sleep, t0=getabstime())
  ;
  ;my(j0=min4deg,j1=max4deg,degs=0,deg=-1)
  ;if(min4deg==-1, degs=max4deg;j0=1;j1=#degs)
  \\ ;for(deg=min4deg,max4deg, ...)
  ;for(j=j0,j1,
    ;deg=if(min4deg==-1, degs[j], j)
    ;if(deg < 2, error("[deg < 2]"))
    ;my(factorization4mulorder4ff=if(-1==deg2factorization4mulorder4ff, -1, deg2factorization4mulorder4ff[deg]))
    ;if(-1 == factorization4mulorder4ff && -1 <> deg2factorization4mulorder4ff, print("skip deg:"  deg); next())
    ;my(zm=zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(bit_count, deg, factorization4mulorder4ff,  ,auto_sleep7deeper))
    ;if(0 <> zm, print(zm),
      ;printsep(":", "null@(bit_count,deg):", bit_count,deg)
      )
    ;if(auto_sleep, t0=auto_sleep_(auto_sleep, t0))
  )
}
/*
show_may_binary_primitive_polynomial_per_deg_ge_le__7bit_count_eq_(3, 7,9, -1,-1)
  [7,1,0]
  cmd: sleep 1
  null@(bit_count,deg)::3:8
  cmd: sleep 1
  [9,4,0]
  cmd: sleep 1

show_may_binary_primitive_polynomial_per_deg_ge_le__7bit_count_eq_(5, 2,9, -1,-1)
  null@(bit_count,deg)::5:2
  cmd: sleep 1
  null@(bit_count,deg)::5:3
  cmd: sleep 1
  null@(bit_count,deg)::5:4
  cmd: sleep 1
  [5,3,2,1,0]
  cmd: sleep 1
  [6,4,3,1,0]
  cmd: sleep 1
  [7,3,2,1,0]
  cmd: sleep 1
  [8,4,3,2,0]
  cmd: sleep 1
  [9,4,3,1,0]
  cmd: sleep 1
  time = 6 ms.

*/

{zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(bit_count, deg, factorization4mulorder4ff=-1,min4weight=3,auto_sleep=0,verbose=0,resume=0)=
  \\ -> (0 | [exp]{len==bit_count})
  ;my(old__bit_count=bit_count)
  ;if(deg < 2, error("[deg < 2]"))
  ;if(bit_count < 0 && bit_count < -2, error("[bit_count < -2]"))

  ;if(-1 == bit_count && 3 < min4weight, error("NotImplementedError:[bit_count:=-1][min4weight > 3]", [deg,bit_count,min4weight]))
  ;if(-2 == bit_count && 5 < min4weight, error("[bit_count:=-2][min4weight > 5]", [deg,bit_count,min4weight]))
  ;if(min4weight < 0, error("[min4weight < 0]"))
  \\;if(min4weight > 1+deg, error("[min4weight > 1+deg]", [deg, min4weight]))
  ;min4weight = max(3, min4weight)
  ;if(0 == min4weight%2, min4weight+=1)
  \\ [3 <= min4weight][1 == min4weight%2]
  ;if(min4weight > 1+deg, return(0))
  \\ [3 <= min4weight <= 1+deg][1 == min4weight%2]

  ;my(mode=max(0,-bit_count))
  ;if(!(0 <= mode && mode <= 2), error("bug:mode=",mode))
  \\ ;if(1==mode, bit_count=3)
  \\ ;if(2==mode, bit_count=3)
  \\ ;if(bit_count < 3 || bit_count > 1+deg || 0 == bit_count%2, return(0))
  ;if(1==mode, bit_count=min4weight)
  ;if(2==mode, bit_count=min4weight)
  ;if(bit_count < min4weight || bit_count > 1+deg || 0 == bit_count%2, return(0))
  \\ [3 <= min4weight <= bit_count <= 1+deg][1 == bit_count%2]

  ;if(1 == mode && 3 < bit_count, error("NotImplementedError:[mode:=1][bit_count > 3]", [deg,mode,min4weight,old__bit_count,bit_count]))
  ;if(2 == mode && 5 < bit_count, error("bug:[mode:=2][bit_count > 5]", [deg,mode,min4weight,old__bit_count,bit_count]))
  ;my(m2b5=(2 == mode && 5 == bit_count))
  \\ ;print("m2b5=",m2b5, " \\\\ ", [deg,mode,min4weight,old__bit_count,bit_count])

  ;my(x='x, g2=x^deg +1)
  ;my(es=vector(bit_count-2, j, j))
  \\ [es :: ascending]
  \\ [es excludes {0,deg}]
  ;if(0 <> resume,
    ;if(1 <> #resume%2, error("bad resume:", [deg, resume]))
    ;if(!(resume[#resume] < deg), error("bad resume:", [deg, resume]))
    \\bug: ;if(resume[1] < 2, error("bad resume:", [deg, resume]))
    ;if(!(0 < resume[1]), error("bad resume:", [deg, resume]))
    ;for(j=1,-1+#resume, if(!(resume[j] < resume[1+j]), error("bad resume:", [deg, resume])))
  \\ [resume :: ascending]
    ;if(-1 == lex(Vecrev(resume),Vecrev(es)), error("bad resume:", [deg, resume]))
    ;es=Vec(resume)
    )
  ;if(mode==1, es=List(es))
  ;if(mode==2, es=List(es))
  ;my(t0=0)
  ;if(auto_sleep, t0=getabstime())
  ;my(t07old=t0)
  ;while(1,
    ;if(verbose, print("testing:", [deg, es]))
    ;my(f2=sum(j=1,#es, x^es[j], g2))
    ;if(is_primitive_polynomial_mod_(2,f2, factorization4mulorder4ff),
        \\ bug@[mode:=1];return(vector(bit_count, j, if(j==1, deg, if(j==bit_count, 0, es[#es+2-j])))) \\ descending
        \\bug: ;if(auto_sleep, if(t07old < t0, print()))
        ;if(auto_sleep < 0 && !verbose, if(t07old < t0, print()))
        ;return(vector(2+#es, j, if(j==1, deg, if(j==2+#es, 0, es[#es+2-j])))) \\ descending
        )
    ;if(auto_sleep, t0=auto_sleep7finer_(auto_sleep, t0, verbose))
    ;while(1,
      ;if(!inplace_inc_exp_vec_(deg, ~es, mode), break(2)) \\ return(0)
      ;if(m2b5 && 1 == #es, next()) \\ lock 5-2 <==> skip 3-2
      ;if(1 == #es && es[#es]*2 > deg, next(), break(1)) \\ half{trinomial}
      )
    )
  ;
  ;return(0)
  ;
  ;
  ;
  ;if(bit_count < 3, error("[bit_count < 3] : ", bit_count))
  ;if(bit_count > 1+deg, error("[bit_count > 1+deg] : ", bit_count, " : ", deg))
  ;if(0 == bit_count%2, error("[0 == bit_count%2] : ", bit_count))
}
/*

===
for(deg=2,8,print(zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(3, deg, -1)))
  [2,1,0]
  [3,1,0]
  [4,1,0]
  [5,2,0]
  [6,1,0]
  [7,1,0]
  0

===
zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(3, 8, -1)
  0
zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(5, 8, -1)
  [8,4,3,2,0]


===
vs:@[deg:=18]
zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(3, 18, -1)
  [18,7,0]
zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(5, 18, -1)
  [18,5,2,1,0]
zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(7, 18, -1)
  [18,5,4,3,2,1,0]
zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-1, 18, -1)
  [18,5,2,1,0]
zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-2, 18, -1)
  [18,5,2,1,0]

===
vs:@[deg:=32]
zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(3, 32, -1)
  3
zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(5, 32, -1)
  [32,7,6,2,0]
zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(7, 32, -1)
  [32,7,5,3,2,1,0]
zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-1, 32, -1)
  [32,7,5,3,2,1,0]
zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-2, 32, -1)
  [32,7,6,2,0]


===
same:
for(deg=2,8,print(zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-1, deg, -1)))
for(deg=2,8,print(zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-2, deg, -1)))
  [2,1,0]
  [3,1,0]
  [4,1,0]
  [5,2,0]
  [6,1,0]
  [7,1,0]
  [8,4,3,2,0]

===
for(deg=18,30,print(zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(3, deg, -1)))
  [18,7,0]
  0
  [20,3,0]
  [21,2,0]
  [22,1,0]
  [23,5,0]
  0
  [25,3,0]
  0
  0
  [28,3,0]
  [29,2,0]
  0
===
same:
for(deg=18,30,print(zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-1, deg, -1)))
for(deg=18,30,print(zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-2, deg, -1)))
  [18,5,2,1,0]
  [19,5,2,1,0]
  [20,3,0]
  [21,2,0]
  [22,1,0]
  [23,5,0]
  [24,4,3,1,0]
  [25,3,0]
  [26,6,2,1,0]
  [27,5,2,1,0]
  [28,3,0]
  [29,2,0]
  [30,6,4,1,0]

===
diff:
for(deg=32,35,print(zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-1, deg, -1)))
  [32,7,5,3,2,1,0]
  [33,6,4,1,0]
  [34,7,6,5,2,1,0]
  [35,2,0]
for(deg=32,35,print(zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-2, deg, -1)))
  [32,7,6,2,0]
  [33,6,4,1,0]
  [34,8,4,3,0]
  [35,2,0]

===
++kw:min4weight
for(deg=7,9,print(zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-2, deg, -1, 3)))
  [7,1,0]
  [8,4,3,2,0]
  [9,4,0]
for(deg=7,9,print(zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-2, deg, -1, 5)))
  [7,3,2,1,0]
  [8,4,3,2,0]
  [9,4,3,1,0]

for(deg=7,9,print(zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-1, deg, -1, 3)))
  [7,1,0]
  [8,4,3,2,0]
  [9,4,0]
for(deg=7,9,print(zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-1, deg, -1, 5)))
  ***   user error: NotImplementedError:[bit_count:=-1][min4weight > 3][7,-1,7]
for(deg=7,9,print(zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-1, deg, -1, 7)))
  ***   user error: NotImplementedError:[bit_count:=-1][min4weight > 3][7,-1,7]

for(deg=7,9,print(zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(3, deg, -1, 5)))
  0
  0
  0



===
++kw:auto_sleep
zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(3, 3000, ~deg2factorization4mulorder4ff, ,-1)
    CTRL+C
zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(3, 1798, factorization4mulorder4ff_7deg_eq_1798, ,-1)
  !:!.!:!.
  time = 2,852 ms.
  [1798,685,0]

zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-1, 32, -1, ,1)
  time = 7 ms.
  [32,7,5,3,2,1,0]
zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-1, 252, -1, ,1)
  time = 148 ms.
  [252,9,8,6,5,4,0]
zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-1, 360, -1, ,1)
  time = 814 ms.
  [360,12,9,8,6,4,3,1,0]
zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-1, 510, -1, ,1)
  time = 264 ms.
  [510,8,6,5,4,3,0]
zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-1, 1200, -1, ,+1)
  time = 2,252 ms.
  [1200,10,7,6,3,2,0]
zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-1, 1200, -1, ,-1)
  !:!.
  time = 1,953 ms.
  [1200,10,7,6,3,2,0]

++kw:verbose,resume
zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-1, 1200, -1, ,-1,1)
  testing:[1200,List([1])]
  testing:[1200,List([2])]
  testing:[1200,List([3])]
  testing:[1200,List([1,2,3])]
  testing:[1200,List([4])]
  ... ...
  testing:[1200,List([2,3,5,6,10])]
  !:!.testing:[1200,List([1,4,5,6,10])]
  testing:[1200,List([2,4,5,6,10])]
  ... ...
  testing:[1200,List([2,3,6,7,10])]

  time = 2,246 ms.
  [1200,10,7,6,3,2,0]
    \\ {before:++kw:verbose@auto_sleep7finer_}NOTE: tiny bug:"!:!.",final "\n" are seperated by verbose/resume info...

zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-1, 1200, -1, ,-1,1,[2,3,6,7,10])
  testing:[1200,List([2,3,6,7,10])]
  time = 772 ms.
  [1200,10,7,6,3,2,0]

++kw:verbose@auto_sleep7finer_()
zmay_find_one_binary_primitive_polynomial__7deg_eq__7bit_count_eq_(-1, 1200, -1, ,-1,1)
  testing:[1200,List([1])]
  ... ...
  testing:[1200,List([2,3,5,6,10])]
  finer-cmd: sleep 3 #### \\ ... !:!.
  testing:[1200,List([1,4,5,6,10])]
  ... ...
  testing:[1200,List([2,3,6,7,10])]
  time = 1,894 ms.
  [1200,10,7,6,3,2,0]

*/


{advance_exp_vec_(mode, deg, sz, es7src=[1],es7dst=0)=
  ;my(es=List(es7src))
  ;if(0 <> es7dst, es7dst=List(es7dst))
  ;if(es==es7dst, return(0))
  ;for(j=1,sz,
    ;if(!inplace_inc_exp_vec_(deg, ~es, mode), return([-j,j-1,Vec(es)]))
    ;if(es==es7dst, return(j))
    )
  ;return(Vec(es))
}
/*
advance_exp_vec_(0, 7, 4)
  [5]
advance_exp_vec_(0, 7, 0)
  [1]
advance_exp_vec_(0, 7, 4, ,[1])
  0
advance_exp_vec_(0, 7, 4, ,[3])
  2
advance_exp_vec_(0, 7, 4, ,[5])
  4
advance_exp_vec_(0, 7, 4, ,[6])
  [5]
advance_exp_vec_(0, 7, 4, [5],[6])
  1

advance_exp_vec_(1, 7, 8)
  [5]
advance_exp_vec_(1, 7, 16)
  [6]
advance_exp_vec_(1, 7, 32)
  [-32,31,[2,3,4,5,6]]
advance_exp_vec_(1, 7, 128, ,[7])
  [-32,31,[2,3,4,5,6]]
advance_exp_vec_(1, 7, 128, [2,3,4,5,6])
  [-1,0,[2,3,4,5,6]]


advance_exp_vec_(2, 7, 8)
  [5]
advance_exp_vec_(2, 7, 16)
  [1,2,6]
advance_exp_vec_(2, 7, 32)
  [-26,25,[4,5,6]]

*/
{inplace_inc_exp_vec_(deg, ~es, mode)=
  \\ -> ok/whether_changed
  \\ [es :: ascending [exp]]
  \\ [[mode:=0] <-> [fixed bit_count{==#es}]]
  \\ [[mode:=1] <-> [inc asif idc of bits of uint until #es be odd][es::List]]
  \\ [[mode:=2] <-> [inc asif idc of bits of uint until #es be {3-2,5-2}][es::List]]
  ;if(0==mode, return(inplace_inc_exp_vec__7mode_eq0_(deg, ~es)))
  ;if(1==mode, return(inplace_inc_exp_vec__7mode_eq1_(deg, ~es)))
  ;if(2==mode, return(inplace_inc_exp_vec__7mode_eq2_(deg, ~es)))
  ;error("bug: unknown mode:", mode)
}
{inplace_inc_exp_vec__7mode_eq0_(deg, ~es)=
  \\ [fixed bit_count{==#es}]
  ;my(i=0)
  ;for(j=1,-1+#es,
    ;if(1+es[j] < es[1+j], i=j;break())
    )
  ;if(!i, i=#es;if(es[i] >= -1+deg, return(0)))
  ;for(j=1,-1+i, es[j]=j)
  ;es[i] += 1
  ;return(1)
}
{inplace_inc_exp_vec__7mode_eq1_(deg, ~es)=
  \\ precodition: [1 == #es %2][@[j<-[1..=(#es)]]->[j <= es[j] < deg]]
  \\ postcodition: same

  \\ [1 == #es %2]
  \\ [1 <= #es]
  ;my(u=sum(j=1,#es, 2^(-1+es[j])))
  ;while(1,
    ;u += 1
    ;if(1 == sumdigits(u,2)%2, break())
    ;
    )
  ;my(ds=digits(u,2))
  ;my(es7new=List())
  ;for(j=1,#ds, if(ds[#ds+1-j], listput(es7new, j)))
  ;if(es7new[#es7new] >= deg, return(0))
  ;listassign_(~es, ~es7new)
  ;return(1)
}
{inplace_inc_exp_vec__7mode_eq2_(deg, ~es)=
  \\ [#es <- {3-2,5-2}]
  \\ [#es <- {1,3}]
  ;my(es7new=0, max4exp7old=es[#es])
  ;if(1 == #es,
    ;if(3 <= es[1],
      ;es7new=[1,2,es[1]]
    ,\\else:
      ;es7new=[1+es[1]]
      )
  ,\\else:
    ;if(3 <> #es, error("bug:[mode:=2][#es !<- {1,3}] : ", [#es, es]))
    ;if(!inplace_inc_exp_vec__7mode_eq0_(deg, ~es), return(0),
      ;if(max4exp7old == es[#es], return(1),
        ;if(1+max4exp7old <> es[#es], error("bug:[[max4exp7old <> es[#es]][1+max4exp7old <> es[#es]]] : ", [max4exp7old, es]))
        ;es7new=[1+max4exp7old]
        )
      )
    )
  ;
  ;if(es7new[#es7new] >= deg, return(0))
  ;listassign_(~es, ~es7new)
  ;return(1)
}
/*

===
{\\testing{inplace_inc_exp_vec_}:

;my(deg=6, es=[1,2,3], ok=1, mode=0)
;while(ok,
  ;ok = inplace_inc_exp_vec_(deg, ~es, mode)
  ;print([ok, es])
  )
}
  [1,[1,2,4]]
  [1,[1,3,4]]
  [1,[2,3,4]]
  [1,[1,2,5]]
  [1,[1,3,5]]
  [1,[2,3,5]]
  [1,[1,4,5]]
  [1,[2,4,5]]
  [1,[3,4,5]]
  [0,[3,4,5]]

===
{\\testing{inplace_inc_exp_vec_}:

;my(deg=6, es=List([1]), ok=1, mode=1)
;while(ok,
  ;ok = inplace_inc_exp_vec_(deg, ~es, mode)
  ;print([ok, es])
  )
}

  [1,List([2])]
  [1,List([3])]
  [1,List([1,2,3])]
  [1,List([4])]
  [1,List([1,2,4])]
  [1,List([1,3,4])]
  [1,List([2,3,4])]
  [1,List([5])]
  [1,List([1,2,5])]
  [1,List([1,3,5])]
  [1,List([2,3,5])]
  [1,List([1,4,5])]
  [1,List([2,4,5])]
  [1,List([3,4,5])]
  [1,List([1,2,3,4,5])]
  [0,List([1,2,3,4,5])]

===
{\\testing{inplace_inc_exp_vec_}:

;my(deg=6, es=List([1]), ok=1, mode=2)
;while(ok,
  ;ok = inplace_inc_exp_vec_(deg, ~es, mode)
  ;print([ok, es])
  )
}
  [1,List([2])]
  [1,List([3])]
  [1,List([1,2,3])]
  [1,List([4])]
  [1,List([1,2,4])]
  [1,List([1,3,4])]
  [1,List([2,3,4])]
  [1,List([5])]
  [1,List([1,2,5])]
  [1,List([1,3,5])]
  [1,List([2,3,5])]
  [1,List([1,4,5])]
  [1,List([2,4,5])]
  [1,List([3,4,5])]
  [0,List([3,4,5])]


*/





{listassign_(~ls7dst, ~ls7src)=
  ;while(#ls7dst > #ls7src, listpop(~ls7dst))
  ;for(j=1,#ls7src, listput(~ls7dst, ls7src[j], j))
}
/*
{\\testing{listassign_}
;my(xs=List([1,2,3]))
;my(ys=[8,9])
;listassign_(~xs, ~ys)
;xs
}
  List([8,9])

{\\testing{listassign_}
;my(xs=List([1]))
;my(ys=[8,9])
;listassign_(~xs, ~ys)
;xs
}
  List([8,9])

*/


{auto_sleep_(auto_sleep, t0)=
  \\ -> (t0|t1)
  ;if(auto_sleep,
    ;my(t1=getabstime()) \\ milliseconds
    ;my(dt=ceil(3*(1+t1-t0)/1000)) \\ seconds
    ;my(cmd=strprintf("sleep %d", dt))
    ;if(auto_sleep < 0, print("cmd: ", cmd)) \\ verbose6neg
    ;system(cmd)
    ;if(auto_sleep < 0, print("!wake!")) \\ verbose6neg
    ;return(t1)
    )
  ;return(t0)
}
{auto_sleep7finer_(auto_sleep, t0, verbose=0)=
  ;if(auto_sleep,
    ;my(t1=getabstime()) \\ milliseconds
    ;my(dt=floor((t1-t0)/1000)) \\ seconds
    ;t1 = t0+1000*dt
    ;if(dt > 0,
      ;my(cmd=strprintf("sleep %d", 3*dt))
      \\ ;if(verbose, print1("finer-cmd: ", cmd, " #### \\\\ ... ")) \\ verbose6finer
      \\ ;if(verbose || auto_sleep < 0, print1("!:")) \\ verbose6neg
      ;if(verbose, print1("finer-cmd: ", cmd)) \\ verbose6finer
      ;if(!verbose && auto_sleep < 0, print1("!:")) \\ verbose6neg
      ;system(cmd)
      \\ ;if(verbose || auto_sleep < 0, print1("!.")) \\ verbose6neg
      \\ ;if(verbose, print()) \\ verbose6finer
      ;if(!verbose && auto_sleep < 0, print1("!.")) \\ verbose6neg
      ;if(verbose, print(" # !wake!")) \\ verbose6finer
      )
    ;return(t1)
    )
  ;return(t0)
}



\\ for Mersenne_prime
\\      [[deg :: exponent{Mersenne_prime}][f :: polynomial{deg}]-> [[is_irreducible_polynomial_mod_(2;f)] <-> [[is_primitive_polynomial_mod_(2;f)]]]]
{mk_one_random_irreducible_binary_polynomial_mod_(deg)=
  ;if(deg < 2, error("[deg < 2]"))
  ;my(x=ffgen([2,deg]), f2=x.mod)
  ;return(exps5binary_polynomial__7descend_(f2))
}
/*
mk_one_random_irreducible_binary_polynomial_mod_(5)
  [5,4,2,1,0]
ffinit(2,5)
  Mod(1,2)*x^5+Mod(1,2)*x^4+Mod(1,2)*x^2+Mod(1,2)*x+Mod(1,2)
ffgen(ffinit(2,5))
  x
ffgen(ffinit(2,5)).mod
  x^5+x^4+x^2+x+1

*/
{exps5binary_polynomial__7descend_(f2)=
  ;my(es=List(),deg=poldegree(f2))
  ;for(e=0,deg, if(polcoef(f2,deg-e), listput(~es,deg-e)))
  ;return(Vec(es))
}
/*
exps5binary_polynomial__7descend_('x^2+3)
  [2,0]
*/
{coeffs5polynomial__7little_endian_(f)=
  ;return(vector(1+poldegree(f), j, polcoef(f,-1+j)))
}
/*
coeffs5polynomial__7little_endian_('x^2+3)
  [3,0,1]
*/


00000 \\ for:read();


