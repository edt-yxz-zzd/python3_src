{-# LANGUAGE TypeFamilies #-}

{-
e ../../python3_src/haskell_src/PureTypeSystem.hs

相等扌:欤子类扌:
    原表达式
    ++地址/addr/id，最终值
    ++类型，语境/映射纟变量冫类型辻鬽值
    ++集合纟自由变量/外赋变量集合

runghc ../../python3_src/haskell_src/PureTypeSystem.hs

$ ghci
Prelude> :info Applicative
Prelude> :info Monad
Prelude> :info Functor
class Functor f => Applicative f where
  pure :: a -> f a
  (<*>) :: f (a -> b) -> f a -> f b
  GHC.Base.liftA2 :: (a -> b -> c) -> f a -> f b -> f c
  (*>) :: f a -> f b -> f b
  (<*) :: f a -> f b -> f a
  {-# MINIMAL pure, ((<*>) | liftA2) #-}
class Applicative m => Monad m where
  (>>=) :: m a -> (a -> m b) -> m b
  (>>) :: m a -> m b -> m b
  return :: a -> m a
  {-# MINIMAL (>>=) #-}
type Functor :: (* -> *) -> Constraint
class Functor f where
  fmap :: (a -> b) -> f a -> f b
  (<$) :: a -> f b -> f a
  {-# MINIMAL fmap #-}


view ../lots/NOTE/PTS/ECC.txt
    view ../lots/NOTE/PTS/impredicativity.txt
    Universe0===Prop===(the-only-one-impredicativity-Universe)
    ===
    impredicativity:涉及『自指』
        [@[a::uX::uI] -> (o::uO)  ::  uX]
        uX既是 输入类型，同时也是 对象全集
        构造规则(uI,uO,uX)里[uI>uX]
          导致uX可能成为输入类型
          导致输入a可能是函数自身
          导致递归调用
    predicativity:不涉及『自指』
        对象全集 不含 自身
        [@[a::i::uX] -> (o::uX)  ::  uX]
        [{输入类型i,输出类型o,函数类型(@[a::i] -> o)} |<| 对象全集uX]并且三者没有一个是uX
    1.比较:(X::UniverseK) vs ((@[mkR:: X -> Universe0] -> (@[x::X] -> mkR x) -> mkR x)::Universe0)
      将全部X包装成右侧形式，岂非全成了Universe0的对象/元素？
      似乎没有区别:??有区别??:
        非Universe的类型:似乎没有毛病
        Universe被包装后，...??
      主要是: 高阶函数 存在 ==>> 高层宇宙
      高层宇宙 只起辅助作用，最终结果 只能 落在Universe0/命题宇宙 (即使 最终结果 仍旧包含了 高层对象)

grep pow -i -r '../lots/NOTE/Type Theory and Formal Proof -- An Introduction (2014)(Rob Nederpelt)/'
view ../lots/NOTE/PTS/构造冫最简单的悖论.txt


view ../lots/NOTE/PTS/concrete PTSs.txt
    规则:(u,0,0)
    规则:(u,v,max{u,v})
view ../lots/NOTE/PTS/idea - exists is not pair.txt
  ==>>PairT分离出AnyT(即Some/Exists)
    ==>>FuncT分离出AllT


-}


-- import Set (Set)

main = print "ok"

-- type Identifier = String
type Level = UInt
type FreshID = UInt
type UInt = Integer


-- newtype Identifier4PTS nm = ID (FreshID, nm)
newtype Context4PTS nm a
  -- = Cxt (FreshID, a)
  = Cxt (FreshID -> (FreshID, a))
    -- fresh_id to mk Var
-- newtype WithAddr fresh_id obj = WithAddr (fresh_id, obj)
newtype ExprWithAddr cxt fresh_id identifier
  = MkExprWithAddr (fresh_id, Expr4PTS cxt (ExprWithAddr cxt fresh_id identifier) identifier)
-- data Validated = Yet | Ok | Bad
data Expr4PTS cxt expr identifier
  -- data Expr4PTS u identifier
  = Var identifier
  | Universe Level  -- UInteger
  -- | Universe (Set u) Level
    -- 不太行: 得组合:子类与对象这两种情况:[uX <: uY][uX :: uY]
    -- <<==:
    -- Universe 真子宇宙集/(Set u) 自提数/Level
    -- [Universe 真子宇宙集 自提数 =[def]= ...]
    -- [Universe 真子宇宙集 (自提数+1) =[def]= (Universe 真子宇宙集 自提数)+1]
    -- [Universe 真子宇宙集 0 =[def]= (Universe 真子宇宙集 自提数)+1]
    -- [(某宇宙+1) =[def]= Gen{某宇宙, *某宇宙}] #即多了个生成元
    -- [某宇宙 <- (某宇宙+1)]
    -- [[子宇宙 <- 父宇宙.真子宇宙集] -> [(子宇宙+1) <- 父宇宙]]
    -- [[表达式丙 <- 宇宙乙] -> [宇宙乙 <- 宇宙甲] -> [表达式丙 <- 宇宙甲]]
    -- (某宇宙+1) 包含 某宇宙
  -- | Typing Validated expr expr
  | Typing expr expr
    -- [obj :: typ]
  | Func identifier expr (expr -> cxt expr)
    -- [\[i::T] -> B i]
  | Pair identifier expr (expr -> cxt expr)
    -- [(x, y)]
    -- [(i:=x, B i)]
  | Any identifier expr (expr -> cxt expr)
  | All identifier expr (expr -> cxt expr)
  | FuncT identifier expr (expr -> cxt expr)
    -- [I -> O]
    -- [@[i::T] -> B i]
    -- [@[i::T]. B i]
    -- xxx -- [(@[i::T::uI] -> (B i)::uO) :: (if uO==Universe0 then Universe0 else max{uI,uO})]
    -- 现:分离出:All,只剩下:
    -- [(@[i::T::uI] -> (B i)::uO) :: (max{uI,uO})]
  | PairT identifier expr (expr -> cxt expr)
    -- [(X, Y)]
    -- [(?[i::T], B i)]
    -- [?[i::T]. B i]
    -- [?[i::T] -> B i]
    -- xxx -- [@[R :: @[i::T] -> @[b::B i] -> ??Universe??] -> @[f :: @[i::T] -> @[b::B i] -> R i b] -> R i b]
    -- [?@[i::T::uI] -> (B i)::uO) :: (max{uI,uO})]
    --      !! fst,snd
  -- | Some identifier expr (expr -> cxt expr)
  | AnyT identifier expr (expr -> cxt expr)
    -- <==> [(@[R :: (@[a::T] -> @[b::B a] -> Universe0)] -> @[f :: @[a::T] -> @[b::B a] -> R a b] -> R a b) :: Universe0]
    --      重点是:
    --      * Universe0是最小的宇宙，即Prop命题宇宙
    --      * Any不是PairT，没有fst,snd
  | AllT identifier expr (expr -> cxt expr)
    -- [(@[i::T::uI] -> (B i)::Universe0) :: Universe0]
  | CallFunc expr expr
    -- [f :: @ ...]
    -- e.g. [f == \ ... or Var or (another call)...]
  | CallAny expr expr
    -- [f :: Any ...]
  | CallAll expr expr
    -- [f :: All ...]
  | CallFuncT expr expr
    -- [f :: Universe...]
    -- [f == @ ...]
  | CallPairT expr expr
    -- [f :: Universe...]
    -- [f == ? ...]
    -- 但没有:CallPair <<==snd 的 x 已被替换成fst
  | CallAnyT expr expr
    -- [f :: Universe...]
    -- [f == Any ...]
  | CallAllT expr expr
    -- [f :: Universe...]
    -- [f == All ...]
  | Fst expr
    -- fst pair
  | Snd expr
    -- snd pair



class Monad m => Context m where
    type Expr m :: *
    type Identifier m :: *
    get_fresh_Var :: (Identifier m) -> m (Expr m)
        -- state-Monad
    type_of :: (Expr m) -> m (Expr m)
        -- type(arg0)
    validate_subtype :: (Expr m) -> (Expr m) -> m Bool
        -- validate:[arg0/subtyp <: arg1/typ]
    validate_Typing :: (Expr m) -> (Expr m) -> m Bool
        -- validate Typing:[arg0/obj :: arg1/typ]
    mk_Typing :: (Expr m) -> (Expr m) -> m (Expr m)
        -- assertion or type_cast
        -- [arg0/obj :: arg1/typ]
    mk_Universe :: Level -> m (Expr m)
        -- Universe0..
    -- arg0:(Identifier m) is hint to form concrete syntax tree #not part of AST
    mk_Func :: (Identifier m) -> (Expr m) -> ((Expr m) -> m (Expr m)) -> m (Expr m)
        -- \[var::arg1] -> arg2 var
        -- arg1: input_type from:[var :: input_type]
        -- arg2: \var -> body
          -- using get_fresh_Var

    mk_Pair :: (Identifier m) -> (Expr m) -> ((Expr m) -> m (Expr m)) -> m (Expr m)
        -- (var:=arg1, arg2 var)
        -- arg1: fst pair
        -- arg2: \var -> snd pair
          -- using get_fresh_Var
    mk_Any :: (Identifier m) -> (Expr m) -> ((Expr m) -> m (Expr m)) -> m (Expr m)
        -- xxx vivi. mk_Pair
        -- (\R -> \[f::(@[var::type(arg1)] -> [b::type(arg2 var)] -> R a b)] -> f arg1 (arg2 arg1))
    mk_All :: (Identifier m) -> (Expr m) -> ((Expr m) -> m (Expr m)) -> m (Expr m)
        -- vivi. mk_Func
        -- \[var::arg1] -> arg2 var


    mk_FuncT :: (Identifier m) -> (Expr m) -> ((Expr m) -> m (Expr m)) -> m (Expr m)
        -- &[var::arg1] -> arg2 var
    mk_PairT :: (Identifier m) -> (Expr m) -> ((Expr m) -> m (Expr m)) -> m (Expr m)
        -- %[var::arg1] -> arg2 var
    mk_AnyT :: (Identifier m) -> (Expr m) -> ((Expr m) -> m (Expr m)) -> m (Expr m)
        -- xxx vivi. mk_PairT
        -- ?[var::arg1] -> arg2 var
        -- <==>:
        -- (@R -> (@[var::arg1] -> [b::arg2 var] -> R a b) -> R a b)::Universe0
    mk_AllT :: (Identifier m) -> (Expr m) -> ((Expr m) -> m (Expr m)) -> m (Expr m)
        -- vivi. mk_FuncT
        -- (@[var::arg1] -> arg2 var)::Universe0

    -- call/apply:
    fst_Pair :: (Expr m) -> m (Expr m)
      -- (fst pair)
    snd_Pair :: (Expr m) -> m (Expr m)
      -- (snd pair)
    call_Func :: (Expr m) -> (Expr m) -> m (Expr m)
        -- (arg0 arg1)
        -- (arg0 :: &[...]...)
    call_Any :: (Expr m) -> (Expr m) -> m (Expr m)
        -- (arg0 arg1)
        -- (arg0 :: ?[...]...)
    call_All :: (Expr m) -> (Expr m) -> m (Expr m)
        -- (arg0 arg1)
        -- (arg0 :: @[...]...)
    --没有call_Pair
    call_PairT :: (Expr m) -> (Expr m) -> m (Expr m)
        -- (arg0 arg1)
        -- (arg0 == %[...]...)
    call_FuncT :: (Expr m) -> (Expr m) -> m (Expr m)
        -- (arg0 arg1)
        -- (arg0 == &[...]...)
    call_AnyT :: (Expr m) -> (Expr m) -> m (Expr m)
        -- (arg0 arg1)
        -- (arg0 == ?[...]...)
    call_AllT :: (Expr m) -> (Expr m) -> m (Expr m)
        -- (arg0 arg1)
        -- (arg0 == @[...]...)

--end:class Monad m => Context m where


instance Functor (Context4PTS nm) where
    fmap a2b (Cxt i2i_a) = Cxt (\fresh_id ->
        fmap a2b (i2i_a fresh_id)
        )
instance Applicative (Context4PTS nm) where
    pure a = return a
    -- (Cxt i2i_a2b) <*> (Cxt i2i_a)
    mf <*> ma = do
        f <- mf
        a <- ma
        return (f a)
instance Monad (Context4PTS nm) where
    return a = Cxt (\fresh_id -> (fresh_id, a))
    ma >>= a2mb = Cxt (\fresh_id4ma ->
        let Cxt f4ma = ma
            (fresh_id4mb, a) =  f4ma fresh_id4ma
            Cxt f4mb = a2mb a
        in  f4mb fresh_id4mb
        )

_get_fresh_id :: (Context4PTS nm FreshID)
_get_fresh_id = Cxt (\fresh_id -> (fresh_id+1, fresh_id))
_wrap :: (Expr4PTS (Context4PTS nm) (Expr (Context4PTS nm)) (Identifier (Context4PTS nm))) -> (Context4PTS nm (Expr (Context4PTS nm)))
_wrap expr = do
    fresh_id <- _get_fresh_id
    return $ MkExprWithAddr (fresh_id, expr)

_mcat :: Monad m => m (m a) -> m a
_mcat mma = do
    ma <- mma
    ma
-- _hm_lift :: Monad m => (a -> m b) -> m (a->b)
-- _hm_lift a2mb = ...impossible!!!
-- _hm_rcall :: Monad m => (a -> m b) -> ((a->b) -> m c) -> m c
-- _hm_rcall a2mb a2bZmc


{-
mk_Func :: (Identifier m) -> (Expr m) -> ((Expr m) -> m (Expr m)) -> m (Expr m)
mk_Func var typ4var var2m_body = _wrap $ Func var typ4var var2m_body
| Func identifier expr (expr -> cxt expr)
-}
-- ==>>:
_mk__mk_Xxx
  -- :: ((Identifier m) -> (Expr m) -> ((Expr m) -> m (Expr m)) -> ???)
  -- -> ((Identifier m) -> (Expr m) -> ((Expr m) -> m (Expr m)) -> m (Expr m))
  :: (e0 -> m_e1)
  -> (a -> b -> c -> e0)
  -> (a -> b -> c -> m_e1)
_mk__mk_Xxx e02m_e1 abc2e0 a b c = e02m_e1 $ abc2e0 a b c
_mk__mk_Yyy
  :: (e0 -> m_e1)
  -> (a -> b -> e0)
  -> (a -> b -> m_e1)
_mk__mk_Yyy e02m_e1 ab2e0 a b = e02m_e1 $ ab2e0 a b

instance Context (Context4PTS nm) where
    -- type Expr (Context4PTS nm) = (ExprWithAddr (Context4PTS nm) FreshID (Identifier (Context4PTS nm)))
      -- The type family application ‘Identifier (Context4PTS nm)’
      --    is no smaller than the instance head ‘Expr (Context4PTS nm)’
      --    (Use UndecidableInstances to permit this)
    type Expr (Context4PTS nm) = (ExprWithAddr (Context4PTS nm) FreshID nm)
    type Identifier (Context4PTS nm) = nm
    get_fresh_Var nm = do
        fresh_id <- _get_fresh_id
        -- return $ MkExprWithAddr (fresh_id, Var (ID (fresh_id, nm)))
        return $ MkExprWithAddr (fresh_id, Var nm)
    type_of = type_of__Context4PTS
    validate_subtype = validate_subtype__Context4PTS
    validate_Typing obj typ = do
        subtyp <- type_of obj
        validate_subtype subtyp typ
    mk_Typing obj typ = _wrap $ Typing obj typ
    mk_Universe level = _wrap $ Universe level
    -- mk_Func var typ4var var2m_body = _wrap $ Func var typ4var var2m_body
    mk_Func = _mk__mk_Xxx _wrap Func
    mk_Pair = _mk__mk_Xxx _wrap Pair
    mk_Any = _mk__mk_Xxx _wrap Any
    mk_All = _mk__mk_Xxx _wrap All

    mk_FuncT = _mk__mk_Xxx _wrap FuncT
    mk_PairT = _mk__mk_Xxx _wrap PairT
    mk_AnyT = _mk__mk_Xxx _wrap AnyT
    mk_AllT = _mk__mk_Xxx _wrap AllT

    fst_Pair = _wrap . Fst
    snd_Pair = _wrap . Snd
    call_Func = _mk__mk_Yyy _wrap CallFunc
    call_Any = _mk__mk_Yyy _wrap CallAny
    call_All = _mk__mk_Yyy _wrap CallAll
    --没有call_Pair
    call_PairT = _mk__mk_Yyy _wrap CallPairT
    call_FuncT = _mk__mk_Yyy _wrap CallFuncT
    call_AnyT = _mk__mk_Yyy _wrap CallAnyT
    call_AllT = _mk__mk_Yyy _wrap CallAllT



validate_subtype__Context4PTS = undefined
type_of__Context4PTS = undefined

















    原表达式
    ++地址/addr/id，最终值
    ++类型，语境/映射纟变量冫类型辻鬽值
    ++集合纟自由变量/外赋变量集合


data WExpr
    -- ++额外信息:地址
    = Kind UInt
    | WExpr
    {original_expr :: MExpr
    ,expr_id :: UInt
    ,expr_value :: VExpr
    ,expr_type :: WExpr
    ,expr_context :: Map VarName VarInfo
    ,free_vars :: Set VarName
    }

{-
data MExpr
    -- no Kind
    = MExpr__apply WExpr WExpr
    | MExpr__nexpr NExpr
newtype NExpr = VExpr_ MExpr
newtype VExpr = VExpr_ VExpr
data ApplyVar
    = ApplyVar__echo
    | ApplyVar__fst
    | ApplyVar__snd
data VExpr__var_apply_ nexpr
    -- no Kind
    -- apply --> (apply var ...)/(apply fst/snd var/(var ...) ...)
    = VExpr__apply__var {apply_case :: ApplyVar, var_name :: VarName, var_type :: WExpr, arg4apply :: WExpr}
    | VExpr__apply__ext {func4apply :: VExpr__var_apply_ nexpr, arg4apply :: WExpr}
    | VExpr__typecast {nexpr :: VExpr__var_apply_ nexpr, wtype :: WExpr}
data VExpr_ nexpr
    = VExpr__typecast
    | VExpr__typecast {nexpr :: WExpr, wtype :: WExpr}
    | VExpr__function FuncInfo
-}

--newtype VExpr = VExpr MExpr
type VExpr = (YExpr_ AExpr)
    -- no Kind
    -- ++apply --> (var ...)/(fst/snd var/(var ...) ...)
    -- 主构造器冫对象终值
type MExpr = (YExpr_ WExpr)
    -- no Kind
    -- 主构造器冫表达式
data YExpr_ xExpr
    -- no Kind
    = YExpr__apply (AExpr_ xExpr)
    | YExpr__func FuncCase FuncInfo
    | YExpr__pair PairCase PairInfo
    -- | YExpr__typecast {expr8obj :: YExpr_ xExpr, expr8typ :: WExpr}
newtype AExpr = AExpr (AExpr_ AExpr)
data AExpr_ xExpr
    -- no Kind
    = AExpr__apply xExpr WExpr
    | AExpr__apply__fst xExpr
    | AExpr__apply__snd xExpr
    -- | AExpr__typecast {expr8obj :: xExpr, expr8typ :: WExpr}
    | AExpr__var VarName WExpr
data PairCase
    = PairObj
    | SomeObj
data FuncCase
    = FuncObj
    | FuncTyp
    | AllObj
    | AllTyp
    | PairTyp
    | SomeTyp
data FuncInfo = FuncInfo {param_name :: VarName, param_type :: WExpr, func_body :: WExpr}
data PairInfo = PairInfo {fst_param :: VarName, fst_obj :: WExpr, snd_obj :: WExpr}
newtype VarName
    = VarName (String, UInt)
data VarInfo
    = VarInfo__typ WExpr
        -- type
    = VarInfo__obj WExpr
        -- value --> (type, value)




