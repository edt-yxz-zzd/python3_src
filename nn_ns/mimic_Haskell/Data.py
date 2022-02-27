#__all__
r'''
bug fixed:
    1. whnf_reduce4apps!
        __call__
        closure4hs = whnf_reduce4apps(closure4hs)
        check_type_is(Data4py, closure4hs)
        data4hs = whnf_reduce4apps(data4hs)
        check_type_is(Data4hs, data4hs)

search /[^*]\<map(
    # [^)]
    may require "*map"

nn_ns.mimic_Haskell.Data
py -m nn_ns.mimic_Haskell.Data
py -m nn_ns.app.debug_cmd   nn_ns.mimic_Haskell.Data
py -m nn_ns.app.debug_cmd   nn_ns.mimic_Haskell.Data > /sdcard/0my_files/tmp/out4py/nn_ns.mimic_Haskell.Data.__all__.txt
view /sdcard/0my_files/tmp/out4py/nn_ns.mimic_Haskell.Data.__all__.txt
py -m   nn_ns.mimic_Haskell.Data 2> /sdcard/0my_files/tmp/out4py/nn_ns.mimic_Haskell.Data.debug.txt
view /sdcard/0my_files/tmp/out4py/nn_ns.mimic_Haskell.Data.debug.txt

e ../../python3_src/nn_ns/mimic_Haskell/Data.py
!mkdir ../../python3_src/nn_ns/mimic_Haskell/



example:
    see:
        _test_compile__mix2____MultiInputUnboxedRecurLet4hs()






syntactic-data@post-parse~~pre-compile
semantic-data@post-compile~~pre-execute

env:
    static-closure.xxx
        #globals(Module)/locals(let/where)
    dynamic-context[instance C a]
        #外挂接口 自动推导填充
    dynamic-context."?xxx"
        #隐参数 自动填充

syntactic: BaseSyntactic4hs
Syntactic4hs = ???
MixSyntactic4hs =
    | Constant Semantic4hs #mix~half_compiled
    | Var
    | Expr8List4hs [MixSyntactic4hs]
    | Lambda4hs [Var] MixSyntactic4hs
    | RecurDoLet4hs [(Var, MixSyntactic4hs)] MixSyntactic4hs
        #copy to
        #   e others/数学/编程/lambda/Monad_recur.txt
        e others/数学/编程/lambda/Monad_recur.txt

        ##################################
        let x = f x
          ==>>
            x = y f
            y f = f (y f)
            y = h h
            h = \h f -> f (h h f)
          ==>>
            x = f (f (f ...))

        ##################################
        let m = do
                  rec x <- f x
                  return x
          ==>>
            m = f undefined >>= k f
            k = y (\k f x -> f x >>= k f)
          ==>>
            m = f undefined >>= \x->
                f x >>= \x->
                f x >>= \x->
                ...


        #plan recur
        x =[def]= f x
            x = f x = f (f x) = (f^inf) $ arbitrary
        y f =[def]= f (y f)
            y f = f (y f) = f (f (y f)) = (f^inf) $ arbitrary
        ==>> [x===y f]
        #monad recur
        rec do x <- f x
            f x = f x >>= return
            f x = f x >>= f
                = f x >>= f >>= f
                = ((>>= f)^inf) (f arbitrary)
                = ((>>= f)^inf) arbitrary
                = y (>>= f)
        f =[def]= \x -> [a, x, b]
            y (>>= f) =[SHOULDBE]= aab-aab-abb-...
            y (>>= f)
                = (>>= f) (y (>>= f))
                =  (y (>>= f)) >>= f
                = undefined
        m === m >>= f  #  vs   x === f x
        m = z f
            = (z f) >>= f
            ## wrong direction
            ##  SHOULD extend to rhs
        ######################
        m0 = f undefined
        m1 = m0 >>= f
        ...
        m = m0 >>= \x -> (f x >>= \x -> f x >>= ...)
             = m0 >>= k f
        k f = \x -> f x >>= k f
        k = y (\k f x -> f x >>= k f)
        m = f undefined >>= k f
            = y f >>= k f

        #error:
        xxx    do
        xxx        recur x <- f x
        xxx        return x
        xxx    let x_jmp = empty _Placeholder4hs
        xxx    in  f x_jmp >>= \x_val -> assert [x_val is not x_jmp] $ x_jmp.set(x_val) `seq` x_val

    | RecurLet4hs as_if_prime/bool [(Var, MixSyntactic4hs)] MixSyntactic4hs
        # why not Expr8List4hs [Lambda4hs ..., ...]?
        #   since def recur_group!
        # let {a=..., b=...} in body
        #   =!= Apps4hs [\a b ... -> body, a, b, ...]
        #   === Apps4hs [\a b ... -> body, bound_a, bound_b, ...]
        #   === Apps4hs [\a b ... -> body, (a closure4a), (b closure4b), ...]
    | Case4hs input4case/MixSyntactic4hs [(XPattern4hs, guarded_body)]
    | BareCase4hs input4case/MixSyntactic4hs [(CtorH4hs, [XVar], body/MixSyntactic4hs)] (may (XVar body))
        #to impl if_then_else4hs Maybe4hs

Var = VarH4hs|VarR4hs|VarN4hs|CtorH4hs|Var4hs #no |UnusedPattern4hs|Infix4hs
guarded_body = guarded_<MixSyntactic4hs, MixSyntactic4hs>
guarded_<guard, body> = body | [(guard, guarded_<guard, body>)]
    fold__guarded_body
    _check_guarded_body




semantic: BaseSemantic4hs
Semantic4hs =
    | Apps4hs [Semantic4hs]
    #| IFixAryCallable4hs
        | LocalBatchRouter uint [[uint]]
        | FreeLocalBatchRouter uint [UIntXs]
        | App4Data4hs CtorH4hs uint [uint]
        #| IFunc4py
            | Expr4py uint py_func [py_arg]
            | Stmt4py uint py_func [py_arg]
    | Data4hs CtorH4hs [Semantic4hs]
    | Data4py py_obj
UIntXs = uint | tuple<UIntXs>
    check_uintXs
    check_uintXs_lt

compile4mix :: MixSyntactic4hs -> Semantic4hs
eg:
    toplevel_defs:
        var = Lambda4hs with free_vars+constants
        ...
    ==>>
        globals = dict(free_vars & constants & toplevel_defs)
        globals[var] = Apps4hs [toplevel_defs[var], globals]
    ==>>
        extend LocalBatchRouter to interpreter neg_int as closure getting
        ExtendedFreeLocalBatchRouter uint UIntXs [[uint]] uint uint [IntXs]
        ExtendedFreeLocalBatchRouter total4closure shape4closure nint2idc num_free_vars num_args4call iXss4body
            iXss4body :: [IntXs<-num_free_vars, num_args4call>]
            #nint2idc :: [[uint]]
            #nint2idc :: [((1,uint,uint)|(2,uint))]
            #nint2idc :: [((0|1), uint)]
            nint2idc :: [((0,uint%3,uint)|(1,uint))]
        ex_router(closure, /, *args4call)
            len(args4call) == sf.num_args4call
            # closure :: (total, objXtuple<hs_obj>)
            # closure = (total, pairs/[([Lambda4hs], closure)], recur_group/[Lambda4hs])
                #pairs=group_closure_pairs4free_vars_not_in_recur_group #for pre defined Lambda4hs
                #   or try [Apps4hs[Lambda4hs, closure]]
                #   or try [hs_obj]
            #closure = ([hs_obj], recur_group/[Lambda4hs])
            closure = (bound_groups/[[hs_obj]], recur_group/[Lambda4hs])
                #bound_groups = [bound_builtins, constants, bound_globals, (bound_let_def_group/bound_nonlocals/bound_free_vars)...]
                bound_groups = (bound_builtins_and_constants, bound_globals, bound_dynamic_free_vars)
                recur_group = ()|[ExtendedFreeLocalBatchRouter]
                    #unbound_group
            recur_group = closure[-1] #maybe empty
            closure.total == sf.total4closure
            shape_of closure == sf.shape4closure
                #shape4closure: no empty tuple except toplevel[-1]=recur_group
                #shape4closure: no tuple with all 0s except empty recur_group=toplevel[-1]
                #positive means len of tuple<hs_obj>
                #shape4closure[-1] means len of recur_group::tuple<hs_obj>
                #0 means ref-to hs_obj except shape4closure[-1]
                #shape4closure[-1] :: uint
                #shape4closure :: [UIntXs]
                #
            i <-- sf.iXss4body
            case i of
                u -> args4call[u]
                    # u >= 0
                n -> do
                    # n < 0
                    #cache?
                    k0, k1 = idc = nint2idc[n]
                    is_recur = k0
                    x = closure[k0][k1]
                    if is_recur:
                        assert k0 == 1
                        #recur_group
                        f = x
                        closure4f = closure
                        x = Apps4hs[f, Data4py[closure4f]]
                    else:
                        assert k0 == 0
                        assert is_obj4hs(x)
                    assert is_obj4hs(x)
                    return x


            ...
IntXs = int | tuple<IntXs>
    fold__objXtuple
    fold__intXiter
    check_uintXs_lt
    check_uintXs
    check_intXs_between
IntXs<m,M> = int_ge_lt<m,M> | tuple<IntXs<m,M> >

objXiter<T> = T | Iter<objXiter<T> >
objXtuple<T> = T | tuple<objXtuple<T> >
objXs = objXtuple
IntXs = objXtuple<int>
UIntXs = objXtuple<uint>


compile4mix order:
    1. findout operator-preference
    2. eliminate Infix4hs : var_op_flow -> app_tree
    3. BIG_STEP: convert OutputUnboxedBlockSugarLet4hs/OutputUnboxedRecurLet4hs/Case4hs/BareCase4hs(Pattern4hs) into _AsIfPrimeRecurLet4hs/Lambda4hs+builtins_and_constants(closure?incomplete)
    4. compile__mix2 :: mix2 -> _MidWayBound
        precondition:
            input only: Semantic4hs, both_Semantic4hs_Syntactic4hs(Apps4hs/xxx Data4hs)/Expr8List4hs, Lambda4hs, Var
        postcondition:
            output:
                builtins_and_constants
                free_vars
                body only: Apps4hs, LocalBatchRouter/FreeLocalBatchRouter/ExtendedFreeLocalBatchRouter
    5. findout which free_vars are globals
    6. prepare closure


TODO:
    #################################
    DONE
    remove Data4hs from both_Semantic4hs_Syntactic4hs
        Data4hs CtorH4hs [MixSyntactic4hs]
            -->> Apps4hs [CtorH4hs, ...]
        =====TODO:cancel this remove
            Apps4hs [MixSyntactic4hs]
            is_obj4hs(CtorH4hs)
            need to known N_ary/num_args4call

    #################################
    DONE
    e ../../python3_src/notes/技巧/分割函数+成员函数互调.txt
        refactor _Apps4hs.___whnf_reduce4apps___
        def ___tmp_env():
            def ___whnf_reduce4apps___...
            def recur1...
            return ___whnf_reduce4apps___
        ___whnf_reduce4apps___ = ___tmp_env()

    #################################
    DONE
    move RopeOps to seed.types

    #################################
    DONE
    remove _14hs, _24hs...
        replaced by ___pre_check___+_ITuple

    #################################
    #respect_emplace_whnf_of_Apps4hs
    half-DONE
    @@_Apps4hs.___whnf_reduce4apps___
    using rope when sf=Apps4hs (Apps4hs ls_at_0:ts)
        ==>> sf := rope(ls_at_0, ts)
    problematic!!
        Apps4hs is whnf emplace
        unbox in above way skip update sf[0]!!
    solve:
        Apps4hs.0.0... until not Apps4hs
        whnf(inner-most Apps4hs)
        if empty ...
        elif IFixAryCallable4hs:
            backtracking until find enough args
            if not enough:..return
            whnf(the-containing-Apps4hs)
            loop
        else:...return

    #################################
    DONE
    Undefined4hs --> Error4hs<msg>

    #################################
    DONE
    BareCase4hs --> (input4case, [(CtorH4hs, [XVar], body)], (may (XVar body)))
        #to impl if_then_else4hs Maybe4hs
    Case4hs --> (input4case, [(XPattern4hs, guarded_body)])

    #################################
    DONE
    XPattern4hs check var no duplicates
        ??? deep-check?
        ___iter_vars4xpattern___ exclude UnusedPattern4hs
            iter_vars4xpattern
            deep_check_xpattern_has_no_duplicates_vars

    #################################

    #################################
    DONE-for-mix0/mix1/mix2
    deep_check<...> between parse~compile
    deep_check_Semantic4hs:
        both_Semantic4hs_Syntactic4hs
            Apps4hs may contains Syntactic4hs
        [no deep check]&[rare shallow check] to speedup at runtime
            ==>> all complex Semantic4hs need attachment check at compile_time
    deep_check_mix<u>:
        ######################
        #deep_check_mix0 === deep_check_Semantic4hs
        mix0 = deep-Semantic4hs
                # by deep_check_Semantic4hs, not just shallow check type(obj)
        ######################
        mix1 =:
            | both_Semantic4hs_Syntactic4hs(Apps4hs/++Data4hs??)
                # by shallow check is both_Semantic4hs_Syntactic4hs + recur deep_check_mix1
            | mix0
                # check after both_Semantic4hs_Syntactic4hs
                # ie. if shallow check the type is Semantic4hs but not both_Semantic4hs_Syntactic4hs, then deep_check_Semantic4hs
            | Expr8List4hs
                #no Infix4hs
                #recur deep_check_mix1
            | Var
            =====
            # | _MidWayBound
                # midway compile_result of mix2 if free_vars is not empty
                # nint2idc <<-- nint2free_var

        ######################
        [[def__mix2]]
        mix2 = mix1
            | Lambda4hs
            | _AsIfPrimeRecurLet4hs #unordered recur
        mix3 = mix2 | BareCase4hs
        mix6 = mix5 | StepSugarLet4hs #ordered nonrecur
            # (\x (\y -> ...) b) a
        mix6 = mix5 | BlockSugarLet4hs #unordered nonrecur
            # (\x y -> ...) a b
        mix3 = mix2 | RecurLet4hs #unordered = Let4hs
        mix4 = mix3 | Case4hs
        mix5 = mix4 | InputUnboxedLambda4hs
        mix7 = mix6 | OutputUnboxedStepSugarLet4hs
        mix7 = mix6 | OutputUnboxedBlockSugarLet4hs
        mix8 = mix7 | OutputUnboxedRecurLet4hs #unordered
        ######################

        ######################
        ######################

    deep_check_MixSyntactic4hs:
        === deep_check_mix<MAX>

    #################################
    DONE
    compile__mix2 +scoped_vars #at runtime

    #################################
    DONE
    let CtorH4hs(1) != CtorH4hs(True)
        #NOTE: _ITuple.__eq__ now consider type(elem)
    __eq__/__hash__ @@_ITuple:
        type(lhs) is type(rhs)
        len(lhs) == len(rhs)
        all(type(x) is type(y) for x,y in zip(lhs, rhs))
        all(x == y for x,y in zip(lhs, rhs))

    #################################
    DONE
    remove singleton-ness of the_unused_pattern
        --> default_unused_pattern

    #################################
    DONE
    BareCase4hs+may default

    #################################
    DONE
    App4Data4hs+N/len

    #################################
    DONE
    ExtendedApp4Data4hs = (aliased/bool, ctor4hs, N_ary/uint, [(idx, may ExtendedApp4Data4hs)])

    #################################
    DONE
    (mix2+Case4hs/BareCase4hs) -> mix2
    def ___deep_convert_to_mixN___(sf, N, recur_convert, /):
        replaced by fmap_on_child_mixN+shallow_degrade_unless_mix2

    #################################
    DONE-half
    refactor ___deep_convert_to_mixN___ framework
    1. shallow transform to which types?? partial ordering types
    2. deep transform but keep __class__
    ==>> 3 possibles
        1. fmap_on_child_mixN(sf, r) #keep __class__
        2. shallow_degrade_unless_mix2(fmap_on_child_mixN(sf, r))
        3. r(shallow_degrade_unless_mix2(sf))
        point out which class to do which???
    #TODO:
    ==>> query which obj need to cache/store free_vars ...
        INOUT__dynamic_mutable_free_vars
        cache/snapshot :: {addr:free_vars}
        Case4hs using used_vars=free_vars to select/filter which named var needed to be extracted

    #################################
    DONE
        StepSugarLet4hs
            # (\x (\y -> ...) b) a
        BlockSugarLet4hs
            # (\x y -> ...) a b
        InputUnboxedLambda4hs
            # \Just x -> ...
            # let f a [b] = ...
        OutputUnboxedBlockSugarLet4hs
            # let (a, b) = ...
        OutputUnboxedStepSugarLet4hs
            # let (a, b) = ...
        OutputUnboxedRecurLet4hs
            # let (a, b) = ...
        MultiInputUnboxedRecurLet4hs
            # let f a [b] = ...
            #     f [a] b = ...
    #################################
    TODO
      compile__mix2...Data4hs transparent or unbox as Apps4hs...
      consider (x,y) ie Data4hs(ctor4hs, var...)
    #################################
    TODO
    MixSyntactic4hs.___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___ :: {cls} or ()->{cls}
    #################################
    TODO
    remove _ITuple.__iter__/__contains__
        #since whnf
        + .iter__isT(sf, T)
        xxx + .iter__whnf_T(sf, T)
        iter__if_type_is
        iter__if_type_in
        iter__if(test, x)
    #################################
    #################################








##################################
##################################
##################################
[[[[[#below is older then above


Data4hs <: tuple
Expr8List4hs <: tuple


ToplevelStmt
    = DefClass ...
    | DefInstance ...
    | DeclInfix ...
    | Import ...
    | Export ...
    | DefTyp CtorH4hs [Var] [(CtorH4hs, [TypeExpr])]
    | DefTypG CtorH4hs TypeExpr [(CtorH4hs, TypeHead, TypeExpr)]
        #| DefTypG CtorH4hs TypeExpr [(CtorH4hs, TypeHead, [TypeExpr], [Expr])]
        #| DefTypG r:CtorH4hs TypeExpr [(CtorH4hs, ArrowTypeExpr<endswith r as ctor>)]
        # Mk :: (forall ..., C ...) => ... -> ... -> Tp ...
InnerStmt
    = Typing Var TypeExpr
    | DefVar Var [Unbox] BoolExpr Expr where:[InnerStmt]

#TypeExpr TypeHead [TypeExpr] TypeExpr #Arrow
TypeExpr
    = AddHeadT TypeHead TypeExpr
    | Arrow TypeExpr TypeExpr
    | Mk CtorH4hs [Expr]
    | TYPE

CtorH4hs for type:
    Arrow :: TYPE -> TYPE -> TYPE
    TYPE :: TYPE

Expr
    = AddHeadT TypeHead TypeExpr
        #= TypeExpr
    | AddHeadF FuncHead Expr # \x -> ...
    | Flow [(Var|Op|Expr)] # f a $ b
        #| Call Var [Expr]
    | If BoolExpr Expr Expr
    | Case Expr [(Unbox, BoolExpr, Expr)]
    | Let [InnerStmt] Expr
    | PyCall Expr [Expr]
    | PyData py_obj
    ---
    | Do ...
    | ListCtor ... #[ Expr | Unbox <- Expr, BoolExpr, ...]
]]]]]
##################################
##################################
##################################










#copy to
#   e others/数学/编程/lambda/CombinatorSKIBC__2__LocalBatchRouter.txt
#
##################################
##################################
##################################
[[[[[#below is copy from TODO.txt @phone


LocalBatchRouter
      LocalBatchRouter局部批量参数路由<触发动作的输入参数数量, [[参数序号]]>
      LocalBatchRouter<L, uintss> x[1..L]
        = Apps [Apps [x[i] | i<-uints] | uints<-uintss]
        where
          Apps = foldl I App

##################################
##################################
py -m nn_ns.functional._try_CombinatoryLogic > $my_tmp/out4py/nn_ns.functional._try_CombinatoryLogic.case0.1-14.txt
    指数增长？！！！
    view /sdcard/0my_files/tmp//out4py/nn_ns.functional._try_CombinatoryLogic.case0.1-14.txt
  ====其实，并非一定要只使用SKIBC，我起初感兴趣的原由在于除去变量名，这样一来函数体显得更规范更容易比较结构的等同性。调用函数也不必替换变量。
  ====等效来讲，只是将远在叶节点的绑定变量所指引的污径在途中的所有丫节点标记指引
  ======显化局部指引
  T[x]=x #必是 自由变量
  T[App f e]=App T[f] T[e]
  T[(Abs x[i])+ z]=K<1+n> z
      #n 表示 Abs 的数量，(1+n)代表 触发动作的输入参数数量
  T[(Abs x[i])+ x[i]]=I<n,i> z
      #n 表示 Abs 的数量，也代表 触发动作的输入参数数量，i代表 反弹的参数的输入序号
  T[(Abs x[i])+ f (App e[j])+]=S<m+n,[[i<-[1..n]{#sorted#} | x[i] <- FV(e[j])] | j<-[1..m]]> T[(Abs x[i] if x[i]<-FV(f))* f] ...T[(Abs x[i] if x[i]<-FV(e[j]))* e[j]]...
    #批量处理，反正，在头部所有连续Abs丫节点都接受到参数之前，函数体 等效于 未触发
    #注意:这与 单纯地使用 SKIBC 是不同的，批量一次性自顶向下vs多层次碰撞自顶向下，后者代码爆炸/或比较难估计，前者上限必然是O(n^3)，现将前者再转化为后者...关键就是T[(\x[1..n] -> Apps [Apps [f[i]]++x[1..n] | i<-[1..n]])]=O(?<n>)??其中 f[1..n]不含x[1..n]也不含Abs。比较难估计，可见，S<m+n,...>编码了大量信息，缩减代码数量。
    # Apps [] === I
    泛化S<m+n,...>以更好地处理 排列组合:
      #old-name:LocalBatchSchedule局部批量参数转发指引
      LocalBatchRouter局部批量参数路由<触发动作的输入参数数量, [[参数序号]]>
      LocalBatchRouter<L, uintss> x[1..L]
        = Apps [Apps [x[i] | i<-uints] | uints<-uintss]
        where
          Apps = foldl I App
    系统[Var+Abs+App]
    <==>系统[Var+Abs+Apps]
    <==>系统[Var+Apps+LocalBatchRouter]
      #Var自由变量
      #Apps 用于表达 LocalBatchRouter 触发动作后的展开式
    Apps 计算:
      Apps 简化:
        Apps [e] -> e
        Apps [Apps hs, ts...] -> Apps (hs++ts)
      Apps 动作:
        Apps [Abs x e, y, ts...] -> Apps [call(Abs x e, y), ts...]
        Apps [LocalBatchRouter<L, uintss>, ys...{len=L}, ts...] -> Apps [call(LocalBatchRouter<L, uintss>, ys), ts...]

SKIBC:
    S = \x2f x2a x -> ((x2f x) (x2a x))
        = LocalBatchRouter(3, [0, 2], [1, 2])
    K = \a b -> a
        = LocalBatchRouter(2, [0])
    I = \a -> a
        = LocalBatchRouter(1, [0])
        = LocalBatchRouter(0)
    B = \f g a -> f (g a)
        = LocalBatchRouter(3, [0], [1, 2])
        #= \f -> S (K f) = B S K
        #=\f g x -> f (g x)
        #   = \f g -> S (K f) g
        #   = \f -> S (K f)
        #   = S (K S) K
        ############################
        # S (K S) K f
        #   = (K S f) (K f)
        #   = S (K f)
        #####################
        # S (K f) g x
        #   = (K f x) (g x)
        #   = f (g x)
        #####################
    C = \f a b -> f b a
        = LocalBatchRouter(3, [0, 2], [1])
        = LocalBatchRouter(3, [0, 2, 1])
        #=\f a b -> f b a
        #   =\f a -> (S f) (K a)
        #   =\f -> S (K (S f)) K
        #   = S (\f-> S (K (S f))) (K K)
        #   = S (S (K S) (\f-> K (S f))) (K K)
        #   = S (S (K S) (S (K K) (\f->S f))) (K K)
        #   = S (S (K S) (S (K K) S)) (K K)
        ############################
        # S (S (K S) (S (K K) S)) (K K) f
        #   = (S (K S) (S (K K) S) f) (K K f)
        #   = ((K S f) (S (K K) S f)) K
        #   = S ((K K f) (S f)) K
        #   = S (K (S f)) K
        #####################
        # S (K (S f)) K a
        #   = (K (S f) a) (K a)
        #   = (S f) (K a)
        #   = S f (K a)
        #####################
        # S f (K a) b
        #   = (f b) (K a b)
        #   = f b a
        #####################


    #fix #calc_fix_point
        x = f x = y f
        y f = f (y f)
        y = h h
        h = \h f -> f (h h f)
    Y = H H
        # Y f = H H f
        #   = f (H H f)
        #   = f (Y f)
    H = \h f -> f (h h f)
        = LocalBatchRouter(2, [1], [0, 0, 1])
        #= \h f -> f (h h f)
        #   = \h -> S I (h h)
        #   = S (K (S I)) (\h-> h h)
        #   = S (K (S I)) (S I I)
        ############################
        # S (K (S I)) (S I I) h
        #   = (K (S I) h) (S I I h)
        #   = (S I) (h h)
        #   = S I (h h)
        #####################
        # S I (h h) f
        #   = f (h h f)
        #####################
    DEAD = (S I I) (S I I)

]]]]]
##################################
##################################
##################################

#'''

