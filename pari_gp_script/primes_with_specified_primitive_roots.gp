
/*
__doc__
e ../../python3_src/pari_gp_script/primes_with_specified_primitive_roots.gp
read("primes_with_specified_primitive_roots.gp");
default('factor_add_primes,1)
  \\ to cache factorint() result

come_from:
view ../../python3_src/seed/math/prime_pint/primes_with_specified_primitive_roots.py


*/
/*
__all__
symmetrically_list_primes_with_specified_primitive_roots_
list_primes_with_specified_primitive_roots_



print_methods6my_fmt7gp ../../python3_src/pari_gp_script/primes_with_specified_primitive_roots.gp

*/
/*
__output__
view ../../python3_src/pari_gp_script/primes_with_specified_primitive_roots.gp.out.txt
  [-189,-179,-83,-59,13,93,141,307] \\64
  [-1307,-1133,-317,-117,13,235,253,435] \\80
  [-1107,-843,-285,-99,277,331,525,627] \\100
  [-1685,-797,-357,-275,51,421,573,757] \\128
  [-1307,-843,-659,-75,291,357,421,501] \\160
  [-635,-387,-285,-75,235,1027,1285,1723] \\200
  [-2027,-1493,-797,-467,115,1125,1405,2091] \\240
  [-19,141] \\255
  [-189,301] \\256

*/

{symmetrically_list_primes_with_specified_primitive_roots_(primitive_roots, begin4prime, half_span4prime, max4size=-1,diff6begin=0,with_p2e4Pmm=0)=
  ;my(min4prime=begin4prime, max4prime=begin4prime+half_span4prime, reverse=0)
  ;my(rs=list_primes_with_specified_primitive_roots_(primitive_roots, min4prime, max4prime, max4size, reverse,diff6begin,with_p2e4Pmm))
  ;my(max4prime=begin4prime, min4prime=begin4prime-half_span4prime, reverse=1)
  ;my(ls=list_primes_with_specified_primitive_roots_(primitive_roots, min4prime, max4prime, max4size, reverse,diff6begin,with_p2e4Pmm))
  ;return(concat(Vecrev(ls), rs))
}
/*
symmetrically_list_primes_with_specified_primitive_roots_([2], 1000, 200, 4,1,0)
  time = 2 ms.
  [-117,-93,-59,-53,19,61,91,109]
symmetrically_list_primes_with_specified_primitive_roots_([2], 1000, 200, 4,1,1)
  time = 2 ms.
  [[-117,[2,1;3,2;7,2]],[-93,[2,1;3,1;151,1]],[-59,[2,2;5,1;47,1]],[-53,[2,1;11,1;43,1]],[19,[2,1;509,1]],[61,[2,2;5,1;53,1]],[91,[2,1;5,1;109,1]],[109,[2,2;277,1]]]

view ../../python3_src/pari_gp_script/primes_with_specified_primitive_roots.gp.out.txt
*/

