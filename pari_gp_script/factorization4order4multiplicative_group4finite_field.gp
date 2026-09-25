
/*
__all__

load_database8p2deg2factorization4mulorder4ff_
  load_database8base2deg2prime_factors4cyclotomic_number_
    default_ipath4database8deg2factorization4mulorder4ff


maplistput_
maplistget_
maplistsize_
maplistput7fill_at_
  listput7fill_at_

factor_pint7primes_



===
print_methods6my_fmt7gp ../../python3_src/pari_gp_script/factorization4order4multiplicative_group4finite_field.gp
1:default_ipath4database8deg2factorization4mulorder4ff
2:factor_pint7primes_
3:maplistput_
4:maplistget_
5:maplistsize_
6:listput7fill_at_
7:maplistput7fill_at_
8:load_database8base2deg2prime_factors4cyclotomic_number_
9:load_database8p2deg2factorization4mulorder4ff_


*/
/*
__doc__
e ../../python3_src/pari_gp_script/factorization4order4multiplicative_group4finite_field.gp
gp7my
read("factorization4order4multiplicative_group4finite_field.gp");

gp
read("../../python3_src/pari_gp_script/factorization4order4multiplicative_group4finite_field.gp");

view ../../python3_src/seed/math/factor_pint/database4factors4cyclotomic_numbers.py.default.db
  line_format-example:
    2:11:[23, 89]
    #p:deg:qs{polcyclo(deg,p)}

*/

{default_ipath4database8deg2factorization4mulorder4ff = "../../python3_src/seed/math/factor_pint/database4factors4cyclotomic_numbers.py.default.db" ;}
/*
  \\ [len(num_bases)==61]
  \\ [num_bases == [1..=72] \-\ ([1..=8] :^: [2,3,5])]

Vec(d) \\ keys
Mat(d) \\ items

*/