#################################
#HHHHH
__all__ = '''

CombinatorSKIBC
    S
    K
    I
    B
    C
    Yh
    Y

deep_convert_to_mix2
deep_check_mix2
compile__mix2
main_link__payload4CASE_MIDWAY
link__payload4CASE_MIDWAY
mk_apps
mk_apps5iter
deep_reduce4apps
whnf_reduce4apps
eq4output4apps
rebuild_apps5output


    Meta4check
    ABC4check
    Meta4check_cls_members_consistent
    Meta4check4object
    Meta4check4tuple
    IIsCls4Obj4hs
    is_obj4hs
    is_cls4obj4hs
    check_obj4hs
    check_cls4obj4hs
    IHasNoInnerMixSyntactic4hs
    BaseSyntactic4hs
    BaseSemantic4hs
    IFixAryCallable4hs
    IReduceable4apps4hs
    is_impure_stmt4hs
    is_cls4impure_stmt4hs
    Apps4hs
    eq4output4placeholder
    rebuild_apps5output
    eq4output4apps
    I
    mk_apps
    mk_apps5iter
    whnf_reduce4apps
    deep_reduce4apps
    deep_reduce4apps_
    check_intXs_between
    check_uintXs_lt
    check_uintXs
    fold__objXtuple
    fold__intXiter
    intXiter2intXtuple
    FreeLocalBatchRouter
    mk_FreeLocalBatchRouter
    mk_LocalBatchRouter
    LocalBatchRouter
    CombinatorSKIBC
    ExtendedFreeLocalBatchRouter
    mk_ExtendedFreeLocalBatchRouter
    Error4hs
    the_undefined
    Data4hs
    Data4py
    IFunc4py
    Expr4py
    Stmt4py
    App4Data4hs
    ExtendedApp4Data4hs
    PathIndex4Data4hs
    var2getter
    Infix4hs
    VarN4hs
    VarH4hs
    VarR4hs
    Var4hs
    UnusedPattern4hs
    default_unused_pattern
    CtorR4hs
    Ctor4hs
    CtorH4hs
    Ctor4Nothing4Data4hs
    Ctor4Just4Data4hs
    Ctor4False4Data4hs
    Ctor4True4Data4hs
    True4Data4hs
    False4Data4hs
    Nothing4Data4hs
    mk_Just4Data4hs
    mk_Ctor4Integer4Data4hs
    mk_Integer4Data4hs
    mk_Ctor4Tuple4Data4hs
    mk_Tuple4Data4hs_
    mk_f4hs__Tuple4Data4hs_
    ctor4hs_to_f4hs
    ctor4Pair4hs
    VarTypes4get
    check_var
    is_var
    is_cls4var
    Expr8List4hs
    mk_Lambda4hs
    Lambda4hs
    ILet4hs
    RecurLet4hs
    Let4hs
    BlockSugarLet4hs
    StepSugarLet4hs
    IOutputUnboxedLet4hs
    OutputUnboxedBlockSugarLet4hs
    OutputUnboxedStepSugarLet4hs
    OutputUnboxedRecurLet4hs
    MultiInputUnboxedRecurLet4hs
    mk_MultiInputUnboxedRecurLet4hs
    InputUnboxedLambda4hs
    is_tuple
    is_pair
    is_pairs
    fold__guarded_body
    check_pairs
    Case4hs
    BareCase4hs
    is_triple
    is_triples
    check_triple
    check_triples
    if_then_else___Syntactic4hs
    fold_Maybe___Syntactic4hs
    xpattern__to__params_ExtendedApp4Data4hs_pair
    is_xvar
    check_xvar
    check_xpattern
    Alias4Pattern4hs
    Pattern4hs
    iter_vars4xpattern
    deep_check_xpattern_has_no_duplicates_vars
    XVarTypes
    XPatternTypes
    IFromName
    MkVarH4hs
    mk_var
    MkCtorH4hs
    mk_ctor
    S
    K
    B
    C
    Yh
    Y
    deep_check_mix0
    MixSyntactic4hs__Types4mix1
    MixSyntactic4hs__Types4mix2
    MixSyntactic4hs__Types4mix3
    MixSyntactic4hs__Types4mix4
    deep_check_mix1
    deep_check_mix2
    deep_check_mix3
    deep_check_mix4
    fmap_on_child_mixN
    shallow_degrade_unless_mix2
    deep_convert_to_mix2
    deep_convert_to_mix3
    deep_convert_to_mix4
    compile__mix2
    main_link__payload4CASE_MIDWAY
    link__payload4CASE_MIDWAY



    '''.split()
#__all__

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
from abc import ABC, abstractmethod, ABCMeta
from collections import namedtuple
from collections import Counter
#from functools import partial
from seed.tiny import fst, snd, echo, mk_tuple, check_uint, check_callable, MapView, check_type_is, check_pair#, check_tuple, check_bool
from seed.tiny_.check import check_uint_lt, check_int_ge_lt as check_int_between #, check_int_ge, check_int_ge_le
from seed.helper.repr_input import repr_helper
from seed.tiny import expectError
from seed.tiny import iter_cls_member_pairs_in_mro_at, get_mro4cls, get_dict4cls#, get_dict4obj
from seed.tiny import get5cls, call5cls, get5cls_, call5cls_
from seed.types.RopeOps import RopeOps
from seed.seq_tools.seq_index_if import seq_find_if #seq_index, seq_index_if, seq_find, seq_find_if
from seed.tiny_.containers import null_frozenset, mk_frozenset #null_str, null_bytes, null_int, null_tuple, null_frozenset, null_mapping_view, null_iter, mk_frozenset, mk_tuple

___end_mark_of_excluded_global_names__0___ = ...

class Meta4check(ABCMeta):
    __slots__ = ()
    def __call__(sf8cls, /, *args, **kwargs):
        if sf8cls.__abstractmethods__: raise TypeError(sorted(sf8cls.__abstractmethods__))


        ##################################
        ##################################

        #sf8cls.___pre_check___(sf8cls, *args, **kwargs)
        for C, ___pre_check___ in iter_cls_member_pairs_in_mro_at(sf8cls, '___pre_check___', apply_descriptor_protocol=True):
            ___pre_check___(sf8cls, *args, **kwargs)
        ##################################
        ##################################
        sf8obj = type(sf8cls).___new4call___(sf8cls, *args, **kwargs)
        ##################################
        ##################################
        #sf8cls.___post_check___(sf8obj)
        for C, ___post_check___ in iter_cls_member_pairs_in_mro_at(sf8cls, '___post_check___', apply_descriptor_protocol=True):
            ___post_check___(sf8obj)
        ##################################
        ##################################
        return sf8obj
    def ___new4call___(sf8cls, /, *args, **kwargs):
        sf8obj = sf8cls.__new__(sf8cls, *args, **kwargs)
        if type(sf8obj) is sf8cls:
            sf8cls.__init__(sf8obj, *args, **kwargs)
        #is type? ==>> __init_subclass__
        return sf8obj
class ABC4check(metaclass=Meta4check):
    __slots__ = ()
    @abstractmethod
    def ___pre_check___(cls, /, *args):
        return
    @abstractmethod
    def ___post_check___(sf, /):
        return


class Meta4check(Meta4check, ABC4check):
    __slots__ = ()
    #@override
    def ___pre_check___(cls, /, *args):
        return
    #@override
    def ___post_check___(sf, /):
        return
class ABC4check(ABC4check, metaclass=Meta4check):
    __slots__ = ()
#ABC4check()

class Meta4check_cls_members_consistent(Meta4check):
    'eg. all boolean members keep the same if be overrided'
    __slots__ = ()
    ___types4consistent_member___ = (bool,)
    #@override
    def ___post_check___(sf8cls, /):
        mro = get_mro4cls(sf8cls)
        k2n = Counter(k for d in map(get_dict4cls, mro) for k in d)
        ks = {k for k, n in k2n.items() if n >= 2}
        ts = sf8cls.___types4consistent_member___
        for k in ks:
            it = iter_cls_member_pairs_in_mro_at(sf8cls, k, apply_descriptor_protocol=True)
            for C, member in it:
                curr = type(member) in ts
                if curr: break
            pre = curr
            pre_C = C
            pre_x = member
            for C, member in it:
                curr = type(member) in ts
                if curr:
                    if not pre: raise TypeError((sf8cls, k, pre_C, C, pre_x, member))
                    if not pre_x == member: raise TypeError((sf8cls, k, pre_C, C, pre_x, member))
                else:
                    pass
                pre = curr
                pre_C = C
                pre_x = member

        return

if 0:
    class Meta4check4type(Meta4check_cls_members_consistent):
        'using type.__new__ #.__init_subclass__'
        __slots__ = ()

class Meta4check4object(Meta4check_cls_members_consistent):
    'using object.__new__'
    __slots__ = ()
    def ___new4call___(sf8cls, /, *args, **kwargs):
        sf8obj = object.__new__(sf8cls)
        sf8cls.__init__(sf8obj, *args, **kwargs)
        return sf8obj

class Meta4check4tuple(Meta4check_cls_members_consistent):
    'using tuple.__new__'
    __slots__ = ()
    def ___new4call___(sf8cls, /, *args):
        #bug:return tuple.__new__(sf8cls, *args, **kwargs)
        return tuple.__new__(sf8cls, args)
    #bug: ___new4call___ = tuple.__new__

r'''
#class Meta4getitem(ABCMeta):
class Meta4check4tuple(ABCMeta):
    'using tuple.__new__'
    __slots__ = ()
    if 0:
        def __getitem__(sf8cls, args, /):
            'T(a, b, c) <==> T[a, b, c]'
            return sf8cls(*args)
    #def __call__(sf8cls, /, *args, **kwargs):
        #sf8cls.___pre_check___(sf8cls, *args, **kwargs)
        #sf8obj = super().__call__(*args, **kwargs)
        #sf8obj = tuple.__new__(sf8cls, *args, **kwargs)
    def __call__(sf8cls, /, *args):
        sf8cls.___pre_check___(sf8cls, *args)
        sf8obj = tuple.__new__(sf8cls, args)
        sf8cls.___post_check___(sf8obj)
        return sf8obj
#'''

#class IIsCls4Obj4hs(metaclass=ABCMeta):
class IIsCls4Obj4hs(ABC4check, metaclass=Meta4check_cls_members_consistent):
    r'''see:is_obj4hs/is_cls4obj4hs # is semantic at runtime (most not syntactic at parse-phase), but Apps4hs both!!!
    # see-[[both_Semantic4hs_Syntactic4hs]]
    #
    #see:is_obj4hs
    #see:is_cls4obj4hs
    #
    #see:_deep_convert_to_mixN
    #see:_deep_check_mixN
    #
    #see:deep_convert_to_mixN
    #
    #see:deep_check_mix0
    #see:deep_check_mix1
    #see:deep_check_mix2
    #see:deep_check_mix3
    #see:deep_check_mix4
    #
    #'''
    __slots__ = ()
    @abstractmethod
    class ___is_cls4obj4hs___:pass
    #___is_cls4obj4hs___ = False
    #___is_cls4impure_stmt4hs___ = False
        #see:IFixAryCallable4hs:which reset to be abstractmethod

    #@override
    def __getattribute__(sf, nm, /):
        raise AttributeError#TypeError

    @abstractmethod
    #see:_deep_check_mixN
    def ___deep_check_mixN___(sf, recur_check, /):
        '-> None #apply recur_check on inner MixSyntactic4hs'
    #fmap_on_child_mixN
    #see:_deep_convert_to_mixN
    #shallow_degrade_unless_mix2
    @abstractmethod
    def ___fmap_on_child_mixN___(sf, recur_convert, /):
        'sf:mix -> (mix->mix) -> mix'
    @abstractmethod
    def ___shallow_degrade_unless_mix2___(sf, /):
        'sf:mix<M> -> mix<N> # 2 <= N < M or 2 == N == M'

    @abstractmethod
    class ___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___:
        ':: {cls} or ()->{cls} #for MixSyntactic4hs #see:___shallow_degrade_unless_mix2___'
    r'''
    @abstractmethod
    #see:_deep_convert_to_mixN
    def ___deep_convert_to_mixN___(sf, N, recur_convert, /):
        'N/uint -> (mix->mix<N>) -> mix<N> #2<=N, recur_convert<N> neednot and cannot accept N'
    #'''

    #see: _ITuple which tuple.__ne__
    #override
    def __ne__(sf, ot, /):
        return not sf == ot


#IIsCls4Obj4hs()
def is_obj4hs(hs_obj, /):
    return is_cls4obj4hs(type(hs_obj))
def is_cls4obj4hs(hs_cls, /):
    r = getattr(hs_cls, '___is_cls4obj4hs___', False)
    #r = hs_cls.___is_cls4obj4hs___
    check_type_is(bool, r)
    return r
def check_obj4hs(hs_obj, /):
    check_cls4obj4hs(type(hs_obj))
def check_cls4obj4hs(hs_cls, /):
    if not is_cls4obj4hs(hs_cls): raise TypeError

class IHasNoInnerMixSyntactic4hs(IIsCls4Obj4hs):
    __slots__ = ()
    #@override
    def ___deep_check_mixN___(sf, recur_check, /):
        '-> None #apply recur_check on inner MixSyntactic4hs'
        return
    #@override
    def ___fmap_on_child_mixN___(sf, recur_convert, /):
        'sf:mix -> (mix->mix) -> mix'
        return sf
    #@override
    def ___shallow_degrade_unless_mix2___(sf, /):
        'sf:mix<M> -> mix<N> # 2 <= N < M or 2 == N == M'
        return sf

    #@override
    ___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___ = null_frozenset
    ':: {cls} or ()->{cls} #for MixSyntactic4hs #see:___shallow_degrade_unless_mix2___'


class ___0:
    __slots__ = ()
class ___1:
    __slots__ = ()
class BaseSyntactic4hs(IIsCls4Obj4hs, ___1, ___0):
    'syntactic'
    __slots__ = ()
    ___is_cls4obj4hs___ = False

    #################################
class BaseSemantic4hs(IIsCls4Obj4hs, ___0, ___1):
    'semantic'
    __slots__ = ()
    ___is_cls4obj4hs___ = True
class _ITuple(tuple, IIsCls4Obj4hs, ABC4check, metaclass=Meta4check4tuple):
    __slots__ = ()
    #@override
    def ___pre_check___(cls, /, *args):
        return
    #@override
    def ___post_check___(sf, /):
        return
    #@override
    def __getitem__(sf, k, /):
        return tuple.__getitem__(sf, k)
    #@override
    def __getattribute__(sf, nm, /):
        raise AttributeError#TypeError
    #@override
    def __repr__(sf, /):
        cls = type(sf)
        nm = cls.__name__
        body = tuple.__repr__(sf)
        return f'{nm!s}{body!s}'
        ls = [*sf]
        return f'{nm!s}{ls!r}' # |..., ]or[]
    if 0:
    #@override
    #deprecated
      def __eq__(sf, ot, /):
        if not (type(sf) is type(ot)):
            return NotImplemented
        return tuple.__eq__(sf, ot)
    if 0:
    #@override
    #deprecated
      def __hash__(sf, /):
        cls = type(sf)
        h = tuple.__hash__(sf)
        return hash((id(cls), h))

    #@override #tuple.__ne__
    __ne__ = IIsCls4Obj4hs.__ne__
    #@override
    def __eq__(lhs, rhs, /):
        if lhs is rhs: return True
        if not (type(lhs) is type(rhs)):
            return NotImplemented
        len = tuple.__len__
        iter = tuple.__iter__
        return (len(lhs) == len(rhs)
            and all(type(x) is type(y) for x,y in zip(iter(lhs), iter(rhs)))
            #and all(x == y for x,y in zip(iter(lhs), iter(rhs)))
            and tuple.__eq__(lhs, rhs)
            )

    #@override
    def __hash__(sf, /):
        cls = type(sf)
        len = tuple.__len__
        iter = tuple.__iter__
        h0 = id(cls)
        h1 = len(sf)
        it = (id(type(x)) for x in iter(sf))
        h2 = hash((*it,))
        h3 = tuple.__hash__(sf)
        return hash((h0, h1, h2, h3))



class IFixAryCallable4hs(BaseSemantic4hs, IIsCls4Obj4hs):
    __slots__ = ()

    @abstractmethod
    class ___is_cls4impure_stmt4hs___:pass
    #___is_cls4impure_stmt4hs___ = False

    @abstractmethod
    def ___get_num_args4call___(sf, /):
        '-> num_args4call'
    @abstractmethod
    def ___call___(sf, /, *args):
        '-> hs_obj'
    def __call__(sf, /, *args):
        cls = type(sf)
        num_args4call = cls.___get_num_args4call___(sf)
        if not len(args) == num_args4call: raise TypeError
        result = cls.___call___(sf, *args)
        return result
#IFixAryCallable4hs()
class IReduceable4apps4hs(IIsCls4Obj4hs):
    __slots__ = ()

    if 0:
        @abstractmethod
        def ___step_one4reduce4apps___(sf, /):
            '-> ?'
    @abstractmethod
    def ___whnf_reduce4apps___(sf, /):
        '-> ?  #see: whnf_reduce4apps'
    @abstractmethod
    def ___deep_reduce4apps___(sf, known_self_is_whnf, /):
        '-> ?  #see: deep_reduce4apps'

def is_impure_stmt4hs(hs_obj, /):
    return is_cls4impure_stmt4hs(type(hs_obj))
def is_cls4impure_stmt4hs(hs_cls, /):
    r = getattr(hs_cls, '___is_cls4impure_stmt4hs___', False)
    #r = hs_cls.___is_cls4impure_stmt4hs___
    check_type_is(bool, r)
    return r

if 0:
  def step_one4reduce4apps(x, /):
    cls = type(x)
    f = get4step_one4reduce4apps(cls)
    return f(x)
if 0:
  def get4step_one4reduce4apps(cls, /):
    return getattr(cls, '___step_one4reduce4apps___', echo)
    mf = getattr(cls, '___step_one4reduce4apps___', None)
        #if cls is Apps4hs/IReduceable4apps4hs:
    if mf is None:
        f = echo
    else:
        f = mf
    return f


r'''
class Apps4hs(_ITuple, IReduceable4apps4hs):
    r'(reduced, *args,)'
    __slots__ = ()
    ___is_cls4obj4hs___ = True
    #@override
    def ___pre_check___(cls4py, reduced, /, *args):
        check_type_is(bool, reduced)
        return
    #@@deprecated Apps4hs
    #@override
    def ___step_one4reduce4apps___(sf, /):
        '-> ?'
        comment out raise NotImplementedError
        reduced = sf[0]
        if reduced:
            return sf
        L = len(sf)
        if L==1:
            #Apps4hs(False, *[])
            #Apps [] === I
            return I
        _1 = sf[1]
        cls1 = type(_1)
        #if isinstance(_1, IFixAryCallable4hs):
        if issubclass(cls1, IFixAryCallable4hs):
            f = _1
            num_args4call = cls1.___get_num_args4call___(f)
            if 2+num_args4call <= L and not is_impure_stmt4hs(f):
                args4call = sf[2:2+num_args4call]
                r = f(*args4call)
                return mk_apps(r, *sf[2+num_args4call:])
            return Apps4hs(True, *sf[1:])

        if L==2 and is_cls4obj4hs(cls1):
            #Apps4hs(False, *[_1])
            #Apps [_1] === _1
            return _1
                #except:IFixAryCallable4hs<num_args4call=0>
                #except:___is_cls4obj4hs___=False

        if cls1 is __class__:
            #Apps4hs
            return mk_apps(*_1[1:], *sf[2:])
        return Apps4hs(True, *sf[1:])
    #end-___step_one4reduce4apps___@@deprecated Apps4hs
I = Apps4hs(True, *[])
def mk_apps(*args):
    return mk_apps5iter(args)
def mk_apps5iter(args, /):
    return Apps4hs(False, *args)
if 0:
  def whnf_reduce4apps(x, /):
    #deprecated
    'whnf - weak_head_normal_form'
    f = step_one4reduce4apps
    while True:
            break
        y = f(x)
        if y is x:
            break
        x = y
    return x
if 0:
  def deep_reduce4apps(x, /):
    #deprecated
    def recur8inside_apps(x, /):
        x = recur8top(x)
        if type(x) is Apps4hs and len(x) == 2:
            (_, x) = x
        return x
    def recur8top(x, /):
        x = whnf_reduce4apps(x)
        if type(x) is Apps4hs:
            return Apps4hs(True, *map(recur8inside_apps, x[1:]))
        return x
    return recur8top(x)


#'''

r'''
e ../../python3_src/seed/types/RopeOps.py
from seed.types.RopeOps import RopeOps
import itertools #chain
class RopeOps:
    'Rope = (size, num_skips, seq, may Rope)'
    empty_rope = (0, 0, (), None)
    def len(rope, /):
        return rope[0]
    def to_tuple(rope, /):
        it = RopeOps.iter(rope)
        return tuple(it)
    def iter(rope, /):
        check_type_is(tuple, rope)
        n = RopeOps.len(rope)
        while not rope is None:
            #(size, num_skips, seq, may_rope) = rope
            (size, num_skips, seq, rope) = rope
            assert n==size
            ls = seq[num_skips:]
            yield from ls
            n -= len(ls)
        if not n==0: raise logic-err
        return#

    def mk(num_skips, seq, may_rope, /):
        if may_rope is None:
            r = RopeOps.mk1(num_skips, seq)
        else:
            rope = may_rope
            r = RopeOps.mk2(num_skips, seq, may_rope)
        return r
    def mk1(num_skips, seq, /):
        check_uint(num_skips)
        size = len(seq) - num_skips
        check_uint(size)
        if not size:
            return RopeOps.empty_rope
        return (size, num_skips, seq, None)
    def mk2(num_skips, seq, rope, /):
        h_rope = RopeOps.mk1(num_skips, seq)
            # check and get size
        check_type_is(tuple, rope)
        if not len(rope)==4: raise TypeError

        sz0 = h_rope[0] #RopeOps.len
        if sz0 == 0:
            return rope

        sz1 = rope[0] #RopeOps.len
        if sz1 == 0:
            return h_rope

        size = sz0 + sz1
        return (size, num_skips, seq, rope)
    def split_at(n, rope, /):
        '-> (initial_seq, tail_rope)'
        check_uint(n)
        check_type_is(tuple, rope)
        if n == 0:
            return (), rope

        size = rope[0]
        if not 0 <= n <= size: raise ValueError
        N = n
        L = size
        lss = []
        while n > 0:
            (size, num_skips, seq, rope) = rope
            end = num_skips+n
            ls = seq[num_skips:end]
            lss.append(ls)
            n -= len(ls)
        if not n == 0: raise logic-err
        #bug:tail_rope = RopeOps.mk(num_skips+n, seq, rope)
        tail_rope = RopeOps.mk(end, seq, rope)
        it = itertools.chain.from_iterable(lss)
        initial_seq = (*it,)
        assert len(initial_seq) == N
        assert L == N + tail_rope[0]
        return initial_seq, tail_rope
#'''


#class _Apps4hs(_ITuple, BaseSemantic4hs, IReduceable4apps4hs):
class _Apps4hs(_ITuple, IReduceable4apps4hs):
    'impl Apps4hs._input'
    __slots__ = ()
    #___is_cls4obj4hs___ = True
    ___is_cls4obj4hs___ = False
            #_Apps4hs is private type (impl-detail), shouldnot be exposed to user
    #@override
    def ___deep_check_mixN___(sf, recur_check, /):
        '-> None #apply recur_check on inner MixSyntactic4hs'
        raise NotImplementedError#user should never see it!
    #@override
    def ___fmap_on_child_mixN___(sf, recur_convert, /):
        'sf:mix -> (mix->mix) -> mix'
        raise NotImplementedError#user should never see it!
    #@override
    def ___shallow_degrade_unless_mix2___(sf, /):
        'sf:mix<M> -> mix<N> # 2 <= N < M or 2 == N == M'
        raise NotImplementedError#user should never see it!

    #@override
    ___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___ = null_frozenset
    ':: {cls} or ()->{cls} #for MixSyntactic4hs #see:___shallow_degrade_unless_mix2___'

    #@@_Apps4hs
    #@override
    if 0:
      def ___step_one4reduce4apps___(sf, /):
        '-> hs_obj'
        raise NotImplementedError
        if sf is _I: return sf
        L = len(sf)
        if L==0:
            #Apps [] === I
            return _I
        _0 = sf[0]
        cls_0 = type(_0)
        #if isinstance(_0, IFixAryCallable4hs):
        raise NotImplementedError
            #TODO
        if cls_0 is _Placeholder4hs:
            _0_old = _0
            move = False
            while cls_0 is _Placeholder4hs:
                _0 = _get_output4placeholder(_0) #raise TypeError
                cls_0 = type(_0)
                if _0 is _0_old: raise RuntimeError('cycle ref @_Placeholder4hs')
                if move:
                    _0_old = _get_output4placeholder(_0_old)
                move = not move
            return __class__(_0, *sf[1:])

        if issubclass(cls_0, IFixAryCallable4hs):
            f = _0
            num_args4call = cls_0.___get_num_args4call___(f)
            if 1+num_args4call <= L and not is_impure_stmt4hs(f):
                args4call = sf[1:1+num_args4call]
                r = f(*args4call)
                return __class__(r, *sf[1+num_args4call:])
            return sf

        elif L==1 and is_cls4obj4hs(cls_0):
            #Apps4hs(*[_0])
            #Apps [_0] === _0
            return _0
                #except:IFixAryCallable4hs<num_args4call=0>
                #except:___is_cls4obj4hs___=False

        elif cls_0 is Apps4hs:#not __class__:
            #Apps4hs
            #bug:return mk_apps(*_0, *sf[1:])
            return __class__(*_0, *sf[1:])
        return sf
    #end-deprecated ___step_one4reduce4apps___@@_Apps4hs

    def ___tmp_env():
        #@@_Apps4hs
        #@override
        def ___whnf_reduce4apps___(sf, /):
            #def ___whnf_reduce4apps___(sf, pre2whnf__ref_dict_view, ancestors__ref_set_view, /):
            '-> hs_obj|_Apps4hs  #see: whnf_reduce4apps'
            if sf is _I: return sf
            rope = ops.mk1(0, sf); del sf
            return main(rope)
        ops = RopeOps
        def main(rope, /):
            r = (recur1, rope, False)
            while not r[0] is None:
                [f, *args] = r
                r = f(*args)
            _, r = r
            if not (is_obj4hs(r) or type(r) is _Apps4hs): raise TypeError
            assert type(r) is not Apps4hs
            assert not type(r) is _Apps4hs or not r or type(r[0]) is not Apps4hs
            return r

        def rope2_apps(rope, /):
            return _Apps4hs(*ops.iter(rope))
            #return __class__(*ops.iter(rope))
        def recur1(rope, known_0_is_whnf, /):
            '-> (None, whnf)|(f, *args)'
            L = ops.len(rope)
            if L==0:
                #Apps [] === I
                return None, _I

            [_0], _rope = ops.split_at(1, rope)
            cls_0 = type(_0)
            _L = L - 1

            #######################
            #######################
            #basic case first
            #if cls_0 in (Apps4hs, __class__):#not __class__:
            if cls_0 is Apps4hs:#not __class__:
                #before test known_0_is_whnf
                #   since using rope to avoid mk _Apps4hs/Apps4hs
                ######
                if not known_0_is_whnf:
                    #once no this branch
                    #respect emplace whnf of Apps4hs
                    #respect_emplace_whnf_of_Apps4hs
                    whnf_reduce4apps(_0)
                    known_0_is_whnf = True
                    ...
                rope = ops.mk2(0, _0, _rope)
                    #<==> rope = [*_0]++_rope
                    #not <==> rope = [_0, *rope]
                #known_0_is_whnf = bool(_0)
                known_0_is_whnf = known_0_is_whnf and bool(_0)
                return recur1, rope, known_0_is_whnf


            #######################
            #######################
            #basic case first
            if issubclass(cls_0, IFixAryCallable4hs):
                #assert not issubclass(Apps4hs, IFixAryCallable4hs)
                #assert not issubclass(_Apps4hs, IFixAryCallable4hs)
                f = _0
                num_args4call = cls_0.___get_num_args4call___(f)
                check_uint(num_args4call)
                if 0 <= num_args4call <= _L and not is_impure_stmt4hs(f):
                    (args4call, _rope) = ops.split_at(num_args4call, _rope)
                    r = f(*args4call)
                    rope = ops.mk2(0, (r,), _rope)
                    known_0_is_whnf = False
                    return recur1, rope, known_0_is_whnf
                #rope = [_0]++_rope
                return None, rope2_apps(rope)
                    #not-enough-args or is_impure_stmt4hs



            #######################
            #######################
            #???[_0 is whnf]???
            if not known_0_is_whnf:
                _1 = whnf_reduce4apps(_0) #overflow <<== _Placeholder4hs mutable cause recur
                cls_1 = type(_1)
                known_0_is_whnf = True
                if _1 is not _0:
                    rope = ops.mk2(0, (_1,), _rope)
                    #rope = [_1]++_rope
                    return recur1, rope, known_0_is_whnf
                else:
                    #[_0 is whnf]
                    del _1, cls_1
                    pass

                #[_0 is whnf]
            #[_0 is whnf]
            if _L==0 and is_cls4obj4hs(cls_0):
                #Apps4hs(*[_0])
                #Apps [_0] === _0
                return None, _0
                    #except:IFixAryCallable4hs<num_args4call=0>
                    #except:___is_cls4obj4hs___=False
            else:
                #rope = [_0]++_rope
                return None, rope2_apps(rope)

            raise logic-err
        #end-recur1
        return ___whnf_reduce4apps___
    ___whnf_reduce4apps___ = ___tmp_env(); del ___tmp_env
    #end-___whnf_reduce4apps___@@_Apps4hs





    #@@_Apps4hs
    #@override
    def ___deep_reduce4apps___(sf, known_self_is_whnf, /):
        '-> hs_obj|_Apps4hs  #see: deep_reduce4apps'
        if not known_self_is_whnf:
            return deep_reduce4apps_(whnf_reduce4apps(sf), True)
        r'''
        return __class__.___deep_reduce4apps__already_whnf___(sf)
    @abstractmethod
    def ___deep_reduce4apps__already_whnf___(sf, /):
        '-> hs_obj  #see: deep_reduce4apps'
        #'''
        #return __class__(*map(deep_reduce4apps, sf))
        def f(elem, /):
            #is_obj4hs(elem)
            elem = deep_reduce4apps(elem)
            #is_obj4hs(elem)
            #assert type(elem) is not _Apps4hs/__class__
            if type(elem) is Apps4hs:#not __class__
                if len(elem)==1:
                    [elem] = elem
                    #may not is_obj4hs(elem)
            return elem
        assert not sf or type(sf[0]) is not Apps4hs
        return __class__(*map(f, sf))
    #end-___deep_reduce4apps___@@_Apps4hs
