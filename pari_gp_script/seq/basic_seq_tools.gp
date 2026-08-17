

\\ e ../../python3_src/pari_gp_script/seq/basic_seq_tools.gp
\\ load by: read("../../python3_src/pari_gp_script/seq/basic_seq_tools.gp")
\\ load by:"\r ../../python3_src/pari_gp_script/seq/basic_seq_tools.gp"

{filter_(~is_ok_,~xs)=
  ;my(ys=List())
  ;foreach(xs,x,if(is_ok_(~x),listput(~ys,x)))
  ;return(Vec(ys))
}

{list_while_(~is_ok_,~x2next_,~x0)=
  ;my(xs=List(),x=x0)
  ;while(is_ok_(x)
    ,listput(~xs,x)
    ;x=x2next_(~x)
    )
  ;return(Vec(xs))
}

{list5iter_(~st2next_,~st0)=
  ;my(xs=List(),x,st=st0,out=st2next_(~st))
  ;while(2 == #out
    ,[x,st] = out
    ;listput(~xs,x)
    ;out=st2next_(~st)
    )
  ;return(Vec(xs))
}

{test4list5iter_()=
  ;my(st2next_(st)=
    my([i,j]=st)
    ;if(i<j,[i,[i+1,j]],[])
    )
  ;if(list5iter_(~st2next_,[0,4]) != [0,1,2,3], error("bug@list5iter_"))
}
{foreach6iter(~st2next_,~st0,~yx2y_,~y0)=
  ;my(x,y=y0,st=st0,out=st2next_(~st))
  ;while(2 == #out
    ,[x,st] = out
    ;y=yx2y_(~y,~x)
    ;out=st2next_(~st)
    )
  ;return(y)
}

{count_(~is_ok_, ~xs)=sum(j=1,#xs,0!=is_ok_(~xs[j]))}
{ratio_(~is_ok_, ~xs)=count_(~is_ok_, ~xs)/#xs}

{randrange(min,max1)=min+random(max1-min)}
{randrange_sz(sz,min,max1)=my(M=max1-min);vector(sz,X,min+random(M))}