{list_primes_with_specified_primitive_roots_(primitive_roots, min4prime, max4prime, max4size=-1, reverse=0,diff6begin=0,with_p2e4Pmm=0)=
  ;if(max4size < -1, error("[max4size < -1]"))
  ;if(-1 <> max4size && max4size <= 0, return([]))
  ;if(-1 <> max4size && max4size < +1, error("bug:[max4size < +1]"))
  ;min4prime = max(2, min4prime)
  ;if(!(min4prime <= max4prime), return([]))
  ;my(ps=List(),ds=0,ls4q2e4Pmm=List(),rs=0)
  ;my(j0=min4prime,j1=max4prime, step=+1)
  ;if(reverse, j0=max4prime;j1=min4prime;step=-1)
  ;forstep(p=j0,j1,step,
    ;my(gs=Set([g%p | g <- primitive_roots]))
    ;foreach(gs, g,
      ;if(g==0, next(2))
      ;if(g==1 && p > 2, next(2))
      ;if(g==p-1 && p > 3, next(2))
      )
    ;if(0==p%2 && p <> 2, next())
    ;if(!isprime(p), next())
    ;if(p <> 2,
      ;my(half=(p-1)/2)
      ;foreach(gs, g,
        ;if(p-1 <> lift(Mod(g,p)^half), next(2))
        )
      ;my(partial_ft2e4Pmm=factor(p-1,2^24))
      ;foreach(partial_ft2e4Pmm[,1]~, ft4Pmm,
        ;if(ft4Pmm==2, next())
        ;my(e6ft=(p-1)/ft4Pmm)
        ;foreach(gs, g,
          ;if(1 == lift(Mod(g,p)^e6ft), next(3))
          )
        )
      )
    \\ slow ops:znorder() will factorint(p-1)
    ;my(q2e4Pmm=factor(p-1),ex=[p-1,q2e4Pmm])
    ;foreach(gs, g,
      ;if(p-1 <> znorder(Mod(g,p),ex), next(2))
      )
    ;listput(~ps,p)
    ;listput(~ls4q2e4Pmm,q2e4Pmm)
    ;if(-1 <> max4size && max4size <= #ps, break())
    )
  ;ps=Vec(ps)
  ;if(diff6begin, ds=[p-j0 | p <- ps])
  \\ ;if(with_p2e4Pmm, ls4q2e4Pmm=[factorint(p-1) | p <- ps])
  ;
  ;rs=if(diff6begin, ds, ps)
  ;if(with_p2e4Pmm, rs=vector(#ps,j,[rs[j],ls4q2e4Pmm[j]]))
  ;return(rs)
}
/*

list_primes_with_specified_primitive_roots_([2], 0, 100)
  [3,5,11,13,19,29,37,53,59,61,67,83]
list_primes_with_specified_primitive_roots_([2,3], 0, 100)
  [5,19,29,53]
list_primes_with_specified_primitive_roots_([2,3,5], 0, 100)
  [53]
list_primes_with_specified_primitive_roots_([2], 0,100, 4)
  [3,5,11,13]
list_primes_with_specified_primitive_roots_([2], 0,100, 4,1)
  [83,67,61,59]
list_primes_with_specified_primitive_roots_([2], 0,100, 4,1,1)
  [-17,-33,-39,-41]
list_primes_with_specified_primitive_roots_([2], 0,100, 4,1,1,1)
  [[-17,[2,1;41,1]],[-33,[2,1;3,1;11,1]],[-39,[2,2;3,1;5,1]],[-41,[2,1;29,1]]]
list_primes_with_specified_primitive_roots_([2], 0,100, 4,1,0,1)
  [[83,[2,1;41,1]],[67,[2,1;3,1;11,1]],[61,[2,2;3,1;5,1]],[59,[2,1;29,1]]]


list_primes_with_specified_primitive_roots_([2], 2^64, 2^65, 3,0)
  time = 17 ms.
  [18446744073709551629,18446744073709551709,18446744073709551757]
list_primes_with_specified_primitive_roots_([2], 2^63, 2^64, 3,1)
  time = 3 ms.
  [18446744073709551557,18446744073709551533,18446744073709551437]

list_primes_with_specified_primitive_roots_([2], 2^64, 2^65, 3,0,1)
  time = 15 ms.
  [13,93,141]
list_primes_with_specified_primitive_roots_([2], 2^63, 2^64, 3,1,1)
  time = 2 ms.
  [-59,-83,-179]

list_primes_with_specified_primitive_roots_([2], 2^128, 2^129, 3,0,1,1)
  time = 286 ms.
  [[51,[2,1;3,5;17,1;89,1;6481,1;5816689,1;12275703273579557140363,1]],[421,[2,2;13,1;19371548347,1;2640298518527,1;127943649510377,1]],[573,[2,2;3,2;6967,1;10470701,1;129573257026980267358107269,1]]]
list_primes_with_specified_primitive_roots_([2], 2^127, 2^128, 3,1,1,1)
  time = 245 ms.
  [[-275,[2,2;5,1;1051,1;16188504610891458775612493217496109,1]],[-357,[2,1;3,1;17,1;23,1;884713791875723,1;163948950010973461931,1]],[-797,[2,1;83,1;32099,1;766501,1;83315753884128718614942437,1]]]

*/


0000 \\ for read()