_I = _Apps4hs(*[])




if 0:
    print(type(BaseSemantic4hs))
    print(type(IReduceable4apps4hs))
#cancel TODO: remove _Placeholder4hs
#DONE: TODO: class Apps4hs(_Placeholder4hs)
class _Placeholder4hs(BaseSemantic4hs, IReduceable4apps4hs, ABC4check, metaclass=Meta4check4object):
    '(may_hs_obj,) #placeholder #see:impl of RecurDoLet4hs'
    __slots__ = '_state  _input  _output'.split()
    ___is_cls4obj4hs___ = True
    #@override
    def ___deep_check_mixN___(sf, recur_check, /):
        '-> None #apply recur_check on inner MixSyntactic4hs'
        recur_check(_get_output4placeholder(sf))
    #@override
    def ___fmap_on_child_mixN___(sf, recur_convert, /):
        'sf:mix -> (mix->mix) -> mix'
        return recur_convert(_get_output4placeholder(sf))
    #@override
    def ___shallow_degrade_unless_mix2___(sf, /):
        'sf:mix<M> -> mix<N> # 2 <= N < M or 2 == N == M'
        return sf
        return _get_output4placeholder(sf)

    #@override
    ___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___ = null_frozenset
    ':: {cls} or ()->{cls} #for MixSyntactic4hs #see:___shallow_degrade_unless_mix2___'

    #@@_Placeholder4hs
    #@override
    def __init__(apps, may_input, may_output, /, **kwargs4repr_detail):
        #assert type(apps) is Apps4hs
        del kwargs4repr_detail # to show extra info in repr()
        if may_output is None:
            # should be both None
            if not may_input is None: raise TypeError
            return#not-init!!!
        else:
            _output = may_output
            _input = may_input
            __class__.___set_once8init___(apps, _input, _output)

    def ___set_once8init___(apps, _input, _output, /):
        cases = _Ops4Apps4hs.___CASE___
        _state = cases.cNULL
        _ops4Apps4hs.init(apps, _state, _input, _output)
    #@override
    #not: def ___pre_check___(cls4py, may_input, may_output, /, **kwargs4repr_detail):
    def ___pre_check___(cls4py, /, *args, **kwargs4repr_detail):
        return
    #@override
    def ___post_check___(sf, /):
        return

    #@@_Placeholder4hs
    #@override
    if 0:
      def ___step_one4reduce4apps___(apps, /):
        '-> hs_obj'
        raise NotImplementedError
        #return _ops4Apps4hs.step_one4reduce4apps(apps)
        _output_0 = ops.get_output(apps)
        return _output_0

        #cases = _Ops4Apps4hs.___CASE___
        marks = _Ops4Apps4hs.___MARK___
        ops = _ops4Apps4hs

        _state = ops.get_state(apps)
        reduced = marks.bWHNF & _state
        if reduced:
            return apps
        _output_0 = ops.get_output(apps)
        return _output_0
        _output_1 = step_one4reduce4apps(_output_0)
    #end-deprecated ___step_one4reduce4apps___@@_Placeholder4hs


    if 0:#___whnf_reduce4apps___
        r'''
        _0 = sf
        cls_0 = type(0)
        if cls_0 is _Placeholder4hs:
            _0_old = _0
            move = False
            while cls_0 is _Placeholder4hs:
                _s = _0
                _0 = _get_output4placeholder(_0) #raise TypeError
                cls_0 = type(_0)
                if _0 is _0_old: raise RuntimeError('cycle ref @_Placeholder4hs')
                if move:
                    _0_old = _get_output4placeholder(_0_old)
                move = not move
            assert _s is not _0
            _state = ops.get_state(_s)
            sf_old = sf
            while sf is not _s:
                ops.update(sf, _state, _s)
                sf = _get_output4placeholder(sf)
            assert _0 is _get_output4placeholder(_s)
            at-most-2-layer-check-in-__init__/___set_once8init___/update
        _output_0 = _0
        #'''

    def ___xxxx_reduce4apps(apps, /, *, _deep):
        '-> hs_obj  #see: whnf_reduce4apps/deep_reduce4apps'
        marks = _Ops4Apps4hs.___MARK___
        ops = _ops4Apps4hs

        _output_0 = ops.get_output(apps) #raise TypeError if not init yet
        _state = ops.get_state(apps)
        if _deep:
            reduced = marks.bDEEP & _state
        else:
            reduced = marks.bWHNF & _state
        if reduced:
            if type(_output_0) is _Apps4hs:
                check_type_is(Apps4hs, apps)
                #is_obj4hs(apps)
                return apps
                    #Apps4hs diff _Placeholder4hs
            #is_obj4hs(_output_0)
            return _output_0

        cases = _Ops4Apps4hs.___CASE___
        if _deep:
            if 1:
                #bug: miss known_self_is_whnf cause inf-recur
                #   see:___deep_reduce4apps___: "del known_self_is_whnf"
                known_self_is_whnf = bool(marks.bWHNF & _state)
            _state |= cases.cDEEP
            recur_reduce4apps = deep_reduce4apps
            recur_reduce4apps_ = deep_reduce4apps_
            _args = (known_self_is_whnf,)
        else:
            _state |= cases.cWHNF
            recur_reduce4apps = whnf_reduce4apps
            recur_reduce4apps_ = whnf_reduce4apps
            _args = ()

        #_output_0 = ops.get_output(apps)
        _output_1 = recur_reduce4apps_(_output_0, *_args) #may inf recur

        ops.update(apps, _state, _output_1)
        return recur_reduce4apps(apps)
            #since reduced!!! test basic-case
        return apps|_output_1
                #Apps4hs diff _Placeholder4hs
    #end-___xxxx_reduce4apps@@_Placeholder4hs&&Apps4hs



    #@@_Placeholder4hs&&Apps4hs
    #@override
    def ___whnf_reduce4apps___(apps, /):
        '-> hs_obj  #see: whnf_reduce4apps'
        return __class__.___xxxx_reduce4apps(apps, _deep=False)

    #@@_Placeholder4hs&&Apps4hs
    #@override
    def ___deep_reduce4apps___(apps, known_self_is_whnf, /):
        '-> hs_obj  #see: deep_reduce4apps'
        del known_self_is_whnf
            #known_self_is_whnf by _state
        return __class__.___xxxx_reduce4apps(apps, _deep=True)



    def __eq__(sf, ot, /):
        if sf is ot: return True
        if not (type(sf) is type(ot)):
            return NotImplemented
        ops = _ops4Apps4hs
        a = ops.get_input(sf)
        b = ops.get_input(ot)
        return a == b
    def __hash__(sf, /):
        cls = type(sf)
        ops = _ops4Apps4hs
        _input = ops.get_input(sf)
        return hash((id(cls), _input))
    def __repr__(apps, /):
        ops = _ops4Apps4hs
        _state = ops.get_state(apps)
        _input = ops.get_input(apps)
        _output = ops.get_output(apps)
        return repr_helper(apps, *_input, _state=_state, _output=_output)

#class Apps4hs(BaseSemantic4hs, IReduceable4apps4hs, ABC4check, metaclass=Meta4check4object):
class Apps4hs(_Placeholder4hs):
    r'''emplace-update-for-pure-expr
    #whnf - weak_head_normal_form
    #._input-slots is immutable
    #
    #Apps4hs is Semantic4hs, not Syntactic4hs
    #   but to impl a Syntactic4hs-version-Apps4hs is too complicate
    #   so, also use Apps4hs as Syntactic4hs
    # Apps4hs-as-Syntactic4hs vs Expr8List4hs-is-Syntactic4hs
    #   Expr8List4hs may using Infix4hs
    #       but Infix4hs required cmp operator-precedence
    #
    # collect-[[both_Semantic4hs_Syntactic4hs]]:
    #   both Semantic4hs&&Syntactic4hs: Apps4hs, Data4hs
    #   cancel!!!##now not include Data4hs
    #       err:using Apps4hs [CtorH4hs, mix...]
    #       not Data4hs CtorH4hs [MixSyntactic4hs]
    #
    #
    #'''
    #emplace-eval:_input, _output, reduce-case{whnf, deep}
    #   IO?? impure-stmt: Stmt4py<___is_cls4impure_stmt4hs___=True>
    #__slots__ = '_whnf  _deep  _input  _output'.split()
    __slots__ = ()
    ___is_cls4obj4hs___ = True
    #@override
    def ___deep_check_mixN___(sf, recur_check, /):
        '-> None #apply recur_check on inner MixSyntactic4hs'
        #bug:recur_check(_get_output4apps(sf))
        _eat_iter(map(recur_check, sf))
    #@override
    def ___fmap_on_child_mixN___(sf, recur_convert, /):
        'sf:mix -> (mix->mix) -> mix'
        return __class__(*map(recur_convert, sf))
    #@override
    def ___shallow_degrade_unless_mix2___(sf, /):
        'sf:mix<M> -> mix<N> # 2 <= N < M or 2 == N == M'
        return sf

    #@override
    ___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___ = null_frozenset
    ':: {cls} or ()->{cls} #for MixSyntactic4hs #see:___shallow_degrade_unless_mix2___'


    #@override
    def __init__(apps, /, *args, **kwargs4repr_detail):
        #assert type(apps) is Apps4hs
        del kwargs4repr_detail # to show extra info in repr()
        _input = args
        _output = _Apps4hs(*args)
        super().__init__(_input, _output)
    #@override
    def ___pre_check___(cls4py, /, *args, **kwargs4repr_detail):
        return
    #@override
    def ___post_check___(sf, /):
        return

    def __len__(apps, /):
        ops = _ops4Apps4hs
        _output = ops.get_output(apps)
        if not type(_output) is _Apps4hs:
            _output = (_output,)
        return len(_output)
    def __getitem__(apps, k, /):
        ops = _ops4Apps4hs
        _output = ops.get_output(apps)
        if not type(_output) is _Apps4hs:
            _output = (_output,)
        return _output[k]



class _Ops4Apps4hs:
    #__slots__ = ()
    #   ._state, ...
    class ___MARK___:
        'bool(state&mark)'
        bWHNF = 0b001 #bit for WHNF(weak-head-normal-form)
        bDEEP = 0b010 #bit for DEEP(deep-reduced)
    class ___CASE___:
        'state=case|case'
        cNULL = 0b000
        cWHNF = 0b001 #case for WHNF(weak-head-normal-form)
        cDEEP = 0b011 #case for DEEP(deep-reduced)

    def init(ops, apps, _state, _input, _output, /):
        ops.check_output(apps, _output)
        #._input-slots is immutable
        #assert type(apps) in (Apps4hs, _Placeholder4hs)
        try:
            ops._input.__get__(apps)
                #post-init
        except AttributeError:
            #pre-init
            pass
        else:
            raise AttributeError

        ops._state.__set__(apps, _state)
        ops._input.__set__(apps, _input)
        ops._output.__set__(apps, _output)
    def check_output(ops, apps, _output, /):
        if not (is_obj4hs(_output) or (type(apps) is Apps4hs and type(_output) is _Apps4hs)): raise TypeError
    def update(ops, apps, _state, _output, /):
        check_uint(_state)
        ops.check_output(apps, _output)
        #._input-slots is immutable
        ops._input.__get__(apps)
            #post-init
        ops._state.__set__(apps, _state)
        ops._output.__set__(apps, _output)
    #def get(ops, apps, /): return (_state, _input, _output)
    def get_state(ops, apps, /):
        return ops._state.__get__(apps)
    def get_input(ops, apps, /):
        return ops._input.__get__(apps)
    def get_output(ops, apps, /):
        return ops._output.__get__(apps)
_ops4Apps4hs = _Ops4Apps4hs()
def __init_ops4Apps4hs(_ops4Apps4hs, Apps4hs, /):
    _ops4Apps4hs._state = Apps4hs._state
    _ops4Apps4hs._input = Apps4hs._input
    _ops4Apps4hs._output = Apps4hs._output
    del Apps4hs._state
    del Apps4hs._input
    del Apps4hs._output
__init_ops4Apps4hs(_ops4Apps4hs, _Placeholder4hs); del __init_ops4Apps4hs
#type.__subclasses__(_Placeholder4hs)
    # -> a fresh list of immediate subclasses.
    # fresh-list
    # immediate


_ops4placeholder = _ops4Apps4hs
def eq4output4placeholder(sf, ot, /):
    lhs = _get_output4placeholder(sf)
    rhs = _get_output4placeholder(ot)
    return lhs == rhs
def _get_output4placeholder(apps, /):
    ops = _ops4placeholder
    _output = ops.get_output(apps)
    return _output
def rebuild_apps5output(x, /):
    '-> ? #deep: _input := output'
    def recur(x, /):
        cls = type(x)
        if cls is Apps4hs:
            return mk_apps5iter(map(recur, x))
        if cls is _Placeholder4hs:
            return recur(_get_output4placeholder(x))
        return x
    return recur(x)

_get_output4apps = _get_output4placeholder
#bug:eq4output4apps = eq4output4placeholder
def eq4output4apps(sf, ot, /):
    lhs = rebuild_apps5output(sf)
    rhs = rebuild_apps5output(ot)
    return lhs == rhs


I = Apps4hs(*[])
def mk_apps(*args):
    return mk_apps5iter(args)
def mk_apps5iter(args, /):
    return Apps4hs(*args)
_types4mutable_hs_obj = (Apps4hs, _Placeholder4hs)
if 0:
  def whnf_reduce4apps(x, /):
    #deprecated
    'whnf - weak_head_normal_form'
    f = step_one4reduce4apps
    z = None
    while True:
        y = f(x)
        if y is x:
            break
        #if z is None and type(x) is Apps4hs:
        if z is None and type(x) in _types4mutable_hs_obj:
            z = x
        x = y
    0
    if z is not None:
        assert type(z) is Apps4hs
        assert is_obj4hs(y) # <- _Apps4hs.___step_one4reduce4apps___
        assert y is not z
        #required to emplace update apps
            #not: if type(y) is _Apps4hs:
        cases = _Ops4Apps4hs.___CASE___
        #marks = _Ops4Apps4hs.___MARK___
        ops = _ops4Apps4hs
        apps = z
        _output = y
        _state = ops.get_state(apps)
        _state |= cases.cWHNF
        ops.update(apps, _state, _output)
        if type(y) is _Apps4hs:
            y = z
            #_Apps4hs is private type (impl-detail), shouldnot be exposed to user
    return y
if 0:
  def deep_reduce4apps(a, /):
    #deprecated
    def recur8inside_apps(x, /):
        x = recur8top(x)
        if type(x) is Apps4hs and len(x) == 1:
            [x] = x
        return x
    def recur8top(z, /):
        if type(z) is Apps4hs:
            ops = _ops4Apps4hs
            apps = z
            marks = _Ops4Apps4hs.___MARK___
            _state = ops.get_state(apps)
            reduced = marks.bDEEP & _state
            if reduced:
                return apps
            _output = ops.get_output(apps)
            x = _output
        else:
            x = z

        y = whnf_reduce4apps(x)
        #error:assert (type(y) is _Apps4hs) is (type(x) is _Apps4hs), (type(y), type(x))
        if type(y) in (_Apps4hs, Apps4hs):
            y = type(y)(*map(recur8inside_apps, y))
        if type(z) is Apps4hs:
            assert is_obj4hs(y) # <- _Apps4hs.___step_one4reduce4apps___
            assert y is not z
            #required to emplace update apps
            if type(y) is Apps4hs:
                y = ops.get_output(y)

            cases = _Ops4Apps4hs.___CASE___
            #ops = _ops4Apps4hs
            #apps = z
            #_state = ops.get_state(apps)
            _output = y
            _state |= cases.cDEEP
            ops.update(apps, _state, _output)
            if type(y) is _Apps4hs:
                y = z
                #_Apps4hs is private type (impl-detail), shouldnot be exposed to user


        return z
    return recur8top(a)

def whnf_reduce4apps(x, /):
    return get5cls.___whnf_reduce4apps___(x, echo)()
    f = getattr(x, '___whnf_reduce4apps___', echo)
    return f(x)
def _default4deep_reduce4apps(x, known_self_is_whnf, /):
    if known_self_is_whnf:
        return x
    return whnf_reduce4apps(x)
def deep_reduce4apps(x, known_self_is_whnf=False, /):
    return deep_reduce4apps_(x, known_self_is_whnf)
def deep_reduce4apps_(x, known_self_is_whnf:bool, /):
    return get5cls.___deep_reduce4apps___(x, _default4deep_reduce4apps)(known_self_is_whnf)
    return get5cls.___deep_reduce4apps___(x, echo)(known_self_is_whnf)

I
assert _I is whnf_reduce4apps(_I)
assert I is whnf_reduce4apps(I)
assert not issubclass(Apps4hs, IFixAryCallable4hs)
assert not issubclass(_Apps4hs, IFixAryCallable4hs)
#assert hasattr(Apps4hs, '___is_cls4obj4hs___')
#assert not hasattr(Apps4hs, '___is_cls4impure_stmt4hs___')
assert is_cls4obj4hs(Apps4hs)
assert not is_cls4impure_stmt4hs(Apps4hs)









#FreeLocalBatchRouter, LocalBatchRouter
check_int_between
def _eat_iter(it:'iter None', /):
    for _ in it:pass
def check_intXs_between(m, M, iXs, /):
    'IntXs<m,M> = int<m,M> | tuple<IntXs<m,M> >'
    def f4i(i, /):
        check_int_between(m, M, i)
    f4s = _eat_iter
    fold__objXtuple(f4i, f4s, iXs)
def check_uintXs_lt(M, uXs, /):
    'UIntXs%M = uint%M | tuple<UIntXs%M>'
    check_intXs_between(0, M, uXs)
def check_uintXs(uXs, /):
    'UIntXs = uint | tuple<UIntXs>'
    f4u = check_uint
    f4s = _eat_iter
    fold__objXtuple(f4u, f4s, uXs)
def fold__objXtuple(f4o, f4s, oXs, /):
    '(obj->r) -> (Iter r -> r) -> objXs -> r   #objXs = obj | tuple<objXs>'

    def recur(oXs, /):
        if type(oXs) is tuple:
            oXss = oXs
            r = f4s(map(recur, oXss))
        else:
            o = oXs
            r = f4o(o)
        return r
    return recur(oXs)
def fold__intXiter(f4i, f4s, iXs, /):
    '(int->r) -> (Iter r -> r) ->  PseudoIntXs -> r   #PseudoIntXs = int | Iterable PseudoIntXs'

    def recur(iXs, /):
        if type(iXs) is int:
            i = iXs
            r = f4i(i)
        else:
            iXss = iXs
            r = f4s(map(recur, iXss))
        return r
    return recur(iXs)
def intXiter2intXtuple(iXit, /):
    'intXiter -> intXtuple'
    return fold__intXiter(echo, mk_tuple, iXit)


class FreeLocalBatchRouter(_ITuple, IFixAryCallable4hs, IHasNoInnerMixSyntactic4hs):
    r'''(num_args4call, uXss4body)
    #'''
    __slots__ = ()
    ___is_cls4obj4hs___ = True
    ___is_cls4impure_stmt4hs___ = False
    #@override
    def ___pre_check___(cls4py, num_args4call, uXss4body, /):
        check_uint(num_args4call)
        #check_type_is(tuple, uXss4body)
        #   uint|tuple
        check_uintXs_lt(num_args4call, uXss4body)
        return
    #@override
    def ___get_num_args4call___(sf, /):
        '-> num_args4call'
        return sf[0]
    #@override
    def ___call___(sf, /, *args):
        '-> Apps4hs'
        (num_args4call, uXss4body) = sf
        if not len(args) == num_args4call: raise TypeError
        f4u = args.__getitem__
        f4s = mk_apps5iter
        return fold__intXiter(f4u, f4s, uXss4body)
FreeLocalBatchRouter(0, ())

def mk_FreeLocalBatchRouter(num_args4call, /, *uXss4body):
    return FreeLocalBatchRouter(num_args4call, intXiter2intXtuple(uXss4body))
def mk_LocalBatchRouter(num_args4call, /, *uss4body):
    return LocalBatchRouter(num_args4call, mk_tuple(map(mk_tuple, uss4body)))
class LocalBatchRouter(_ITuple, IFixAryCallable4hs, IHasNoInnerMixSyntactic4hs):
    r'''(num_args4call, uss4body)

    LocalBatchRouter(3, [2, 1], [0, 1]) ==>> \a b c -> ((c b) (a b))'

SKIBC:
    S = \x2f x2a x -> ((x2f x) (x2a x))
        = LocalBatchRouter(3, [0, 2], [1, 2])
    K = \a b -> a
        = LocalBatchRouter(2, [0])
    I = \a -> a
        = LocalBatchRouter(1, [0])
        = LocalBatchRouter(0)
    B = \f g a -> f (g a)
        = LocalBatchRouter(3, [0], [1, 2])
    C = \f a b -> f b a
        = LocalBatchRouter(3, [0, 2], [1])
        = LocalBatchRouter(3, [0, 2, 1])

    #'''
    __slots__ = ()
    ___is_cls4obj4hs___ = True
    ___is_cls4impure_stmt4hs___ = False
    #@override
    def ___pre_check___(cls4py, num_args4call, uss4body, /):
        check_uint(num_args4call)
        check_type_is(tuple, uss4body)
        for us in uss4body:
            check_type_is(tuple, us)
        for us in uss4body:
            for u in us:
                check_uint_lt(num_args4call, u)
        return
    #@override
    def ___get_num_args4call___(sf, /):
        '-> num_args4call'
        return sf[0]
    #@override
    def ___call___(sf, /, *args):
        '-> Apps4hs'
        (num_args4call, uss4body) = sf
        if not len(args) == num_args4call: raise TypeError
        f = args.__getitem__
        return mk_apps5iter(mk_apps5iter(map(f, us)) for us in uss4body)
LocalBatchRouter(0, ())

def _prepare_CombinatorSKIBC__FreeLocalBatchRouter():
    S = mk_FreeLocalBatchRouter(3, [0, 2], [1, 2])
    K = mk_FreeLocalBatchRouter(2, 0)
    I = mk_FreeLocalBatchRouter(0)
    B = mk_FreeLocalBatchRouter(3, 0, [1, 2])
    C = mk_FreeLocalBatchRouter(3, 0, 2, 1)
    Yh = mk_FreeLocalBatchRouter(2, 1, [0, 0, 1])
    _test_SKIBC(S, K, I, B, C, Yh)
    return (S, K, I, B, C, Yh)
def _prepare_CombinatorSKIBC__LocalBatchRouter():
    S = mk_LocalBatchRouter(3, [0, 2], [1, 2])
    K = mk_LocalBatchRouter(2, [0])
    I = mk_LocalBatchRouter(0)
    B = mk_LocalBatchRouter(3, [0], [1, 2])
    C = mk_LocalBatchRouter(3, [0, 2, 1])
    Yh = mk_LocalBatchRouter(2, [1], [0, 0, 1])
    _test_SKIBC(S, K, I, B, C, Yh)
    return (S, K, I, B, C, Yh)
def _prepare_BCYh_from_SKI(S, K, I, /):
    _ = mk_apps
    _B = _(S, _(K, S), K)
    _C = _(S, _(S, _(K, S), _(S, _(K, K), S)), _(K, K))
    _Yh = _(S, _(K, _(S, I)), _(S, I, I))
    return (_B, _C, _Yh)
def _test_SKIBC(S, K, I, B, C, Yh, /, *, MoreRouterTypes=(), mk_Data4py=echo):
    _ = mk_apps
    (_B, _C, _Yh) = _prepare_BCYh_from_SKI(S, K, I)
    Y = _(Yh, Yh)
    _Y = _(_Yh, _Yh)
    def t(f5Router, f5SKI, N, expected_result, /):
        #assert type(f5Router) in {LocalBatchRouter, FreeLocalBatchRouter, Apps4hs, *MoreRouterTypes} or (f5Router is Y and f5SKI is _Y)
        assert type(f5SKI) in [Apps4hs]

        _test_f5Router = _(f5Router, *map(mk_Data4py, range(N)))
        _test_f5SKI = _(f5SKI, *map(mk_Data4py, range(N)))

        _result_f5Router = deep_reduce4apps(_test_f5Router)
        _result_f5SKI = deep_reduce4apps(_test_f5SKI)
        assert eq4output4apps(_result_f5Router, expected_result), _get_output4apps(_result_f5Router)
        assert eq4output4apps(_result_f5SKI, expected_result), _get_output4apps(_result_f5SKI)
        return
    _0, _1, _2 = map(mk_Data4py, range(3))
    t(B, _B, 3, Apps4hs(_0, Apps4hs(_1, _2)))
    t(C, _C, 3, Apps4hs(_0, _2, _1))
    t(Yh, _Yh, 2, Apps4hs(_1, Apps4hs(_0, _0, _1)))
    ##error:t(Y, _Y, 1, inf)
    ##################################

    ##################################
    #old:
    _testB = _(_B, _0, _1, _2)
    _testC = _(_C, _0, _1, _2)
    _resultB = deep_reduce4apps(_testB)
    _resultC = deep_reduce4apps(_testC)
    #assert _resultB == Apps4hs(True, _0, Apps4hs(True, _1, _2)), _resultB
    #assert _resultC == Apps4hs(True, _0, _2, _1), _resultC
    assert eq4output4apps(_resultB, Apps4hs(_0, Apps4hs(_1, _2))), _get_output4apps(_resultB)
    assert eq4output4apps(_resultC, Apps4hs(_0, _2, _1)), _get_output4apps(_resultC)
class CombinatorSKIBC:
    (S, K, I, B, C, Yh) = _prepare_CombinatorSKIBC__FreeLocalBatchRouter()
    (S, K, I, B, C, Yh) = _prepare_CombinatorSKIBC__LocalBatchRouter()
    #(S, K, I, B, C, Yh) = _prepare_CombinatorSKIBC__Lambda4hs()
    Y = mk_apps(Yh, Yh)
    recur = fix = Y
    composite = B
    flip = C
    const = K
    echo = id = I

