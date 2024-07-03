-- __all__:goto
-- SECTION:goto
{-# LANGUAGE KindSignatures #-}
{-# LANGUAGE TypeFamilies #-}
{-# LANGUAGE MultiParamTypeClasses #-}
-- {-# LANGUAGE ExplicitForAll #-}
{-# LANGUAGE ScopedTypeVariables #-}

-- {-# LANGUAGE GADTs #-}
{-# LANGUAGE RankNTypes #-}
{-# LANGUAGE ImpredicativeTypes #-}
-- {-# LANGUAGE DataKinds #-}
-- {-# LANGUAGE DefaultSignatures #-}
-- {-# LANGUAGE Rank2Types #-}
{-
• Type constructor ‘Type’ cannot be used here
        (perhaps you intended to use DataKinds)

-}
{- xxx -}

{-
e ../../python3_src/haskell_src/Framework4Translation.hs

view others/数学/编程/编译/翻译框架设计.txt
view ../../python3_src/haskell_src/Framework4Translation-ver2-tedious.hs
runghc ../../python3_src/haskell_src/Framework4Translation.hs



view ../lots/NOTE/Haskell/forall-polymorphic_type.txt
view ../lots/NOTE/Haskell/01start.txt
view ../lots/NOTE/Haskell/run_hs_script.txt

$ ghci
Prelude> :?
Prelude> :show imports
import Prelude -- implicit
Prelude> :browse Prelude
Prelude> :quit

ghci '--show-options' | grep GADT
ghci '--show-options' | grep Type
ghci '--show-options' | grep Kind
ghci '--show-options' | grep '^-X' | grep '^-XNo' -v
view ../lots/NOTE/Haskell/options.txt


:read !grep $'^type ' ../../python3_src/haskell_src/Framework4Translation.hs
:.+1,.+17s/^type \(\w\+\) .*/,\1
,Echo
,Try_PolymorphicType
,UFile8VirtualMachine
,UFile8Translator
,UTranslator_
,UTranslator
,File8VirtualMachine
,File8Translator
,Translator
,VirtualMachine
,File8Data
,UFile8Script
,File8Script
,UScript
,Script


-}


-- __all__:here
module Framework4Translation
(main
,Translation_Hierarchy(..)
--,File8VirtualMachine
--,File8Translator
,Label(..), unbox_Label
--,Echo
--,Try_PolymorphicType
,UFile8VirtualMachine
,UFile8Translator
,UTranslator_
,UTranslator
,File8VirtualMachine
,File8Translator
,Translator
,VirtualMachine
,File8Data
--,UFile8Script
--,File8Script
--,UScript
--,Script
--
--
,Portable_Interpretive_Compiler_Kit(..)
,Installer4Portable_Interpretive_Compiler_Kit(..)
,Native_Kit4Portable_Interpretive_Compiler_Kit(..)
--
,prepare4portable_interpretive_compiler_kit
,prepare4installer4portable_interpretive_compiler_kit
,prepare4native_kit4portable_interpretive_compiler_kit
--
--
--
,mk0__run_tr6P_999
,mk1__run_tr6P_999
,mk2__run_tr6P_999
,mk3__run_tr6P_999
    -- [:def____run_tr6P_999]:goto
    -- 运行器{P-翻译诀tr_X5Y_6P}
    -- dat_D_6X = run_tr6P_999 tr_X5Y_6P dat_D_6Y
--
--
--
,Is_Similar_Dialect(..)
,Manually_Adapt_Front_End_Dialect(..)
,Manually_Adapt_Back_End_Dialect(..)
--
-- ,Manually_Cat4File8Script(..)
,Manually_Cat4File8Translator(..)
--
,Is_Subset_Language(..)
,Lift_Subset_Language(..)
,lift_subset_language__tr_fl__999
,lift_subset_language__tr_prg__999
--
--
)
{-
-}
where

main = print "ok"
-- __all__




{-
-- SECTION:typing


abbr:
    nml:native_machine_language
    fmt:file_format
    fl:file
    prg:program/script/function
    tr:translate
    vm:virtual_machine
    dat:data
naming:
    xxx_6Z:file-name
    xxx_999:program-name#function
        现在使用RankNTypes，支持多态类型
        ===old:
        vs:xxx_9Z:LoadedData/装载后的数据#
        vs:xxx_996:GADT封装的多态函数
        由于Haskell的 数据类型『data』『*』并不支持『多态类型』『forall ...』
            只能通过GADT封装『多态函数』
            导致『非函数』#『不可调用』
        所以需要exec_tr_fl_999显式转换/解包GADT:
          tr_X5Y_999 = exec_tr_fl_999 tr_X5Y_996

ver1-to-ver2:
  ver1-LoadedData完全封装(所有状态参数集成一起)，函数/硬件 需要先装载(包括调整参数次序/Adjustable)
  ver2-分离式参数
ver2-to-ver3:
  ver2 任意数据 导致 需要 (load/eval/dump)中dump 区别 对待 文件
  ver3 只考虑 数据{file2file/程序纟文件变换} 去掉 (load/eval/dump)中的，只保留 load{file2file}
ver3-to-ver4:
  ver4:提升所有参数:hr xxx #包括:vm_V_996
  :.+1,$s/\(:: \|[-=]> \)\@<=\w\+\( \w\+\)*\($\| ->\)\@=/(\0)/g
  !cp -i ../../python3_src/haskell_src/Framework4Translation.hs ../../python3_src/haskell_src/Framework4Translation-ver4-polymorphic_type.hs



三种文件+两种程序+基本操作:
*三种文件:
tr_X5Y_6Z :: File8Translator Z Y X
  File8Translator fmt i_fmt o_fmt

vm_V_6Z :: File8VirtualMachine Z V
  File8VirtualMachine fmt nml
    --  [nml <: fmt]
    --  nml:native_machine_language
    --  fmt:file_format

dat_D_6Z :: File8Data Z D
  File8Data fmt dat



*两种程序:
vm_V_996 :: VirtualMachine V
  VirtualMachine nml

tr_X5Y_996 :: Translator Y X
  Translator i_fmt o_fmt
  <=!=> tr_X5Y_999 :: (File8Data Y D -> File8Data X D)
    现在使用RankNTypes，支持多态类型

*基本操作:
load_vm_999 :: VirtualMachine Z -> File8VirtualMachine Z V -> VirtualMachine V
  vm_V_996 = load_vm_999 vm_Z_996 vm_V_6Z

load_tr_999 :: VirtualMachine V -> File8Translator V Y X -> Translator Y X
  tr_X5Y_996 = load_tr_999 vm_Z_996 tr_X5Y_6Z

load_fl_999 :: VirtualMachine Z -> File8Data Z dat -> hr dat
  dat_D_999 = load_fl_999 vm_Z_996 dat_D_6Z

cat_vm_fl_999 :: File8VirtualMachine Y X -> File8VirtualMachine Z Y -> File8VirtualMachine Z X
  vm_X_6Z = cat_vm_fl_999 vm_X_6Y vm_Y_6Z

cat_tr_prg_999 :: Translator Y X -> Translator Z Y -> Translator Z X
  tr_X5Z_996 = cat_tr_prg_999 tr_X5Y_996 tr_Y5Z_996


exec_tr_tr_999 :: Translator Y X -> (File8Translator Y i_fmt o_fmt -> File8Translator X i_fmt o_fmt)
  tr_O5I_6X = exec_tr_tr_999 tr_X5Y_996 tr_O5I_6Y

exec_tr_vm_999 :: Translator Y X -> (File8VirtualMachine Y V -> File8VirtualMachine X V)
  vm_V_6X = exec_tr_vm_999 tr_X5Y_996 vm_V_6Y

exec_tr_fl_999 :: Translator Y X -> (File8Data Y D -> File8Data X D)
  dat_D_6X = exec_tr_fl_999 tr_X5Y_996 dat_D_6Y
  tr_X5Y_999 = exec_tr_fl_999 tr_X5Y_996



run_tr6P_999 :: File8Translator P Y X -> (File8Data Y D -> File8Data X D)
  ==>>:++hr:
  run_tr6P_999 :: (File8Translator P Y X) -> ((File8Data Y D) -> (File8Data X D))
  mk0__run_tr6P_999
    -- [:def____run_tr6P_999]:goto


others:
  tr_M5P_6Z = manually_adapt_back_end_dialect__999 tr_V5P_6Z
  tr_V5H_6Z = manually_adapt_front_end_dialect__999 tr_V5P_6Z
  tr_X5Z_6R = manually_cat_tr_fl_999 tr_X5Y_6R tr_Y5Z_6R
  dat_D_6G = lift_subset_language__fl__999 dat_D_6K
      ==>>:
      tr_X5Y_6G = lift_subset_language__fl__999 tr_X5Y_6K
      vm_V_6G = lift_subset_language__fl__999 vm_V_6K
  tr_F5K_6H = lift_subset_language__tr_fl__999 tr_E5G_6A
      [A <: H]
  tr_F5K_996 = lift_subset_language__tr_prg__999 tr_E5G_996
      [E <: F]
      [K <: G]


==>>:
目标:翻译
  长期性目标:翻译诀:tr_X5Y_6Z
  过渡性目标:翻译器:tr_X5Y_996#<=!=>tr_X5Y_999
  辅助性目标:虚拟机:vm_V_996
  辅助性目标:虚拟诀:vm_V_6Z
#下面的『至多一次』表示『局域同类串联可以一步到位』
#下面的『可能多次』导致分支复杂化:
  manually_cat_tr_fl_999
  cat_tr_prg_999
  cat_vm_fl_999
构造器{翻译诀/tr_X5Y_6Z}:
  tr_O5I_6X = exec_tr_tr_999 tr_X5Y_996 tr_O5I_6Y
      翻译冫翻译诀
      至多一次<<==cat_tr_prg_999
  tr_M5P_6Z = manually_adapt_back_end_dialect__999 tr_V5P_6Z
      人工适配后端方言冫翻译诀
      至多一次#一步到位
  tr_V5H_6Z = manually_adapt_front_end_dialect__999 tr_V5P_6Z
      人工适配前端方言冫翻译诀
      至多一次#一步到位
  tr_X5Z_6R = manually_cat_tr_fl_999 tr_X5Y_6R tr_Y5Z_6R
      人工串联冫翻译诀
      可能多次
  tr_F5K_6H = lift_subset_language__tr_fl__999 tr_E5G_6A
      [A <: H]
      [E <: F]
      [K <: G]
      tr_X5Y_6G = lift_subset_language__fl__999 tr_X5Y_6K
      提升冫翻译诀
      至多一次#一步到位
构造器{翻译器/tr_X5Y_996}:
  tr_X5Y_996 = load_tr_999 vm_Z_996 tr_X5Y_6Z
      装载冫翻译器
      至多一次<<==cat_vm_fl_999
  tr_X5Z_996 = cat_tr_prg_999 tr_X5Y_996 tr_Y5Z_996
      串联冫翻译器
      可能多次
  tr_F5K_996 = lift_subset_language__tr_prg__999 tr_E5G_996
      [E <: F]
      [K <: G]
      提升冫翻译器
      至多一次#一步到位
构造器{虚拟机/vm_X_996}:
  vm_V_996 = load_vm_999 vm_Z_996 vm_V_6Z
      运行冫虚拟机
      至多一次<<==cat_vm_fl_999
构造器{虚拟诀/vm_X_6Z}:
  vm_X_6Z = cat_vm_fl_999 vm_X_6Y vm_Y_6Z
      堆叠冫虚拟诀
      可能多次
  vm_V_6X = exec_tr_vm_999 tr_X5Y_996 vm_V_6Y
      翻译冫虚拟诀
      至多一次<<==cat_tr_prg_999
  vm_V_6G = lift_subset_language__fl__999 vm_V_6K
      提升冫虚拟诀
      至多一次#一步到位



-}

{-
-- 尝试:解包使用:多态类型
e ../lots/NOTE/Haskell/forall-polymorphic_type.txt

type Echo = (forall a. a -> a)
data Try_RankNTypes = Try_RankNTypes5echo (forall a. a -> a)
    -- {-# LANGUAGE RankNTypes #-}
    -- {-# LANGUAGE ImpredicativeTypes #-}
unbox_Try_RankNTypes :: Try_RankNTypes -> (a -> a)
unbox_Try_RankNTypes (Try_RankNTypes5echo echo) = echo

try_using_polymorphic_type_0 :: Echo -> (a -> a)
try_using_polymorphic_type_0 = id

try_using_polymorphic_type_1 :: Try_RankNTypes -> (a -> a)
try_using_polymorphic_type_1 = unbox_Try_RankNTypes

try_using_polymorphic_type_2 :: Try_RankNTypes -> (Bool -> Bool)
try_using_polymorphic_type_2 = unbox_Try_RankNTypes

data Wrapper a = Mk_Wrapper a
type Try_PolymorphicType = Wrapper Echo
unbox_Wrapper :: Wrapper a -> a
unbox_Wrapper (Mk_Wrapper a) = a


{-
try_using_polymorphic_type_11 :: Try_PolymorphicType -> (a -> a)
try_using_polymorphic_type_11 = unbox_Wrapper
    --fail:使用unbox_Wrapper
-}
try_using_polymorphic_type_12 :: Try_PolymorphicType -> (a -> a)
try_using_polymorphic_type_12 (Mk_Wrapper a) = a
    --ok:使用Mk_Wrapper而不使用unbox_Wrapper
-}


{-
data Try_GADT where
    Try_GADT5echo :: (forall a. a -> a) -> Try_GADT
    -- {-# LANGUAGE GADTs #-}
    -- {-# LANGUAGE RankNTypes #-}
    -- error:
    --  • Illegal polymorphic type: forall a. a -> a
    --      Perhaps you intended to use RankNTypes
unbox_Try_GADT :: Try_GADT -> (a -> a)
unbox_Try_GADT (Try_GADT5echo echo) = echo
-}




-- type Label hr a = hr a
newtype Label (hr :: * -> *) a = Mk_Label a
unbox_Label :: Label hr a -> a
unbox_Label (Mk_Label a) = a

unbox_Label4tr :: (File8Translator hr fmt i_fmt o_fmt) -> (UFile8Translator hr fmt i_fmt o_fmt)
unbox_Label4tr = unbox_Label

{-
fail:隔了个外层『UFile8Data hr fmt』，内层『forall...』无法消除/无法外移
    普通文件、脚本文件、翻译诀:
      类型 无法自动兼容/形式上非广狭关系(概念上是广狭关系)
unbox_Label4tr999 :: (File8Translator hr fmt i_fmt o_fmt) -> UFile8Data hr fmt (UTranslator_ hr i_fmt o_fmt dat)
unbox_Label4tr999 = unbox_Label
-}

type UFile8VirtualMachine hr fmt nml = UFile8Data hr fmt (UVirtualMachine hr nml)
type UFile8Translator hr fmt i_fmt o_fmt = UFile8Data hr fmt (UTranslator hr i_fmt o_fmt)
  -- {-# LANGUAGE ImpredicativeTypes #-}
  {-
  • Illegal polymorphic type:
        forall dat.  (UFile8Data hr i_fmt dat) -> (UFile8Data hr o_fmt dat)
      GHC doesn't yet support impredicative polymorphism
    • In the expansion of type synonym ‘Translator’
      In the type synonym declaration for ‘File8Translator’
  -}
type UTranslator_ hr i_fmt o_fmt dat = ((UFile8Data hr i_fmt dat) -> (UFile8Data hr o_fmt dat))
type UTranslator hr i_fmt o_fmt = (forall dat . (UTranslator_ hr i_fmt o_fmt dat))
-- type UTranslator hr i_fmt o_fmt = (forall dat . (UFile8Data hr i_fmt dat) -> (UFile8Data hr o_fmt dat))
    -- exec_tr_fl_999
    -- {-# LANGUAGE RankNTypes #-}


type File8VirtualMachine hr fmt nml = Label hr (UFile8VirtualMachine hr fmt nml)
-----------
-- type File8Translator hr fmt i_fmt o_fmt = File8Data hr fmt (UTranslator hr i_fmt o_fmt)
type File8Translator hr fmt i_fmt o_fmt = Label hr (UFile8Translator hr fmt i_fmt o_fmt)
type Translator hr i_fmt o_fmt = Label hr (UTranslator hr i_fmt o_fmt)
-----------
-- type File8Translator hr fmt i_fmt o_fmt = forall dat . File8Data hr fmt (UTranslator_ hr i_fmt o_fmt dat)
-- type Translator hr i_fmt o_fmt = (forall dat . Label hr (UTranslator_ hr i_fmt o_fmt dat))
-----------
type VirtualMachine hr nml = Label hr (UVirtualMachine hr nml)
type File8Data hr fmt dat = Label hr (UFile8Data hr fmt dat)

class Translation_Hierarchy (hr :: * -> *) where
    -- * =>三种文件:
    type UFile8Data hr :: * -> * -> *
    -- * =>两种程序:
    type UVirtualMachine hr :: * -> *

    ----------------------
    ----------------------
    -- *三种文件:
    -- File8Data hr fmt dat
    -- File8VirtualMachine hr fmt nml
    -- File8Translator hr fmt i_fmt o_fmt

    -- *两种程序:
    -- VirtualMachine hr nml
    -- Translator hr i_fmt o_fmt

    -- *基本操作:
    load_vm_999 :: (VirtualMachine hr _Z) -> (File8VirtualMachine hr _Z _V) -> (VirtualMachine hr _V)
      -- vm_V_996 = load_vm_999 vm_Z_996 vm_V_6Z
    load_vm_999 = load_fl_999

    load_tr_999 :: (VirtualMachine hr _V) -> (File8Translator hr _V _Y _X) -> (Translator hr _Y _X)
      -- tr_X5Y_996 = load_tr_999 vm_Z_996 tr_X5Y_6Z
    load_tr_999 = load_fl_999

    load_fl_999 :: (VirtualMachine hr _Z) -> (File8Data hr _Z _D) -> Label hr _D
      -- dat_D_999 = load_fl_999 vm_Z_996 dat_D_6Z


    cat_vm_fl_999 :: (File8VirtualMachine hr _Y _X) -> (File8VirtualMachine hr _Z _Y) -> (File8VirtualMachine hr _Z _X)
      -- vm_X_6Z = cat_vm_fl_999 vm_X_6Y vm_Y_6Z

    cat_tr_prg_999 :: (Translator hr _Y _X) -> (Translator hr _Z _Y) -> (Translator hr _Z _X)
      -- tr_X5Z_996 = cat_tr_prg_999 tr_X5Y_996 tr_Y5Z_996


    exec_tr_tr_999 :: (Translator hr _Y _X) -> (File8Translator hr _Y i_fmt o_fmt) -> (File8Translator hr _X i_fmt o_fmt)
      -- tr_O5I_6X = exec_tr_tr_999 tr_X5Y_996 tr_O5I_6Y
    exec_tr_tr_999 = exec_tr_fl_999

    exec_tr_vm_999 :: (Translator hr _Y _X) -> (File8VirtualMachine hr _Y _V) -> (File8VirtualMachine hr _X _V)
      -- vm_V_6X = exec_tr_vm_999 tr_X5Y_996 vm_V_6Y
    exec_tr_vm_999 = exec_tr_fl_999

    exec_tr_fl_999 :: (Translator hr _Y _X) -> (File8Data hr _Y _D) -> (File8Data hr _X _D)
      -- dat_D_6X = exec_tr_fl_999 tr_X5Y_996 dat_D_6Y
      -- tr_X5Y_999 = exec_tr_fl_999 tr_X5Y_996
    -- exec_tr_fl_999 = id
    -- default exec_tr_fl_999 :: Applicative hr => (Translator hr _Y _X) -> (File8Data hr _Y _D) -> (File8Data hr _X _D)
    -- exec_tr_fl_999 = (<*>)

    -- exec_tr_fl_999 tr fl = Mk_Label . unbox_Label tr $ unbox_Label fl
        -- fail:using unbox_Label
    exec_tr_fl_999 (Mk_Label tr) fl = Mk_Label . tr $ unbox_Label fl
        -- ok:using Mk_Label


-- class Translation_Hierarchy hr where




class Is_Similar_Dialect o i where
    --is_similar_dialect
    -- Too many parameters for class ‘Is_Similar_Dialect’
    --  (Enable MultiParamTypeClasses to allow multi-parameter classes)
class (Is_Similar_Dialect o_fmt8o_back_end o_fmt8i_back_end, Translation_Hierarchy hr) => Manually_Adapt_Back_End_Dialect hr fmt i_fmt8io_front_end o_fmt8i_back_end o_fmt8o_back_end where
    manually_adapt_back_end_dialect__999 :: (File8Translator hr fmt i_fmt8io_front_end o_fmt8i_back_end) -> (File8Translator hr fmt i_fmt8io_front_end o_fmt8o_back_end)
      -- tr_M5P_6Z = manually_adapt_back_end_dialect__999 tr_V5P_6Z
class (Is_Similar_Dialect i_fmt8o_front_end i_fmt8i_front_end, Translation_Hierarchy hr) => Manually_Adapt_Front_End_Dialect hr fmt o_fmt8io_back_end i_fmt8i_front_end i_fmt8o_front_end where
    manually_adapt_front_end_dialect__999 :: (File8Translator hr fmt i_fmt8i_front_end o_fmt8io_back_end) -> (File8Translator hr fmt i_fmt8o_front_end o_fmt8io_back_end)
      -- tr_V5H_6Z = manually_adapt_front_end_dialect__999 tr_V5P_6Z


{-
非必要:
type UFile8Script hr fmt i_dat o_dat = UFile8Data hr fmt (UScript hr i_dat o_dat)
    -- universal-raw-prg_X5Y_6Z
type File8Script hr fmt i_dat o_dat = Label hr (UFile8Script hr fmt i_dat o_dat)
    -- prg_X5Y_6Z
    -- labelled-prg_X5Y_6Z
type UScript (hr :: * -> *) i_dat o_dat = (i_dat -> o_dat)
    -- prg_X5Y_999
type Script hr i_dat o_dat = Label hr (UScript hr i_dat o_dat)
    -- prg_X5Y_996

class Manually_Cat4File8Script hr fmt i_dat tmp_dat o_dat where
    manually_cat_prg_fl_999 :: (File8Script hr fmt tmp_dat o_dat) -> (File8Script hr fmt i_dat tmp_dat) -> (File8Script hr fmt i_dat o_dat)
-}
{-
-}



class Manually_Cat4File8Translator hr fmt i_fmt tmp_fmt o_fmt where
    manually_cat_tr_fl_999 :: (File8Translator hr fmt tmp_fmt o_fmt) -> (File8Translator hr fmt i_fmt tmp_fmt) -> (File8Translator hr fmt i_fmt o_fmt)
      -- tr_X5Z_6R = manually_cat_tr_fl_999 tr_X5Y_6R tr_Y5Z_6R

class Is_Subset_Language super_fmt sub_fmt where
    --is_subset_language(super_fmt;sub_fmt)
    -- bug:[super_fmt <: sub_fmt]
    -- [sub_fmt <: super_fmt]

class Is_Subset_Language super_fmt sub_fmt => Lift_Subset_Language hr super_fmt sub_fmt where
    lift_subset_language__fl__999 :: (File8Data hr sub_fmt dat) -> (File8Data hr super_fmt dat)
      -- dat_D_6G = lift_subset_language__fl__999 dat_D_6K
      -- ==>>:
      -- tr_X5Y_6G = lift_subset_language__fl__999 tr_X5Y_6K
      -- vm_V_6G = lift_subset_language__fl__999 vm_V_6K


    -- lift_subset_language__half_tr_flO__999 :: (File8Data hr fmt (UScript hr i_dat (UFile8Data hr sub_fmt o_dat))) -> (File8Data hr fmt (UScript hr i_dat (UFile8Data hr super_fmt o_dat)))
    lift_subset_language__tr_flO__999 :: (File8Translator hr fmt i_fmt sub_fmt) -> (File8Translator hr fmt i_fmt super_fmt)
      -- tr_G5Y_6Z = lift_subset_language__tr_flO__999 tr_K5Y_6Z

    -- lift_subset_language__half_tr_flI__999 :: (File8Data hr fmt (UScript hr (UFile8Data hr super_fmt o_dat) o_dat)) -> (File8Data hr fmt (UScript hr (UFile8Data hr sub_fmt o_dat) o_dat))
    lift_subset_language__tr_flI__999 :: (File8Translator hr fmt super_fmt o_fmt) -> (File8Translator hr fmt sub_fmt o_fmt)
      -- tr_X5K_6Z = lift_subset_language__tr_flI__999 tr_X5G_6Z


    lift_subset_language__tr_prgO__999 :: (Translator hr i_fmt sub_fmt) -> (Translator hr i_fmt super_fmt)
      -- tr_G5Y_996 = lift_subset_language__tr_prgO__999 tr_K5Y_996
    lift_subset_language__tr_prgI__999 :: (Translator hr super_fmt o_fmt) -> (Translator hr sub_fmt o_fmt)
      -- tr_X5K_996 = lift_subset_language__tr_prgI__999 tr_X5G_996

-- end:class Is_Subset_Language super_fmt sub_fmt => Lift_Subset_Language hr super_fmt sub_fmt where

lift_subset_language__tr_fl__999 :: (Lift_Subset_Language hr _Z _C, Lift_Subset_Language hr _B _Y, Lift_Subset_Language hr _X _A) => (File8Translator hr _C _B _A) -> (File8Translator hr _Z _Y _X)
lift_subset_language__tr_fl__999 = lift_subset_language__fl__999 . lift_subset_language__tr_flI__999 . lift_subset_language__tr_flO__999

lift_subset_language__tr_prg__999 :: (Lift_Subset_Language hr _B _Y, Lift_Subset_Language hr _X _A) => (Translator hr _B _A) -> (Translator hr _Y _X)
lift_subset_language__tr_prg__999 = lift_subset_language__tr_prgI__999 . lift_subset_language__tr_prgO__999
      -- tr_F5K_6H = lift_subset_language__tr_fl__999 tr_E5G_6A
      --    [A <: H]
      -- tr_F5K_996 = lift_subset_language__tr_prg__999 tr_E5G_996
      --    [E <: F]
      --    [K <: G]









{-
-- SECTION:porting
===
:s/\v%(^|\A@<=)(\a)(\a*)/\u\1\L\2/g
    大写化首字母
===
    .+3,$s/runV_6R/vm_V_6R/g
    .+3,$s/runV_9R/vm_V_9R/g
    runW_9R-->vm_W_996
.+3,$s/run\(\u\)_6\(\u\)/vm_\1_6\2/g
.+3,$s/run\(\u\)_9\(\u\)/vm_\1_9\2/g
===
%s/translateFL_\(\u\)_999/run_tr6\1_999/g
    translateFL_P_999-->run_tr6P_999
%s/\<\(tr_\(\u\)5\(\u\)_99\)9\>/\16/g
  tr_X5Y_999-->tr_X5Y_996
%s/vm_\(\u\)_999/vm_\1_996/g
  vm_V_999-->vm_V_996
===



=====================
[:def__portable_interpretive_compiler_kit]:here
=====================
#package:
[portable_interpretive_compiler_kit(V,P) =[def]= (tr_V5P_6P,tr_V5P_6V,vm_V_6P)]
#package4specific_machine:
[installer4portable_interpretive_compiler_kit(V,P,M) =[def]= (portable_interpretive_compiler_kit(V,P),vm_V_6M,tr_M5P_6P)]
  #安装时生成:tr_M5P_6M
  # !! [tr_M5P_6M占用空间远大于tr_M5P_6P]
[native_kit4portable_interpretive_compiler_kit(V,P,M) =[def]= (portable_interpretive_compiler_kit(V,P),vm_V_6M,tr_M5P_6M)]
  #目标机实际运行时使用的工具包
=====================

=====================
使用情景:3个:
  *辅助起草冫便携式灬
  *打包生成冫安装包灬
  *安装生成冫本地包灬
prepare4portable_interpretive_compiler_kit
prepare4installer4portable_interpretive_compiler_kit
prepare4native_kit4portable_interpretive_compiler_kit
=====================
-}

--newtype Portable_Interpretive_Compiler_Kit hr vm_code/virtual_machine_bytecode portable_language
newtype Portable_Interpretive_Compiler_Kit hr _V _P
    = Mk_Portable_Interpretive_Compiler_Kit ((File8Translator hr _P _P _V), (File8Translator hr _V _P _V), (File8VirtualMachine hr _P _V))
    -- (tr_V5P_6P,tr_V5P_6V,vm_V_6P)

--newtype Installer4Portable_Interpretive_Compiler_Kit hr vm_code/virtual_machine_bytecode portable_language target_machine_code
newtype Installer4Portable_Interpretive_Compiler_Kit hr _V _P _M
    = Mk_Installer4Portable_Interpretive_Compiler_Kit (Portable_Interpretive_Compiler_Kit hr _V _P, (File8VirtualMachine hr _M _V), (File8Translator hr _P _P _M))
    -- (portable_interpretive_compiler_kit(V,P),vm_V_6M,tr_M5P_6P)


--newtype Native_Kit4Portable_Interpretive_Compiler_Kit hr vm_code/virtual_machine_bytecode portable_language target_machine_code
newtype Native_Kit4Portable_Interpretive_Compiler_Kit hr _V _P _M
    = Mk_Native_Kit4Portable_Interpretive_Compiler_Kit (Portable_Interpretive_Compiler_Kit hr _V _P, (File8VirtualMachine hr _M _V), (File8Translator hr _M _P _M))
    -- (portable_interpretive_compiler_kit(V,P),vm_V_6M,tr_M5P_6M)










mk0__run_tr6P_999 :: (Translation_Hierarchy hr) => (VirtualMachine hr _P) -> ((File8Translator hr _P i_fmt o_fmt) -> (File8Data hr i_fmt dat) -> (File8Data hr o_fmt dat))
mk0__run_tr6P_999 vm_P_996 = if True then _1_run_tr6P_999 else run_tr6P_999 where
    _1_run_tr6P_999 = exec_tr_fl_999 . load_tr_999 vm_P_996
    ---------
    ---------
    run_tr6P_999 tr_X5Y_6P dat_D_6Y = dat_D_6X where
        tr_X5Y_996 = load_tr_999 vm_P_996 tr_X5Y_6P
        dat_D_6X = exec_tr_fl_999 tr_X5Y_996 dat_D_6Y
          -- ->: dat_D_6X
        -- [:def____run_tr6P_999]:here
        -- dat_D_6X = run_tr6P_999 tr_X5Y_6P dat_D_6Y




mk1__run_tr6P_999 :: forall hr _W _P i_fmt o_fmt dat . (Translation_Hierarchy hr) => (File8Translator hr _W _P _W) -> (VirtualMachine hr _W) -> ((File8Translator hr _P i_fmt o_fmt) -> (File8Data hr i_fmt dat) -> (File8Data hr o_fmt dat))
mk1__run_tr6P_999 tr_W5P_6W vm_W_996 = if True then _1_run_tr6P_999 else run_tr6P_999 where
    -- _1_run_tr6P_999 = (mk0__run_tr6P_999 vm_W_996) . (mk0__run_tr6P_999 vm_W_996) tr_W5P_6W
    _1_run_tr6P_999 = run_tr6W_999 . run_tr6W_999 tr_W5P_6W
    run_tr6W_999 :: forall i_fmt o_fmt dat . ((File8Translator hr _W i_fmt o_fmt) -> (File8Data hr i_fmt dat) -> (File8Data hr o_fmt dat))
        -- {-# LANGUAGE ExplicitForAll #-}
        -- {-# LANGUAGE ScopedTypeVariables #-}
    ---------
    ---------
    run_tr6W_999 = mk0__run_tr6P_999 vm_W_996
    -- run_tr6P_999 = run_tr6W_999 . run_tr6W_999 tr_W5P_6W
    --run_tr6P_999 tr_X5Y_6P dat_D_6Y = do
    run_tr6P_999 tr_X5Y_6P dat_D_6Y = dat_D_6X where
      tr_X5Y_6W = run_tr6W_999 tr_W5P_6W tr_X5Y_6P
      dat_D_6X = mk0__run_tr6P_999 vm_W_996 tr_X5Y_6W dat_D_6Y
        -- <==>[SHOULD_BE]:run_tr6W_999 tr_X5Y_6W dat_D_6Y
    --
    -- [:def____run_tr6P_999]:goto
    --





mk2__run_tr6P_999 :: (Translation_Hierarchy hr) => Either ((File8VirtualMachine hr _W _P)) ((File8Translator hr _W _P _W)) -> (VirtualMachine hr _W) -> ((File8Translator hr _P i_fmt o_fmt) -> (File8Data hr i_fmt dat) -> (File8Data hr o_fmt dat))
    -- either__vm_P_6W__tr_W5P_6W
mk2__run_tr6P_999 (Left vm_P_6W) vm_W_996 = if True then _1_run_tr6P_999 else run_tr6P_999 where
    _1_run_tr6P_999 = mk0__run_tr6P_999 (load_vm_999 vm_W_996 vm_P_6W)
    ---------
    ---------
    run_tr6P_999 tr_X5Y_6P dat_D_6Y = dat_D_6X where
        vm_P_996 = load_vm_999 vm_W_996 vm_P_6W
        dat_D_6X = mk0__run_tr6P_999 vm_P_996 tr_X5Y_6P dat_D_6Y
mk2__run_tr6P_999 (Right tr_W5P_6W) vm_W_996 = run_tr6P_999 where
    run_tr6P_999 = mk1__run_tr6P_999 tr_W5P_6W vm_W_996






mk3__run_tr6P_999 :: (Translation_Hierarchy hr) => (File8Translator hr _V _P _V) -> Either ((File8VirtualMachine hr _W _V)) ((File8Translator hr _W _P _W)) -> (VirtualMachine hr _W) -> ((File8Translator hr _P i_fmt o_fmt) -> (File8Data hr i_fmt dat) -> (File8Data hr o_fmt dat))
    -- either__vm_V_6W__tr_W5P_6W
mk3__run_tr6P_999 tr_V5P_6V either__vm_V_6W__tr_W5P_6W vm_W_996 = run_tr6P_999 where
    -- (tr_X5P_6X, vm_X_996) :: (File8Translator hr _W _P _W, VirtualMachine hr _W)
    run_tr6P_999 = case either__vm_V_6W__tr_W5P_6W of
      (Right tr_W5P_6W) ->
            mk1__run_tr6P_999 tr_W5P_6W vm_W_996
      (Left vm_V_6W) ->
        let vm_V_996 = load_vm_999 vm_W_996 vm_V_6W
        in  mk1__run_tr6P_999 tr_V5P_6V vm_V_996
    -------











-- 辅助起草冫便携式灬
-- [(tr_V5P_6P,vm_V_6P,(vm_P_6W|tr_W5P_6W),vm_W_996) -> portable_interpretive_compiler_kit(V,P)]
prepare4portable_interpretive_compiler_kit :: (Translation_Hierarchy hr) => (File8Translator hr _P _P _V) -> (File8VirtualMachine hr _P _V) -> Either ((File8VirtualMachine hr _W _P)) ((File8Translator hr _W _P _W)) -> (VirtualMachine hr _W) -> (Portable_Interpretive_Compiler_Kit hr _V _P)
prepare4portable_interpretive_compiler_kit tr_V5P_6P vm_V_6P either__vm_P_6W__tr_W5P_6W vm_W_996 = portable_interpretive_compiler_kit where
    run_tr6P_999 = mk2__run_tr6P_999 either__vm_P_6W__tr_W5P_6W vm_W_996
    tr_V5P_6V = run_tr6P_999 tr_V5P_6P tr_V5P_6P
    portable_interpretive_compiler_kit = Mk_Portable_Interpretive_Compiler_Kit (tr_V5P_6P,tr_V5P_6V,vm_V_6P)







-- 打包生成冫安装包灬
-- [(tr_V5P_6P,tr_V5P_6V,vm_V_6P,{similar(V,M)},manually_V5P_P_back_end_dialectM_999,(vm_V_6W|tr_W5P_6W),vm_W_996) -> (vm_V_6M,tr_M5P_6P)]
prepare4installer4portable_interpretive_compiler_kit :: (Translation_Hierarchy hr, Manually_Adapt_Back_End_Dialect hr _P _P _V _M) => (Portable_Interpretive_Compiler_Kit hr _V _P) -> Either ((File8VirtualMachine hr _W _V)) ((File8Translator hr _W _P _W)) -> (VirtualMachine hr _W) -> (Installer4Portable_Interpretive_Compiler_Kit hr _V _P _M)
prepare4installer4portable_interpretive_compiler_kit portable_interpretive_compiler_kit@(Mk_Portable_Interpretive_Compiler_Kit (tr_V5P_6P,tr_V5P_6V,vm_V_6P)) either__vm_V_6W__tr_W5P_6W vm_W_996 = installer4portable_interpretive_compiler_kit where
    run_tr6P_999 = mk3__run_tr6P_999 tr_V5P_6V either__vm_V_6W__tr_W5P_6W vm_W_996
    tr_M5P_6P = manually_adapt_back_end_dialect__999 tr_V5P_6P
    vm_V_6M = run_tr6P_999 tr_M5P_6P vm_V_6P
    installer4portable_interpretive_compiler_kit = Mk_Installer4Portable_Interpretive_Compiler_Kit (portable_interpretive_compiler_kit,vm_V_6M,tr_M5P_6P)







-- 安装生成冫本地包灬
prepare4native_kit4portable_interpretive_compiler_kit :: (Translation_Hierarchy hr, Manually_Adapt_Back_End_Dialect hr _P _P _V _M) => (Installer4Portable_Interpretive_Compiler_Kit hr _V _P _M) -> (VirtualMachine hr _M) -> (Native_Kit4Portable_Interpretive_Compiler_Kit hr _V _P _M)
prepare4native_kit4portable_interpretive_compiler_kit installer4portable_interpretive_compiler_kit@(Mk_Installer4Portable_Interpretive_Compiler_Kit (portable_interpretive_compiler_kit@(Mk_Portable_Interpretive_Compiler_Kit (tr_V5P_6P,tr_V5P_6V,vm_V_6P)),vm_V_6M,tr_M5P_6P)) vm_M_996 = native_kit4portable_interpretive_compiler_kit where
    either__vm_V_6M__tr_M5P_6M = Left vm_V_6M
    run_tr6P_999 = mk3__run_tr6P_999 tr_V5P_6V either__vm_V_6M__tr_M5P_6M vm_M_996
    tr_M5P_6M = run_tr6P_999 tr_M5P_6P tr_M5P_6P
    native_kit4portable_interpretive_compiler_kit = Mk_Native_Kit4Portable_Interpretive_Compiler_Kit (portable_interpretive_compiler_kit,vm_V_6M,tr_M5P_6M)













{-
-}
{-
-}
