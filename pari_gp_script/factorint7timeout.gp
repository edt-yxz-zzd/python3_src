
/*
__all__:here

factorint7timeout_



===
print_methods6my_fmt7gp ../../python3_src/pari_gp_script/factorint7timeout.gp
1:factorint7timeout_

*/


/*
__doc__:here

e ../../python3_src/pari_gp_script/factorint7timeout.gp
gp7my
  read("factorint7timeout.gp");

come_from:
view ../../python3_src/seed/math/factor_pint/factorint6PARI_GP_.py
  ??alarm
      \\ Time-bounded partial factorization
  ??factor_add_primes
  ??path
view others/app/termux/help/gp-help-interesting.txt
e ../../python3_src/pari_gp_script/__TODO__.txt

*/


{factorint7timeout_(timeout, n)=
  ;my(old__factor_add_primes=default('factor_add_primes))
  ;my(old__primes=if(old__factor_add_primes, [], addprimes()))
  ;if(!old__factor_add_primes,
      ;default('factor_add_primes,1) \\ will log any factors found by factorint
      )
  ;my(err_or_fc4n = iferr(alarm(timeout, factorint(n)), err,  "pass",
    ;if(!old__factor_add_primes,
      \\ restore old values
      ;default('factor_add_primes,0)
      ;removeprimes(addprimes())
      ;addprimes(old__primes)
      )
    ;0 \\ re-raise err
    ))

  ;my(partial_fc4n=if(type(err_or_fc4n) <> "t_ERROR", err_or_fc4n,
    \\bug: ;factorint(n, 2^24)
    \\  factorint(x,{flag = 0}):
    \\  factor(x,{D}):
    ;factor(n, 2^24)
      \\ ??alarm
      \\ ??factor_add_primes => 2^24
    ))

  ;if(!old__factor_add_primes,
      \\ restore old values
      ;default('factor_add_primes,0)
      ;removeprimes(addprimes())
      ;addprimes(old__primes)
      )

  ;return(partial_fc4n)
}
/*
read("factorint7timeout.gp");
factorint7timeout_(10, -1+2^257)
  *** factorint: the PARI stack overflows !
  current stack size: 8000000 (7.629 Mbytes)
  [hint] set 'parisizemax' to a nonzero value in your GPRC


default('parisizemax,256*10^6)
factorint7timeout_(10, -1+2^257)
partial_fc4n=% ;
ispseudoprime(partial_fc4n[,1])
(-1+2^257) == factorback(partial_fc4n)
isprime(partial_fc4n[,1])
factorint7timeout_(3, -1+2^257)
partial_fc4n=factorint7timeout_(1, -1+2^1207)
==>>:
? default('parisizemax,256*10^6)
  ***   Warning: new maximum stack size = 256000000 (244.141 Mbytes).
? factorint7timeout_(10, -1+2^257)
  *** factorint: Warning: increasing stack size to 16000000.
  time = 9,529 ms.
  [535006138814359,1;1155685395246619182673033,1;374550598501810936581776630096313181393,1]
? partial_fc4n=% ;
? ispseudoprime(partial_fc4n[,1])
  time = 1 ms.
  [1,1,1]~
? (-1+2^257) == factorback(partial_fc4n)
  1
? isprime(partial_fc4n[,1])
  [1,1,1]~
? factorint7timeout_(3, -1+2^257)
  time = 1 ms.
  [535006138814359,1;1155685395246619182673033,1;374550598501810936581776630096313181393,1]
? partial_fc4n=factorint7timeout_(1, -1+2^1207)
  time = 1,200 ms.
  [131071,1;228479,1;48544121,1;212885833,1;7121450524338129034228935888406290342440924878292924475154549706165967683018106989365212535726088820424187252154592086367126609115652316059905387197810171357101484623269226530219357641629634637632902818929376633641165995708421341209033069328278856607776384578328080846029713646218471064646270016968312691054210973840071649700163924918271,1]
? ispseudoprime(partial_fc4n[,1])
  time = 6 ms.
  [1,1,1,1,0]~

*/