class _MidWayBound(_ITuple, IFixAryCallable4hs, IHasNoInnerMixSyntactic4hs):
    r'''(nint2free_var, num_free_vars, num_args4call, iXss4body)

        # midway compile_result of mix2 if free_vars is not empty
        #finally filled free_vars ==>> ExtendedFreeLocalBatchRouter

        _MidWayBound nint2free_var num_free_vars num_args4call iXss4body
            closure = (var2xxx, recur_vars)
                * var2xxx :: {var: ???}
                * recur_vars :: {var}
                closure<_MidWayBound> is not closure<ExtendedFreeLocalBatchRouter>
    #'''
    __slots__ = ()
    ___is_cls4obj4hs___ = True
    ___is_cls4impure_stmt4hs___ = False
    #@override
    def ___pre_check___(cls4py, nint2free_var, num_free_vars, num_args4call:'exclude closure', iXss4body, /):
        ##################################
        check_type_is(tuple, nint2free_var)

        check_uint(num_free_vars)
        check_uint(num_args4call)
        #check_type_is(tuple, iXss4body)
        #   int|tuple


        ##################################
        if not len(nint2free_var) == num_free_vars: raise TypeError
        for var in nint2free_var:
            check_var(var)
        ##################################
        check_intXs_between(-num_free_vars, num_args4call, iXss4body)
        return
    #@override
    def ___get_num_args4call___(sf, /):
        '-> num_args4call#include closure'
        return 1+sf[-2]
    #@override
    def ___call___(sf, closure4hs, /, *args):
        '-> Apps4hs'
        (nint2free_var, num_free_vars, num_args4call, iXss4body) = sf
        if not len(args) == num_args4call: raise TypeError
        closure4hs = whnf_reduce4apps(closure4hs)
        check_type_is(Data4py, closure4hs)
        [closure4py] = closure4hs
        (var2xxx, recur_vars) = closure4py
        if 1:
            if not len(recur_vars) <= len(nint2free_var) <= len(var2xxx): raise TypeError
            if not recur_vars <= set(nint2free_var) <= var2xxx.keys(): raise TypeError

        f4s = mk_apps5iter
        def f4i(i, /):
            if i < 0:
                var = nint2free_var[i]
                x = var2xxx[var]
                #if not is_obj4hs(x): raise TypeError
                    #may not is_obj4hs(x)
                if var in recur_vars:
                    #recur_group
                    check_type_is(__class__, x)
                    bound_x = mk_apps(x, closure4hs)
                else:
                    bound_x = x
                r = bound_x

            else:
                r = args[i]
            #may not is_obj4hs(r)
            return r

        return fold__intXiter(f4i, f4s, iXss4body)
_MidWayBound((), 0, 0, ())


class ExtendedFreeLocalBatchRouter(_ITuple, IFixAryCallable4hs, IHasNoInnerMixSyntactic4hs):
    r'''(total4closure, shape4closure, nint2idc, num_free_vars, num_args4call, iXss4body)

        #see:_MidWayBound nint2free_var num_free_vars num_args4call iXss4body

        ExtendedFreeLocalBatchRouter total4closure shape4closure nint2idc num_free_vars num_args4call iXss4body
            * total4closure :: uint
                == sum of shape4closure
            * shape4closure :: ((uint, uint, uint), uint)
                == lift len of closure
            * nint2idc :: [((0,uint%3,uint)|(1,uint))]
            * num_free_vars :: uint
                == len nint2idc
            * num_args4call :: uint
                #input num_args4call: exclude closure
                #___get_num_args4call___ -> include closure
            * iXss4body :: [IntXs<-num_free_vars, num_args4call>]
                why not (iXss4body::IntXs)?
                    ie. why iXss4body is tuple not uint
                    since __call__ -> hs_obj
                        if uint, may return non-hs_obj
                        using tuple, always wrapped by Apps4hs



        ex_router(closure, /, *args4call)
            len(args4call) == sf.num_args4call
            closure = (bound_groups/[[hs_obj]], recur_group/[ExtendedFreeLocalBatchRouter])
                bound_groups = (bound_builtins_and_constants, bound_globals, bound_dynamic_free_vars)
                recur_group = ()|[ExtendedFreeLocalBatchRouter]
                    #unbound_group
            recur_group = closure[-1] #maybe empty
            shape_of closure == sf.shape4closure
 
    #'''
    __slots__ = ()
    ___is_cls4obj4hs___ = True
    ___is_cls4impure_stmt4hs___ = False
    #@override
    def ___pre_check___(cls4py, total4closure, shape4closure, nint2idc, num_free_vars, num_args4call:'exclude closure', iXss4body, /):
        ##################################
        check_uint(total4closure)
        check_type_is(tuple, shape4closure)
        check_type_is(tuple, nint2idc)

        check_uint(num_free_vars)
        check_uint(num_args4call)
        #check_type_is(tuple, iXss4body)
        #   int|tuple

        ##################################
        if not len(shape4closure) == 2: raise TypeError
        check_uintXs(shape4closure)
        (lens_of_3_bound_groups, len_recur_group) = shape4closure
        if not len(lens_of_3_bound_groups) == 3: raise TypeError
        if not sum(lens_of_3_bound_groups) + len_recur_group == total4closure: raise TypeError


        ##################################
        if not len(nint2idc) == num_free_vars: raise TypeError
        check_uintXs(nint2idc)
        for idc in nint2idc:
            if not idc:  raise TypeError
            i = idc[0]
            if not i < 2:  raise TypeError
            if i:
                if not len(idc) == 2: raise TypeError
                _, j = idc
                if not j < shape4closure[i]:  raise TypeError
            else:
                if not len(idc) == 3: raise TypeError
                _, j, k = idc
                if not j < 3:  raise TypeError
                if not k < shape4closure[i][j]:  raise TypeError
        ##################################

        ##################################
        check_intXs_between(-num_free_vars, num_args4call, iXss4body)
        return
    #@override
    def ___get_num_args4call___(sf, /):
        '-> num_args4call#include closure'
        return 1+sf[-2]
    #@override
    def ___call___(sf, closure4hs, /, *args):
        '-> Apps4hs'
        (total4closure, shape4closure, nint2idc, num_free_vars, num_args4call, iXss4body) = sf
        if not len(args) == num_args4call: raise TypeError
        if 1:
            closure4hs = whnf_reduce4apps(closure4hs)
            check_type_is(Data4py, closure4hs)
            [closure4py] = closure4hs
            ((bound_builtins_and_constants, bound_globals, bound_dynamic_free_vars), recur_group) = closure4py
            (lens_of_3_bound_groups, len_recur_group) = shape4closure
            if not len(recur_group) == len_recur_group: raise TypeError
            if not (*map(len, closure4py[0]),) == lens_of_3_bound_groups: raise TypeError

        def f4i(i, /):
            if i < 0:
                idc = nint2idc[i]
                x = closure4py
                for j in idc:
                    check_type_is(tuple, x)
                    x = x[j]
                if not is_obj4hs(x): raise TypeError
                if idc[0] == 1:
                    #recur_group
                    check_type_is(__class__, x)
                    bound_x = mk_apps(x, closure4hs)
                else:
                    assert idc[0] == 0
                    bound_x = x
                r = bound_x
                #is_obj4hs(r)

            else:
                r = args[i]
                #may not is_obj4hs(r)???
            return r
        ls = [None]*(num_args4call+1+num_free_vars)
        for i in range(-num_free_vars, num_args4call):
            ls[i] = f4i(i)
        assert ls[num_args4call] is None
        assert all(x is not None or i == num_args4call for i, x in enumerate(ls))
        f4i = ls.__getitem__
        f4s = mk_apps5iter
        return fold__intXiter(f4i, f4s, iXss4body)
ExtendedFreeLocalBatchRouter(0, ((0,0,0),0), (), 0,0,())

def mk_ExtendedFreeLocalBatchRouter(shape4closure, nint2idc, num_free_vars, num_args4call, iXss4body, /):
    'why not len(nint2idc)? num_free_vars occur for human eyes'
    shape4closure = intXiter2intXtuple(shape4closure)
    nint2idc = intXiter2intXtuple(nint2idc)
    iXss4body = intXiter2intXtuple(iXss4body)
    total4closure = sum(shape4closure[0])+shape4closure[1]
    #num_free_vars = len(nint2idc)
    assert num_free_vars == len(nint2idc)
    num_args4call
    return ExtendedFreeLocalBatchRouter(total4closure, shape4closure, nint2idc, num_free_vars, num_args4call, iXss4body)





r'''
class Undefined4hs(BaseSemantic4hs, IReduceable4apps4hs, IHasNoInnerMixSyntactic4hs, metaclass=Meta4check4object):
    'vs Data4hs'
    __slots__ = ()
    ___is_cls4obj4hs___ = True
    #@override
    def ___pre_check___(cls4py, /):
        raise TypeError('Undefined4hs is singleton')
        return
    #@override
    def ___post_check___(sf, /):
        return
    #@override
    def __getattribute__(sf, nm, /):
        raise AttributeError#TypeError
    def __repr__(sf, /):
        return 'the_undefined'
    #@override
    def ___whnf_reduce4apps___(sf, /):
        '-> ?  #see: whnf_reduce4apps'
        raise TypeError('whnf(undefined)')
        return the_undefined
    #@override
    def ___deep_reduce4apps___(sf, known_self_is_whnf, /):
        '-> ?  #see: deep_reduce4apps'
        raise TypeError('whnf(undefined)')
        return the_undefined
the_undefined = object.__new__(Undefined4hs)
Undefined4hs.__abstractmethods__ = frozenset([' '])
#'''


class Error4hs(_ITuple, BaseSemantic4hs, IReduceable4apps4hs, IHasNoInnerMixSyntactic4hs):
    '(err_msg,) #impl the_undefined #vs Data4hs'
    __slots__ = ()
    ___is_cls4obj4hs___ = True
    #@override
    def ___pre_check___(cls4py, err_msg, /):
        #check_type_is(str, err_msg)
        return
    #@override
    def ___post_check___(sf, /):
        return
    #@override
    def __getattribute__(sf, nm, /):
        raise AttributeError#TypeError
    def __repr__(sf, /):
        [err_msg] = sf
        return repr_helper(sf, err_msg)
    #@override
    def ___whnf_reduce4apps___(sf, /):
        '-> ?  #see: whnf_reduce4apps'
        raise TypeError(f'whnf({sf!r})')
    #@override
    def ___deep_reduce4apps___(sf, known_self_is_whnf, /):
        '-> ?  #see: deep_reduce4apps'
        raise TypeError(f'whnf({sf!r})')
the_undefined = Error4hs('the_undefined')



#class Tuple4Data4hs -->> CtorH4hs -->> Tuple4CtorH4hs -> Ctor4Tuple4Data4hs
#   mk_Ctor4Tuple4Data4hs
class Data4hs(_ITuple, BaseSemantic4hs, IReduceable4apps4hs):
    r'''(constructor, *args:[MixSyntactic4hs]) #Data4hs vs Tuple4Data4hs vs Undefined4hs
    #
    # see-[[both_Semantic4hs_Syntactic4hs]]
    #
    #'''
    __slots__ = ()
    ___is_cls4obj4hs___ = True
    #@override
    def ___deep_check_mixN___(sf, recur_check, /):
        '-> None #apply recur_check on inner MixSyntactic4hs'
        _, *args = sf
        #bug:_eat_iter(map(recur_check, sf))
        _eat_iter(map(recur_check, args))
        return
    #@override
    def ___fmap_on_child_mixN___(sf, recur_convert, /):
        'sf:mix -> (mix->mix) -> mix'
        (ctor4hs, *args) = sf
        return __class__(ctor4hs, *map(recur_convert, args))
    #@override
    def ___shallow_degrade_unless_mix2___(sf, /):
        'sf:mix<M> -> mix<N> # 2 <= N < M or 2 == N == M'
        if not _is_cls_both(__class__):
            return sf
        else:
            #both_Semantic4hs_Syntactic4hs
            #unbox into Apps4hs
            (ctor4hs, *args) = sf
            N = len(args)
            f4hs = ctor4hs_to_f4hs(N, ctor4hs)
            return mk_apps(f4hs, *args)
    #@override

    #@override
    ___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___ = null_frozenset
    ':: {cls} or ()->{cls} #for MixSyntactic4hs #see:___shallow_degrade_unless_mix2___'


    #@override
    def ___pre_check___(cls4py, ctor4hs, /, *args):
        check_type_is(CtorH4hs, ctor4hs)
        return
        try:
            if ctor4hs == ctor4Pair4hs:
                #print(len(args))
                assert len(args) == 2
        except NameError:pass

        return

    #@override
    def ___whnf_reduce4apps___(sf, /):
        '-> Data4hs  #see: whnf_reduce4apps'
        return sf
    #@override
    def ___deep_reduce4apps___(sf, known_self_is_whnf, /):
        '-> Data4hs  #see: deep_reduce4apps'
        del known_self_is_whnf
            #since known_self_is_whnf=True
        #bug:return __class__(sf[0], map(deep_reduce4apps, sf[1:]))
        return __class__(sf[0], *map(deep_reduce4apps, sf[1:]))


r'''
class _14hs(_ITuple):
    __slots__ = ()
    #@override
    def ___pre_check___(cls4py, the_only_arg, /):
        return
class _24hs(_ITuple):
    __slots__ = ()
    #@override
    def ___pre_check___(cls4py, x0, x1, /):
        return
#'''

class Data4py(_ITuple, BaseSemantic4hs, IHasNoInnerMixSyntactic4hs):
#class Data4py(_14hs, BaseSemantic4hs):
    #WrappedPythonData4hs
    'data4py'
    __slots__ = ()
    ___is_cls4obj4hs___ = True

    #@override
    def ___pre_check___(cls4py, data4py, /):
        return
class IFunc4py(_ITuple, IFixAryCallable4hs, IHasNoInnerMixSyntactic4hs):
    #WrappedPythonFunc4hs
    r'''(num_args4call, func4py, *py_args) #see:var2getter :: var -> (hs_env -> hs_env[0][var])

    ???Monad IO??? or impl basic runtime framework #pure-expr

    sf(*hs_args) -> hs_result
        assert len(hs_args) == num_args4call
        return func4py(*py_args, *hs_args)
            #func4py<*py_args>(*hs_args)

    #'''
    __slots__ = ()
    ___is_cls4obj4hs___ = True

    #@override
    def ___pre_check___(cls4py, num_args4call, func4py, /, *py_args):
        check_uint(num_args4call)
        check_callable(func4py)
        return
    #@override
    def ___get_num_args4call___(sf, /):
        '-> num_args4call'
        return sf[0]
    #@override
    def ___call___(sf, /, *hs_args):
        '(*hs_obj)-> hs_obj'
        (num_args4call, func4py, *py_args) = sf
        if not len(hs_args) == num_args4call: raise TypeError
        for x in hs_args: check_obj4hs(x)
        hs_result = func4py(*py_args, *hs_args)
        check_obj4hs(hs_result)
        return hs_result

        if py_args == [ctor4Pair4hs]:
            if 0:
                print(hs_result)
                print(py_args)
                print(hs_args)
            else:
                print(hs_result)
                print(len(hs_result))
                print(len(py_args))
                print(len(hs_args))
        return hs_result

class Expr4py(IFunc4py):
    '#pure #expr'
    __slots__ = ()
    ___is_cls4impure_stmt4hs___ = False
class Stmt4py(IFunc4py):
    '#impure #stmt-not-expr'
    __slots__ = ()
    ___is_cls4impure_stmt4hs___ = True


r'''[[[[[
def mk_JmpApp4Data4hs(ctor2us, /):
    if type(ctor2us) is not MapView:
        ctor2us = MapView(ctor2us)
    return ctor2us

class JmpApp4Data4hs(_ITuple, IFixAryCallable4hs, IHasNoInnerMixSyntactic4hs):
    '({CtorH4hs, us4unbox},) #to impl pattern match branch #see:BareCase4hs'
    __slots__ = ()
    ___is_cls4obj4hs___ = True
    ___is_cls4impure_stmt4hs___ = False

    #@override
    def ___pre_check___(cls4py, ctor2us, /):
        check_type_is(MapView, ctor2us)
        for ctor4hs, us4unbox in ctor2us.items():
            check_type_is(CtorH4hs, ctor4hs)
            check_type_is(tuple, us4unbox)
            for u in us4unbox:
                check_uint(u) #idx to fetch value from data2hs
        return
    #@override
    def ___get_num_args4call___(sf, /):
        '-> num_args4call'
        return 3
    #@override
    def ___call___(sf, on_error, ctor2on_match, data4hs, /):
        '-> Apps4hs'
        [ctor2us] = sf
        data4hs = whnf_reduce4apps(data4hs)
        check_type_is(Data4hs, data4hs)
        check_type_is(Data4py, ctor2on_match)
        [ctor2on_match] = ctor2on_match
        #check_type_is(MapView, ctor2on_match)
        if not len(ctor2on_match) == len(ctor2us): raise TypeError

        ctor4hs = data4hs[0]
        if not ctor4hs in ctor2us:
            return mk_apps(on_error, data4hs)
        if not ctor4hs in ctor2on_match: raise TypeError#ctor2on_match.keys() != ctor2us.keys()

        us4unbox = ctor2us[ctor4hs]
        on_match = ctor2on_match[ctor4hs]#KeyError
        it = (data4hs[1+u] for u in us4unbox)
        return mk_apps(on_match, *it)
#end-class JmpApp4Data4hs(_ITuple, IFixAryCallable4hs, IHasNoInnerMixSyntactic4hs):
#]]]]]'''


class App4Data4hs(_ITuple, IFixAryCallable4hs, IHasNoInnerMixSyntactic4hs):
    '(CtorH4hs, N_ary, *us4unbox) #to impl pattern match branch #see:BareCase4hs'
    __slots__ = ()
    ___is_cls4obj4hs___ = True
    ___is_cls4impure_stmt4hs___ = False

    #@override
    def ___pre_check___(cls4py, ctor4hs, N, /, *us4unbox):
        check_type_is(CtorH4hs, ctor4hs)
        check_uint(N) #N-ary of ctor4hs
        for u in us4unbox:
            check_uint_lt(N, u) #idx to fetch value from data2hs
        return
    #@override
    def ___get_num_args4call___(sf, /):
        '-> num_args4call'
        return 3
    #@override
    def ___call___(sf, on_error, on_match, data4hs, /):
        '-> Apps4hs'
        (ctor4hs, N, *us4unbox) = sf
        data4hs = whnf_reduce4apps(data4hs)
        check_type_is(Data4hs, data4hs)
        if not data4hs[0] == ctor4hs:
            #mismatch
            return mk_apps(on_error, data4hs)
        if not len(data4hs) == 1+N: raise TypeError
        it = (data4hs[1+u] for u in us4unbox)
        return mk_apps(on_match, *it)


class ExtendedApp4Data4hs(_ITuple, IFixAryCallable4hs, IHasNoInnerMixSyntactic4hs):
    '(aliased/bool, ctor4hs/CtorH4hs, N_ary/uint, [(idx/uint, may ExtendedApp4Data4hs)]) #to impl pattern match branch #see:Case4hs,Pattern4hs'
    __slots__ = ()
    ___is_cls4obj4hs___ = True
    ___is_cls4impure_stmt4hs___ = False

    #@override
    def ___pre_check___(cls4py, aliased, ctor4hs, N, umpairs4unbox, /):
        check_type_is(bool, aliased)
        check_type_is(CtorH4hs, ctor4hs)
        check_uint(N) #N-ary of ctor4hs

        check_pairs(umpairs4unbox)
        for u, m in umpairs4unbox:
            check_uint_lt(N, u) #idx to fetch value from data2hs
            if m is not None: check_type_is(__class__, m)
        return
    #@override
    def ___get_num_args4call___(sf, /):
        '-> num_args4call'
        return 3
    #@override
    def ___call___(sf, on_error, default2on_match, data4hs, /):
        '-> Apps4hs'
        ok = [1]
        def recur_iter(sf, data4hs, /):
            if not ok: return
            (aliased, ctor4hs, N, umpairs4unbox) = sf
            data4hs = whnf_reduce4apps(data4hs)
            check_type_is(Data4hs, data4hs)
            if not data4hs[0] == ctor4hs:
                #mismatch
                ok.clear()
                return
            if not len(data4hs) == 1+N: raise TypeError
            if aliased:
                yield data4hs
            for u, m in umpairs4unbox:
                d = data4hs[1+u]
                if m is None:
                    yield d
                else:
                    yield from recur_iter(m, d)
                    if not ok: return
        #end-def recur_iter(sf, data4hs, /):
        default = mk_apps(on_error, data4hs)
        [*ls] = recur_iter(sf, data4hs)
        if not ok:
            #mismatch
            return default
        on_match = mk_apps(default2on_match, default)
        return mk_apps(on_match, *ls)



class PathIndex4Data4hs(_ITuple, IFixAryCallable4hs, IHasNoInnerMixSyntactic4hs):
    '(*triple_path8idc/[(ctor4hs/CtorH4hs, N_ary/uint, idx/uint)],) #to impl per-var-pickout from result of pattern match #see:OutputUnboxedRecurLet4hs,ExtendedApp4Data4hs,Pattern4hs'
    __slots__ = ()
    ___is_cls4obj4hs___ = True
    ___is_cls4impure_stmt4hs___ = False

    #@override
    def ___pre_check___(cls4py, /, *triple_path8idc):
        check_triples(triple_path8idc)
        for ctor4hs, N, idx in triple_path8idc:
            check_type_is(CtorH4hs, ctor4hs)
            check_uint(N) #N-ary of ctor4hs
            check_uint_lt(N, idx)
        return
    #@override
    def ___get_num_args4call___(sf, /):
        '-> num_args4call'
        return 1
    #@override
    def ___call___(sf, data4hs, /):
        '-> ?hs_obj'
        triple_path8idc = sf
        #data4hs = tuple4data4hs8pattern_match_result
        #   eg. pattern_match_result = mk_apps(ExtendedApp4Data4hs(...), data4hs, mk_f4hs__Tuple4Data4hs_(N))
        #       N = ...iter_vars4xpattern...
        #
        for ctor4hs, N, idx in triple_path8idc:
            data4hs = whnf_reduce4apps(data4hs)
            check_type_is(Data4hs, data4hs)
            if not data4hs[0] == ctor4hs: raise TypeError
            if not len(data4hs) == 1+N: raise TypeError
            data4hs = data4hs[1+idx]
        return data4hs



r'''
class Var2Getter(_ITuple, IFixAryCallable4hs):
    __slots__ = ()
    ___is_cls4obj4hs___ = True
    #@override
    def ___pre_check___(cls4py, var, /):
        check_var(var)
#'''

def _var_getter4env4hs(var, hs_env, /):
    'hs_env is recur_group/closure/context/globals/locals/...'
    #static-closure.xxx
    #dynamic-context[instance C a]
    check_var(var)
    hs_env = whnf_reduce4apps(hs_env)
    check_type_is(Data4py, hs_env)
    [py_env_view] = hs_env
    check_type_is(MapView, py_env_view)
    return py_env_view[var]
def var2getter(var, /):
    'var2getter :: var -> (hs_env -> hs_env[0][var])  #see: Expr4py #to impl closure.xxx/context.xxx/Module.xxx/globals.xxx/where.xxx/let.xxx/...'
    check_var(var)
    return Expr4py(_var_getter4env4hs, var)


class Infix4hs(_ITuple, BaseSyntactic4hs, IHasNoInnerMixSyntactic4hs):
    'var4hs <: VarH4hs|VarR4hs|VarN4hs|CtorH4hs'
    __slots__ = ()
    ___is_cls4obj4hs___ = False

    #@override
    def ___pre_check___(cls4py, var, /):
        'elem x d === x `elem` d'
        check_var(var)

class VarN4hs(_ITuple, BaseSyntactic4hs, IHasNoInnerMixSyntactic4hs):
#class VarN4hs(_24hs, BaseSyntactic4hs):
    '(py_hashable8name, distinguish_number)  #semantic'
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    #@override
    def ___pre_check___(cls4py, py_hashable8name, distinguish_number, /):
        return
class VarH4hs(_ITuple, BaseSyntactic4hs, IHasNoInnerMixSyntactic4hs):
#class VarH4hs(_14hs, BaseSyntactic4hs):
    'py_hashable8name  #syntactic'
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    #@override
    def ___pre_check___(cls4py, py_hashable8name, /):
        return
class VarR4hs(tuple, BaseSyntactic4hs, IHasNoInnerMixSyntactic4hs):
    'py_ref8name  #semantic'
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    #@override
    def __getitem__(sf, k, /):
        return tuple.__getitem__(sf, k)
    #@override
    def __getattribute__(sf, nm, /):
        raise AttributeError#TypeError
    def __new__(cls, py_ref8name, /, **kwargs4repr_detail):
        del kwargs4repr_detail # to show extra info in repr()
        return tuple.__new__(cls, [py_ref8name])
    def __eq__(sf, ot, /):
        if sf is ot: return True
        if not (type(sf) is type(ot)):
            return NotImplemented
        [a] = sf
        [b] = ot
        return a is b
    def __hash__(sf, /):
        cls = type(sf)
        [a] = sf
        return hash((id(cls), id(a)))

    #var-using-show-magic
    def __repr__(sf, /):
        [ref] = sf
        return repr_helper(sf, ref, _addr=id(ref))
class Var4hs(BaseSyntactic4hs, IHasNoInnerMixSyntactic4hs, metaclass=Meta4check4object):
    '()  #semantic'
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    #@override
    def __getattribute__(sf, nm, /):
        raise AttributeError#TypeError
    def __init__(sf, /, **kwargs4repr_detail):
        del kwargs4repr_detail # to show extra info in repr()
    #@override
    def ___pre_check___(cls4py, /, **kwargs4repr_detail):
        return
    #@override
    def ___post_check___(sf, /):
        return
    #var-using-show-magic
    def __repr__(sf, /):
        return repr_helper(sf, _addr=id(sf))
assert not Var4hs() is Var4hs()
assert not Var4hs() == Var4hs()
assert Var4hs() is not Var4hs()
assert Var4hs() != Var4hs()


r'''[[[[[deprecated: singleton-UnusedPattern4hs/the_unused_pattern

class UnusedPattern4hs(BaseSyntactic4hs, IHasNoInnerMixSyntactic4hs, metaclass=Meta4check4object):
    '()  #syntactic'
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    #@override
    def ___pre_check___(cls4py, /):
        raise TypeError('UnusedPattern4hs is singleton')
    #@override
    def __getattribute__(sf, nm, /):
        raise AttributeError#TypeError
    def __repr__(sf, /):
        return 'the_unused_pattern'
the_unused_pattern = object.__new__(UnusedPattern4hs)
UnusedPattern4hs.__abstractmethods__ = frozenset([' '])
#]]]]]'''

class UnusedPattern4hs(_ITuple, BaseSyntactic4hs, IHasNoInnerMixSyntactic4hs):
    '(py_hashable8name,)  #syntactic #eg. _ _xxx'
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    #@override
    def ___pre_check___(cls4py, py_hashable8name, /):
        return
default_unused_pattern = UnusedPattern4hs('_')