{factor_pint7primes_(ps, n)=
  ;if(n < 1, error("[n < 1]"))
  ;my(fc4n=List(), u=n)
  ;foreach(ps, p,
    ;if(p < 2, error("[p < 2]"))
    ;if(1==u, break())
    ;if(u < p, next())
    ;my(ep=0)
    ;while(u >= p,
      ;[q,r]=divrem(u, p)
      ;if(r, break())
      ;ep += 1
      ;u = q
      )
    ;if(ep, listput(~fc4n, [p,ep]))
    )
  ;if(u <> 1, error("[not complete factor_pint7primes_()]:", [n, ps, u]))
  ;fc4n = matrix(#fc4n, 2, i,j, fc4n[i][j])
  ;if(n <> factorback(fc4n), error("bug: [n <> factorback(fc4n)] : ", [n, fc4n]))
  ;return(fc4n)
}
/*

factor_pint7primes_([], 1)
  matrix(0,2)
factor_pint7primes_([2], 8)
  Mat([2,3])
factor_pint7primes_([2,3], 72)
  [2,3;3,2]
factor_pint7primes_([2,3], 6)
  [2,1;3,1]
factor_pint7primes_([2,3], 3)
  Mat([3,1])

factor_pint7primes_([3], 6)
  ***   user error: [not complete factor_pint7primes_()]:[6,[3],2]

*/

{maplistput_(~d, k, v) = mapapply(~d, k, (~ls)->listput(~ls,v), ()->List(v)); }
{maplistget_(~d, k, j) = mapapply(~d, k, (~ls)->ls[j]); }
{maplistsize_(~d, k) = mapapply(~d, k, (~ls)->#ls); }

{listput7fill_at_(~ls,v7fill,j,v7put)=
  ;if(j > #ls, for(i=1+#ls,j,listput(~ls,v7fill)))
  ;if(1 <= j && j <= #ls, 999,error("IndexError:", j, ":", #ls))
  ;listput(~ls,v7put,j)
}

{maplistput7fill_at_(~d, k, v7fill, j, v7put) = mapapply(~d, k, (~ls)->listput7fill_at_(~ls,v7fill,j,v7put), (()->my(ls=List());listput7fill_at_(~ls,v7fill,j,v7put);return(ls))) }

{load_database8base2deg2prime_factors4cyclotomic_number_(ipath="") =
  ;if(""==ipath, ipath=default_ipath4database8deg2factorization4mulorder4ff)
  ;my(lines=readstr(ipath),base2deg2prime_factors4cyclotomic_number=Map())
  ;my(x='x, put=((~base2deg2prime_factors4cyclotomic_number,s)->
      ;my([p,deg,qs]=apply(eval, strsplit(s,":")))
      ;maplistput7fill_at_(~base2deg2prime_factors4cyclotomic_number, p, -1, deg, qs)
      )
    )
  ;for(j=1,#lines, put(~base2deg2prime_factors4cyclotomic_number,lines[j]))
  ;return(base2deg2prime_factors4cyclotomic_number)
}


{load_database8p2deg2factorization4mulorder4ff_(ipath_or_base2deg2prime_factors4cyclotomic_number="") =
  ;my(d7I=if("t_STR" == type(ipath_or_base2deg2prime_factors4cyclotomic_number), load_database8base2deg2prime_factors4cyclotomic_number_(ipath_or_base2deg2prime_factors4cyclotomic_number), ipath_or_base2deg2prime_factors4cyclotomic_number)) \\ base2deg2prime_factors4cyclotomic_number
  ;my(max4base=if(0 == #d7I, 0, vecmax(Vec(d7I))))
  ;my(d7O=Map()) \\ p2deg2factorization4mulorder4ff
  ;forprime(p=2,max4base,
    \\;if(mapisdefined(~d7I, p, &d2qs) ...)
    ;if(mapisdefined(d7I, p, &d2qs), \\deg2prime_factors4cyclotomic_number
      \\,for(deg=1,#d2qs,
        \\ ;fordiv(deg, n, d2qs[])
        \\ )
      ;forfactored(pair=1,#d2qs,
        ;my([deg,fc4deg]=pair)
        ;my(qs=List(), ok=1) \\fc4deg=factorint(deg)
        ;
        \\ ;foreach(fc4deg[,1], q, d2qs[deg/p])
        ;fordiv(fc4deg, ft, if(-1 == d2qs[ft], ok=0))
        ;if(!ok, next())
        ;fordiv(fc4deg, ft, foreach(d2qs[ft], q, listput(~qs, q)))
        ;qs=Vec(Set(qs))
        \\ bug: ;my(fc4n6deg=factor_pint7primes_(qs, polcyclo(deg,p)))
        ;my(fc4n6deg=factor_pint7primes_(qs, (-1+p^deg)))
        ;maplistput7fill_at_(~d7O, p, -1, deg, fc4n6deg)
        )
      )
    )
  ;
  ;return(d7O)
}


/*

base2deg2prime_factors4cyclotomic_number = load_database8base2deg2prime_factors4cyclotomic_number_("");

p2deg2factorization4mulorder4ff = load_database8p2deg2factorization4mulorder4ff_(base2deg2prime_factors4cyclotomic_number);

#p2deg2factorization4mulorder4ff
  20
primepi(72)
  20

maplistsize_(~p2deg2factorization4mulorder4ff, 2)
  3000
maplistget_(~p2deg2factorization4mulorder4ff, 2, 1)
  matrix(0,2)
maplistget_(~p2deg2factorization4mulorder4ff, 2, 1207)
  -1
maplistget_(~p2deg2factorization4mulorder4ff, 2, 3000)
  [3,2;5,4;7,1;11,1;13,1;17,1;31,1;41,1;61,1;101,1;151,1;241,1;251,1;331,1;401,1;601,1;751,1;1201,1;1321,1;1801,1;2251,1;3001,1;4001,1;4051,1;7001,1;8101,1;28001,1;61681,1;63901,1;96001,1;100801,1;268501,1;340801,1;1074001,1;2020001,1;2787601,1;3775501,1;10567201,1;13334701,1;22624001,1;229668251,1;791058001,1;1182468601,1;3173389601,1;4562284561,1;269089806001,1;271191084001,1;1133836730401,1;1481124532001,1;168069194932501,1;4710883168879506001,1;47970133603445383501,1;94291866932171243501,1;5519485418336288303251,1;19963778429046466946251,1;1261828167347816850332890667592001,1;4028493980595041855367835954324501,1;35758633131596900685051378954141001,1;490085601781975781872492242606604272001,1;1461503031127477825099979369543473122548042956801,1;2139731020464054092520609592459940706818275139793055476751,1;1606545773279325100753216665442817637284047671432352410624001,1;8877945148742945001146041439025147034098690503591013177336356694416517527310181938001,1;39760236847989925866972456346098401045759081806932549580163925424066737427038613818550817379110080176703469132872154250474966124707250960331228232944753436001,1]
maplistget_(~p2deg2factorization4mulorder4ff, 2, 3001)
  ***   nonexistent component: index > 3000


*/

00000 \\ for:read();


