{-# LANGUAGE KindSignatures #-}



{-
e ../../python3_src/haskell_src/Framework4Translation__Adjustable.hs
view ../../python3_src/haskell_src/Framework4Translation.hs
runghc ../../python3_src/haskell_src/Framework4Translation__Adjustable.hs

-}
module Framework4Translation__Adjustable
    (AdjustableALLEqv(..)
    ,AdjustableEqv0(..)
    ,AdjustableEqv1(..)
    ,AdjustableEqv2(..)
    ,AdjustableEqv3(..)
    )
where


main = print "ok"

data Zzz st :: *
    -- Zzz仅限用于确认纯虚函数集合
newtype New hp st = New (hp st)
unbox__New (New a) = a
--instance Functor New where
--    fmap f = fmap__New $ f
fmap__New :: (hp x -> hp y) -> New hp x -> New hp y
fmap__New f = fmap__New $ f


class (AdjustableEqv0 hp, AdjustableEqv1 hp, AdjustableEqv2 hp, AdjustableEqv3 hp) => AdjustableALLEqv (hp :: * -> *) where
instance AdjustableALLEqv Zzz where


--class Adjustable (hp :: * -> *) where
class AdjustableEqv0 (hp :: * -> *) where
    -- 1. 提取参数:遍历/迭代树节点，并挑选出所需节点O(N)
    --      但是由于次序固定，还需进一步处理:调整次序，复制重复项，将线性结构变更为树状结构
    -- 2. 先变成均衡二叉树，再直接定位节点:O(NlogN)
    -- 2.1. 变成均衡二叉树O(N)
    -- 2.2. 直接定位节点:O(NlogN)

    -- 1. 提取参数:遍历/迭代树节点，并挑选出所需节点O(N)
    -- begin with (hp st)
    -- pushE_L1_2 :: hp st -> hp ((), st)
    initE :: hp st -> hp ((), st)
        -- need () #empty node
        -- __init__ --> (lnkls, tree)
        -- begin of select nodes
    -- copy1_2 :: hp st -> hp (st, st)
    initW :: hp st -> hp (st, st)
        -- donot need () #empty node
        -- __init__ --> (lnkls, tree)
        -- begin of select nodes
    push_tree :: hp (lnkls, tree) -> hp ((lnkls, tree), tree)
        -- need root_node
    -- popR2_1 :: hp (lnkls, tree) -> hp lnkls
    pop_tree :: hp (lnkls, tree) -> hp lnkls
        -- donot need root_node
        -- end of select nodes
        -- end with (hp lnkls)
    push_childL :: hp (lnkls, (childL, childR)) -> hp ((lnkls, childL), (childL, childR))
        -- need left_child-node
    enter_childL :: hp (lnkls, ((a, b), childR)) -> hp (lnkls, (a, (b, childR)))
        -- need children of left_child
    enter_childR :: hp (lnkls, (childL, childR)) -> hp (lnkls, childR)
        -- donot need left_child
        -- maybe need right_child
        -- reduce to tree case

    -- 2. 先变成均衡二叉树，再直接定位节点:O(NlogN)
    -- 2.1. 变成均衡二叉树O(N)
    -- begin with (hp lnkls)
    -- begin with (hp (lnkls, top))
    -- begin with (hp (lnkls, tree_lnkls))
    -- begin with (hp (lnkls/leftIO, tree_lnkls/rightIO))
    move_topL :: hp ((lnkls, top), tree_lnkls) -> hp (lnkls, (top, tree_lnkls))
    mk_treeR2 :: hp (lnkls, (a, (b, tree_lnkls))) -> hp (lnkls, ((a, b), tree_lnkls))
    mk_treeL1 :: hp (a, (b, tree_lnkls)) -> hp ((a, b), tree_lnkls)
        -- end of mk balanced tree
        -- end with (hp balanced_tree)


    -- 2.2. 直接定位节点:O(NlogN)
    -- begin0 with (hp balanced_tree)
    -- init begin0 with (hp balanced_tree)
    -- loop begin2 with (hp arged_balanced_tree)
    -- !! copy1_2/initW :: hp st -> hp (st, st)
    -- init begin1 with (hp (balanced_tree, balanced_tree))
    -- loop begin3 with (hp (arged_balanced_tree, arged_balanced_tree))
    chooseLW :: hp ((childL, childR), balanced_tree) -> hp (childL, balanced_tree)
        -- (left, whole)
    chooseRW :: hp ((childL, childR), balanced_tree) -> hp (childR, balanced_tree)
        -- (right, whole)
        -- middle1 :: hp (arg, balanced_tree)
        -- middle1 :: hp (arg_lnkls, balanced_tree)
        -- middle1 :: hp arged_balanced_tree
        -- !! apply again
        -- middle2 :: hp (arg, arged_balanced_tree)
        -- middle2 :: hp (arg, (arg_lnkls, balanced_tree))
    push_argL_RLR :: hp (arg, (arg_lnkls, balanced_tree)) -> hp ((arg_lnkls, arg), balanced_tree)
        -- middle3==middle1 :: hp arged_balanced_tree
        -- end0 with (hp arged_balanced_tree)
        -- end0 with (hp (arg_lnkls, balanced_tree))
        -- !! popR2_1/pop_tree
        -- end1 with (hp arg_lnkls)
    -- end with (hp arg_lnkls)
    -- end of mk arg_lnkls
    -- !! 能:变成均衡二叉树
    -- => 能:变成任意树(保持元素次序不变)
    -- end of mk new_st
    -- end of adjustment


    {-
    -- 等价操作包=>所需要的操作包
    initE :: hp a -> hp ((), a)
    initW :: hp a -> hp (a, a)
    push_tree :: hp (a, b) -> hp ((a, b), b)
    pop_tree :: hp (a, b) -> hp a
    push_childL :: hp (a, (b, c)) -> hp ((a, b), (b, c))
    enter_childL :: hp (a, ((b, c), d)) -> hp (a, (b, (c, d)))
    enter_childR :: hp (a, (b, c)) -> hp (a, c)
    move_topL :: hp ((a, b), c) -> hp (a, (b, c))
    mk_treeR2 :: hp (a, (b, (c, d))) -> hp (a, ((b, c), d))
    mk_treeL1 :: hp (a, (b, c)) -> hp ((a, b), c)
    chooseLW :: hp ((a, b), c) -> hp (a, c)
    chooseRW :: hp ((a, b), c) -> hp (b, c)
    push_argL_RLR :: hp (a, (b, c)) -> hp ((b, a), c)
    -}
-- end-class AdjustableEqv0






instance AdjustableEqv0 Zzz where
    -- Zzz仅限用于确认纯虚函数集合
    -- :.+1,.+15s/ :: .*/ = undefined
    initE = undefined
    initW = undefined
    push_tree = undefined
    pop_tree = undefined
    push_childL = undefined
    enter_childL = undefined
    enter_childR = undefined
    move_topL = undefined
    mk_treeR2 = undefined
    mk_treeL1 = undefined
    chooseLW = undefined
    chooseRW = undefined
    push_argL_RLR = undefined

instance AdjustableEqv0 hp => AdjustableEqv3 (New hp) where
    wpush_w = fmap__New $ initW
    o2w = fmap__New $ pop_tree . chooseRW . initW
    opushE = fmap__New $ move_topL . pop_tree . push_childL . chooseRW . initW . initE
    oswap_oR = fmap__New $ move_topL . move_topL . pop_tree . push_argL_RLR . chooseLW . chooseRW . chooseRW . initW . push_argL_RLR . chooseRW . chooseRW . chooseRW . initW . chooseLW . initW . mk_treeL1
    opack_oR = fmap__New $ enter_childL

class AdjustableEqv1 (hp :: * -> *) where
    -- 等价操作包
    --修改最右侧
    -- 单参数
    pop1_0 :: hp a -> hp ()
    pop1_0 = popL2_1 . pushE_R1_2
    copy1_2 :: hp a -> hp (a, a)
    -- copy1_2 = popL2_1 . pushB_RR2_12 . pushE_L1_2
    pushE_R1_2 :: hp a -> hp (a, ())
    pushE_L1_2 :: hp a -> hp ((), a)
    pushE_L1_2 = swap2_2 . pushE_R1_2
    -- 双参数
    swap2_2 :: hp (a, b) -> hp (b, a)
    swap2_2 = popL2_1 . swapR12_12 . copy1_2
    popR2_1 :: hp (a, b) -> hp a
    popR2_1 = popL2_1 . swap2_2
    popL2_1 :: hp (a, b) -> hp b
    -- popL2_1 = popR2_1 . swap2_2
    pushE_RR2_12 :: hp (a, b) -> hp (a, (b, ()))
    pushE_RR2_12 = moveM21_12 . pushE_R1_2
    pushA_RR2_12 :: hp (a, b) -> hp (a, (b, a))
    pushA_RR2_12 = swap2_2 . moveM12_21 . pushB_RR2_12 . swap2_2
    pushB_RR2_12 :: hp (a, b) -> hp (a, (b, b))
    pushB_RR2_12 = moveM21_12 . getB2_21
    getA2_21 :: hp (a, b) -> hp ((a, b), a)
    getA2_21 = popR12_11 . copy1_2
    getB2_21 :: hp (a, b) -> hp ((a, b), b)
    getB2_21 = popM12_11 . copy1_2
    --- lr_ - get from childL push childR.right_end
    lr_getL_pushR_R_2_12 :: hp (a, b) -> hp (a, (b, a))
    lr_getL_pushR_R_2_12 = pushA_RR2_12
    -- 三参数
    swapL21_21 :: hp ((a, b), c) -> hp ((b, a), c)
    swapL21_21 = swap2_2 . swapR12_12 . swap2_2
    swapR12_12 :: hp (a, (b, c)) -> hp (a, (c, b))
    swapL12_12 :: hp (a, (b, c)) -> hp (b, (a, c))
    swapL12_12 = swap2_2 . moveM12_21 . swapR12_12
    swapR21_21 :: hp ((a, b), c) -> hp ((a, c), b)
    swapR21_21 = moveM12_21 . swapR12_12 . moveM21_12
    popL21_11 :: hp ((a, b), c) -> hp (b, c)
    popL21_11 = swap2_2 . popM12_11 . swap2_2
    popR12_11 :: hp (a, (b, c)) -> hp (a, b)
    popR12_11 = popR2_1 . moveM12_21
    popM21_11 :: hp ((a, b), c) -> hp (a, c)
    popM21_11 = swap2_2 . popR12_11 . swap2_2
    popM12_11 :: hp (a, (b, c)) -> hp (a, c)
    popM12_11 = popR12_11 . swapR12_12

    moveM12_21 :: hp (a, (b, c)) -> hp ((a, b), c)
    moveM21_12 :: hp ((a, b), c) -> hp (a, (b, c))
    moveM21_12 = swapR12_12 . swapL12_12 . swap2_2
    copyM12_22 :: hp (a, (b, c)) -> hp ((a, b), (b, c))
    copyM12_22 = swapR21_21 . popR12_11 . getB2_21
    copyM21_22 :: hp ((a, b), c) -> hp ((a, b), (b, c))
    copyM21_22 = swapR12_12 . swap2_2 . swapR12_12 . copyM12_22 . swapR12_12 . swap2_2
    --- lr_ - get from childL push childR.right_end
    lr_getLL_pushR_R_2_12 :: hp ((a, b), c) -> hp ((a, b), (c, a))
    lr_getLL_pushR_R_2_12 = moveM21_12 . popR12_11 . getA2_21
    lr_getLR_pushR_R_2_12 :: hp ((a, b), c) -> hp ((a, b), (c, b))
    lr_getLR_pushR_R_2_12 = moveM21_12 . popM12_11 . getA2_21
    -- 四参数
    unpackM13_13 :: hp (a, ((b, c), d)) -> hp (a, (b, (c, d)))
    unpackM13_13 = moveM21_12 . swapR12_12 . moveM21_12 . popM12_11 . moveM12_21 . swapR12_12 . swapR21_21 . popR12_11 . popR12_11 . getB2_21
        -- swapR12_12 . moveM21_12 :: hp ((a, b), c) -> hp (a, (c, b))
        -- moveM21_12 . popR12_11 :: hp ((a, b), (c, d)) -> hp (a, (b, c))
        -- popR12_11 . swapR12_12 == popM12_11
        -- swapR12_12 . moveM12_21 :: hp (a, (b, (c, d))) -> hp ((a, b), (d, c))
        -- moveM12_21 . swapR12_12 :: hp (a, (b, c)) -> hp ((a, c), b)
        -- swapR21_21 . popR12_11
    unpackM31_31 :: hp ((a, (b, c)), d) -> hp (((a, b), c), d)
    unpackM31_31 = swap2_2 . packM13_13 . swap2_2
    packM13_13 :: hp (a, (b, (c, d))) -> hp (a, ((b, c), d))
    packM13_13 = swapR12_12 . moveM21_12 . moveM21_12 . popR12_11 . moveM12_21 . swapR21_21 . popM12_11 . popM12_11 . getB2_21
    packM31_31 :: hp (((a, b), c), d) -> hp ((a, (b, c)), d)
    packM31_31 = swap2_2 . unpackM13_13 . swap2_2


    {-
    -- 等价操作包=>所需要的操作包
    copy1_2 :: hp a -> hp (a, a)
    popL2_1 :: hp (a, b) -> hp b
    pushE_R1_2 :: hp a -> hp (a, ())
    swapR12_12 :: hp (a, (b, c)) -> hp (a, (c, b))
    moveM12_21 :: hp (a, (b, c)) -> hp ((a, b), c)

    -}
-- end-class AdjustableEqv1
instance AdjustableEqv1 Zzz where
    -- Zzz仅限用于确认纯虚函数集合
    -- :.+1,.+7s/ :: .*/ = undefined
    copy1_2 = undefined
    popL2_1 = undefined
    pushE_R1_2 = undefined
    swapR12_12 = undefined
    moveM12_21 = undefined




instance AdjustableEqv1 hp => AdjustableEqv0 (New hp) where
  -- instance AdjustableEqv1 hp => Adjustable hp where
    -- Illegal instance declaration for ‘Adjustable hp’
    --  (All instance types must be of the form (T a1 ... an)
    --   where a1 ... an are *distinct type variables*,
    --   and each type variable appears at most once in the instance head.
    --   Use FlexibleInstances if you want to disable this.)
    --
    --
    --
    --
    -- The constraint ‘AdjustableEqv1 hp’
    --  is no smaller than the instance head ‘Adjustable hp’
    --  (Use UndecidableInstances to permit this)
    --
    --
    --
    --
    -- Illegal type signature in instance declaration:
    --  initE :: hp a -> hp ((), a)
    --  (Use InstanceSigs to allow this)
    --
    --
    -- :.,.+32s/= \(.*\)$/= fmap__New $ \1
    --
    --
    -- 等价操作包=>所需要的操作包
    -- initE :: hp a -> hp ((), a)
    initE = fmap__New $ pushE_L1_2
    -- initW :: hp a -> hp (a, a)
    initW = fmap__New $ copy1_2
    -- push_tree :: hp (a, b) -> hp ((a, b), b)
    push_tree = fmap__New $ getB2_21
    -- pop_tree :: hp (a, b) -> hp a
    pop_tree = fmap__New $ popR2_1
    -- push_childL :: hp (a, (b, c)) -> hp ((a, b), (b, c))
    push_childL = fmap__New $ copyM12_22
    -- enter_childL :: hp (a, ((b, c), d)) -> hp (a, (b, (c, d)))
    enter_childL = fmap__New $ unpackM13_13
    -- enter_childR :: hp (a, (b, c)) -> hp (a, c)
    enter_childR = fmap__New $ popM12_11

    -- move_topL :: hp ((a, b), c) -> hp (a, (b, c))
    move_topL = fmap__New $ moveM21_12
    -- mk_treeR2 :: hp (a, (b, (c, d))) -> hp (a, ((b, c), d))
    mk_treeR2 = fmap__New $ packM13_13
    -- mk_treeL1 :: hp (a, (b, c)) -> hp ((a, b), c)
    mk_treeL1 = fmap__New $ moveM12_21


    -- chooseLW :: hp ((a, b), c) -> hp (a, c)
    chooseLW = fmap__New $ popM21_11
    -- chooseRW :: hp ((a, b), c) -> hp (b, c)
    chooseRW = fmap__New $ popL21_11
    -- push_argL_RLR :: hp (a, (b, c)) -> hp ((b, a), c)
    push_argL_RLR = fmap__New $ swapL21_21 . moveM12_21



class AdjustableEqv2 (hp :: * -> *) where
    -- stack ops
    -- getN, popN, moveN, reverseN, rotateN
    -- getM_N, popM_N, moveM_N, reverseM_N, rotateM_N
    -- (st, target)
    -- (st, (f, args))
    -- ((st, frame), target)
    -- (((code, memory), cache), register)
    -- (((constant, stack), frame), target)
    -- 数据流动方向:
    -- whole <-- target
    -- constant --> target
    -- stack <-> target
    -- cache <-> target
    -- target --> target
    init_CSFT_1 :: hp st -> hp ((((), st), st), ())
    setW :: hp (st, target) -> hp target
    clearW :: hp st -> hp ()
    clearW = setW . init_CSFT_1
    init_CSFT_2 :: hp (st, target) -> hp ((((), (st, target)), st), target)
    init_CSFT_2 = rpopLR_R . init_CSFT_1
    init_CSFT_3__full :: hp ((st, frame), target) -> hp ((((), ((st, frame), target)), frame), target)
    init_CSFT_3__full = rpopLR_R . rpopLR_L . rpackLR_R . init_CSFT_1
    init_CSFT_3__base :: hp ((st, frame), target) -> hp ((((), st), frame), target)
    init_CSFT_3__base = rpopLR_R . rpopLR_L . rpackLR_R . rpopLLR . rpopLLR . init_CSFT_1
        -- xxx:init_CSFT_3__base = rpopLLR . rpopLLR . init_CSFT_3__full

    -- register is used to access attribute
    -- rget... - register.get-and-replace-target
    rgetW :: hp (st, target) -> hp (st, (st, target))
    rgetRR :: hp (st, (childL, childR)) -> hp (st, childR)
    rgetRL :: hp (st, (childL, childR)) -> hp (st, childL)

    rgetL :: hp (st, target) -> hp (st, st)
    rgetL = rgetRL . rgetW
    rgetLR :: hp ((st, frame), target) -> hp ((st, frame), frame)
    rgetLR = rgetRR . rgetL
    rgetLL :: hp ((st, frame), target) -> hp ((st, frame), st)
    rgetLL = rgetRL . rgetL
    rgetLLR :: hp (((constant, stack), frame), target) -> hp (((constant, stack), frame), stack)
    rgetLLR = rgetRR . rgetLL
    rgetLLL :: hp (((constant, stack), frame), target) -> hp (((constant, stack), frame), constant)
    rgetLLL = rgetRL . rgetLL

    rsetL :: hp (st, target) -> hp (target, target)
    rsetLR :: hp ((st, frame), target) -> hp ((st, target), target)
    rsetLL :: hp ((st, frame), target) -> hp ((target, frame), target)
    rsetLLR :: hp (((constant, stack), frame), target) -> hp (((constant, target), frame), target)
    rsetLLL :: hp (((constant, stack), frame), target) -> hp (((target, stack), frame), target)


    rswapL :: hp (st, target) -> hp (target, st)
    rswapLR :: hp ((st, frame), target) -> hp ((st, target), frame)
    rswapLL :: hp ((st, frame), target) -> hp ((target, frame), st)
    rswapLLR :: hp (((constant, stack), frame), target) -> hp (((constant, target), frame), stack)
    rswapLLL :: hp (((constant, stack), frame), target) -> hp (((target, stack), frame), constant)


    -- 修改:target/register
    -- 构造:cache:遍历访问树:破坏性访问树/register,如需保存，暂存到stack
    rpushLLR :: hp (((constant, stack), frame), target) -> hp (((constant, (stack, target)), frame), target)
    rpopLLR :: hp (((constant, (stack, top)), frame), target) -> hp (((constant, stack), frame), top)

    rpushLR_R :: hp ((st, tree), target) -> hp ((st, (tree, target)), target)
    rpushLR_L :: hp ((st, tree), target) -> hp ((st, (target, tree)), target)
        -- rpushLLR/rpopLLR 保存 target 到 stack
        -- rgetRL/rgetRR 取出 子树
        -- 支持 前序树访问/中序树访问/后序树访问...从左往右/从右往左...

    rpackLR_R :: hp ((st, ((tree, x), y)), target) -> hp ((st, (tree, (x, y))), target)
    rpackLR_L :: hp ((st, (x, (y, tree))), target) -> hp ((st, ((x, y), tree)), target)
        -- LR - 双向栈
        -- 用于构造:树状结构
        -- 如:用于构造:均衡二叉树/balanced_tree

    rpopLR_R :: hp ((st, (tree, x)), target) -> hp ((st, tree), x)
    rpopLR_L :: hp ((st, (x, tree)), target) -> hp ((st, tree), x)
    rpopLR_L = rswapLR . rpopLR_R
        -- 相应于 rpushLR_R/rpushLR_L
        -- 可用于构造 hp (st, (x,y))
        --   先保存x到frame/cache:rpushLR_R=>(hp ((st, (tree, x)), x))
        --   再求y=>(hp ((st, (tree, x)), y))
        --   保存y到frame/cache:rpushLR_R=>(hp ((st, ((tree, x), y)), y))
        --   *之后方法1.
        --   打包xy于frame/cache:rpackLR_R=>(hp ((st, (tree, (x,y))), y))
        --   取出xy:rpopLR_R=>(hp ((st, tree), (x,y)))
        --   *之后方法2.
        --   rgetLR,...修改target...,rgetRR
        --
        -- 上面的方法太麻烦了=>rpopLLR_pushR_R

    runpackLR_R :: hp ((st, (tree, (x, y))), target) -> hp ((st, ((tree, x), y)), target)
    runpackLR_R = rpackLR_L
    runpackLR_L :: hp ((st, ((x, y), tree)), target) -> hp ((st, (x, (y, tree))), target)
    runpackLR_L = rpackLR_R
        -- 相应于 rpackLR_R/rpackLR_L

    -- 修改:target/register
    -- 先取出数据:rgetLR.../rswapLR.../
    -- 在register里修改后，再归位:rsetLR.../rswapLR...
    --
    --
    -- mix_get,mix_pop:数据混合，综合处理
    rpopLLR_pushR_R :: hp (((constant, (stack, top)), frame), target) -> hp (((constant, stack), frame), (target, top))
    rpopLR_R_pushR_R :: hp ((st, (tree, x)), target) -> hp ((st, tree), (target, x))
    rpopLR_L_pushR_R :: hp ((st, (x, tree)), target) -> hp ((st, tree), (target, x))

    rgetW_pushR_R :: hp (st, target) -> hp (st, (target, (st, target)))
    rgetL_pushR_R :: hp (st, target) -> hp (st, (target, st))
    rgetLR_pushR_R :: hp ((st, frame), target) -> hp ((st, frame), (target, frame))
    rgetLL_pushR_R :: hp ((st, frame), target) -> hp ((st, frame), (target, st))
    rgetLLR_pushR_R :: hp (((constant, stack), frame), target) -> hp (((constant, stack), frame), (target, stack))
    rgetLLL_pushR_R :: hp (((constant, stack), frame), target) -> hp (((constant, stack), frame), (target, constant))
    rgetRR_pushR_R :: hp (st, (x, y)) -> hp (st, ((x, y), y))
    rgetRL_pushR_R :: hp (st, (x, y)) -> hp (st, ((x, y), x))
        --  xxx --> fstR/sndR
    -- rgetR_pushR_R :: hp (st, target) -> hp (st, (target, target))
    --  --> copyR



    -- 修改:target/register
    -- 无关其余:
    --      要么经过mix_pop/mix_get而含有所有的所需数据
    --      要么多余数据太多，先进行删除/排序，之后再通过mix_pop/mix_get增加数据
    -- 前面已支持的方法: stack存放target父节点，frame构造树状结构，可得任意次序结构，似乎已无必要...只是 别名捷径...不对，除非 类型是CSFT(init_CSFT_1)
    clearR :: hp (st, target) -> hp (st, ())
    clearR = setW . rgetLR_pushR_R . rgetRL . rswapLR . init_CSFT_1
    copyR :: hp (st, target) -> hp (st, (target, target))
    copyR = setW . rgetLR . rpackLR_R . rpushLR_R . rpeekLR_R . init_CSFT_1
        -- copyR = setW . rgetLR . rpackLR_R . rpushLR_R . rpushLR_R . init_CSFT_2
    swapR :: hp (st, (x, y)) -> hp (st, (y, x))
    swapR = setW . rgetLR . rpackLR_R . rpushLR_R . rgetRL . rpopLLR . rpushLR_R . rgetRR . init_CSFT_2
        -- swapR = setW . rgetLR . rpackLR_R . rpushLR_R . rgetRL . rpopLLR . rpushLR_R . rgetRR . rpopLR_R . init_CSFT_1
        -- swapR = setW . rpopLR_R_pushR_R . rgetRL . rgetLLR . rpushLR_R . rpopLR_L_pushR_R . rpeekLR_R . rpopLR_L . init_CSFT_1
        -- swapR = setW . rgetLR . rpackLR_R . rpushLR_R . rpopLLR . rpushLR_R . rgetRR . rpopLR_R . rpushLLR . rgetRL . rpeekLR_R . init_CSFT_1
        --
    swapR_top2 :: hp (st, ((x, y), z)) -> hp (st, ((x, z), y))
    swapR_top2 = setW . rgetLR . rpackLR_R . rpushLR_R . rgetRR . rgetRL . rpopLLR . rpackLR_R . rpushLR_R . rgetRR . rpeekLLR . rpushLR_R . rgetRL . rgetRL . init_CSFT_2
        -- swapR_top2 = setW . rgetLR . rpackLR_R . rpushLR_R . rgetRR . rgetRL . rpopLLR . rpackLR_R . rpushLR_R . rgetRR . rpeekLLR . rpushLR_R . rgetRL . rgetRL . rpopLR_R . init_CSFT_1


    rpeekLLR :: hp (((constant, (stack, top)), frame), target) -> hp (((constant, (stack, top)), frame), top)
    rpeekLLR = rgetRR . rgetLLR
        -- rpeekLLR = rpushLLR . rpopLLR
    rpeekLR_R :: hp ((st, (tree, x)), target) -> hp ((st, (tree, x)), x)
    rpeekLR_R = rgetRR . rgetLR
    rpeekLR_L :: hp ((st, (x, tree)), target) -> hp ((st, (x, tree)), x)
    rpeekLR_L = rgetRL . rgetLR

    rpeekLLR_pushR_R :: hp (((constant, (stack, top)), frame), target) -> hp (((constant, (stack, top)), frame), (target, top))
    rpeekLLR_pushR_R = rpopLLR_pushR_R . rpopLR_R . rpushLLR . rpeekLLR . rpushLR_R

    rpeekLR_R_pushR_R :: hp ((st, (tree, x)), target) -> hp ((st, (tree, x)), (target, x))
    rpeekLR_R_pushR_R =  setW . rgetLR_pushR_R . rgetRL . rgetLLR . rsetLR . rpopLR_R_pushR_R . init_CSFT_3__full
    rpeekLR_L_pushR_R :: hp ((st, (x, tree)), target) -> hp ((st, (x, tree)), (target, x))
    rpeekLR_L_pushR_R =  setW . rgetLR_pushR_R . rgetRL . rgetLLR . rsetLR . rpopLR_L_pushR_R . init_CSFT_3__full


    -- getN, popN, moveN, reverseN, rotateN
    -- getM_N, popM_N, moveM_N, reverseM_N, rotateM_N





    {-
    -- 拆包 以便删除多余数据
    -- 已有:rgetRL/rgetRR:无需 popR_R
    swapR :: hp (st, (x, y)) -> hp (st, (y, x))
    swapR_top2 :: hp (st, ((x, y), z)) -> hp (st, ((x, z), y))
        -- to pop y
    clearR :: hp (st, target) -> hp (st, ())
    --单参数
    copyR :: hp (st, target) -> hp (st, (target, target))
    -- pushE_R1_2 :: hp a -> hp (a, ())
    pushR_R_E :: hp (st, target) -> hp (st, (target, ()))
    pushR_L_E :: hp (st, target) -> hp (st, ((), target))
    -- 双参数
    -- 已有:rgetRL/rgetRR
    -- 已有:rgetRL_pushR_R/rgetRR_pushR_R
    swapR :: hp (st, (x, y)) -> hp (st, (y, x))
    -- 三参数
    swapR_21_R :: hp (st, ((x, y), z)) -> hp ((x, z), y)
    -}


    {-
    -- 等价操作包=>所需要的操作包
    init_CSFT_1 :: hp st -> hp ((((), st), st), ())
    setW :: hp (st, target) -> hp target
    rgetW :: hp (st, target) -> hp (st, (st, target))
    rgetRR :: hp (st, (childL, childR)) -> hp (st, childR)
    rgetRL :: hp (st, (childL, childR)) -> hp (st, childL)
    rsetL :: hp (st, target) -> hp (target, target)
    rsetLR :: hp ((st, frame), target) -> hp ((st, target), target)
    rsetLL :: hp ((st, frame), target) -> hp ((target, frame), target)
    rsetLLR :: hp (((constant, stack), frame), target) -> hp (((constant, target), frame), target)
    rsetLLL :: hp (((constant, stack), frame), target) -> hp (((target, stack), frame), target)
    rswapL :: hp (st, target) -> hp (target, st)
    rswapLR :: hp ((st, frame), target) -> hp ((st, target), frame)
    rswapLL :: hp ((st, frame), target) -> hp ((target, frame), st)
    rswapLLR :: hp (((constant, stack), frame), target) -> hp (((constant, target), frame), stack)
    rswapLLL :: hp (((constant, stack), frame), target) -> hp (((target, stack), frame), constant)
    rpushLLR :: hp (((constant, stack), frame), target) -> hp (((constant, (stack, target)), frame), target)
    rpopLLR :: hp (((constant, (stack, top)), frame), target) -> hp (((constant, stack), frame), top)

    rpushLR_R :: hp ((st, tree), target) -> hp ((st, (tree, target)), target)
    rpushLR_L :: hp ((st, tree), target) -> hp ((st, (target, tree)), target)
    rpackLR_R :: hp ((st, ((tree, x), y)), target) -> hp ((st, (tree, (x, y))), target)
    rpackLR_L :: hp ((st, (x, (y, tree))), target) -> hp ((st, ((x, y), tree)), target)
    rpopLR_R :: hp ((st, (tree, x)), target) -> hp ((st, tree), x)
    rpopLLR_pushR_R :: hp (((constant, (stack, top)), frame), target) -> hp (((constant, stack), frame), (target, top))
    rpopLR_R_pushR_R :: hp ((st, (tree, x)), target) -> hp ((st, tree), (target, x))
    rpopLR_L_pushR_R :: hp ((st, (x, tree)), target) -> hp ((st, tree), (target, x))

    rgetW_pushR_R :: hp (st, target) -> hp (st, (target, (st, target)))
    rgetL_pushR_R :: hp (st, target) -> hp (st, (target, st))
    rgetLR_pushR_R :: hp ((st, frame), target) -> hp ((st, frame), (target, frame))
    rgetLL_pushR_R :: hp ((st, frame), target) -> hp ((st, frame), (target, st))
    rgetLLR_pushR_R :: hp (((constant, stack), frame), target) -> hp (((constant, stack), frame), (target, stack))
    rgetLLL_pushR_R :: hp (((constant, stack), frame), target) -> hp (((constant, stack), frame), (target, constant))
    rgetRR_pushR_R :: hp (st, (x, y)) -> hp (st, ((x, y), y))
    rgetRL_pushR_R :: hp (st, (x, y)) -> hp (st, ((x, y), x))

    -}
-- end-class AdjustableEqv2


instance AdjustableEqv2 Zzz where
    -- Zzz仅限用于确认纯虚函数集合
    -- :.+1,.+37s/ :: .*/ = undefined
    init_CSFT_1 = undefined
    setW = undefined
    rgetW = undefined
    rgetRR = undefined
    rgetRL = undefined
    rsetL = undefined
    rsetLR = undefined
    rsetLL = undefined
    rsetLLR = undefined
    rsetLLL = undefined
    rswapL = undefined
    rswapLR = undefined
    rswapLL = undefined
    rswapLLR = undefined
    rswapLLL = undefined
    rpushLLR = undefined
    rpopLLR = undefined

    rpushLR_R = undefined
    rpushLR_L = undefined
    rpackLR_R = undefined
    rpackLR_L = undefined
    rpopLR_R = undefined
    rpopLLR_pushR_R = undefined
    rpopLR_R_pushR_R = undefined
    rpopLR_L_pushR_R = undefined

    rgetW_pushR_R = undefined
    rgetL_pushR_R = undefined
    rgetLR_pushR_R = undefined
    rgetLL_pushR_R = undefined
    rgetLLR_pushR_R = undefined
    rgetLLL_pushR_R = undefined
    rgetRR_pushR_R = undefined
    rgetRL_pushR_R = undefined

instance AdjustableEqv2 hp => AdjustableEqv1 (New hp) where
    -- :.+1,.+18s/= \(.*\)$/= fmap__New $ \1
    {-
    pop1_0 :: hp a -> hp ()
    copy1_2 :: hp a -> hp (a, a)
    pushE_R1_2 :: hp a -> hp (a, ())
    swap2_2 :: hp (a, b) -> hp (b, a)
    popR2_1 :: hp (a, b) -> hp a
    swapR12_12 :: hp (a, (b, c)) -> hp (a, (c, b))
    moveM12_21 :: hp (a, (b, c)) -> hp ((a, b), c)
    -}
    -- pop1_0 = fmap__New $ clearW
    copy1_2 = fmap__New $ setW . rgetLR_pushR_R . rgetLR . init_CSFT_1
        -- copy1_2 = fmap__New $ setW . copyR . init_CSFT_2
    pushE_R1_2 = fmap__New $ setW . rgetLR . rpushLR_R . init_CSFT_1
    -- swap2_2 = fmap__New $ setW . rpopLR_L_pushR_R . rpeekLR_R . init_CSFT_1
    -- swap2_2 = fmap__New $ rswapL
        -- swap2_2 = fmap__New $ setW . swapR . init_CSFT_2
    -- popR2_1 = fmap__New $ setW . rgetL
    popL2_1 = fmap__New $ setW
    swapR12_12 = fmap__New $ swapR
    moveM12_21 = fmap__New $ setW . rgetLR . runpackLR_R . init_CSFT_1

class AdjustableEqv3 (hp :: * -> *) where
    -- 所有基础修改只发生于R/output/target，直接更新整个W
    --  其余修改函数只是高层功能函数(非基础)(有缺省具现)
    --
    -- o... - output/target
    -- w... - whole st
    wpush_w :: hp st -> hp (st, st)
        -- init
        -- 取第二参数前，先保存第一参数:wpush_w,wpush_o,wpush_wL
    o2w :: hp (st, o) -> hp o
        -- update
        -- end
    wpushE :: hp st -> hp (st, ())
    -- wpushE = oclear . wpush_w
    wpushE = o2w . opushE . wpush_w
    wpush_o :: hp (st, o) -> hp ((st, o), o)
    wpush_o = odel_oL . wpush_w
    wpush_wL :: hp (wL, o) -> hp ((wL, o), wL)
    wpush_wL = odel_oR . wpush_w
        -- to access attribute in wL/st, save o firstly
    wpack_o :: hp ((st, x), y) -> hp (st, (x, y))
    wpack_o = o2w . opack_oR . o5w
        -- 1. 用途其一
        -- 取:双参数:
        -- 流程:
        --  +先取第一参数:o5w,o5oL,o5oR
        --  +保存第一参数:wpush_w
        --  +再取第二参数:o5oL,o5oR
        --  +打包双参数:wpush_o
        -- === 之后就是变换o:如:排序o:得到目标『属性值』
        -- === 之后就是将『属性值』o插入相应位置:『o是属性值』=>o5w>>>『o是 属性值+散装的原对象』=>排序o>>>『o是新对象』=>o2w
        -- 2. 用途其二:构造树
        -- treat wLR as arg_lnkls
        -- wpush_w init wLR-arg_lnkls as [o]
        -- (wpush_w . (opack_oR .)* wpack_o)/(wpush_wL . (opack_oR .)* wpack_o) move o and push o into wLR-arg_lnkls as [wLR, o]
        -- #
    wunpack_o :: hp (st, (x, y)) -> hp ((st, x), y)
    wunpack_o = o2w . ounpack_oR . o5w
    -- wLR_push_o :: hp ((st, wLR), o) -> hp ((st, (wLR, o)), o)

    -- access attribute
    -- ？遍历树？:仅止于取特定节点。因为还没有 父树栈，所以不能遍历
    --      见上面:构造树:wpack_o
    o5w :: hp (st, o) -> hp (st, (st, o))
    o5w = o2w . oswap_o . wpush_w . o5oR . oswap_o . wpush_w
    o5oL :: hp (st, (oL, oR)) -> hp (st, oL)
    o5oL = o5oR . oswap_o
    o5oR :: hp (st, (oL, oR)) -> hp (st, oR)
    o5oR = o2w . o2w . oswap_oR . opack_oR . oswap_o . wpush_w
        -- 取:单参数
        -- 见上面:取:双参数:wpack_o

    opushE :: hp (st, o) -> hp (st, (o, ()))
    oclear :: hp (st, o) -> hp (st, ())
        -- *1. ??选择oclear而非wpushE
        --  !! 直接修改w纯虚函数的数量越少越符合设计目标:只能是wpush_w,o2w
        -- *2. ??但是，从单独功能的角度看，oclear构造叶节点并替换旧节点，导致部分元素重复数下降，这功能就不够明晰
        -- 现改用:++opushE
    oclear = o5oR . opushE
    _oclear :: hp (st, o) -> hp (st, ())
    -- _oclear = o2w . odel_oLR . wpush_w . wpushE
    _oclear = o5oL . o2w . oswap_oR . opack_oR . wpush_w . wpushE
        -- 假设:使用wpushE替换oclear作为纯虚函数
    odel_o :: hp (st, o) -> hp (st, ())
    odel_o = oclear
    odel_oR :: hp (st, (oL, oR)) -> hp (st, oL)
    odel_oR = o5oL
    odel_oL :: hp (st, (oL, oR)) -> hp (st, oR)
    odel_oL = o5oR

    oswap_o :: hp (st, (oL, oR)) -> hp (st, (oR, oL))
    oswap_o = o2w . oswap_oR . wpush_w
    oswap_oR :: hp (st, (oL, (oRL, oRR))) -> hp (st, (oL, (oRR, oRL)))
    oswap_oL :: hp (st, ((oLL, oLR), oR)) -> hp (st, ((oLR, oLL), oR))
    oswap_oL = oswap_o . oswap_oR . oswap_o
    oswap_top2_R :: hp (st, ((oLL, x), y)) -> hp (st, ((oLL, y), x))
    oswap_top2_R = ounpack_oR . oswap_oR . opack_oR
    oswap_top2_L :: hp (st, (x, (y, oRR))) -> hp (st, (y, (x, oRR)))
    oswap_top2_L = oreverse_21_12 . oswap_top2_R . oreverse_12_21
    oreverse_12_21 :: hp (st, (x, (oM, y))) -> hp (st, ((y, oM), x))
    oreverse_12_21 = oswap_o . oswap_oR
    oreverse_21_12 :: hp (st, ((x, oM), y)) -> hp (st, (y, (oM, x)))
    oreverse_21_12 = oswap_oR . oswap_o

    odel_oRR :: hp (st, (oL, (oRL, oRR))) -> hp (st, (oL, oRL))
    odel_oRR = o5oL . opack_oL
    odel_oRL :: hp (st, (oL, (oRL, oRR))) -> hp (st, (oL, oRR))
    odel_oRL = odel_oRR . oswap_oR
    odel_oLR :: hp (st, ((oLL, oLR), oR)) -> hp (st, (oLL, oR))
    odel_oLR = oswap_o . odel_oRR . oswap_o
    odel_oLL :: hp (st, ((oLL, oLR), oR)) -> hp (st, (oLR, oR))
    odel_oLL = oswap_o . odel_oRL . oswap_o


    opush_o :: hp (st, o) -> hp (st, (o, o))
    opush_o = o2w . opack_oR . odel_oRL . o5w . wpush_w

    opack_oR :: hp (st, ((x, oM), y)) -> hp (st, (x, (oM, y)))
    opack_oL :: hp (st, (x, (oM, y))) -> hp (st, ((x, oM), y))
    opack_oL = oswap_o . oswap_oR . opack_oR . oswap_o . oswap_oR
    ounpack_oL :: hp (st, ((x, oM), y)) -> hp (st, (x, (oM, y)))
    ounpack_oL = opack_oR
    ounpack_oR :: hp (st, (x, (oM, y))) -> hp (st, ((x, oM), y))
    ounpack_oR = opack_oL
    omove_oM_21_12 :: hp (st, ((x, oM), y)) -> hp (st, (x, (oM, y)))
    omove_oM_21_12 = opack_oR
    omove_oM_12_21 :: hp (st, (x, (oM, y))) -> hp (st, ((x, oM), y))
    omove_oM_12_21 = opack_oL



    -- 存取冫结果:returned_value
    wLpush_opop :: hp (st, (x, z))  -> hp ((st, z), x)
    -- wLpush_opop = o2w . omove_oM_12_21 . oswap_oR . wpush_w
    wLpush_opop = wunpack_o . oswap_o
    wLpop_opush :: hp ((st, z), x)  -> hp (st, (x, z))
    -- wLpop_opush = o2w . oswap_oR . omove_oM_21_12 . wpush_w
    wLpop_opush = oswap_o . wpack_o
    wLpush_oRpop :: hp (st, (x, (y, z)))  -> hp ((st, z), (x, y))
    -- wLpush_oRpop = wLpush_opop . omove_oM_12_21
    wLpush_oRpop = wunpack_o . oswap_o . opack_oL
    wLpop_oRpush :: hp ((st, z), (x, y))  -> hp (st, (x, (y, z)))
    -- wLpop_oRpush = omove_oM_21_12 . wLpop_opush
    wLpop_oRpush = opack_oR . oswap_o . wpack_o

    -- 更新冫对象属性牜输入输出隐藏牜单栈
    oupdate__pop :: hp ((st, args4update), (context, inner_obj)) -> hp (st, (context, (inner_obj, args4update)))
    oupdate__pop = wLpop_oRpush
    oupdate__push :: hp (st, (context, (inner_obj, returned_value))) -> hp ((st, returned_value), (context, inner_obj))
    oupdate__push = wLpush_oRpop

    oupdate_U__start :: hp (arged_st, obj) -> hp (arged_st, ((), obj))
    oupdate_U__start = oswap_o . opushE
    oupdate_U__start_arged_obj :: hp (st, (obj, args4update)) -> hp ((st, args4update), ((), obj))
    oupdate_U__start_arged_obj = oupdate__push . oupdate_U__start
    oupdate_U__start_wL :: hp (st, args4update) -> hp ((st, args4update), ((), st))
    oupdate_U__start_wL = oupdate_U__start . wpush_wL
    oupdate_U__start_w :: hp arged_st -> hp (arged_st, ((), arged_st))
    oupdate_U__start_w = oupdate_U__start . wpush_w
    --
    --
    oupdate_U__enterL :: hp (arged_st, (context, (inner_objL, inner_objR))) -> hp (arged_st, ((context, inner_objR), inner_objL))
    oupdate_U__enterL = opack_oL . oswap_oR
    oupdate_U__enterR :: hp (arged_st, (context, (inner_objL, inner_objR))) -> hp (arged_st, ((context, inner_objL), inner_objR))
    oupdate_U__enterR = opack_oL
    --
    --
    oupdate_U__exitL :: hp (rsted_st, ((context, inner_objR), new_inner_objL)) -> hp (rsted_st, (context, (new_inner_objL, inner_objR)))
    oupdate_U__exitL = oswap_oR . opack_oR
    oupdate_U__exitR :: hp (rsted_st, ((context, inner_objL), new_inner_objR)) -> hp (rsted_st, (context, (inner_objL, new_inner_objR)))
    oupdate_U__exitR = opack_oR
    --
    --
    oupdate_U__insideL
        :: (hp (arged_st, ((context, inner_objR), inner_objL)) -> hp (rsted_st, ((context, inner_objR), new_inner_objL)))
        -> (hp (arged_st, (context, (inner_objL, inner_objR))) -> hp (rsted_st, (context, (new_inner_objL, inner_objR))))
    oupdate_U__insideL f = oupdate_U__exitL . f . oupdate_U__enterL
    --
    --
    oupdate_U__insideR
        :: (hp (arged_st, ((context, inner_objL), inner_objR)) -> hp (rsted_st, ((context, inner_objL), new_inner_objR)))
        -> (hp (arged_st, (context, (inner_objL, inner_objR))) -> hp (rsted_st, (context, (inner_objL, new_inner_objR))))
    oupdate_U__insideR f = oupdate_U__exitR . f . oupdate_U__enterR
    --
    --
    --
    --





    -- 更新冫对象属性牜输入输出隐藏牜双栈
    oupdate_UU__start :: hp (arged_st, obj) -> hp (arged_st, (((), ()), obj))
    oupdate_UU__start = oswap_o . wpack_o . wpack_o . wpushE . wpushE
    oupdate_UU__start_arged_obj :: hp (st, (obj, args4update)) -> hp ((st, args4update), (((), ()), obj))
    oupdate_UU__start_arged_obj = oupdate_UU__start . wunpack_o . oswap_o
    oupdate_UU__start_wL :: hp (st, args4update) -> hp ((st, args4update), (((), ()), st))
    oupdate_UU__start_wL = oupdate_UU__start . wpush_wL
    oupdate_UU__start_w :: hp arged_st -> hp (arged_st, (((), ()), arged_st))
    oupdate_UU__start_w = oupdate_UU__start . wpush_w
    --
    --
    oupdate_UU__pop_args :: hp ((st, args4update), (uu, inner_obj)) -> hp (st, (uu, (inner_obj, args4update)))
    oupdate_UU__pop_args = wLpop_oRpush
    oupdate_UU__push_result :: hp (st, (uu, (inner_obj, returned_value))) -> hp ((st, returned_value), (uu, inner_obj))
    oupdate_UU__push_result = wLpush_oRpop
    --
    --
    oupdate_UU__enterL :: hp (arged_st, ((uncleLs, uncleRs), (inner_objL, inner_objR))) -> hp (arged_st, ((uncleLs, (inner_objR, uncleRs)), inner_objL))
    -- oupdate_UU__enterL = see:below
    oupdate_UU__enterR :: hp (arged_st, ((uncleLs, uncleRs), (inner_objL, inner_objR))) -> hp (arged_st, (((uncleLs, inner_objL), uncleRs), inner_objR))
    -- oupdate_UU__enterR = see:below
    --
    --
    oupdate_UU__exitL :: hp (rsted_st, ((uncleLs, (inner_objR, uncleRs)), new_inner_objL)) -> hp (rsted_st, ((uncleLs, uncleRs), (new_inner_objL, inner_objR)))
    -- oupdate_UU__exitL = see:below
    oupdate_UU__exitR :: hp (rsted_st, (((uncleLs, inner_objL), uncleRs), new_inner_objR)) -> hp (rsted_st, ((uncleLs, uncleRs), (inner_objL, new_inner_objR)))
    -- oupdate_UU__exitR = see:below
    --
    --
    oupdate_UU__insideL
        :: (hp (arged_st, ((uncleLs, (inner_objR, uncleRs)), inner_objL)) -> hp (rsted_st, ((uncleLs, (inner_objR, uncleRs)), new_inner_objL)))
        -> (hp (arged_st, ((uncleLs, uncleRs), (inner_objL, inner_objR))) -> hp (rsted_st, ((uncleLs, uncleRs), (new_inner_objL, inner_objR))))
    oupdate_UU__insideL f = oupdate_UU__exitL . f . oupdate_UU__enterL
    --
    --
    oupdate_UU__insideR
        :: (hp (arged_st, (((uncleLs, inner_objL), uncleRs), inner_objR)) -> hp (rsted_st, (((uncleLs, inner_objL), uncleRs), new_inner_objR)))
        -> (hp (arged_st, ((uncleLs, uncleRs), (inner_objL, inner_objR))) -> hp (rsted_st, ((uncleLs, uncleRs), (inner_objL, new_inner_objR))))
    oupdate_UU__insideR f = oupdate_UU__exitR . f . oupdate_UU__enterR
    --
    --
    --
    --



    -- 更新冫对象属性牜输入输出随行
    oinsert__start :: hp (st, (obj, args4update)) -> hp (st, (((), ()), (obj, args4update)))
    oinsert__start = oswap_o . wpack_o . wpack_o . wpushE . wpushE
    oinsert__start_wL :: hp (st, args4update) -> hp (st, (((), ()), (st, args4update)))
    oinsert__start_wL = oinsert__start . o5w
    oinsert__start_w :: hp (st, args4update) -> hp (st, (((), ()), ((st, args4update), args4update)))
    oinsert__start_w = oinsert__start . oswap_o . wpack_o . wpush_w
    --
    --
    oinsert__enterL__input :: hp (st, ((uncleLs, uncleRs), ((inner_objL, inner_objR), args4update))) -> hp (st, ((uncleLs, (inner_objR, uncleRs)), (inner_objL, args4update)))
    -- oinsert__enterL__input = see:below
    oinsert__enterL__input = oupdate_UU__pop_args . oupdate_UU__enterL . oupdate_UU__push_result
    oinsert__enterR__input :: hp (st, ((uncleLs, uncleRs), ((inner_objL, inner_objR), args4update))) -> hp (st, (((uncleLs, inner_objL), uncleRs), (inner_objR, args4update)))
    -- oinsert__enterR__input = see:below
    oinsert__enterR__input = oupdate_UU__pop_args . oupdate_UU__enterR . oupdate_UU__push_result
    --
    --
    oinsert__exitL :: hp (st, ((uncleLs, (inner_objR, uncleRs)), new_inner_objL)) -> hp (st, ((uncleLs, uncleRs), (new_inner_objL, inner_objR)))
    -- oinsert__exitL = see:below
    oinsert__exitL = oupdate_UU__exitL
    oinsert__exitR :: hp (st, (((uncleLs, inner_objL), uncleRs), new_inner_objR)) -> hp (st, ((uncleLs, uncleRs), (inner_objL, new_inner_objR)))
    -- oinsert__exitR = see:below
    oinsert__exitR = oupdate_UU__exitR
    --
    --
    oinsert__insideL
        :: (hp (st, ((uncleLs, (inner_objR, uncleRs)), (inner_objL, args4update))) -> hp (st, ((uncleLs, (inner_objR, uncleRs)), new_inner_objL)))
        -> (hp (st, ((uncleLs, uncleRs), ((inner_objL, inner_objR), args4update))) -> hp (st, ((uncleLs, uncleRs), (new_inner_objL, inner_objR))))
    oinsert__insideL f = oinsert__exitL . f . oinsert__enterL__input
    --
    --
    oinsert__insideR
        :: (hp (st, (((uncleLs, inner_objL), uncleRs), (inner_objR, args4update))) -> hp (st, (((uncleLs, inner_objL), uncleRs), new_inner_objR)))
        -> (hp (st, ((uncleLs, uncleRs), ((inner_objL, inner_objR), args4update))) -> hp (st, ((uncleLs, uncleRs), (inner_objL, new_inner_objR))))
    oinsert__insideR f = oinsert__exitR . f . oinsert__enterR__input
    --
    --
    --
    --
    oinsert__exitL__return :: hp (st, ((uncleLs, (inner_objR, uncleRs)), (new_inner_objL, returned_value))) -> hp (st, ((uncleLs, uncleRs), ((new_inner_objL, inner_objR), returned_value)))
    oinsert__exitL__return = wLpop_oRpush . oinsert__exitL . wLpush_oRpop
    --
    oinsert__exitR__return :: hp (st, (((uncleLs, inner_objL), uncleRs), (new_inner_objR, returned_value))) -> hp (st, ((uncleLs, uncleRs), ((inner_objL, new_inner_objR), returned_value)))
    oinsert__exitR__return = wLpop_oRpush . oinsert__exitR . wLpush_oRpop
    --
    --
    oinsert__insideL__return
        :: (hp (st, ((uncleLs, (inner_objR, uncleRs)), (inner_objL, args4update))) -> hp (st, ((uncleLs, (inner_objR, uncleRs)), (new_inner_objL, returned_value))))
        -> (hp (st, ((uncleLs, uncleRs), ((inner_objL, inner_objR), args4update))) -> hp (st, ((uncleLs, uncleRs), ((new_inner_objL, inner_objR), returned_value))))
    oinsert__insideL__return f = oinsert__exitL__return . f . oinsert__enterL__input
    --
    --
    oinsert__insideR__return
        :: (hp (st, (((uncleLs, inner_objL), uncleRs), (inner_objR, args4update))) -> hp (st, (((uncleLs, inner_objL), uncleRs), (new_inner_objR, returned_value))))
        -> (hp (st, ((uncleLs, uncleRs), ((inner_objL, inner_objR), args4update))) -> hp (st, ((uncleLs, uncleRs), ((inner_objL, new_inner_objR), returned_value))))
    oinsert__insideR__return f = oinsert__exitR__return . f . oinsert__enterR__input
    --
    --
    oinsert__replace__return :: hp (st, ((uncleLs, uncleRs), (inner_obj, (new_inner_obj, returned_value)))) -> hp (st, ((uncleLs, uncleRs), (new_inner_obj, returned_value)))
    oinsert__replace__return = odel_oRL
    --
    --
    oinsert__replace :: hp (st, ((uncleLs, uncleRs), (inner_obj, new_inner_obj))) -> hp (st, ((uncleLs, uncleRs), new_inner_obj))
    oinsert__replace = odel_oRL
        -- 只需要替换:因为其他可能的修改如下:
        -- push@R == id #see:rpushLLR@AdjustableEqv2
        -- push@L == oswap_oR
        -- modify__init == wunpack_o #see:oinsert__delL
        -- modify__stop == wpack_o
    oinsert__delL :: hp (st, ((uncleLs, uncleRs), ((inner_objL, inner_objR), args4update))) -> hp (st, ((uncleLs, uncleRs), inner_objR))
    oinsert__delL = wpack_o . o5oR . o5oL . wunpack_o
    oinsert__delR :: hp (st, ((uncleLs, uncleRs), ((inner_objL, inner_objR), args4update))) -> hp (st, ((uncleLs, uncleRs), inner_objL))
    oinsert__delR = wpack_o . o5oL . o5oL . wunpack_o
    --
    oinsert__delL__return :: hp (st, ((uncleLs, uncleRs), ((inner_objL, inner_objR), args4update))) -> hp (st, ((uncleLs, uncleRs), (inner_objR, ((inner_objL, inner_objR), args4update))))
    -- oinsert__delL__return :: hp (st, (x, ((y, z), a))) -> hp (st, (x, (z, ((y, z), a))))
    oinsert__delL__return = wpack_o . oswap_o . wpack_o . o5oR . o5oL . wpush_o . wunpack_o
    oinsert__delR__return :: hp (st, ((uncleLs, uncleRs), ((inner_objL, inner_objR), args4update))) -> hp (st, ((uncleLs, uncleRs), (inner_objL, ((inner_objL, inner_objR), args4update))))
    oinsert__delR__return = wpack_o . oswap_o . wpack_o . o5oL . o5oL . wpush_o . wunpack_o
        -- see:rpopLLR@AdjustableEqv2
    oinsert__delL__returnL :: hp (st, ((uncleLs, uncleRs), ((inner_objL, inner_objR), args4update))) -> hp (st, ((uncleLs, uncleRs), (inner_objR, inner_objL)))
    oinsert__delL__returnL = oswap_oR . odel_oRR
    oinsert__delR__returnR :: hp (st, ((uncleLs, uncleRs), ((inner_objL, inner_objR), args4update))) -> hp (st, ((uncleLs, uncleRs), (inner_objL, inner_objR)))
    oinsert__delR__returnR = odel_oRR
    --
    oinsert__stop :: hp (st, (((), ()), new_obj)) -> hp (st, new_obj)
        -- or: (o5w . o5w) if oinsert__start_w/oinsert__start_wL
    oinsert__stop = o5oR
    oinsert__next :: hp ((st, ((uncleLs, uncleRs), new_inner_obj)), next_new_inner_obj) -> hp (st, ((uncleLs, uncleRs), (new_inner_obj, next_new_inner_obj)))
    oinsert__next = opack_oR . wpack_o




    oupdate_UU__enterL = opack_oL . wpack_o . oswap_o . opack_oR . oswap_o . wunpack_o . opack_oR
      -- [I :: ((uncleLs, uncleRs), (inner_objL, inner_objR))]
      -- [O :: ((uncleLs, (inner_objR, uncleRs)), inner_objL)]
      -- [I :: ((a, b), (c, d))]
      -- [O :: ((a, (d, b)), c)]
    oupdate_UU__enterR = opack_oL . oupdate_UU__pop_args . oswap_top2_R . oupdate_UU__push_result
      -- [I :: ((uncleLs, uncleRs), (inner_objL, inner_objR))]
      -- [O :: (((uncleLs, inner_objL), uncleRs), inner_objR)]
      -- [I :: ((a, b), (c, d))]
      -- [O :: (((a, c), b), d)]
    oupdate_UU__exitL = opack_oL . wpack_o . oswap_o . opack_oL . oswap_o . wunpack_o . opack_oR
      -- inverse of:oupdate_UU__enterL = opack_oL . wpack_o . oswap_o . opack_oR . oswap_o . wunpack_o . opack_oR
    oupdate_UU__exitR = oupdate_UU__pop_args . oswap_top2_R . oupdate_UU__push_result . opack_oR
      -- inverse of:oupdate_UU__enterR = opack_oL . oupdate_UU__pop_args . oswap_top2_R . oupdate_UU__push_result

    {-
    -- 超长具现:最好还是要有直接具现
    --      这里旨在验证
    oinsert__enterL__input =
        -- treat wLR as arg_lnkls
        -- (wpush_w . (opack_oR .)* wpack_o)/(wpush_wL . (opack_oR .)* wpack_o) move o and push o into wLR-arg_lnkls as [wLR, o]
        -- ==>>:
      -- (st, o/result) <<==:
      o5oR
      -- (st, o/(I, result))
      . wpack_o
      -- ((st, I), o/result)
      -- ((st, I), o/((uncleLs, (inner_objR, uncleRs)), (inner_objL, args4update)))
      . opack_oR
      -- ((st, I), o/(((uncleLs, (inner_objR, uncleRs)), inner_objL), args4update))
      . wpack_o
      -- (((st, I), wLR/((uncleLs, (inner_objR, uncleRs)), inner_objL)), o/args4update)
      . o5oR . o5oR . o5oR
      -- (((st, I), wLR/((uncleLs, (inner_objR, uncleRs)), inner_objL)), o/(st, I))
      . wpush_wL . wpack_o
      -- (((st, I), wLR/(uncleLs, (inner_objR, uncleRs))), o/inner_objL)
      . o5oL . o5oL . o5oR . o5oR
      -- (((st, I), wLR/(uncleLs, (inner_objR, uncleRs))), o/(st, I))
      . wpush_wL
      -- (wL/(st, I), o/(uncleLs, (inner_objR, uncleRs)))
      . opack_oR
      -- ((st, I), o/((uncleLs, inner_objR), uncleRs))
      . wpack_o
      -- (((st, I), wLR/(uncleLs, inner_objR)), uncleRs)
      . o5oR . o5oL . o5oR
      -- (((st, I), wLR/(uncleLs, inner_objR)), (st, I))
      . wpush_wL . wpack_o
      -- (((st, I), uncleLs), inner_objR)
      . o5oR . o5oL . o5oR . o5oR
      -- (wL/((st, I), wLR/uncleLs), o/(st, I))
      . wpush_wL
      -- (wL/(st, I), o/uncleLs)
      . o5oL . o5oL
      -- ((st, I), o/I/((uncleLs, uncleRs), _))
      -- ((st, I), o/I) <<==:
      . wpush_o
      -- (st, o/I)
      --
      -- [I :: ((uncleLs, uncleRs), ((inner_objL, inner_objR), args4update))]
      -- [I.L :: (uncleLs, uncleRs)]
      -- [I.R :: ((inner_objL, inner_objR), args4update)]
      -- [I.R.L :: (inner_objL, inner_objR)]
    oinsert__enterR__input =
        -- treat wLR as arg_lnkls
        -- (wpush_w . (opack_oR .)* wpack_o)/(wpush_wL . (opack_oR .)* wpack_o) move o and push o into wLR-arg_lnkls as [wLR, o]
        -- ==>>:
      -- (st, o/result) <<==:
      o5oR
      -- (st, o/(I, result))
      . wpack_o
      -- ((st, I), o/result)
      -- ((st, I), o/(((uncleLs, inner_objL), uncleRs), (inner_objR, args4update)))
      . opack_oR
      -- ((st, I), o/((((uncleLs, inner_objL), uncleRs), inner_objR), args4update))
      . wpack_o
      -- (((st, I), wLR/(((uncleLs, inner_objL), uncleRs), inner_objR)), o/param)
      . o5oR . o5oR . o5oR
      -- (((st, I), wLR/(((uncleLs, inner_objL), uncleRs), inner_objR)), o/(st, I))
      . wpush_wL . wpack_o
      -- (((st, I), wLR/((uncleLs, inner_objL), uncleRs)), o/inner_objR)
      . o5oR . o5oL . o5oR . o5oR
      -- (((st, I), wLR/((uncleLs, inner_objL), uncleRs)), o/(st, I))
      . wpush_wL
      -- (wL/(st, I), o/((uncleLs, inner_objL), uncleRs))
      . wpack_o
      -- (((st, I), wLR/(uncleLs, inner_objL)), uncleRs)
      . o5oR . o5oL . o5oR
      -- (((st, I), wLR/(uncleLs, inner_objL)), (st, I))
      . wpush_wL . wpack_o
      -- (((st, I), uncleLs), inner_objL)
      . o5oL . o5oL . o5oR . o5oR
      -- (wL/((st, I), wLR/uncleLs), o/(st, I))
      . wpush_wL
      -- (wL/(st, I), o/uncleLs)
      . o5oL . o5oL
      -- ((st, I), o/I/((uncleLs, uncleRs), _))
      -- ((st, I), o/I) <<==:
      . wpush_o
      -- (st, o/I)
      --
    oupdate_UU__exitL =
      -- (st, o/result) <<==:
      o5oR
      -- (st, o/(I, result))
      . wpack_o
      -- ((st, I), o/result)
      -- ((st, I), o/((uncleLs, uncleRs), (new_inner_objL, inner_objR)))
      . opack_oR . wpack_o
      -- (((st, I), wLR/((uncleLs, uncleRs), new_inner_objL)), o/inner_objR)
      -- ILRL/inner_objR
      . o5oL . o5oR . o5oL . o5oR
      -- (((st, I), wLR/((uncleLs, uncleRs), new_inner_objL)), o/(st, I))
      . wpush_wL . wpack_o
      -- (((st, I), wLR/(uncleLs, uncleRs)), o/new_inner_objL)
      -- IR/new_inner_objL
      . o5oR . o5oR
      -- (((st, I), wLR/(uncleLs, uncleRs)), (st, I))
      . wpush_wL . wpack_o
      -- (wL/((st, I), wLR/uncleLs), o/uncleRs)
      -- ILRR/uncleRs
      . o5oR . o5oR . o5oL . o5oR
      -- (wL/((st, I), wLR/uncleLs), o/(st, I))
      . wpush_wL
      -- (wL/(st, I), o/uncleLs)
      -- ILL/uncleLs
      . o5oL . o5oL
      -- ((st, I), o/I/((uncleLs, _), _))
      -- ((st, I), o/I) <<==:
      . wpush_o
      -- (st, o/I)
      --
      -- [I :: ((uncleLs, (inner_objR, uncleRs)), new_inner_objL)]
      -- [I :: (IL/(ILL/uncleLs, ILR/(ILRL/inner_objR, ILRR/uncleRs)), IR/new_inner_objL)]
    oupdate_UU__exitR =
      -- (st, o/result) <<==:
      o5oR
      -- (st, o/(I, result))
      . wpack_o
      -- ((st, I), o/result)
      -- ((st, I), o/((uncleLs, uncleRs), (inner_objL, new_inner_objR)))
      . opack_oR . wpack_o
      -- (((st, I), wLR/((uncleLs, uncleRs), inner_objL)), o/new_inner_objR)
      -- IR/new_inner_objR
      . o5oR . o5oR
      -- (((st, I), wLR/((uncleLs, uncleRs), inner_objL)), o/(st, I))
      . wpush_wL . wpack_o
      -- (((st, I), wLR/(uncleLs, uncleRs)), o/inner_objL)
      -- ILLR/inner_objL
      . o5oR . o5oL . o5oL . o5oR
      -- (((st, I), wLR/(uncleLs, uncleRs)), (st, I))
      . wpush_wL . wpack_o
      -- (wL/((st, I), wLR/uncleLs), o/uncleRs)
      -- ILR/uncleRs
      . o5oR . o5oL . o5oR
      -- (wL/((st, I), wLR/uncleLs), o/(st, I))
      . wpush_wL
      -- (wL/(st, I), o/uncleLs)
      -- ILLL/uncleLs
      . o5oL . o5oL . o5oL
      -- ((st, I), o/I/((uncleLs, _), _))
      -- ((st, I), o/I) <<==:
      . wpush_o
      -- (st, o/I)
      --
      -- [I :: (((uncleLs, inner_objL), uncleRs), new_inner_objR)]
      -- [I :: (IL/(ILL/(ILLL/uncleLs, ILLR/inner_objL), ILR/uncleRs), IR/new_inner_objR)]
    -}

    {-
    -- 等价操作包=>所需要的操作包
    wpush_w :: hp st -> hp (st, st)
    o2w :: hp (st, o) -> hp o
    opushE :: hp (st, o) -> hp (st, (o, ()))
    oswap_oR :: hp (st, (oL, (oRL, oRR))) -> hp (st, (oL, (oRR, oRL)))
    opack_oR :: hp (st, ((x, oM), y)) -> hp (st, (x, (oM, y)))
    -}
    {-
    -- 等价操作包=>所需要的操作包
    wpush_w :: hp st -> hp (st, st)
        -- 复制
        -- 这是增加原有元素重复数的唯一基本操作，不可简省
        -- 不能用o5w替代:因为o5w要求输入为有序对，无法实现wpush_w
        -- opushE不能重复原有元素
    o2w :: hp (st, o) -> hp o
        -- 删除
        -- 这是降低元素重复数的唯一基本操作，不可简省
        --
        -- !! opushE不降低元素重复数
        -- #obsolete:
        -- 不能用oclear实现，因为oclear输出为有序对，无法实现o2w
        -- oclear也降低元素重复数(但增加『()』重复数)，但是oclear可被wpushE替换，可视为『仅构造』
    opushE :: hp (st, o) -> hp (st, (o, ()))
        -- 新增/构造:『()』
        -- 这是构造叶节点的唯一基本操作，不可简省
        -- <<==:
        -- 现更换oclear为opushE
        -- <<==:
        -- oclear :: hp (st, o) -> hp (st, ())
        -- 新增/构造:『()』
        -- 这是构造叶节点的唯一基本操作，不可简省
        -- oclear可更换为wpushE:见:_oclear
    oswap_oR :: hp (st, (oL, (oRL, oRR))) -> hp (st, (oL, (oRR, oRL)))
        -- 调序#结构不变#元素重复数不变
        -- ???这是修改元素次序的唯一基本操作，不可简省???
        -- wpush_w,o2w,opushE通过增删元素也可能修改元素次序
        -- wpush_w,o2w,opushE,opack_oR的组合可否实现oswap_oR???不能<<==:
        --  要求:某一步:构造(oRR, oRL)
        --      *wpush_w=>『(a,a)』不匹配
        --      *o2w=>『a』要求已有=>不匹配
        --      *opushE=>『(a,())』不匹配
        --      *opack_oR=>要求先构造((a, oRR), oRL) => 要求wpush_w复制+删除中间元素，但o2w删左侧，无法删除中间元素=>不能
    opack_oR :: hp (st, ((x, oM), y)) -> hp (st, (x, (oM, y)))
        -- 修改树状结构#次序不变#元素重复数不变
        -- ???这是修改树状结构的唯一基本操作，不可简省???
        -- wpush_w,o2w,opushE也都修改树状结构，但都改变元素重复数
        -- wpush_w,o2w,opushE,oswap_oR的组合可否实现opack_oR???不能<<==:
        --  要求:某一步:构造(oM, y)/(y, oM)
        --      *wpush_w=>『(a,a)』不匹配
        --      *o2w=>『a』要求已有=>不匹配
        --      *opushE=>『(a,())』不匹配
        --      *oswap_oR=>要求先构造(y, oM)/(oM, y) => 不能
    -}
-- end-class AdjustableEqv3

instance AdjustableEqv3 Zzz where
    -- Zzz仅限用于确认纯虚函数集合
    wpush_w = undefined
    o2w = undefined
    opushE = undefined
      -- oclear = undefined
      -- wpushE = undefined
    oswap_oR = undefined
    opack_oR = undefined


instance AdjustableEqv3 hp => AdjustableEqv2 (New hp) where
    -- :.+1,.+36s/= \(.*\)$/= fmap__New $ \1

    -- init_CSFT_1 :: hp st -> hp ((((), st), st), ())
    init_CSFT_1 = fmap__New $ o2w . wpack_o . wpushE . wpack_o . wpush_wL . wpack_o . wpush_wL . wpushE

    setW = fmap__New $ o2w
    rgetW = fmap__New $ o5w
    rgetRR = fmap__New $ o5oR
    rgetRL = fmap__New $ o5oL
    rsetL = fmap__New $ o2w . opush_o
    -- rsetLR :: hp ((st, frame), target) -> hp ((st, target), target)
    -- rsetLR = fmap__New $ wpush_o . o5oR . wpack_o
    rsetLR = fmap__New $ wpush_o . o2w . odel_oLR . wpush_w
    -- rsetLL :: hp ((st, frame), target) -> hp ((target, frame), target)
    -- rsetLL = fmap__New $ o5oL . wpush_w . o2w . odel_oRL . oswap_o . wpush_w
    rsetLL = fmap__New $ o2w . opack_oL . odel_oLL . wpush_w . wpush_w . o2w . odel_oLL . wpush_w

    -- rsetLLR :: hp (((constant, stack), frame), target) -> hp (((constant, target), frame), target)
    -- rsetLLR = fmap__New $ o2w . o2w . (oinsert__insideL . oinsert__insideL . oinsert__insideR $ oinsert__replace) . oinsert__start_w
    rsetLLR = fmap__New $ o2w . o2w . (oupdate_U__insideL . oupdate_U__insideL . oupdate_U__insideR $ odel_oRL . oupdate__pop) . oupdate_U__start_w
        -- using oupdate_U__...

    -- rsetLLL = fmap__New $ o2w . o2w . (oinsert__insideL . oinsert__insideL . oinsert__insideL $ oinsert__replace) . oinsert__start_w
    rsetLLL = fmap__New $ o2w . o2w . (oupdate_U__insideL . oupdate_U__insideL . oupdate_U__insideL $ odel_oRL . oupdate__pop) . oupdate_U__start_w
        -- using oupdate_U__...

    -- rswapL :: hp (st, target) -> hp (target, st)
    rswapL = fmap__New $ o2w . oswap_o . wpush_w
    -- rswapLR :: hp ((st, frame), target) -> hp ((st, target), frame)
    rswapLR = fmap__New $ o2w . opack_oL . oswap_oR . opack_oR . wpush_w
    rswapLL = fmap__New $ o2w . opack_oL . oreverse_21_12 . wpush_w
    -- rswapLLR :: hp (((constant, stack), frame), target) -> hp (((constant, target), frame), stack)
    -- rswapLLR = fmap__New $ o2w . wpack_o . o5oR . o5oL . wpush_wL . o5oL . oinsert__stop . (oinsert__insideL . oinsert__insideL . oinsert__insideR $ oinsert__replace) . oinsert__start_w
    rswapLLR = fmap__New $ o2w . o2w . oupdate__pop . (oupdate_U__insideL . oupdate_U__insideR $ oupdate__push . oswap_oR . oupdate__pop) . oupdate_U__start_wL
        -- using oupdate_U__...

    -- rswapLLL = fmap__New $ o2w . wpack_o . o5oL . o5oL . wpush_wL . o5oL . oinsert__stop . (oinsert__insideL . oinsert__insideL . oinsert__insideL $ oinsert__replace) . oinsert__start_w
    rswapLLL = fmap__New $ o2w . o2w . oupdate__pop . (oupdate_U__insideL . oupdate_U__insideL $ oupdate__push . oswap_oR . oupdate__pop) . oupdate_U__start_wL
        -- using oupdate_U__...

    -- rpushLLR :: hp (((constant, stack), frame), target) -> hp (((constant, (stack, target)), frame), target)
    -- rpushLLR = fmap__New $ o2w . o2w . (oinsert__insideL . oinsert__insideL . oinsert__insideR $ id) . oinsert__start_w
    rpushLLR = fmap__New $ o2w . o2w . (oupdate_U__insideL . oupdate_U__insideL . oupdate_U__insideR $ oupdate__pop) . oupdate_U__start_w
        -- using oupdate_U__...
    -- rpopLLR :: hp (((constant, (stack, top)), frame), target) -> hp (((constant, stack), frame), top)
    -- rpopLLR = fmap__New $ o2w . o2w . (oinsert__insideL__return . oinsert__insideR__return $ oinsert__delR__returnR) . oinsert__start_wL
    rpopLLR = fmap__New $ o2w . o2w . oupdate__pop . (oupdate_U__insideL . oupdate_U__insideR $ oupdate__push) . oupdate_U__start_wL
        -- using oupdate_U__...


    -- rpushLR_R :: hp ((st, tree), target) -> hp ((st, (tree, target)), target)
    rpushLR_R = fmap__New $ odel_oL . wpush_o . wpack_o
    -- rpushLR_L :: hp ((st, tree), target) -> hp ((st, (target, tree)), target)
    rpushLR_L = fmap__New $ odel_oR . wpush_o . oswap_o . wpack_o
    -- rpackLR_R :: hp ((st, ((tree, x), y)), target) -> hp ((st, (tree, (x, y))), target)
    rpackLR_R = fmap__New $ o2w . oswap_top2_R . wpush_w . opack_oR . o2w . oswap_top2_R . wpush_w
    rpackLR_L = fmap__New $ o2w . oswap_top2_R . wpush_w . opack_oL . o2w . oswap_top2_R . wpush_w

    -- rpopLR_R :: hp ((st, (tree, x)), target) -> hp ((st, tree), x)
    rpopLR_R = fmap__New $ o2w . opack_oL . o5oL . wpush_w
    -- rpopLLR_pushR_R :: hp (((constant, (stack, top)), frame), target) -> hp (((constant, stack), frame), (target, top))
    -- rpopLLR_pushR_R = fmap__New $ o2w . opack_oR . o5oR . oupdate_UU__pop_args . (oupdate_UU__insideL . oupdate_UU__insideL . oupdate_UU__insideR $ oupdate_UU__push_result) . oupdate_UU__start_w
    rpopLLR_pushR_R = fmap__New $ o2w . opack_oR . o5oR . oupdate__pop . (oupdate_U__insideL . oupdate_U__insideL . oupdate_U__insideR $ oupdate__push) . oupdate_U__start_w
        -- using oupdate_U__...

    -- rpopLR_R_pushR_R :: hp ((st, (tree, x)), target) -> hp ((st, tree), (target, x))
    rpopLR_R_pushR_R = fmap__New $ o2w . opack_oR . o5oR . oupdate__pop . (oupdate_U__insideL . oupdate_U__insideR $ oupdate__push) . oupdate_U__start_w
    rpopLR_L_pushR_R = fmap__New $ o2w . opack_oR . o5oR . oupdate__pop . (oupdate_U__insideL . oupdate_U__insideR $ oupdate__push . oswap_oR) . oupdate_U__start_w

    -- rgetW_pushR_R :: hp (st, target) -> hp (st, (target, (st, target)))
    rgetW_pushR_R = fmap__New $ wpack_o . wpush_w
    rgetL_pushR_R = fmap__New $ wpack_o . wpush_wL
    rgetLR_pushR_R = fmap__New $ wpack_o . o5oR . wpush_wL
    rgetLL_pushR_R = fmap__New $ wpack_o . o5oL . wpush_wL
    rgetLLR_pushR_R = fmap__New $ wpack_o . o5oR . o5oL . wpush_wL
    rgetLLL_pushR_R = fmap__New $ wpack_o . o5oL . o5oL . wpush_wL
    -- rgetRR_pushR_R :: hp (st, (x, y)) -> hp (st, ((x, y), y))
    rgetRR_pushR_R = fmap__New $ odel_oRL . opush_o
    -- rgetRL_pushR_R :: hp (st, (x, y)) -> hp (st, ((x, y), x))
    rgetRL_pushR_R = fmap__New $ odel_oRR . opush_o


{-
TODO:
  if_else:
  BOOL === a -> a -> a
  虚拟机脚本 可以有流程，但『硬件』没有


e ../lots/NOTE/abbr/software.txt
hard_coded vs hard_wired
  hard_wired
  hard_coded
  cp -r ~/../usr/share/vim/vim82/colors/ /sdcard/0my_files/tmp/out4cp/vim82_colors
  view /sdcard/0my_files/tmp/out4cp/vim82_colors/README.txt
    - Do not use hard coded escape sequences, these will not work in other
    - When targetting 8-16 colors terminals, don't count on "darkblue" to be blue

TODO:
  AdjustableEqv4__complete_but_inefficient
      线性化
      增删
      调整次序
      树状化
  <<==:
      线性化=取出冫树的最左节点/opack_oR+入栈冫树的最左节点/wunpack_o # (hp (lnkls/leftIO, tree_lnkls/rightIO))
      增删=wpush_w,opushE,o2w/删
      调整次序=oswap_oR
      树状化=opack_oR
  <<==:
  AdjustableEqv3
    wpush_w = undefined
    o2w = undefined
    opushE = undefined
    oswap_oR = undefined
    opack_oR = undefined
  AdjustableEqv1
    copy1_2 = undefined
    popL2_1 = undefined
    pushE_R1_2 = undefined
    swapR12_12 = undefined
    moveM12_21 = undefined

-}
