#where is Semantic4hs-version-CtorH4hs?
#   No such thing!
#       always wrapped by Data4py
#   using CtorH4hs<qname/symbol> at runtime
#where is Semantic4hs-version-Tuple4CtorH4hs to mk Tuple4Data4hs?
#   No such thing!
#   using CtorH4hs<uint> at runtime
#
# why no CtorR4hs/Ctor4hs like VarR4hs/Var4hs??
#   CtorR4hs(x) = CtorH4hs(VarR4hs(x))
#   Ctor4hs() = CtorH4hs(Var4hs())
# H - Hash
# R - Ref/id/addr
#
def CtorR4hs(x, /):
    return CtorH4hs(VarR4hs(x))
def Ctor4hs():
    return CtorH4hs(Var4hs()) #fresh
class CtorH4hs(_ITuple, BaseSyntactic4hs, IHasNoInnerMixSyntactic4hs):
#class CtorH4hs(_14hs, BaseSyntactic4hs):
    'py_hashable8constructor_name  #syntactic #Syntactic4hs SHOULD_BE created everywhere, hence (==) isnot (is)'
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    #@override
    def ___pre_check___(cls4py, py_hashable8constructor_name, /):
        return

Ctor4Nothing4Data4hs = CtorH4hs(None)
Ctor4Just4Data4hs = CtorH4hs(...) #Ellipsis, NotImplemented
Ctor4False4Data4hs = CtorH4hs(False)
Ctor4True4Data4hs = CtorH4hs(True)
    #NOTE: _ITuple.__eq__ now consider type(elem)
    #   ==>> [CtorH4hs(1) != Ctor4True4Data4hs]
assert CtorH4hs.__ne__ is not object.__ne__
#print([(C.__ne__ is CtorH4hs.__ne__, C)for C in CtorH4hs.__mro__])
assert CtorH4hs.__ne__ is IIsCls4Obj4hs.__ne__
assert CtorH4hs(1) == CtorH4hs(1)
assert not CtorH4hs(1) == Ctor4True4Data4hs
assert CtorH4hs(1) != Ctor4True4Data4hs
assert CtorH4hs(True) == Ctor4True4Data4hs
assert CtorH4hs(True) is not Ctor4True4Data4hs
assert Ctor4False4Data4hs != Ctor4True4Data4hs


True4Data4hs = Data4hs(Ctor4True4Data4hs)
False4Data4hs = Data4hs(Ctor4False4Data4hs)
Nothing4Data4hs = Data4hs(Ctor4Nothing4Data4hs)
def mk_Just4Data4hs(x, /):
    raise 'lazy'
    return Data4hs(Ctor4Just4Data4hs, x)

#Integer4Data4hs
def mk_Ctor4Integer4Data4hs(i, /):
    check_type_is(int, i)
    return CtorH4hs((int, i))
def mk_Integer4Data4hs(i, /):
    ctor4hs = mk_Ctor4Integer4Data4hs(i)
    return Data4hs(ctor4hs)

#Tuple4Data4hs
def mk_Ctor4Tuple4Data4hs(N, /):
    check_uint(N)
    return CtorH4hs((tuple, N))
def mk_Tuple4Data4hs_(N, /, *s):
    #why not return Data4hs(N, s)
    #   see: App4Data4hs
    check_uint(N)
    if not len(s) == N: raise TypeError
    if 0:
        #bug:SHOULD_BE lazy mk using Apps4hs
        #   ==>> to substitute var #Data4hs is mix0!!!
        ctor4hs = mk_Ctor4Tuple4Data4hs(N)
        return Data4hs(ctor4hs, *s)
    return mk_apps(mk_f4hs__Tuple4Data4hs_(N), *s)
def _mk_Tuple4Data4hs(*s):
    N = len(s)
    return mk_Tuple4Data4hs_(N, *s)
def mk_f4hs__Tuple4Data4hs_(N, /):
    ctor4hs = mk_Ctor4Tuple4Data4hs(N)
        #check_uint(N)
    return ctor4hs_to_f4hs(N, ctor4hs)
def ctor4hs_to_f4hs(N, ctor4hs, /):
    check_uint(N)
    return Expr4py(N, Data4hs, ctor4hs)


ctor4Pair4hs = mk_Ctor4Tuple4Data4hs(2)


VarTypes4get = (VarH4hs, VarR4hs, VarN4hs, CtorH4hs, Var4hs) #no Infix4hs, UnusedPattern4hs
VarTypes4get = frozenset(VarTypes4get)
def check_var(var, /):
    if not is_var(var): raise TypeError
def is_var(var, /):
    return is_cls4var(type(var))
def is_cls4var(cls, /):
    return cls in VarTypes4get
check_var(VarH4hs('x'))
assert is_var(VarH4hs('x'))

#class Apply4hs(_ITuple):
class Expr8List4hs(_ITuple, BaseSyntactic4hs):
    r'''(*MixSyntactic4hs,)   #MixSyntactic4hs = (BaseSyntactic4hs|BaseSemantic4hs)

    f ... | f ... + g ... #vs case...of | let ... in | ... where ...
    #'''
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    #@override
    def ___deep_check_mixN___(sf, recur_check, /):
        '-> None #apply recur_check on inner MixSyntactic4hs'
        _eat_iter(map(recur_check, sf))
    #@override
    def ___fmap_on_child_mixN___(sf, recur_convert, /):
        'sf:mix -> (mix->mix) -> mix'
        return __class__(*map(recur_convert, sf))
    #@override
    def ___shallow_degrade_unless_mix2___(sf, /):
        'sf:mix<M> -> mix<N> # 2 <= N < M or 2 == N == M'
        return sf

    #@override
    ___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___ = null_frozenset
    ':: {cls} or ()->{cls} #for MixSyntactic4hs #see:___shallow_degrade_unless_mix2___'


    #@override
    def ___pre_check___(cls4py, /, *expr_flow):
        return


def mk_Lambda4hs(xvars8params, body):
    'replace UnusedPattern4hs by fresh Var4hs #see:default_unused_pattern'
    params = mk_tuple(Var4hs() if type(xvar) is UnusedPattern4hs else xvar for xvar in xvars8params)
    return Lambda4hs(params, body)
class Lambda4hs(_ITuple, BaseSyntactic4hs):
    '(params/[Var], body/MixSyntactic4hs)'
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    #@override
    def ___deep_check_mixN___(sf, recur_check, /):
        '-> None #apply recur_check on inner MixSyntactic4hs'
        _, body = sf
        recur_check(body)
    #@override
    def ___fmap_on_child_mixN___(sf, recur_convert, /):
        'sf:mix -> (mix->mix) -> mix'
        params, body = sf
        return __class__(params, recur_convert(body))
    #@override
    def ___shallow_degrade_unless_mix2___(sf, /):
        'sf:mix<M> -> mix<N> # 2 <= N < M or 2 == N == M'
        return sf

    #@override
    ___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___ = null_frozenset
    ':: {cls} or ()->{cls} #for MixSyntactic4hs #see:___shallow_degrade_unless_mix2___'


    #@override
    def ___pre_check___(cls4py, params, body, /):
        check_type_is(tuple, params)
        #params = mk_tuple(v if type(v) is not UnusedPattern4hs else Var4hs() for v in params)
        for var in params:
            check_var(var)
        if not len({*params}) == len(params): raise ValueError('params duplicated')

class ILet4hs(_ITuple, BaseSyntactic4hs):
    '(pairs4def:[(var:Var, rhs:MixSyntactic4hs)], body:MixSyntactic4hs)'
    __slots__ = ()
    ___is_cls4obj4hs___ = False

    @abstractmethod
    class ___vars4Let4hs_duplicated_ok___:pass
    #@override
    def ___deep_check_mixN___(sf, recur_check, /):
        '-> None #apply recur_check on inner MixSyntactic4hs'
        pairs4def, body = sf
        for var, rhs in pairs4def:
            recur_check(rhs)
        recur_check(body)

    #@override
    def ___fmap_on_child_mixN___(sf, recur_convert, /):
        'sf:mix -> (mix->mix) -> mix'
        pairs4def, body = sf
        pairs4def = mk_tuple((var, recur_convert(rhs)) for var, rhs in pairs4def)
        body = recur_convert(body)
        return type(sf)(pairs4def, body)
        #return __class__(pairs4def, body)

    #@override
    def ___pre_check___(cls4py, pairs4def, body, /):
    #def ___pre_check___(cls4py, as_if_prime, pairs4def, body, /):
        #check_type_is(bool, as_if_prime)#_AsIfPrimeRecurLet4hs
        check_pairs(pairs4def)
        for var, rhs in pairs4def:
            #assert is_var(var),   var
            check_var(var)
        if not cls4py.___vars4Let4hs_duplicated_ok___:
            if not len(dict(pairs4def)) == len(pairs4def): raise TypeError('duplicated: vars@let-hs')


class RecurLet4hs(ILet4hs):
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    ___vars4Let4hs_duplicated_ok___ = False
    #@override
    def ___shallow_degrade_unless_mix2___(sf, /):
        'sf:mix<M> -> mix<N> # 2 <= N < M or 2 == N == M'
        pairs4def, body = sf
        return _AsIfPrimeRecurLet4hs(pairs4def, body)

    #@override
    ___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___ = '''
        _AsIfPrimeRecurLet4hs
        '''
    ':: {cls} or ()->{cls} #for MixSyntactic4hs #see:___shallow_degrade_unless_mix2___'
Let4hs = RecurLet4hs

class _AsIfPrimeRecurLet4hs(RecurLet4hs):
    r'''(pairs4def:[(var:Var, rhs:MixSyntactic4hs)], body:MixSyntactic4hs)
    #
    #intend: to split RecurLet4hs into min-prime-recur-groups and seq-groups, _AsIfPrimeRecurLet4hs is the output
    #
    # when compile__mix2, do not check really prime, so-called as-if-prime
    #
    # may replace whole Module/globals:
    #   import Xxx (xxx, yyy)
    #   x = ...
    #   y = ...
    #   ==>>
    #   \Xxx -> rec-let
    #           xxx = Xxx.xxx
    #           yyy = Xxx.yyy
    #           x = ...
    #           y = ...
    #       in  (x, y)
    #
    #'''
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    ___vars4Let4hs_duplicated_ok___ = False

    #@override
    def ___shallow_degrade_unless_mix2___(sf, /):
        'sf:mix<M> -> mix<N> # 2 <= N < M or 2 == N == M'
        return sf

    #@override
    ___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___ = null_frozenset
    ':: {cls} or ()->{cls} #for MixSyntactic4hs #see:___shallow_degrade_unless_mix2___'

class BlockSugarLet4hs(ILet4hs):
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    ___vars4Let4hs_duplicated_ok___ = False
    #@override
    def ___shallow_degrade_unless_mix2___(sf, /):
        'sf:mix<M> -> mix<N> # 2 <= N < M or 2 == N == M'
        pairs4def, body = sf
        params = mk_tuple(map(fst, pairs4def))
        f4hs = Lambda4hs(params, body)
        return mk_apps(f4hs, *map(snd, pairs4def))

    #@override
    ___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___ = '''
        Lambda4hs
        '''
    ':: {cls} or ()->{cls} #for MixSyntactic4hs #see:___shallow_degrade_unless_mix2___'



class StepSugarLet4hs(ILet4hs):
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    ___vars4Let4hs_duplicated_ok___ = True
    #@override
    def ___shallow_degrade_unless_mix2___(sf, /):
        'sf:mix<M> -> mix<N> # 2 <= N < M or 2 == N == M'
        pairs4def, body = sf
        for var, rhs in reversed(pairs4def):
            f4hs = Lambda4hs((var,), body)
            body = mk_apps(f4hs, rhs)
        return body

    #@override
    ___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___ = '''
        Lambda4hs
        '''
    ':: {cls} or ()->{cls} #for MixSyntactic4hs #see:___shallow_degrade_unless_mix2___'

class IOutputUnboxedLet4hs(_ITuple, BaseSyntactic4hs):
    '(pairs4def:[(xpattern_lhs:XPattern4hs, rhs:MixSyntactic4hs)], body:MixSyntactic4hs)'
    __slots__ = ()
    ___is_cls4obj4hs___ = False

    @abstractmethod
    class ___vars4Let4hs_duplicated_ok___:pass
    #@override
    def ___deep_check_mixN___(sf, recur_check, /):
        '-> None #apply recur_check on inner MixSyntactic4hs'
        pairs4def, body = sf
        for xpattern_lhs, rhs in pairs4def:
            recur_check(rhs)
        recur_check(body)

    #@override
    def ___fmap_on_child_mixN___(sf, recur_convert, /):
        'sf:mix -> (mix->mix) -> mix'
        pairs4def, body = sf
        pairs4def = mk_tuple((xpattern_lhs, recur_convert(rhs)) for xpattern_lhs, rhs in pairs4def)
        body = recur_convert(body)
        return type(sf)(pairs4def, body)
        #return __class__(pairs4def, body)

    #@override
    def ___pre_check___(cls4py, pairs4def, body, /):
        check_pairs(pairs4def)
        for xpattern_lhs, rhs in pairs4def:
            check_xpattern(xpattern_lhs)
        if cls4py.___vars4Let4hs_duplicated_ok___:
            #per-xpattern_lhs has no duplicates
            for xpattern_lhs, rhs in pairs4def:
                deep_check_xpattern_has_no_duplicates_vars(xpattern_lhs) #@@IOutputUnboxedLet4hs
        else:
            vs = []
            for xpattern_lhs, rhs in pairs4def:
                it = iter_vars4xpattern(xpattern_lhs)
                vs.extend(it)
            if not len({*vs}) == len(vs): raise TypeError('duplicated: vars@let-hs') #@@IOutputUnboxedLet4hs


#OutputUnboxedBlockSugarLet4hs -> InputUnboxedLambda4hs
class OutputUnboxedBlockSugarLet4hs(IOutputUnboxedLet4hs):
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    ___vars4Let4hs_duplicated_ok___ = False
    #@override
    def ___shallow_degrade_unless_mix2___(sf, /):
        'sf:mix<M> -> mix<N> # 2 <= N < M or 2 == N == M'
        pairs4def, body = sf
        xpatterns8params = mk_tuple(map(fst, pairs4def))
        f4hs = InputUnboxedLambda4hs(xpatterns8params, body)
        return mk_apps(f4hs, *map(snd, pairs4def))

    #@override
    ___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___ = '''
        InputUnboxedLambda4hs
        '''
    ':: {cls} or ()->{cls} #for MixSyntactic4hs #see:___shallow_degrade_unless_mix2___'


#OutputUnboxedStepSugarLet4hs -> InputUnboxedLambda4hs
class OutputUnboxedStepSugarLet4hs(IOutputUnboxedLet4hs):
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    ___vars4Let4hs_duplicated_ok___ = True
    #@override
    def ___shallow_degrade_unless_mix2___(sf, /):
        'sf:mix<M> -> mix<N> # 2 <= N < M or 2 == N == M'
        pairs4def, body = sf
        for xpattern_lhs, rhs in reversed(pairs4def):
            f4hs = InputUnboxedLambda4hs((xpattern_lhs,), body)
            body = mk_apps(f4hs, rhs)
        return body

    #@override
    ___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___ = '''
        InputUnboxedLambda4hs
        '''
    ':: {cls} or ()->{cls} #for MixSyntactic4hs #see:___shallow_degrade_unless_mix2___'


PathIndex4Data4hs
#OutputUnboxedRecurLet4hs -> RecurLet4hs
class OutputUnboxedRecurLet4hs(IOutputUnboxedLet4hs):
    'see: RecurLet4hs,PathIndex4Data4hs #vs App4Data4hs'
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    ___vars4Let4hs_duplicated_ok___ = False

    #@override
    def ___shallow_degrade_unless_mix2___(sf, /):
        'sf:mix<M> -> mix<N> # 2 <= N < M or 2 == N == M'
        def _it(pairs4def, /):
            '-> Iter (var, rhs)'
            for xpattern_lhs, rhs in pairs4def:
                if is_var(xpattern_lhs):
                    var = xpattern_lhs
                    yield var, rhs
                    continue
                cls = type(xpattern_lhs)
                if cls is UnusedPattern4hs:
                    _ = xpattern_lhs
                        #discard
                    continue
                assert cls in (Pattern4hs, Alias4Pattern4hs)
                yield from _it4xp_but_xv(xpattern_lhs, rhs)

        def _it4xp_but_xv(xpattern_lhs, rhs, /):
            '-> Iter (var, rhs)'
            check_xpattern(xpattern_lhs)
            assert not is_xvar(xpattern_lhs)
            may_used_vars = None
            params, extract4hs = xpattern__to__params_ExtendedApp4Data4hs_pair(xpattern_lhs, may_used_vars)
                #extract4hs::ExtendedApp4Data4hs<xpattern_lhs>
            N = len(params)
            ctor4hs = mk_Ctor4Tuple4Data4hs(N)
            hs_mk_tupleN = mk_f4hs__Tuple4Data4hs_(N)
            #default2on_match = mk_Lambda4hs([default_unused_pattern], hs_mk_tupleN)
            default2on_match = mk_apps(K, hs_mk_tupleN)
                #has no guard, hence no mismatch
            on_error = Error4hs(xpattern_lhs)
            hs_tpl = mk_apps(extract4hs, on_error, default2on_match, rhs)
                # rhs->tpl4hs
            fresh_var4hidden_state = Var4hs()
            yield fresh_var4hidden_state, hs_tpl
            for i, var in enumerate(params):
                get4hs = PathIndex4Data4hs((ctor4hs, N, i))
                yield var, mk_apps(get4hs, fresh_var4hidden_state)
        #end-def _it4xp_but_xv(xpattern_lhs, rhs, /):
        #end-def _it(pairs4def, /):
        def main():
            pairs4def, body = sf
            var_rhs_pairs = mk_tuple(_it(pairs4def))
            return RecurLet4hs(var_rhs_pairs, body)
        return main()

    #@override
    ___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___ = '''
        RecurLet4hs
        '''
    ':: {cls} or ()->{cls} #for MixSyntactic4hs #see:___shallow_degrade_unless_mix2___'


#MultiInputUnboxedRecurLet4hs -> OutputUnboxedRecurLet4hs
class MultiInputUnboxedRecurLet4hs(_ITuple, BaseSyntactic4hs):
    '(pairs4data_def:[(xpattern_lhs:XPattern4hs, rhs:MixSyntactic4hs)], triples4func_def:[(Var, N_ary/uint, [(xpatterns8params:[XPattern4hs], guarded_body)])], body:MixSyntactic4hs)'
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    #___vars4Let4hs_duplicated_ok___ = False

    #@override
    def ___deep_check_mixN___(sf, recur_check, /):
        '-> None #apply recur_check on inner MixSyntactic4hs'
        pairs4data_def, triples4func_def, body = sf

        for xpattern_lhs, rhs in pairs4data_def:
            recur_check(rhs)

        f4g = f4body = recur_check
        f4ps = _eat_iter
        for var, N, xpatterns__guarded_body__pairs in triples4func_def:
            for xpatterns8params, guarded_body in xpatterns__guarded_body__pairs:
                fold__guarded_body(f4g, f4body, f4ps, guarded_body, is_pairs=is_tuple)

        recur_check(body)

    #@override
    def ___fmap_on_child_mixN___(sf, recur_convert, /):
        'sf:mix -> (mix->mix) -> mix'
        pairs4data_def, triples4func_def, body = sf
        def _it(triples4func_def, /):
            f4g = f4body = recur_convert
            f4ps = mk_tuple
            def _it():
                for xpatterns8params, guarded_body in xpatterns__guarded_body__pairs:
                    guarded_body = fold__guarded_body(f4g, f4body, f4ps, guarded_body, is_pairs=is_tuple)
                    yield xpatterns8params, guarded_body
            for var, N, xpatterns__guarded_body__pairs in triples4func_def:
                yield var, N, mk_tuple(_it())
            return


        pairs4data_def = mk_tuple((xpattern_lhs, recur_convert(rhs)) for xpattern_lhs, rhs in pairs4data_def)
        triples4func_def = mk_tuple(_it(triples4func_def))
        body = recur_convert(body)
        return __class__(pairs4data_def, triples4func_def, body)

    #@override
    def ___shallow_degrade_unless_mix2___(sf, /):
        'sf:mix<M> -> mix<N> # 2 <= N < M or 2 == N == M'
        def _it1(N, xpatterns__guarded_body__pairs, /):
            '-> Iter (pattern, guarded_body)'
            ctor4hs = mk_Ctor4Tuple4Data4hs(N)
            for xpatterns8params, guarded_body in xpatterns__guarded_body__pairs:
                assert N == len(xpatterns8params)
                pattern = Pattern4hs(ctor4hs, xpatterns8params)
                yield pattern, guarded_body
        def _it2(triples4func_def, /):
            '-> Iter (var, f4hs/rhs)'
            for var, N, xpatterns__guarded_body__pairs in triples4func_def:
                body4case = mk_tuple(_it1(N, xpatterns__guarded_body__pairs))
                params = mk_tuple(Var4hs() for _ in range(N))
                input4case = mk_Tuple4Data4hs_(N, *params)
                    #using lazy-version to substitute params
                case4hs = Case4hs(input4case, body4case)
                f4hs = Lambda4hs(params, case4hs)
                yield var, f4hs#rhs
        #def _it2(triples4func_def, /):
        #def _it1(N, xpatterns__guarded_body__pairs, /):
        def main():
            pairs4data_def, triples4func_def, body = sf
            #below impl: triples4func_def -> pairs4data_def
            #   ==>> MultiInputUnboxedRecurLet4hs -> OutputUnboxedRecurLet4hs
            more__pairs4data_def = _it2(triples4func_def)
            pairs4data_def = mk_tuple([*pairs4data_def, *more__pairs4data_def])
            return OutputUnboxedRecurLet4hs(pairs4data_def, body)


        return main()

    #@override
    ___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___ = '''
        OutputUnboxedRecurLet4hs
        '''
    ':: {cls} or ()->{cls} #for MixSyntactic4hs #see:___shallow_degrade_unless_mix2___'

    #@override
    def ___pre_check___(cls4py, pairs4data_def, triples4func_def, body, /):
        check_pairs(pairs4data_def)
        for xpattern_lhs, rhs in pairs4data_def:
            check_xpattern(xpattern_lhs)

        check_triples(triples4func_def)
        for var, N, xpatterns__guarded_body__pairs in triples4func_def:
            check_var(var)
            check_uint(N) #N-ary of var
            check_pairs(xpatterns__guarded_body__pairs)
            for xpatterns8params, guarded_body in xpatterns__guarded_body__pairs:
                check_type_is(tuple, xpatterns8params)
                if not len(xpatterns8params) == N:raise TypeError
                for xpattern in xpatterns8params:
                    check_xpattern(xpattern)
                _check_guarded_body(guarded_body)

        if 1:
            vs = []
            for xpattern_lhs, rhs in pairs4data_def:
                it = iter_vars4xpattern(xpattern_lhs)
                vs.extend(it)
            if 1:
                it = map(fst, triples4func_def)
                vs.extend(it)
            if not len({*vs}) == len(vs): raise TypeError('duplicated: vars@let-hs') #@@MultiInputUnboxedRecurLet4hs

def mk_MultiInputUnboxedRecurLet4hs(lss4def, body, /):
    'Iter((xpattern, rhs)|(var, *xpatterns, guarded_body)) -> body -> MultiInputUnboxedRecurLet4hs'
    def _f1(lss4def, /):
        pairs4data_def = []
        _triples4func_def = []
        for ls in lss4def:
            check_type_is(tuple, ls)
            L = len(ls)
            if L < 2: raise TypeError
            rhs_or_gbody = ls[-1]
            if L == 2 and type(rhs_or_gbody) is not tuple:
                #f = f4data_def
                xpattern_lhs, rhs = ls
                pairs4data_def.append((xpattern_lhs, rhs))
            else:
                #f = f4func_def
                [var, *xpatterns] = ls[:-1]
                check_var(var)
                guarded_body = ls[-1]
                xpatterns = mk_tuple(xpatterns)
                _triples4func_def.append((var, xpatterns, guarded_body))
        pairs4data_def = mk_tuple(pairs4data_def)
        _triples4func_def = mk_tuple(_triples4func_def)
        return pairs4data_def, _triples4func_def
    #def _f1(lss4def, /): -> (pairs4data_def, _triples4func_def)
    def _f2(_triples4func_def, /):
        def _post_act(prev_var, /):
            if prev_var is NULL:
                #not exists: N, ...
                pass
            else:
                triples4func_def.append((prev_var, N, xpatterns__guarded_body__pairs))
        prev_var = NULL = []#None
        triples4func_def = []
        for (var, xpatterns, guarded_body) in _triples4func_def:
            if var is not prev_var:
                _post_act(prev_var)
                ##before update prev_var
                prev_var = var
                N = len(xpatterns)
                xpatterns__guarded_body__pairs = []
            else:
                assert N == len(xpatterns)
            xpatterns__guarded_body__pairs.append((xpatterns, guarded_body))
        else:
            _post_act(prev_var)
        #end-for-loop
        triples4func_def = mk_tuple(triples4func_def)
        return triples4func_def
    #def _f2(_triples4func_def, /): -> triples4func_def
    def main():
        lss4def, body
        (pairs4data_def, _triples4func_def) = _f1(lss4def)
        triples4func_def = _f2(_triples4func_def)
        return MultiInputUnboxedRecurLet4hs(pairs4data_def, triples4func_def, body)
    return main()




class InputUnboxedLambda4hs(_ITuple, BaseSyntactic4hs):
    '(xpatterns8params/[XPattern4hs], body/MixSyntactic4hs) #see:Case4hs,Lambda4hs'
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    #@override
    def ___deep_check_mixN___(sf, recur_check, /):
        '-> None #apply recur_check on inner MixSyntactic4hs'
        _, body = sf
        recur_check(body)
    #@override
    def ___fmap_on_child_mixN___(sf, recur_convert, /):
        'sf:mix -> (mix->mix) -> mix'
        xpatterns8params, body = sf
        return __class__(xpatterns8params, recur_convert(body))
    #@override
    def ___shallow_degrade_unless_mix2___(sf, /):
        'sf:mix<M> -> mix<N> # 2 <= N < M or 2 == N == M'
        xpatterns8params, body = sf
        N = len(xpatterns8params)
        ctor4hs = mk_Ctor4Tuple4Data4hs(N)
        pattern = Pattern4hs(ctor4hs, xpatterns8params)
        params = mk_tuple(Var4hs() for _ in range(N))
        input4case = mk_Tuple4Data4hs_(N, *params)
            #using lazy-version to substitute params
        case4hs = Case4hs(input4case, ((pattern, body),))
        f4hs = Lambda4hs(params, case4hs)
        return f4hs

    #@override
    ___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___ = '''
        Case4hs
        '''
    ':: {cls} or ()->{cls} #for MixSyntactic4hs #see:___shallow_degrade_unless_mix2___'


    #@override
    def ___pre_check___(cls4py, xpatterns8params, body, /):
        check_type_is(tuple, xpatterns8params)
        N = len(xpatterns8params)
        ctor4hs = mk_Ctor4Tuple4Data4hs(N)
        pattern = Pattern4hs(ctor4hs, xpatterns8params)
            #check Pattern4hs
        deep_check_xpattern_has_no_duplicates_vars(pattern) #@@InputUnboxedLambda4hs








def is_tuple(t, /):
    return type(t) is tuple
def is_pair(t, /):
    return type(t) is tuple and len(t) == 2
def is_pairs(ps, /):
    return is_tuple(ps) and all(map(is_pair, ps))

def fold__guarded_body(f4guard, f4body, f4pairs, guarded_body, /, is_pairs):
    'guarded_body = body | [(guard, guarded_body)]'
    if is_pairs is None:
        is_pairs = is_tuple
    def recur(guarded_body, /):
        if is_pairs(guarded_body):
            pairs = guarded_body
            return f4pairs(map(f4p, pairs))
        else:
            body = guarded_body
            return f4body(body)


    def f4p(pair, /):
        g, gd_b = pair
        g = f4guard(g)
        gd_b = recur(gd_b)
        return g, gd_b
    return recur(guarded_body)
def check_pairs(ps, /):
    if not is_pairs(ps): raise TypeError
def _is_pairs__if_is_tuple(ps, /):
    'is_tuple ==>> is_pairs'
    r = is_tuple(ps)
    if r: check_pairs(ps)
    return r
def _check_guarded_body(x, /):
    'is_tuple ==>> is_pairs'
    f4g = f4body = echo #MixSyntactic4hs
    f4ps = _eat_iter
    fold__guarded_body(f4g, f4body, f4ps, x, is_pairs=_is_pairs__if_is_tuple)


def _guarded_body__to__fresh_var4default_body_pair(guarded_body, /):
    '-> (fresh_var4default, body)'
    fresh_var4default = Var4hs() #fresh
    params = (fresh_var4default,)
    f4g = echo
    def f4body(body, /):
        # -> default2result
        # => (default -> r)
        result = body
        default2result = Lambda4hs(params, result)
        return default2result
        #bug:return mk_apps(K, body)
        #   must be in-form: Lambda4hs [fresh_var4default] body
    def f4ps(ps, /):
        # -> default2result
        # => (default -> r)
        [*ps] = ps
        [result] = params
        for guard, default2result in reversed(ps):
            default = result
            default2result = if_then_else___Syntactic4hs(guard, default2result, I)
            result = mk_apps(default2result, default)
        default2result = Lambda4hs(params, result)
        return default2result

    default2result = fold__guarded_body(f4g, f4body, f4ps, guarded_body, is_pairs=is_tuple)
    check_type_is(Lambda4hs, default2result)
    _params, body = default2result
    assert _params is params
    return fresh_var4default, body
class Case4hs(_ITuple, BaseSyntactic4hs):
    r'''(input4case, [(XPattern4hs, guarded_body)])
    # guarded_body = body | [(guard, guarded_body)]
    # input4case, guard, body :: MixSyntactic4hs

    #NOTE: if any toplevel XPattern4hs be XVar: terminate the test list

    #'''
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    #@override
    def ___deep_check_mixN___(sf, recur_check, /):
        '-> None #apply recur_check on inner MixSyntactic4hs'
        input4case, xpattern_guarded_body_pairs = sf
        recur_check(input4case)
        f4g = f4body = recur_check
        f4ps = _eat_iter
        for xpattern, guarded_body in xpattern_guarded_body_pairs:
            fold__guarded_body(f4g, f4body, f4ps, guarded_body, is_pairs=is_tuple)

    #@override
    def ___fmap_on_child_mixN___(sf, recur_convert, /):
        'sf:mix -> (mix->mix) -> mix'
        input4case, xpattern_guarded_body_pairs = sf
        def _it():
            f4g = f4body = recur_convert
            f4ps = mk_tuple
            for xpattern, guarded_body in xpattern_guarded_body_pairs:
                guarded_body = fold__guarded_body(f4g, f4body, f4ps, guarded_body, is_pairs=is_tuple)
                yield xpattern, guarded_body
            return
        input4case = recur_convert(input4case)
        xpattern_guarded_body_pairs = mk_tuple(_it())
        return __class__(input4case, xpattern_guarded_body_pairs)


    #@override
    def ___shallow_degrade_unless_mix2___(sf, /):
        'sf:mix<M> -> mix<N> # 2 <= N < M or 2 == N == M'
        input4case, xpattern_guarded_body_pairs = sf
        #result__mix2 = result__mix3 #bug: introduce BareCase4hs via if_then_else___Syntactic4hs in shallow layer

        #NOTE: if any toplevel XPattern4hs be XVar: terminate the test list
        (imay, may_tail) = seq_find_if(xpattern_guarded_body_pairs, lambda x: is_xvar(fst(x)))
        if imay == -1:
            assert may_tail is None
        else:
            idx = imay
            assert 0 <= idx < len(xpattern_guarded_body_pairs)
            assert may_tail is xpattern_guarded_body_pairs[idx]
            xpattern_guarded_body_pairs = xpattern_guarded_body_pairs[:idx]
            del idx
        assert not any(map(is_xvar, map(fst, xpattern_guarded_body_pairs)))
        may_tail; del imay

        err_msg = 'Case4hs mismatch'
        may_xparam_body_pair = may_tail
        on_error = _may_xparam_body_pair2on_error(may_xparam_body_pair, err_msg)

        #NOTE: if_then_else___Syntactic4hs -->> mix3 using BareCase4hs
        i2o = on_error
        for xpattern, guarded_body in reversed(xpattern_guarded_body_pairs):
            on_error = i2o
            fresh_var4default, body = _guarded_body__to__fresh_var4default_body_pair(guarded_body)
                #Lambda4hs [var4default] body

            #may_used_vars = free_vars_of(body)
            #   O(n^2)
            may_used_vars = None
            params, extract4hs = xpattern__to__params_ExtendedApp4Data4hs_pair(xpattern, may_used_vars)
            default2on_match = Lambda4hs((fresh_var4default,), Lambda4hs(params, body))

            #next round
            i2o = mk_apps(extract4hs, on_error, default2on_match)

        mix__shallow_removed_Case4hs = mk_apps(i2o, input4case)
        return (mix__shallow_removed_Case4hs)
        #return recur_convert(mix__shallow_removed_Case4hs)

        #xpattern__to__extract_data2Maybe___Syntactic4hs
        xpattern__to__params_ExtendedApp4Data4hs_pair
        ExtendedApp4Data4hs

    #@override
    ___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___ = '''
        BareCase4hs
        '''
    ':: {cls} or ()->{cls} #for MixSyntactic4hs #see:___shallow_degrade_unless_mix2___'



    #@override
    def ___pre_check___(cls4py, input4case, xpattern_guarded_body_pairs, /):
        #?check MixSyntactic4hs? see:___deep_check_mixN___
        check_pairs(xpattern_guarded_body_pairs)
        for xpattern, guarded_body in xpattern_guarded_body_pairs:
            check_xpattern(xpattern)
            _check_guarded_body(guarded_body)


    r'''
    if 0:
        #@override
        def ___deep_check_mixN___(sf, recur_check, /):
            '-> None #apply recur_check on inner MixSyntactic4hs'
            input4case, xpattern_guard_body_triples = sf
            recur_check(input4case)
            for xpattern, guard, body in xpattern_guard_body_triples:
                recur_check(guard)
                recur_check(body)

        #@override
        def ___pre_check___(cls4py, input4case, xpattern_guard_body_triples, /):
            check_type_is(tuple, xpattern_guard_body_triples)
            for p in xpattern_guard_body_triples:
                check_type_is(tuple, p)
                if not len(p)==3: raise TypeError
            for xpattern, guard, body in xpattern_guard_body_triples:
                check_xpattern(xpattern)
    #'''
def _may_xparam_body_pair2on_error(may_xparam_body_pair, err_msg, /):
    'may_tail-for-Case/(may (XVar, MixSyntactic4hs)) -> err_msg -> on_error/MixSyntactic4hs # on_error :: x -> r in Syntactic4hs domain'
    if may_xparam_body_pair is not None:
        xvar, body = may_xparam_body_pair
        if is_var(xvar):
            var = xvar
            f = Lambda4hs((var,), body)
            #will be mk_apps(f, input4case)
            on_error = f
        else:
            check_type_is(UnusedPattern4hs, xvar)
            on_error = mk_apps(K, body)
    else:
        body4on_error = Error4hs(err_msg)
        on_error = mk_apps(K, body4on_error)
    return on_error

class BareCase4hs(_ITuple, BaseSyntactic4hs):
    r'''(input4case, [(CtorH4hs, [XVar], body)], (may (XVar body)))
    # input4case, body :: MixSyntactic4hs
    # to impl if_then_else4hs Maybe4hs
    #
    # see: JmpApp4Data4hs/App4Data4hs used in ___deep_convert_to_mixN___
    #   JmpApp4Data4hs: impl ctor2on_match is complicate...
    #       should define Syntactic4hs-Ctor2Expr in seq-style
    #       should compile Syntactic4hs-Ctor2Expr to Semantic4hs-Ctor2Expr
    #       should convert Semantic4hs-Ctor2Expr to mapping-style (may require closure)
    #


    #'''
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    #@override
    def ___deep_check_mixN___(sf, recur_check, /):
        '-> None #apply recur_check on inner MixSyntactic4hs'
        input4case, ctor_xparams_body_triples, may_xparam_body_pair = sf
        recur_check(input4case)
        for ctor4hs, xparams, body in ctor_xparams_body_triples:
            recur_check(body)
        if may_xparam_body_pair is not None:
            xvar, body = may_xparam_body_pair
            recur_check(body)

    #@override
    def ___fmap_on_child_mixN___(sf, recur_convert, /):
        'sf:mix -> (mix->mix) -> mix'
        input4case, ctor_xparams_body_triples, may_xparam_body_pair = sf

        input4case = recur_convert(input4case)

        it = ((ctor4hs, xparams, recur_convert(body)) for ctor4hs, xparams, body in ctor_xparams_body_triples)
        ctor_xparams_body_triples = (*it,)

        if may_xparam_body_pair is not None:
            xvar, body = may_xparam_body_pair
            body = recur_convert(body)
            may_xparam_body_pair = xvar, body
        return __class__(input4case, ctor_xparams_body_triples, may_xparam_body_pair)


    #@override
    def ___shallow_degrade_unless_mix2___(sf, /):
        'sf:mix<M> -> mix<N> # 2 <= N < M or 2 == N == M'
        input4case, ctor_xparams_body_triples, may_xparam_body_pair = sf

        err_msg = 'BareCase4hs mismatch'
        on_error = _may_xparam_body_pair2on_error(may_xparam_body_pair, err_msg)

        i2o = on_error
        for ctor4hs, xparams, body in reversed(ctor_xparams_body_triples):
            on_error = i2o
            us4unbox = [u for u, xvar in enumerate(xparams) if is_var(xvar)]
            N = len(xparams)
            f = App4Data4hs(ctor4hs, N, *us4unbox)
            params = mk_tuple(filter(is_var, xparams))
            on_match = Lambda4hs(params, body)
            i2o = mk_apps(f, on_error, on_match)
        #return recur_convert(mk_apps(on_error, input4case))
        result__mix2 = mk_apps(i2o, input4case)
        return result__mix2

    #@override
    ___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___ = '''
        Lambda4hs
        '''
    ':: {cls} or ()->{cls} #for MixSyntactic4hs #see:___shallow_degrade_unless_mix2___'


    #@override
    def ___pre_check___(cls4py, input4case, ctor_xparams_body_triples, may_xparam_body_pair, /):
        #?check MixSyntactic4hs? see:___deep_check_mixN___
        check_triples(ctor_xparams_body_triples)
        for ctor4hs, xparams, body in ctor_xparams_body_triples:
            check_type_is(CtorH4hs, ctor4hs)
            check_type_is(tuple, xparams)
            for xvar in xparams:
                check_xvar(xvar)
            deep_check_xpattern_has_no_duplicates_vars(Pattern4hs(ctor4hs, xparams))
                #shallow since flatten/only-one-layer
        if may_xparam_body_pair is not None:
            xparam_body_pair = may_xparam_body_pair
            check_pair(xparam_body_pair)
            xvar, body = xparam_body_pair
            check_xvar(xvar)


def is_triple(t, /):
    return is_tuple(t) and len(t) == 3
def is_triples(ts, /):
    return is_tuple(ts) and all(map(is_triple, ts))
def check_triple(t, /):
    if not is_triple(t): raise TypeError
def check_triples(ts, /):
    if not is_triples(ts): raise TypeError

def if_then_else___Syntactic4hs(if_, then_, else_, /):
    'MixSyntactic4hs -> MixSyntactic4hs -> MixSyntactic4hs -> MixSyntactic4hs-BareCase4hs'
    return BareCase4hs(if_, (
        (Ctor4True4Data4hs, (), then_)
        ,(Ctor4False4Data4hs, (), else_)
        ), None)
    pass


def fold_Maybe___Syntactic4hs(may4hs, on_Nothing, on_Just, /):
    'MixSyntactic4hs -> MixSyntactic4hs -> MixSyntactic4hs -> MixSyntactic4hs-BareCase4hs'
    a = Var4hs() #fresh
    return BareCase4hs(may4hs, (
        (Ctor4Nothing4Data4hs, (), on_Nothing)
        ,(Ctor4Just4Data4hs, (a,), mk_apps(on_Just, a))
        ), None)
    pass




def xpattern__to__params_ExtendedApp4Data4hs_pair(xpattern, may_used_vars, /):
    '(Pattern4hs|Alias4Pattern4hs) -> may Set<Var>/used_vars/frees4body -> (params, ExtendedApp4Data4hs)'
    def main0():
        '-> (params, used_vars)'
        if not type(xpattern) in (Pattern4hs, Alias4Pattern4hs): raise TypeError
        check_xpattern(xpattern)
        deep_check_xpattern_has_no_duplicates_vars(xpattern)

        params = iter_vars4xpattern(xpattern)
        if may_used_vars is not None:
            #too slow: used_vars = {*may_used_vars}
            used_vars = may_used_vars
            params = (v for v in params if v in used_vars)
        params = mk_tuple(params)
        used_vars = {*params}
        return (params, used_vars)
    (params, used_vars) = main0()
    #del xpattern, may_used_vars

    def on_inner(idx, x, /):
        '-> may (idx, may ExtendedApp4Data4hs)'
        if is_xvar(x):
            #bug:return None if x in used_vars else (idx, None)
            return None if x not in used_vars else (idx, None)
        ext = on_non_basic(x)
        return (idx, ext)
    def on_non_basic(x, /):
        '-> ExtendedApp4Data4hs'
        #x - xpattern_but_not_xvar
        cls = type(x)
        assert cls in (Pattern4hs, Alias4Pattern4hs)
        if cls is Alias4Pattern4hs:
            var, x = x
            cls = type(x)
            aliased = var in used_vars
        else:
            aliased = False
            pass
        if not cls is Pattern4hs: raise TypeError
        ctor4hs, xpatterns = x
        N = len(xpatterns)
        ms = (on_inner(i, x) for i, x in enumerate(xpatterns))
        ps = filter(None, ms)
        return ExtendedApp4Data4hs(aliased, ctor4hs, N, (*ps,))
    def main1():
        ext = on_non_basic(xpattern)
        return (params, ext)
    return main1()



r'''[[[[[
def xpattern__to__extract_data2Maybe___Syntactic4hs(xpattern, used_vars, /):
    'xpattern -> used_vars/frees4body -> (params, mix2) #mix2 :: whnf-Data4hs -> Maybe<Tuple4Data4hs>'
    check_xpattern(xpattern)
    deep_check_xpattern_has_no_duplicates_vars(xpattern)
    params = iter_vars4xpattern(xpattern)
    params = (v for v in params if v in used_vars)
    params = (*params,)
    used_vars = {*params}
    def shallow_extract0(x, /):
        '-> (may_var, may_pattern)'
        cls = type(x)
        if cls is Pattern4hs:
            may_pattern = x
            may_var = None
        elif cls is Alias4Pattern4hs:
            v, pattern = x
            may_pattern = pattern
            may_var = v if v in used_vars else None
        else:
            check_xvar(x)
            v = x
            may_pattern = None
            may_var = v if v in used_vars else None
        return may_var, may_pattern
    def shallow_extract1(x, /):
        #x - xpattern_but_not_xvar
        cls = type(x)
        assert cls in (Pattern4hs, Alias4Pattern4hs)
        if cls is Alias4Pattern4hs:
            _, x = x
            cls = type(x)
        else:
            pass
        if not cls is Pattern4hs: raise TypeError
        ctor4hs, xpatterns = xpattern
        [*ps] = map(shallow_extract0, xpatterns)
        bs = [not mv is mp is None for mv, mp in ps]
        us = [u for u, b in enumerate(bs) if b]
        App4Data4hs(ctor4hs, N, *us)
        map(fst, ps)
        Pattern4hs(ctor4hs, )



    App4Data4hs...too complicate
    new type!
    TODO
#]]]]]'''

def is_xvar(xvar, /):
    return type(xvar) in XVarTypes
def check_xvar(xvar, /):
    'XVarTypes = (UnusedPattern4hs|Var)'
    if not is_xvar(xvar): raise TypeError

def check_xpattern(xpattern, /):
    'XPattern4hs = (Pattern4hs|Alias4Pattern4hs|UnusedPattern4hs|Var)'
    if not type(xpattern) in XPatternTypes: raise TypeError
    #if not type(xpattern) in XPatternTypes: check_var(xpattern)

class Alias4Pattern4hs(_ITuple, BaseSyntactic4hs, IHasNoInnerMixSyntactic4hs):
    '(Var, Pattern4hs) # var@(ctor4hs, ...)'
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    #@override
    def ___pre_check___(cls4py, var, pattern, /):
        check_var(var)
        check_type_is(Pattern4hs, pattern)


class Pattern4hs(_ITuple, BaseSyntactic4hs, IHasNoInnerMixSyntactic4hs):
    r'(CtorH4hs, [XPattern4hs]) #see: check_xpattern #see:App4Data4hs'
    __slots__ = ()
    ___is_cls4obj4hs___ = False
    #@override
    def ___pre_check___(cls4py, ctor4hs, xpatterns, /):
        check_type_is(CtorH4hs, ctor4hs)
        check_type_is(tuple, xpatterns)
        for xpattern in xpatterns:
            check_xpattern(xpattern)
            #deep_check_xpattern_has_no_duplicates_vars(xpattern)
            #   O(n^2)!!!
    #def ___iter_vars4xpattern___(sf, /):
def iter_vars4xpattern(xpattern, /):
    '-> Iter<Var> #to check vars no duplicates #exclude UnusedPattern4hs'
    check_xpattern(xpattern)
    def recur(xpattern, /):
        cls = type(xpattern)
        if cls is Pattern4hs:
            ctor4hs, xpatterns = xpattern
            for vs in map(recur, xpatterns):
                yield from vs
        elif cls is Alias4Pattern4hs:
            var, pattern = xpattern
            #bug: yield var
            #bug: yield f4xv(var)
            yield from f4xv(var)
            yield from recur(pattern)
        else:
            #var = xpattern
            #bug: check_var(var)
            xvar = xpattern
            yield from f4xv(xvar)
        return
    def f4xv(xvar, /):
        if is_var(xvar):
            var = xvar
            check_var(var)
            yield var
            #bug: without "return"
            return
        #print(xvar)
        check_type_is(UnusedPattern4hs, xvar)
        return
    return recur(xpattern)
def deep_check_xpattern_has_no_duplicates_vars(xpattern, /):
    [*vs] = iter_vars4xpattern(xpattern)
    if not len({*vs}) == len(vs): raise TypeError
XVarTypes = (UnusedPattern4hs, *VarTypes4get)
XPatternTypes = (Pattern4hs, Alias4Pattern4hs, *XVarTypes)
XVarTypes = frozenset(XVarTypes)
XPatternTypes = frozenset(XPatternTypes)



def _fulfill___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___(verbose, /):
    '___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___ from callable/str to frozenset'
    import inspect
    k = '___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___'
    #only direct subclasses: for C in IIsCls4Obj4hs.__subclasses__():
    to_do = {IIsCls4Obj4hs}
    done = set()
    #print(help(inspect.isabstract))
    assert not inspect.isabstract(Lambda4hs)
    #bug: why fail??: assert inspect.isabstract(IIsCls4Obj4hs)
    while to_do:
        C = to_do.pop()
        if C in done: continue
        done.add(C)
        to_do.update(C.__subclasses__())
        if verbose: print(C)
        if inspect.isabstract(C): continue
            #not work
        if (C.__abstractmethods__): continue
        if k not in C.__dict__:
            if not issubclass(C, IHasNoInnerMixSyntactic4hs):
                raise Exception(C)
            continue
        x = getattr(C, k)
        if callable(x):
            x = x()
        ##
        if type(x) is str:
            x = mk_frozenset(globals()[nm] for nm in x.split())
        x = mk_frozenset(x)
        assert all(isinstance(cls, type) for cls in x)
        setattr(C, k, x)
        if verbose: print('    ', x)
#_fulfill___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___(True)
_fulfill___introduced_non_mix2_types_in_shallow_degrade_unless_mix2___(False)



assert is_cls4obj4hs(Apps4hs)
assert is_cls4obj4hs(_Placeholder4hs)
assert not is_cls4obj4hs(_Apps4hs)
assert is_cls4obj4hs(FreeLocalBatchRouter)
assert is_cls4obj4hs(LocalBatchRouter)
assert is_cls4obj4hs(ExtendedFreeLocalBatchRouter)
assert is_cls4obj4hs(_MidWayBound)

#assert is_cls4obj4hs(Undefined4hs)
assert is_obj4hs(the_undefined)
assert is_cls4obj4hs(Data4hs)
assert is_cls4obj4hs(Data4py)
assert is_cls4obj4hs(Expr4py)
assert is_cls4obj4hs(Stmt4py)
#assert is_cls4obj4hs(JmpApp4Data4hs)
assert is_cls4obj4hs(App4Data4hs)
assert is_cls4obj4hs(ExtendedApp4Data4hs)
assert is_cls4obj4hs(PathIndex4Data4hs)

assert not is_cls4obj4hs(Infix4hs)
assert not is_cls4obj4hs(VarH4hs)
assert not is_cls4obj4hs(VarR4hs)
assert not is_cls4obj4hs(VarN4hs)
assert not is_cls4obj4hs(Var4hs)
assert not is_cls4obj4hs(CtorH4hs)
assert not is_cls4obj4hs(Expr8List4hs)
assert not is_cls4obj4hs(Lambda4hs)
assert not is_cls4obj4hs(RecurLet4hs)
assert not is_cls4obj4hs(_AsIfPrimeRecurLet4hs)
assert not is_cls4obj4hs(BlockSugarLet4hs)
assert not is_cls4obj4hs(StepSugarLet4hs)
assert not is_cls4obj4hs(InputUnboxedLambda4hs)
assert not is_cls4obj4hs(OutputUnboxedBlockSugarLet4hs)
assert not is_cls4obj4hs(OutputUnboxedStepSugarLet4hs)
assert not is_cls4obj4hs(OutputUnboxedRecurLet4hs)
assert not is_cls4obj4hs(MultiInputUnboxedRecurLet4hs)
assert not is_cls4obj4hs(Case4hs)
assert not is_cls4obj4hs(BareCase4hs)
assert not is_cls4obj4hs(Alias4Pattern4hs)
assert not is_cls4obj4hs(Pattern4hs)
assert not is_cls4obj4hs(Alias4Pattern4hs)
assert not is_cls4obj4hs(UnusedPattern4hs)
assert not is_obj4hs(default_unused_pattern)

class IFromName(ABC):
    __slots__ = ()
    if 1:
        @abstractmethod
        class __mk__:pass
    else:
        @classmethod
        @abstractmethod
        def __mk__(cls, nm, /):
            pass
    def __getattribute__(sf, nm, /):
        return type(sf).__mk__(nm)

class MkVarH4hs(IFromName):
    __slots__ = ()
    #@override
    __mk__ = VarH4hs

mk_var = MkVarH4hs()
mk_var.xxx
assert mk_var.xxx == mk_var.xxx




class MkCtorH4hs(IFromName):
    __slots__ = ()
    #@override
    __mk__ = CtorH4hs

mk_ctor = MkCtorH4hs()
mk_ctor.Xxx
assert mk_ctor.Xxx == mk_ctor.Xxx


#TODO:wrapper4infix^var ==>> infix


S = CombinatorSKIBC.S
K = CombinatorSKIBC.K
#I = CombinatorSKIBC.I
I = I #Apps4hs(*[])
B = CombinatorSKIBC.B
C = CombinatorSKIBC.C
Yh = CombinatorSKIBC.Yh
Y = CombinatorSKIBC.Y



def _deep_check_mixN(mix, recur_check, /):
    call5cls.___deep_check_mixN___(mix, recur_check) #raise AttributeError if no ___deep_check_mixN___

def ___tmp_env():
    def deep_check_mix0(mix, /):
        check_obj4hs(mix)
            #shallow_check
        _deep_check_mixN(mix, deep_check_mix0)
            #recur_check
    return deep_check_mix0
deep_check_mix0 = ___tmp_env(); del ___tmp_env

_Types4both = (Apps4hs, Data4hs)
def _is_cls_both(cls, /):
    #both_Semantic4hs_Syntactic4hs
    return cls in _Types4both
    return cls is Apps4hs
def _is_obj_both(obj, /):
    #both_Semantic4hs_Syntactic4hs
    return _is_cls_both(type(obj))

def ___types2deep_check_mix_(Types, /):
    def recur_check(mix, /):
        cls = type(mix)
        if (not _is_cls_both(cls)) and is_cls4obj4hs(cls):
            deep_check_mix0(mix)
                #Semantic4hs except Apps4hs/Data4hs should not contain Syntactic4hs
        else:
            if not cls in Types: raise TypeError
                #shallow_check
            _deep_check_mixN(mix, recur_check)
                #recur_check
    return recur_check
# mix1
MixSyntactic4hs__Types4mix1 = frozenset([Expr8List4hs, Apps4hs, Data4hs, *_Types4both, *VarTypes4get])
# mix2
MixSyntactic4hs__Types4mix2 = frozenset([_AsIfPrimeRecurLet4hs, Lambda4hs, *MixSyntactic4hs__Types4mix1])
MixSyntactic4hs__Types4mix3 = frozenset([BareCase4hs, *MixSyntactic4hs__Types4mix2])
MixSyntactic4hs__Types4mix4 = frozenset([Case4hs, *MixSyntactic4hs__Types4mix3])
deep_check_mix1 = ___types2deep_check_mix_(MixSyntactic4hs__Types4mix1)
deep_check_mix2 = ___types2deep_check_mix_(MixSyntactic4hs__Types4mix2)
deep_check_mix3 = ___types2deep_check_mix_(MixSyntactic4hs__Types4mix3)
deep_check_mix4 = ___types2deep_check_mix_(MixSyntactic4hs__Types4mix4)
assert Data4hs in MixSyntactic4hs__Types4mix2
assert Apps4hs in MixSyntactic4hs__Types4mix2
assert _AsIfPrimeRecurLet4hs in MixSyntactic4hs__Types4mix2


_deep_check_mixNs = (
    deep_check_mix0
    ,deep_check_mix1
    ,deep_check_mix2
    ,deep_check_mix3
    ,deep_check_mix4
    )
r'''
def _deep_convert_to_mixN(mix, N, recur_convert, /):
    return call5cls.___deep_convert_to_mixN___(mix, N, recur_convert) #raise AttributeError if no ___deep_convert_to_mixN___
def deep_convert_to_mixN(mix, N, /):
    check_uint(N)
    if not 2 <= N: raise TypeError
    def recur_convert(mix, /):
        return _deep_convert_to_mixN(mix, N, recur_convert)
    if N <= len(_deep_check_mixNs):
        f = _deep_check_mixNs
    else:
        f = echo
    return f(recur_convert(mix))
#'''

def fmap_on_child_mixN(mix, recur_convert, /):
    return call5cls.___fmap_on_child_mixN___(mix, recur_convert) #raise AttributeError if no ___fmap_on_child_mixN___
def shallow_degrade_unless_mix2(mix, /):
    return call5cls.___shallow_degrade_unless_mix2___(mix) #raise AttributeError if no ___shallow_degrade_unless_mix2___

def ___types2deep_convert_to_mix_(Types, /):
    def recur_convert(mix, /):
        rhs = []
        while not (mix is rhs or type(mix) in Types):
            rhs = mix
            mix = shallow_degrade_unless_mix2(rhs)
        #now mix is shallow mixN

        return fmap_on_child_mixN(mix, recur_convert)
    return recur_convert
deep_convert_to_mix2 = ___types2deep_convert_to_mix_(MixSyntactic4hs__Types4mix2)
deep_convert_to_mix3 = ___types2deep_convert_to_mix_(MixSyntactic4hs__Types4mix3)
deep_convert_to_mix4 = ___types2deep_convert_to_mix_(MixSyntactic4hs__Types4mix4)
#deep_convert_to_mix5 = ___types2deep_convert_to_mix_(MixSyntactic4hs__Types4mix5)

_deep_convert_to_mixNs = (
    None#deep_convert_to_mix0
    ,None#deep_convert_to_mix1
    ,deep_convert_to_mix2
    ,deep_convert_to_mix3
    ,deep_convert_to_mix4
    )


fst, snd
#OrderedDict
def ___tmp_env():
    CASE_CONST = 0
    CASE_MIDWAY = 1
        # _MidWayBound <<== Lambda4hs
    CASE_CLOSURE_ = 2
        # closure_4hs@link_time <<== closure@runtime <<== _AsIfPrimeRecurLet4hs
        #CASE_RECUR = 2
    #[[def__compile__mix2]]
    def compile__mix2(mix2, scoped_vars, /):
        r'''compile__mix2 :: mix2 -> scoped_vars/Iter<Var> -> payload<CASE_MIDWAY>
        #
        #payload4CASE_MIDWAY = (midway/_MidWayBound, inner_cased_xxx, inner_FVs, global_FVs, scoped_FVs)
        #   see:[[def__bottomup]] bottomup()
        #   see:[[def__link__payload4CASE_MIDWAY]] link__payload4CASE_MIDWAY()
        #   see:[[def__mix2]] mix2
        #   see:is_var()
        #   see:deep_check_mix2()
        #   see:deep_convert_to_mix2()
        #       mix0 := (\pd->main_link__payload4CASE_MIDWAY pd {} {}) $ (\mix2->compile__mix2 mix2 []) $ deep_convert_to_mix2 mix

scoped_vars - assume outer env exists
    * a var that is in scoped_vars is scoped_FVs
        #runtime/dynamic/scoped
    * a var that is not in scoped_vars is global_FVs
        #statc
    * inner_FVs is for constants, eg|:
        #statc
        ######################
        * pre-compile-builtins
            ##################
            * constants:
                to replace cased_payload4CASE_CONST
                any mix0
                Data4py
                Data4hs
                    Integer4Data4hs
                    Tuple4Data4hs
                    True4Data4hs
                    False4Data4hs
                FreeLocalBatchRouter/LocalBatchRouter
                    SKIBC
            ##################
            * Expr4py
                builtin__mk_mk_closure
                builtin__apply_closure
            ##################
            * ExtendedApp4Data4hs # used to impl Case4hs
                Error4hs, App4Data4hs # used to impl BareCase4hs, if_then_else___Syntactic4hs
            ##################

        ######################
        * post-link-object:
            ##################
            * ExtendedFreeLocalBatchRouter
                to replace cased_payload4CASE_MIDWAY
            ##################
            * closure_4hs::Data4py
                to replace cased_payload4CASE_CLOSURE_
                #closure4hs requires scoped_FVs4closure/bound_dynamic_free_vars
                #runtime-closure4hs
                #
            ##################

        ######################

        #'''
        scoped_vars = {*scoped_vars}
        old_mix2 = mix2
        not_Lambda4hs = type(mix2) is not Lambda4hs
        if not_Lambda4hs:
            mix2 = Lambda4hs((), mix2)
        deep_check_mix2(mix2)

        payload4CASE_MIDWAY = _main4Lambda4hs(mix2, scoped_vars)
        return payload4CASE_MIDWAY
        return not_Lambda4hs, payload4CASE_MIDWAY

    def _main4Lambda4hs(mix2, scoped_vars, /):
        '-> payload<CASE_MIDWAY>'
        check_type_is(Lambda4hs, mix2)
        ofrees = set()
        ov2cxx = {} #OrderedDict()
        #is_mix0, varXs = bottomup(scoped_vars, mix2, ofrees, ov2cxx)
        is_mix0, varXs = _bottomup__Lambda4hs(scoped_vars, mix2, ofrees, ov2cxx)
        assert ofrees&ov2cxx.keys() == set()
        var4f, (case, payload) = ov2cxx.popitem()
        if ov2cxx: raise logic-err

        if case == CASE_MIDWAY:
            payload4CASE_MIDWAY = payload
            (midway, inner_cased_xxx, inner_FVs, global_FVs, scoped_FVs) = payload4CASE_MIDWAY
            check_type_is(_MidWayBound, midway)
            (nint2free_var, num_free_vars, num_args4call, iXss4body) = midway
            if not ofrees == {*scoped_FVs} <= scoped_vars: raise logic-err
            return payload4CASE_MIDWAY
        else:
            raise NotImplementedError(f'case={case} #CASE_CONST==1')

    #[[def___bottomup__Lambda4hs]]
    def _bottomup__Lambda4hs(scoped_vars, mix2, ofrees, ov2cxx, /):
        (params, varXs4body, body_frees, body_v2cxx) = _0_Lambda4hs(scoped_vars, mix2)
        (case, payload) = _1_Lambda4hs(scoped_vars, params, varXs4body, body_frees, body_v2cxx)
        if 0b0: assert not (ofrees & ov2cxx.keys()),    (ofrees & ov2cxx.keys())
        (is_mix0, varXs) = _2_Lambda4hs(ofrees, ov2cxx, case, payload)
        if 0b0: assert not (ofrees & ov2cxx.keys())
        return is_mix0, varXs

    def _0_Lambda4hs(scoped_vars, mix2, /):
        check_type_is(Lambda4hs, mix2)
        params, body = mix2

        body_frees = set()
        body_v2cxx = {} #OrderedDict()
        _adds = set(params) - scoped_vars
        _L = len(scoped_vars)
        scoped_vars.update(_adds)
        assert _L + len(_adds) == len(scoped_vars)
        body_is_mix0, varXs4body = bottomup(scoped_vars, body, body_frees, body_v2cxx)
        scoped_vars.difference_update(_adds)
            #scoped_vars -= _adds
        assert _L == len(scoped_vars)
        del _adds, _L
        return (params, varXs4body, body_frees, body_v2cxx)
    #end-def _0_Lambda4hs(scoped_vars, mix2, /):
    def _2_Lambda4hs(ofrees, ov2cxx, case, payload, /):
        if case == CASE_MIDWAY:
            (midway, inner_cased_xxx, inner_FVs, global_FVs, scoped_FVs) = payload
            var4f = Var4hs() #fresh var
            ov2cxx[var4f] = (case, payload)
            ofrees.update(scoped_FVs)
            varXs = (var4f, *scoped_FVs)
            is_mix0 = False
            return is_mix0, varXs
        else:
            raise NotImplementedError(f'case={case} #CASE_CONST==1')
        raise logic-err

        return
    #end-def _2_Lambda4hs(ofrees, ov2cxx, case, payload, /):

        r'''[[[[[
        if body_is_mix0:
            var4body = varXs4body
            assert not body_frees
            assert len(body_v2cxx) == 1
            (case, body) = body_v2cxx.pop(var4body)
            assert not body_v2cxx
            assert case == CASE_CONST

            if not params:
                constant = body
                return _bottomup__mix0(constant, ov2cxx)
            #all params are unused
            f = LocalBatchRouter(1+len(params), (0,))
            constant = mk_apps(f, body)
            return _bottomup__mix0(constant, ov2cxx)
        if not body_frees: raise logic-err

        if not (body_frees & param2idx.keys()):
            #all params are unused
            f = LocalBatchRouter(1+len(params), (0,))
            #mix2 === mk_apps(f, body)
            (_, var4f) = _bottomup__mix0(f, ov2cxx)
            ofrees.update(body_frees)
            ov2cxx.update(body_v2cxx)
            return False, (var4f, varXs4body)

        if 0:
            if (not body_v2cxx) and body_frees <= param2idx.keys():
                #no constants and no free_vars
                is_mix0 = True
                pass
        #]]]]]'''
        # _1_Lambda4hs() move out

        r'''[[[[[
        if not external_frees:
            #no free_vars
            assert body_frees <= param2idx.keys()
            assert midway_bound_vars == nint2free_var

            if not nint2free_var:
                #no constants/midways and no free_vars
                assert not body_v2cxx
                assert num_free_vars == 0
                uXss4body = iXss4body
                f = FreeLocalBatchRouter(num_args4call, uXss4body)
                return _bottomup__mix0(f, ov2cxx)
            assert body_v2cxx
            #has constants/midways, but no free_vars
            is_mix0 = {CASE_CONST} == {*map(fst, body_v2cxx.values())}
            if is_mix0:
                #no _MidWayBound
                constants = (body_v2cxx[v][1] for v in midway_bound_vars)
                assert midway_bound_vars == nint2free_var
                uXss4body = fold__objXtuple(num_free_vars.__add__, mk_tuple, iXss4body)
                f = FreeLocalBatchRouter(num_args4call, uXss4body)
                mix0 = mk_apps(f, *constants)
                return _bottomup__mix0(mix0, ov2cxx)
            #has _MidWayBound, no external_frees
            TODO

        assert not body_frees <= param2idx.keys():
        ... ...
        TODO
        #]]]]]'''


    def ordered_by(nint2free_var, FVs, /):
        return mk_tuple(v for v in nint2free_var if v in FVs)

    def _1_Lambda4hs(scoped_vars, params, varXs4body, body_frees, body_v2cxx, /):
        #params = mk_tuple(v if type(v) is not UnusedPattern4hs else Var4hs() for v in params)
        param2idx = {v:i for i, v in enumerate(params)}
        if not len(param2idx) == len(params): raise TypeError


        fv2nidx = {}
        fvs = []
        def f4v(var, /):
            if var in param2idx:
                return param2idx[var]
            if var not in fv2nidx:
                nidx = - len(fv2nidx) - 1
                fv2nidx[var] = nidx
                fvs.append(var)
            return fv2nidx[var]
        f4s = tuple
        iXss4body = fold__objXtuple(f4v, f4s, varXs4body)
        fvs.reverse()
        for v, i in fv2nidx.items():
            if not v is fvs[i]: raise logic-err
        nint2free_var = (*fvs,)
        num_free_vars = len(nint2free_var)
        num_args4call = len(params)
        midway = _MidWayBound(nint2free_var, num_free_vars, num_args4call, iXss4body)
        assert len(nint2free_var) == len({*nint2free_var})
        assert len(params) == len({*params})
        assert set(nint2free_var)&set(params) == set()
        assert set(nint2free_var)|set(params) >= body_frees|body_v2cxx.keys()
            # >= not ==
            #   since there are unused params
        assert set() == body_frees&body_v2cxx.keys(),    body_frees&body_v2cxx.keys()


        external_frees = body_frees - set(params)
        assert external_frees == set(nint2free_var) - body_v2cxx.keys()

        inner_FVs = midway_bound_vars = set(body_v2cxx)
            #ordered/sorted
        assert inner_FVs&external_frees == set()
        assert inner_FVs|external_frees == set(nint2free_var)
        global_FVs = external_frees - scoped_vars
        scoped_FVs = external_frees - global_FVs

        inner_FVs = ordered_by(nint2free_var, inner_FVs)
        global_FVs = ordered_by(nint2free_var, global_FVs)
        scoped_FVs = ordered_by(nint2free_var, scoped_FVs)
        assert {*inner_FVs, *global_FVs, *scoped_FVs} == {*nint2free_var}


        inner_cased_xxx = mk_tuple(body_v2cxx[v] for v in inner_FVs)
        for case, payload in inner_cased_xxx:
            if case == CASE_CONST:
                #payload4CASE_CONST
                deep_check_mix0(payload)
            elif case == CASE_MIDWAY:
                #payload4CASE_MIDWAY
                check_type_is(tuple, payload)
                assert len(payload) == 5
            elif case == CASE_CLOSURE_:
                #payload4CASE_CLOSURE_
                check_type_is(tuple, payload)
                assert len(payload) == 6
            else:
                raise ValueError(case)
        case, payload = CASE_MIDWAY, (midway, inner_cased_xxx, inner_FVs, global_FVs, scoped_FVs)
        #may return diff cases
        #   CASE_CONST is possible
        #       special situation Lambda4hs can be transformed to mix0
        return case, payload
    #end-def _1_Lambda4hs(scoped_vars, params, varXs4body, body_frees, body_v2cxx, /):

    #end-def _bottomup__Lambda4hs(scoped_vars, mix2, ofrees, ov2cxx, /):

    #[[def___bottomup___AsIfPrimeRecurLet4hs]]
    def _bottomup___AsIfPrimeRecurLet4hs(scoped_vars, mix2, ofrees, ov2cxx, /):
        check_type_is(_AsIfPrimeRecurLet4hs, mix2)
        pairs4def, body = mix2

        var2rhs = dict(pairs4def)
        if not len(var2rhs) == len(pairs4def): raise TypeError('duplicated: vars')
        params = mk_tuple(map(fst, pairs4def))
        def on_body(body, /):
            ######################
            ######################
            if 0:
                #bug:recur_vars occur as scoped_vars not params
                #   params be refered by offsetted uint in iXss4body@ExtendedFreeLocalBatchRouter
                f = Lambda4hs(params, body)
                payload4CASE_MIDWAY = _main4Lambda4hs(f, scoped_vars)
            ######################
            else:
            ######################
                _adds = set(params) - scoped_vars
                _L = len(scoped_vars)
                scoped_vars.update(_adds)
                assert _L + len(_adds) == len(scoped_vars)
                f = Lambda4hs((), body)
                payload4CASE_MIDWAY = _main4Lambda4hs(f, scoped_vars)
                scoped_vars.difference_update(_adds)
                    #scoped_vars -= _adds
                assert _L == len(scoped_vars)
                del _adds, _L
            ######################
            ######################
            (midway, inner_cased_xxx, inner_FVs, global_FVs, scoped_FVs) = payload4CASE_MIDWAY
            check_type_is(_MidWayBound, midway)
            (nint2free_var, num_free_vars, num_args4call, iXss4body) = midway
            assert not (set(inner_FVs) & set(params))
            assert not (set(global_FVs) & set(params))
            #assert (set(scoped_FVs) & set(params))
            #direct_used_recur_vars = set(scoped_FVs) & set(params)
            return payload4CASE_MIDWAY

        recur_vars = params
        recur_midway_payloads = mk_tuple(map(on_body, map(snd, pairs4def)))

        #check ? really min-prime-recur-group???

        if 0:
            # for (global_FVs4closure, scoped_FVs4closure), but too slow, O(2^n)
            payload4CASE_MIDWAY4let_defs = on_body(_mk_Tuple4Data4hs(*map(snd, pairs4def)))
        #
        def _calc_FVs():
            '-> (global_FVs4closure, scoped_FVs4closure)'
            oinner_FVs = []
            oglobal_FVs = []
            oscoped_FVs = []
            #
            _inner_FVs = set()
            _global_FVs = set()
            #bug: _scoped_FVs = set()
            #   see:below call builtin__mk_mk_closure to build closure
            _scoped_FVs = set(recur_vars)
            def unique(ls, _s, inputs, /):
                #remove duplicates in inputs
                #inputs <- inputss
                #   ==>> unique(chain(*inputss))
                for x in inputs:
                    if x not in _s:
                        _s.add(x)
                        ls.append(x)
            oinner_cased_xxx = []
            for payload4CASE_MIDWAY in recur_midway_payloads:
                (midway, inner_cased_xxx, inner_FVs, global_FVs, scoped_FVs) = payload4CASE_MIDWAY
                check_type_is(_MidWayBound, midway)
                (nint2free_var, num_free_vars, num_args4call, iXss4body) = midway
                unique(oinner_FVs, _inner_FVs, inner_FVs)
                oinner_cased_xxx.extend(inner_cased_xxx)
                    #by +=
                    #check len==
                unique(oglobal_FVs, _global_FVs, global_FVs)
                unique(oscoped_FVs, _scoped_FVs, scoped_FVs)
            inner_cased_xxx4closure = mk_tuple(oinner_cased_xxx)
            inner_FVs4closure = mk_tuple(oinner_FVs)
            global_FVs4closure = mk_tuple(oglobal_FVs)
            scoped_FVs4closure = mk_tuple(oscoped_FVs)
            if not len(inner_cased_xxx4closure) == len(inner_FVs4closure): raise logic-err
            return (inner_cased_xxx4closure, inner_FVs4closure, global_FVs4closure, scoped_FVs4closure)
        (inner_cased_xxx4closure, inner_FVs4closure, global_FVs4closure, scoped_FVs4closure) = _calc_FVs()
        if not len(inner_cased_xxx4closure) == len(inner_FVs4closure): raise logic-err
        cased_payload4CASE_CLOSURE_ = (CASE_CLOSURE_, (recur_vars, recur_midway_payloads, inner_cased_xxx4closure, inner_FVs4closure, global_FVs4closure, scoped_FVs4closure))
        assert not (set(recur_vars) & set(global_FVs4closure))
        assert not (set(recur_vars) & set(scoped_FVs4closure))
        assert not (set(global_FVs4closure) & set(scoped_FVs4closure))

        var4closure_ = Var4hs() #fresh
        if 0:
            #bug? should be later?
            #   see:_bottomup__Lambda4hs.assert before _2_Lambda4hs()
            #       assert not (ofrees & ov2cxx.keys())
            #
            ov2cxx[var4closure_] = cased_payload4CASE_CLOSURE_
        closure__Var = mk_apps(builtin__mk_mk_closure, var4closure_, *scoped_FVs4closure)
            #scoped_FVs4closure ==>> bound_dynamic_free_vars
            #
            #if above unique()::_scoped_FVs init empty, here will leak_out recur_vars
            #
        f4body = Lambda4hs(params, body)
        eqv_form = mk_apps(builtin__apply_closure, closure__Var, f4body)
        #return bottomup(scoped_vars, eqv_form, ofrees, ov2cxx)
        result = bottomup(scoped_vars, eqv_form, ofrees, ov2cxx)
        if 1:
            #moved from above to here
            ov2cxx[var4closure_] = cased_payload4CASE_CLOSURE_
            ofrees.remove(var4closure_)
        return result
    #end-def _bottomup___AsIfPrimeRecurLet4hs(scoped_vars, mix2, ofrees, ov2cxx, /):

    ##################################
    def builtin__mk_mk_closure(closure_4hs, /):
        r'''
        # builtin__mk_mk_closure::closure_<num_scoped_FVs4closure> -> mk_closure
        #   builtin__mk_mk_closure.___get_num_args4call___ -> 1
        #   mk_closure::(*scoped_FVs4closure) -> closure
        # see:builtin__apply_closure'
        # see:closure<ExtendedFreeLocalBatchRouter>
        #   closure<_MidWayBound> is not closure<ExtendedFreeLocalBatchRouter>
        #
        # closure = ((bound_builtins_and_constants, bound_globals, bound_dynamic_free_vars), recur_group)
        #
        # closure_ = ((bound_builtins_and_constants, bound_globals), recur_group, num_bound_dynamic_free_vars)
        #
        # bound_dynamic_free_vars := scoped_FVs4closure
        #
    ##################################
    copy from ExtendedFreeLocalBatchRouter.__doc__:
            closure = (bound_groups/[[hs_obj]], recur_group/[ExtendedFreeLocalBatchRouter])
                bound_groups = (bound_builtins_and_constants, bound_globals, bound_dynamic_free_vars)
                recur_group = ()|[ExtendedFreeLocalBatchRouter]
                    #unbound_group
    ##################################
        #'''
        check_type_is(Data4py, closure_4hs)
        [closure_4py] = closure_4hs
        ((bound_builtins_and_constants, bound_globals), recur_group, num_bound_dynamic_free_vars) = closure_4py
        def mk_closure(*bound_dynamic_free_vars):
            assert len(bound_dynamic_free_vars) == num_bound_dynamic_free_vars
            closure4py = ((bound_builtins_and_constants, bound_globals, bound_dynamic_free_vars), recur_group)
            closure4hs = Data4py(closure4py)
            return closure4hs
        return Expr4py(num_bound_dynamic_free_vars, mk_closure)
    builtin__mk_mk_closure = Expr4py(1, builtin__mk_mk_closure)

    ##################################
    def builtin__apply_closure(closure4hs, f4hs, /):
        r'''
        # builtin__apply_closure::closure -> (\(*recur_vars) -> r) -> r
        # builtin__apply_closure closure f
        #   = f (get<0> closure) (get<1> closure) ...
        # closure = builtin__mk_mk_closure closure_ *scoped_FVs4closure
        # closure_ is filled by compiler when global_FVs fulfilled
        #
        #'''
        closure4hs = whnf_reduce4apps(closure4hs)
        check_type_is(Data4py, closure4hs)
        [closure4py] = closure4hs
        ((bound_builtins_and_constants, bound_globals, bound_dynamic_free_vars), recur_group) = closure4py
        args4hs = (mk_apps(g, closure4hs) for g in recur_group)
        return mk_apps(f4hs, *args4hs)
    builtin__apply_closure = Expr4py(2, builtin__apply_closure)

    ##################################
    #[[def___bottomup__mix0]]
    def _bottomup__mix0(constant, ov2cxx, /):
        var = Var4hs() #fresh var
        ov2cxx[var] = (CASE_CONST, constant)
        #hs_obj = constant
        return True, var
    #[[def__bottomup]]
    def bottomup(scoped_vars, mix2, ofrees, ov2cxx, /):
        r'''-> (is_mix0, varXs)=((True, var)|(False, varXs) #varXs=Var|tuple<varXs>))
        #ofrees - output__free_vars
        #ov2cxx - output__var2cased #using .pop()
        #
        #see:[[def___bottomup__Lambda4hs]] _bottomup__Lambda4hs
        #see:[[def___bottomup___AsIfPrimeRecurLet4hs]] _bottomup___AsIfPrimeRecurLet4hs
        #see:[[def___bottomup__mix0]] _bottomup__mix0

        ##################################
        ofrees :: {var}
            #not include: inner_FVs   - placeholder for builtins_and_constants
            global_FVs  - placeholder for global static hs_objs
            scoped_vars - placeholder for runtime params/args

        ##################################
        ov2cxx :: {var: (case, payload)}
            (CASE_CONST, mix0)
                = cased_payload4CASE_CONST
                = (CASE_CONST, payload4CASE_CONST)
            (CASE_MIDWAY, (midway, inner_cased_xxx, inner_FVs, global_FVs, scoped_FVs))
                = cased_payload4CASE_MIDWAY
                = (CASE_MIDWAY, payload4CASE_MIDWAY)
            (CASE_CLOSURE_, (recur_vars, recur_midway_payloads, inner_cased_xxx4closure, inner_FVs4closure, global_FVs4closure, scoped_FVs4closure))
                = cased_payload4CASE_CLOSURE_
                = (CASE_CLOSURE_, payload4CASE_CLOSURE_)
            ########################
            CASE_CLOSURE_:
            recur_vars :: [Var]
            recur_midway_payloads :: [payload<CASE_MIDWAY>] = [payload4CASE_MIDWAY]
            rec-let x = ...
                y = ...
            in  body
            ==>>
                # f = (\x y -> body)
                apply_closure closure f
                <==> f (get<x> closure) (get<y> closure)
            ########################
            CASE_MIDWAY:
            midway :: _MidWayBound
            inner_cased_xxx :: [(case, payload)]
                <<-- body_v2cxx <<-- ov2cxx
                dict(zip(inner_FVs, inner_cased_xxx))
            inner_FVs, global_FVs, scoped_FVs :: [Var]
            nint2free_var = midway.nint2free_var
            len(nint2free_var) == len(inner_FVs)+len(global_FVs)+len(scoped_FVs)
            set(nint2free_var) == set(inner_FVs)+set(global_FVs)+set(scoped_FVs)
                keep same ordering
                scoped_FVs:
                    this <==> Apps4hs [var4f, *scoped_FVs]
                    f is to be computed
                    f <==> Apps4hs [g, result5midway]
                    result5midway :: Expr8List4hs

                    this <==> Apps4hs [g, result5midway, *args<scoped_FVs>]
                        <==> Apps4hs [result5midway, closure]
        ##################################
        #'''
        cls = type(mix2)
        if cls is Data4hs:
            mix2 = shallow_degrade_unless_mix2(mix2)
            cls = type(mix2)
        assert cls is type(mix2) is not Data4hs
        if cls in (Apps4hs, Expr8List4hs):
            ls = [bottomup(scoped_vars, x, ofrees, ov2cxx) for x in mix2]
            if all(map(fst, ls)):
                #all children are is_mix0
                constant = mix0 = mk_apps5iter(map(snd, map(ov2cxx.pop, map(snd, ls))))
                return _bottomup__mix0(constant, ov2cxx)
            else:
                #varXs = mk_apps5iter(map(snd, ls))
                varXs = mk_tuple(map(snd, ls))
                return False, varXs

        if (not _is_cls_both(cls)) and is_cls4obj4hs(cls):
            constant = mix0 = mix2 #constant!!!
            return _bottomup__mix0(constant, ov2cxx)

        if is_cls4var(cls):
            var = mix2
            ofrees.add(var)
            varXs = var
            return False, varXs

        if cls is Lambda4hs:
            return _bottomup__Lambda4hs(scoped_vars, mix2, ofrees, ov2cxx)
        if cls is _AsIfPrimeRecurLet4hs:
            return _bottomup___AsIfPrimeRecurLet4hs(scoped_vars, mix2, ofrees, ov2cxx)
        raise TypeError('logic-err in compile__mix2 or deep_check_mix2')
    #end-def bottomup(scoped_vars, mix2, ofrees, ov2cxx, /):

    def link__cased_xxx(cased_xxx, global_var2hs_obj, /):
        r'''
        #see:[[def__link__payload4CASE_MIDWAY]]
        #'''
        case, payload = cased_xxx
        if case == CASE_MIDWAY:
            f = link__payload4CASE_MIDWAY
            #d = dict(recur_FVs=(), recur_group=())
        elif case == CASE_CONST:
            f = link__payload4CASE_CONST
            #d = {}
        elif case == CASE_CLOSURE_:
            f = link__payload4CASE_CLOSURE_
            #d = {}
        else:
            raise TypeError-logic-err
        return f(payload, global_var2hs_obj)
        #return f(payload, global_var2hs_obj, **d)

    def link__payload4CASE_CONST(payload4CASE_CONST, global_var2hs_obj, /):
        '-> mix0'
        mix0 = payload4CASE_CONST
        return mk_apps(mix0) #emplace-whnf
    def link__payload4CASE_CLOSURE_(payload4CASE_CLOSURE_, global_var2hs_obj, /):
        r'''-> closure_4hs
        #see:[[def__link__payload4CASE_MIDWAY]]
        #'''
        (recur_vars, recur_midway_payloads, inner_cased_xxx4closure, inner_FVs4closure, global_FVs4closure, scoped_FVs4closure) = payload4CASE_CLOSURE_
        recur_FVs = recur_vars
        if 0:
            #bug: recur_group=f(...recur_group...)
            recur_group = mk_tuple(link__payload4CASE_MIDWAY(payload4CASE_MIDWAY, global_var2hs_obj, recur_FVs=recur_FVs, recur_group=None) for payload4CASE_MIDWAY in recur_midway_payloads)
                #recur ...
            num_bound_dynamic_free_vars = len(scoped_FVs4closure)
            bound_globals = mk_tuple(global_var2hs_obj[v] for v in global_FVs4closure)
            bound_builtins_and_constants = ()

            closure_4py = ((bound_builtins_and_constants, bound_globals), recur_group, num_bound_dynamic_free_vars)

            closure_4hs = Data4py(closure_4py)
            return closure_4hs
        ##################################
        #see:_link__midway
        (shape4closure, var2idc, num_bound_dynamic_free_vars, bound_globals, bound_builtins_and_constants) = _1_link__midway(global_var2hs_obj, recur_FVs=recur_FVs, inner_cased_xxx4closure=inner_cased_xxx4closure, inner_FVs4closure=inner_FVs4closure, global_FVs4closure=global_FVs4closure, scoped_FVs4closure=scoped_FVs4closure)
        rs = []
        for payload4CASE_MIDWAY in recur_midway_payloads:
            (midway, inner_cased_xxx, inner_FVs, global_FVs, scoped_FVs) = payload4CASE_MIDWAY
            check_type_is(_MidWayBound, midway)
            f__4hs = _2_link__midway(midway, shape4closure, var2idc)
            check_type_is(ExtendedFreeLocalBatchRouter, f__4hs)
                #to mk recur_group::[f__4hs]
            rs.append(f__4hs)
        #end-loop
        recur_group = mk_tuple(rs); del rs

        closure_4py = ((bound_builtins_and_constants, bound_globals), recur_group, num_bound_dynamic_free_vars)

        closure_4hs = Data4py(closure_4py)
        return closure_4hs


    def main_link__payload4CASE_MIDWAY(payload4CASE_MIDWAY, global_var2hs_obj, scoped_var2hs_obj, /):
        r'''-> f4hs:(*args4Lambda4hs -> r)
        required:
            main_link__payload4CASE_MIDWAY.scoped_var2hs_obj.keys() == compile__mix2.scoped_vars
            main_link__payload4CASE_MIDWAY.payload4CASE_MIDWAY := compile__mix2.output
            #see:[[def__compile__mix2]]
        #'''
        f_4hs = link__payload4CASE_MIDWAY(payload4CASE_MIDWAY, global_var2hs_obj)
        (midway, inner_cased_xxx, inner_FVs, global_FVs, scoped_FVs) = payload4CASE_MIDWAY
        hs_objs4bound_dynamic_free_var = (scoped_var2hs_obj[v] for v in scoped_FVs)
        f4hs = mk_apps(f_4hs, *hs_objs4bound_dynamic_free_var)
        return f4hs

    #[[def__link__payload4CASE_MIDWAY]]
    def link__payload4CASE_MIDWAY(payload4CASE_MIDWAY, global_var2hs_obj, /):
        r''' -> f_4hs:(*scoped_FVs4closure -> *args4Lambda4hs -> r)
        # [len(scoped_FVs+global_FVs+inner_FVs) == num_free_vars]
        #
        ##################################
        -> as-if-link(ExtendedFreeLocalBatchRouter, closure_4hs)
            ==>> expected scoped_FVs4closure++args4Lambda4hs
            num_bound_dynamic_free_vars+num_args4call
            len(scoped_FVs)+num_args4call
        ##################################
        #
        #closure4hs = Apps4hs(builtin__mk_mk_closure, closure_4hs, *scoped_FVs4closure)
        #see: _2_Lambda4hs: "varXs = (var4f, *scoped_FVs)"
        #   f :: ExtendedFreeLocalBatchRouter
        #   fvs = scoped_FVs4closure
        #
        #   (f? *fvs *args) === (f closure4hs *args)
        #   (f? *fvs) === (f closure4hs)
        #   (f? *fvs) === (f (mkmk closure_4hs *fvs))
        #   f? === (g? closure_4hs f)
        #   (g? closure_4hs f *fvs) === (f (mkmk closure_4hs *fvs))
        #   so what is g?
        #   g? closure_4hs = (FreeLocalBatchRouter(2+closure_4hs.num_bound_dynamic_free_vars, (1, (0, 2..1+num_bound_dynamic_free_vars)))  (mkmk closure_4hs))
        #

        payload4CASE_MIDWAY:
            output of compile__mix2()
            #see:[[def__compile__mix2]]
            #see:[[def__bottomup]] bottomup()
        ##xxx cancel: scoped_var2hs_obj :: {Var:hs_obj}
        #       runtime not link_time
        #
        global_var2hs_obj :: {Var:hs_obj}
        ######################
        hs_obj:
            is_obj4hs(hs_obj)
            #see:IIsCls4Obj4hs.___is_cls4obj4hs___
            #see:Error4hs, the_undefined
            #   may use defaultdict(Error4hs)
            #
        #'''
        recur_FVs = ()
        recur_group = ()
        ##################################
        (f__4hs, num_bound_dynamic_free_vars, bound_globals, bound_builtins_and_constants) = _1_link__payload4CASE_MIDWAY(payload4CASE_MIDWAY, global_var2hs_obj)
        check_type_is(ExtendedFreeLocalBatchRouter, f__4hs)
            #recur_group::[f__4hs]
            #f__4hs :: closure4hs -> *args -> r
        f_4hs = _2_link__payload4CASE_MIDWAY(recur_group, f__4hs, num_bound_dynamic_free_vars, bound_globals, bound_builtins_and_constants)
            #f_4hs :: *scoped_FVs -> *args -> r
        return f_4hs
    def _1_link__payload4CASE_MIDWAY(payload4CASE_MIDWAY, global_var2hs_obj, /):
        (midway, inner_cased_xxx, inner_FVs, global_FVs, scoped_FVs) = payload4CASE_MIDWAY
        check_type_is(_MidWayBound, midway)
        (nint2free_var, num_free_vars, num_args4call, iXss4body) = midway
        assert len(nint2free_var) == num_free_vars == len(inner_FVs) + len(global_FVs) + len(scoped_FVs)
        assert len(inner_FVs) == len(inner_cased_xxx)

        recur_FVs = ()
        (f__4hs, num_bound_dynamic_free_vars, bound_globals, bound_builtins_and_constants) = _link__midway(midway, global_var2hs_obj, recur_FVs=recur_FVs, inner_cased_xxx4closure=inner_cased_xxx, inner_FVs4closure=inner_FVs, global_FVs4closure=global_FVs, scoped_FVs4closure=scoped_FVs)
        return (f__4hs, num_bound_dynamic_free_vars, bound_globals, bound_builtins_and_constants)
    def _link__midway(midway, global_var2hs_obj, /, *, recur_FVs, inner_cased_xxx4closure, inner_FVs4closure, global_FVs4closure, scoped_FVs4closure):
        (shape4closure, var2idc, num_bound_dynamic_free_vars, bound_globals, bound_builtins_and_constants) = _1_link__midway(global_var2hs_obj, recur_FVs=recur_FVs, inner_cased_xxx4closure=inner_cased_xxx4closure, inner_FVs4closure=inner_FVs4closure, global_FVs4closure=global_FVs4closure, scoped_FVs4closure=scoped_FVs4closure)
        f__4hs = _2_link__midway(midway, shape4closure, var2idc)
        return (f__4hs, num_bound_dynamic_free_vars, bound_globals, bound_builtins_and_constants)
    def _1_link__midway(global_var2hs_obj, /, *, recur_FVs, inner_cased_xxx4closure, inner_FVs4closure, global_FVs4closure, scoped_FVs4closure):
        fvss = (recur_FVs, inner_FVs4closure, global_FVs4closure, scoped_FVs4closure)
        for fvs in fvss:
            check_type_is(tuple, fvs)
            assert all(map(is_var, fvs))
        assert sum(map(len, fvss)) == len(set().union(*fvss))
            #isdisjoint-pairwise

        check_type_is(tuple, inner_cased_xxx4closure)
        assert len(inner_cased_xxx4closure) == len(inner_FVs4closure)




        ##################################
        #closure4py = ((bound_builtins_and_constants, bound_globals, bound_dynamic_free_vars), recur_group)
        #recur_FVs = ()

        ######################
        ######################
        num_bound_dynamic_free_vars = len(scoped_FVs4closure)
        num_bound_globals = len(global_FVs4closure)
        num_bound_builtins_and_constants = len(inner_FVs4closure)
        len_recur_group = len(recur_FVs)
        shape4closure = ((num_bound_builtins_and_constants, num_bound_globals, num_bound_dynamic_free_vars), len_recur_group)
        #target:nint2idc, closure_4hs

        closure4py__Var = ((inner_FVs4closure, global_FVs4closure, scoped_FVs4closure), recur_FVs)
        var2idc = {}
        ##################################
        ##################################
        i = 0
        for j, xxx_FVs in enumerate(closure4py__Var[i]):
            for k, var in enumerate(xxx_FVs):
                var2idc[var] = (i,j,k)
        ##################################
        i = 1
        for j, var in enumerate(closure4py__Var[i]):
            var2idc[var] = (i,j)
        ##################################
        ##################################

        ##################################
        bound_globals = mk_tuple(global_var2hs_obj[v] for v in global_FVs4closure)
        #recur_group = ()
        #target:bound_builtins_and_constants
        bound_builtins_and_constants = mk_tuple(link__cased_xxx(cased_xxx, global_var2hs_obj) for cased_xxx in inner_cased_xxx4closure)
            #deep-recur ...link__cased_xxx()
        return (shape4closure, var2idc, num_bound_dynamic_free_vars, bound_globals, bound_builtins_and_constants)


    def _2_link__midway(midway, shape4closure, var2idc, /):
        r'''-> f__4hs

        f__4hs vs f_4hs:
            f__4hs <<== _2_link__midway
            f_4hs <<== _2_link__payload4CASE_MIDWAY
            ######################
            f__4hs :: closure4hs -> *args -> r
            f_4hs :: *scoped_FVs4closure -> *args -> r
            ######################
            f_4hs = bind<f__4hs, closure_4hs>
        #'''
        ##################################
        check_type_is(_MidWayBound, midway)
        (nint2free_var, num_free_vars, num_args4call, iXss4body) = midway
        #assert set(nint2free_var) <= set().union(*fvss)
        assert set(nint2free_var) <= var2idc.keys()

        #to mk ExtendedFreeLocalBatchRouter(total4closure, shape4closure, nint2idc, num_free_vars, num_args4call, iXss4body)
        #mk_ExtendedFreeLocalBatchRouter(shape4closure, nint2idc, num_free_vars, num_args4call, iXss4body)
        nint2idc = mk_tuple(var2idc[var] for var in nint2free_var)
        f__4hs = mk_ExtendedFreeLocalBatchRouter(shape4closure, nint2idc, num_free_vars, num_args4call, iXss4body)
        return f__4hs
        ##################################

    #end-def _link__midway
    #end-def _1_link__payload4CASE_MIDWAY
    def _2_link__payload4CASE_MIDWAY(recur_group, f__4hs, num_bound_dynamic_free_vars, bound_globals, bound_builtins_and_constants, /):
        check_type_is(tuple, recur_group)
        #assert len(recur_group) == len(recur_FVs)
        closure_4py = ((bound_builtins_and_constants, bound_globals), recur_group, num_bound_dynamic_free_vars)

        closure_4hs = Data4py(closure_4py)
        #copy from __doc__ above:
        #   g? closure_4hs = (FreeLocalBatchRouter(2+closure_4hs.num_bound_dynamic_free_vars, (1, (0, 2..1+num_bound_dynamic_free_vars)))  (mkmk closure_4hs))
        f_4hs = result5midway = mk_apps(FreeLocalBatchRouter(2+num_bound_dynamic_free_vars, (1, (0, *range(2, 2+num_bound_dynamic_free_vars)))), mk_apps(builtin__mk_mk_closure, closure_4hs), f__4hs)
            #link f__4hs&closure_4hs

        return f_4hs
        return (result5midway)
        return mk_apps(result5midway)
            #since whnf-emplace??
            #   No!! neednot, since mix0 donot containts Lambda4hs
            #
    #end-def _2_link__payload4CASE_MIDWAY
    #end-def link__payload4CASE_MIDWAY(payload4CASE_MIDWAY, scoped_var2hs_obj, global_var2hs_obj, /):

    compile__mix2.CASE_CONST = CASE_CONST
    compile__mix2.CASE_MIDWAY = CASE_MIDWAY
    compile__mix2.CASE_CLOSURE_ = CASE_CLOSURE_
    return compile__mix2, main_link__payload4CASE_MIDWAY, link__payload4CASE_MIDWAY
compile__mix2, main_link__payload4CASE_MIDWAY, link__payload4CASE_MIDWAY = ___tmp_env(); del ___tmp_env
assert not compile__mix2.CASE_CONST == compile__mix2.CASE_MIDWAY
assert not compile__mix2.CASE_CLOSURE_ == compile__mix2.CASE_MIDWAY
assert not compile__mix2.CASE_CLOSURE_ == compile__mix2.CASE_CONST
if 1:
    # mix0 := (\pd->main_link__payload4CASE_MIDWAY pd {} {}) $ (\mix2->compile__mix2 mix2 []) $ deep_convert_to_mix2 mix
    deep_convert_to_mix2
    deep_check_mix2
    compile__mix2
    main_link__payload4CASE_MIDWAY
    link__payload4CASE_MIDWAY
    mk_apps
    mk_apps5iter
    deep_reduce4apps
    whnf_reduce4apps
    eq4output4apps
    rebuild_apps5output #to show

def _test_compile__mix2___on_Data4hs():
    r'''
    \x y -> case (x,y) of
        ...
    Data4hs(ctor4Pair4hs, var_x, var_y)
    but Var is Syntactic4hs not Semantic4hs
    ...
    #'''
    ctor4Pair4hs
    x = mk_var.x
    y = mk_var.y
    mixN = Data4hs(ctor4Pair4hs, x, y)
    mix2 = deep_convert_to_mix2(mixN)
    assert mix2 == mixN
    deep_check_mix2(mixN)
    payload4CASE_MIDWAY = compile__mix2(mixN, {})
    (midway, inner_cased_xxx, inner_FVs, global_FVs, scoped_FVs) = payload4CASE_MIDWAY
    print(inner_cased_xxx, inner_FVs, global_FVs, scoped_FVs)
    assert global_FVs == (y, x)
        #transparent-Data4hs as Apps4hs
        #
        #why not (x,y)?
        #   FVs sorted by midway.nint2idc
        #       see:ordered_by()
        #   nint2idc index in reversed ordered: -1=x, -2=y, -3,...
        #       put into seq [...,y,x]
_test_compile__mix2___on_Data4hs()


def _prepare_CombinatorSKIBC__Lambda4hs():
    x = mk_var.x
    y = mk_var.y
    z = mk_var.z
    f = mk_var.f
    g = mk_var.g
    _ = mk_apps

    S = Lambda4hs((f, g, x), _(_(f,x), _(g,x)))
    K = Lambda4hs((x, y), x)
    I = Lambda4hs((x,), x)
    B = Lambda4hs((f,g,x), _(f, _(g,x)))
    C = Lambda4hs((f,x,y), _(f,y,x))
    Yh = Lambda4hs((g,f), _(f, _(g,g,f)))
    #_test_SKIBC(S, K, I, B, C, Yh)
    #return (S, K, I, B, C, Yh)
    (_B, _C, _Yh) = _prepare_BCYh_from_SKI(S, K, I)
    return (S, K, I, B, C, Yh, _B, _C, _Yh)


def _test_SKIBC__Lambda4hs():
    #r = (S, K, I, B, C, Yh) = _prepare_CombinatorSKIBC__Lambda4hs()
    r = (S, K, I, B, C, Yh, _B, _C, _Yh) = _prepare_CombinatorSKIBC__Lambda4hs()
    d = {}
    r = (compile__mix2(x, d) for x in r)
    r = (main_link__payload4CASE_MIDWAY(x, d, d) for x in r)
    (S, K, I, B, C, Yh, _B, _C, _Yh) = r
    kwargs = dict(mk_Data4py=Data4py, MoreRouterTypes=[ExtendedFreeLocalBatchRouter])
    _test_SKIBC(S, K, I, B, C, Yh, **kwargs)
    _test_SKIBC(S, K, I, _B, _C, _Yh, **kwargs)
_test_SKIBC__Lambda4hs()
def _test_compile__mix2____MultiInputUnboxedRecurLet4hs():
    hs_mk_pair = f4Pair4hs = mk_f4hs__Tuple4Data4hs_(2)
    hs_tuple0 = f4EmptyTuple4hs = mk_f4hs__Tuple4Data4hs_(0)
    _u = default_unused_pattern
    _p = lambda a,b,/:mk_apps(f4Pair4hs, a, b)
    ctor4Pair4hs = mk_Ctor4Tuple4Data4hs(2)
    ctor4EmptyTuple4hs = mk_Ctor4Tuple4Data4hs(0)
    MAX = 20
    us = uint4hs__ls = mk_tuple(map(Data4py, range(MAX)))

    def check_Pair4hs(xy4hs, /):
        check_type_is(Data4hs, xy4hs)
        assert xy4hs[0] == ctor4Pair4hs
    def _compile(lss4def, body, /):
        x__mixN = mk_MultiInputUnboxedRecurLet4hs(lss4def, body)
        x__mix2 = deep_convert_to_mix2(x__mixN)
        deep_check_mix2(x__mix2)
        x__pd = compile__mix2(x__mix2, [])
        x4hs = main_link__payload4CASE_MIDWAY(x__pd, {}, {})
        return x4hs


    MultiInputUnboxedRecurLet4hs
    mk_MultiInputUnboxedRecurLet4hs
    def t1():
        r'''
        test RecurLet4hs
        let x = (k0,x)
        in  x
        #'''
        x = mk_var.x
        k0 = us[9]
        lss4def = [
            (x, mk_apps(f4Pair4hs, k0, x))
            ]
        body = x

        x4hs = _compile(lss4def, body)
        for i in range(9):
            x4hs = whnf_reduce4apps(x4hs)
            assert type(x4hs) is Data4hs, (i, x4hs)
            #raise err: x4hs = Data4py(closure4py)
                #??looking main_link__payload4CASE_MIDWAY
                # ==>> discard xxx_FVs from recur_midway_payloads
                # ==>> merge them into xxx_FVs4closure since MUST share same closure_4hs
                # ==>> split link__payload4CASE_MIDWAY === _1_link__payload4CASE_MIDWAY+_2_link__payload4CASE_MIDWAY
                # ==>> split _1_link__payload4CASE_MIDWAY === _link__midway === _1_link__midway+_2_link__midway
                #
            #raise err: missing "x" in global_var2hs_obj
                #looking _bottomup___AsIfPrimeRecurLet4hs
                #   find a bug: init "_scoped_FVs = set()"
                #   SHOULD_BE "_scoped_FVs = set(recur_vars)"
            check_type_is(Data4hs, x4hs)
            assert x4hs[0] == ctor4Pair4hs
            _, _a, _b = x4hs
            #_a = Apps4hs [k0]
            _a = whnf_reduce4apps(_a)
            assert _a is k0, _a
            x4hs = _b
    ##################################
    t1()
    ##################################
    ##################################
    def t2():
        r'''
        test OutputUnboxedRecurLet4hs
        let y@(x, _) = ((k0,k1), (x,x))
        in  (x, y)
        #'''
        x = mk_var.x
        y = mk_var.y
        k0 = us[9]
        k1 = us[6]
        lss4def = [
            (Alias4Pattern4hs(y, Pattern4hs(ctor4Pair4hs, (x, _u))), _p(_p(k0,k1), _p(x,x)))
            ]
        body = _p(x, y)
        xy4hs = _compile(lss4def, body)

        deep_reduce4apps
        whnf_reduce4apps
        eq4output4apps
        rebuild_apps5output #to show
        xy4hs = whnf_reduce4apps(xy4hs)
        #print(xy4hs)
        check_Pair4hs(xy4hs)
        _, x4hs, y4hs = xy4hs
        x4hs = whnf_reduce4apps(x4hs)
        check_Pair4hs(x4hs)
        _, xa4hs, xb4hs = x4hs
        xa4hs = whnf_reduce4apps(xa4hs)
        xb4hs = whnf_reduce4apps(xb4hs)
        #assert xa4hs is k0, xa4hs
        #assert xa4hs is k0, [type(xa4hs), *map(type, xa4hs)]
        #assert xa4hs is k0, [type(xa4hs) is Data4hs, *map(len, xa4hs)]
        #assert xa4hs is k0, [(ctor4hs == ctor4Pair4hs, type(a) is type(b) is Apps4hs, a is b, a[0] is b[0], a[1] is b[1]) for (ctor4hs, a, b) in [xa4hs]]
        #assert xa4hs is k0, [xa4hs[1][0] == ExtendedFreeLocalBatchRouter(11, ((8, 0, 0), 3), ((1, 0), (0, 0, 7)), 2, 0, (-1, -2)), type(xa4hs[1][1]) is Data4py, type(xa4hs[1][1][0]) is tuple, xa4hs[2] is xa4hs[1]]
        #---->>
            #raise xa4hs contains Data4py(...Apps4hs(...)...): wrong wrap by Data4py
            #   No, correct, Apps4hs inside closure_4hs/closure4hs
            #
            #looking MultiInputUnboxedRecurLet4hs.___shallow_degrade_unless_mix2___:
            #   mk_Tuple4Data4hs_ for input4case
            #       fixed by using lazy-version
            #looking OutputUnboxedRecurLet4hs/RecurLet4hs/_AsIfPrimeRecurLet4hs/_bottomup___AsIfPrimeRecurLet4hs
            #   not found bug
            #looking: py -m   nn_ns.mimic_Haskell.Data 2> /sdcard/0my_files/tmp/out4py/nn_ns.mimic_Haskell.Data.debug.txt
            #   assert xa4hs is k0, xa4hs
            #   xa4hs[0] == ctor4Pair4hs
            #   xa4hs[1] :: Apps4hs
            #   xa4hs[1][0] == ExtendedFreeLocalBatchRouter(11, ((8, 0, 0), 3), ((1, 0), (0, 0, 7)), 2, 0, (-1, -2))
            #   xa4hs[1][1] == closure4hs == Data4py(closure4py)
            #   xa4hs[2] is xa4hs[1]
            #
        try:
            assert xa4hs is k0
        except AssertionError:
            check_Pair4hs(xa4hs)
            _, xaa4hs, xab4hs = xa4hs
            assert xaa4hs is xab4hs
            check_type_is(Apps4hs, xaa4hs)
            x__4hs, closure4hs = xaa4hs
                #xaa4hs = Apps4hs [x__4hs, closure4hs] === x4hs
                #but xaa4hs := x4hs[1][1]
                # ==>> x = ((x,x), ???)
                # guess y@(x,_) is parse wrong
                #==>> findout extract4hs===closure4py.builtins_and_constants[5]
                #   found bug:
                    #5:extract4hs for "y@(x,_)"
                    # Apps4hs(ExtendedApp4Data4hs(True, CtorH4hs((<class 'tuple'>, 2),), 2, ((1, None),)), _output = _Apps4hs(ExtendedApp4Data4hs(True, CtorH4hs((<class 'tuple'>, 2),), 2, ((1, None),)),), _state = 1)
                        #bug: SHOULD_BE (0,None)
                        #   xpattern__to__params_ExtendedApp4Data4hs_pair.on_inner
                            #bug:return None if x in used_vars else (idx, None)
                            #==>>return None if x not in used_vars else (idx, None)
                        #

        assert xb4hs is k1, xb4hs
        if 1:
            xy4hs = deep_reduce4apps(xy4hs)
            xy4hs = rebuild_apps5output(xy4hs)
            manual__k0_k1 = _p(k0,k1)
            manual__x = manual__k0_k1
            manual__y = _p(manual__x, _p(manual__x, manual__x))
            manual__xy = _p(manual__x, manual__y)
            manual__xy = deep_reduce4apps(manual__xy)
            manual__xy = rebuild_apps5output(manual__xy)
            assert manual__xy == xy4hs
            #print(xy4hs)
    ##################################
    t2()
    ##################################
    ##################################
    ##################################
    ##################################

_test_compile__mix2____MultiInputUnboxedRecurLet4hs()

#TAIL_FOR_WRITING
r'''
Func 调用 = (lambda函数体, closure静态闭包, 动态自动填充参数(隐参数,外挂接口推导), 用户提供的输入参数)

Typing # xxx :: ...
DefTyp # data Xxx ... = ...
DefVar # xxx = ... | f ... = ... | Xxx ... = ...
#Arrow #Expr8List4hs + Infix4hs



py-hierarchy
    ---register-mro, first-get-or-forbid-register
    --extend register further ++ private state ++ interpreter(::callable)++controller state
    --      vs public state
    input: sf, symbol, args_kwargs_mpair4get, args4call, kwargs4call
    cls = __class__ = type(sf) -> mro-search-registered?
    result = register.call(cls, symbol, tmay_sf, args_kwargs_mpair4get, *args4call, **kwargs4call)
    None|(args4get, kwargs4get) = (args_kwargs_mpair4get)
    method = register.get(cls, symbol, tmay_sf, *args4get, **kwargs4get)
        (interpreter) = register._get0(symbol)
        (whole_state) = register._get1(cls, symbol)
        whole_state{.controller_state4interpreter, .private_state4hierarchy_further_register, .private_state4instance, .public_state4instance_query}
        method = interpreter(controller_state4interpreter).get(cls, symbol, tmay_sf, *args4get, **kwargs4get)
        result = method(cls, symbol, tmay_sf, *args4get, **kwargs4get)(*args4call, **kwargs4call)
    #
    symbol :: ref_key
    hashable = (symbol|value_key) = (ref_key|value_key)
    symbol_leading_path = (symbol, [hashable])
        ???weakable
        ???ref/val
        ???list/dict
    symbol_rooted_tree<x> = (symbol, xchildren<x>)
    hashable_tree<x> = (hashable, xchildren<x>)
    xchildren<x{weighted=False}> = None|bool|{hashable_tree<x>}
        #None - leaf
        #bool - naming a subtree
        #   False - check if default #be override
        #   True - check always
    xchildren<x{weighted=True}> = ((None|bool), weight)|{hashable_tree<x>}
    symbol->impl ?or? symbol_leading_path->impl
    register4api_group(api_group, super_api_groups, extra_symbols/extra_symbol_rooted_trees, symbol_subset2checker/symbol_rooted_tree_subset2checker)
        symbol2api_group
    register4py_cls(py_cls, api_groups, symbol2impl)

#'''
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):

#TAIL_FOR_WRITING
