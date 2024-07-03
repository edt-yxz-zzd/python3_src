-- __all__:goto
-- SECTION:goto

{-# LANGUAGE KindSignatures #-}
{-# LANGUAGE TypeFamilies #-}
{-# LANGUAGE MultiParamTypeClasses #-}
{- xxx -}

{-
e ../../python3_src/haskell_src/Framework4Translation.hs

view others/数学/编程/编译/翻译框架设计.txt
view ../../python3_src/haskell_src/Framework4Translation-ver2-tedious.hs
runghc ../../python3_src/haskell_src/Framework4Translation.hs



view ../lots/NOTE/Haskell/01start.txt
view ../lots/NOTE/Haskell/run_hs_script.txt

$ ghci
Prelude> :?
Prelude> :show imports
import Prelude -- implicit
Prelude> :browse Prelude
Prelude> :quit

ghci '--show-options' | grep GADT



-}


-- __all__:here
module Framework4Translation
(main
,Translation_Hierarchy(..)
,File8VirtualMachine
,File8Translator
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
,mk0__translateFL_P_999
,mk1__translateFL_P_999
,mk2__translateFL_P_999
,mk3__translateFL_P_999
    -- [:def____translateFL_P_999]:goto
    -- 运行器{P-翻译诀tr_X5Y_6P}
    -- dat_D_6X <- translateFL_P_999 tr_X5Y_6P dat_D_6Y
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
--
--
)
where

main = print "ok"
-- __all__




{-
-- SECTION:typing


abbr:
    nml:native_machine_language
    fmt:file_format
    fl:file
    prg:program
    tr:translate
    vm:virtual_machine
    dat:data
naming:
    xxx_6Z:file-name
    xxx_999:program-name

ver2-to-ver3:
  ver2 任意数据 导致 需要 (load/eval/dump)中dump 区别 对待 文件
  ver3 只考虑 数据{file2file/程序纟文件变换} 去掉 (load/eval/dump)中的，只保留 load{file2file}



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
vm_V_999 :: VirtualMachine V
  VirtualMachine nml

tr_X5Y_999 :: Translator Y X
  Translator i_fmt o_fmt

*基本操作:
load_vm_999 :: VirtualMachine Z -> File8VirtualMachine Z V -> VirtualMachine V
  vm_V_999 = load_vm_999 vm_Z_999 vm_V_6Z

load_tr_999 :: VirtualMachine V -> File8Translator V Y X -> Translator Y X
  tr_X5Y_999 = load_tr_999 vm_Z_999 tr_X5Y_6Z

load_fl_999 :: VirtualMachine Z -> File8Data Z dat -> hr dat
  dat_D_999 = load_fl_999 vm_Z_999 dat_D_6Z

cat_vm_fl_999 :: File8VirtualMachine Y X -> File8VirtualMachine Z Y -> File8VirtualMachine Z X
  vm_X_6Z = cat_vm_fl_999 vm_X_6Y vm_Y_6Z

cat_tr_prg_999 :: Translator Y X -> Translator Z Y -> Translator Z X
  tr_X5Z_999 = cat_tr_prg_999 tr_X5Y_999 tr_Y5Z_999


exec_tr_tr_999 :: Translator Y X -> (File8Translator Y i_fmt o_fmt -> File8Translator X i_fmt o_fmt)
  tr_O5I_6X = exec_tr_tr_999 tr_X5Y_999 tr_O5I_6Y

exec_tr_vm_999 :: Translator Y X -> (File8VirtualMachine Y V -> File8VirtualMachine X V)
  vm_V_6X = exec_tr_vm_999 tr_X5Y_999 vm_V_6Y

exec_tr_fl_999 :: Translator Y X -> (File8Data Y D -> File8Data X D)
  dat_D_6X = exec_tr_fl_999 tr_X5Y_999 dat_D_6Y



translateFL_P_999 :: File8Translator P Y X -> (File8Data Y D -> File8Data X D)
  ==>>:++hr:
  translateFL_P_999 :: File8Translator P Y X -> (File8Data Y D -> hr (File8Data X D))
  mk0__translateFL_P_999
    -- [:def____translateFL_P_999]:goto


others:
  tr_M5P_6Z = manually_adapt_back_end_dialect__999 tr_V5P_6Z
  tr_V5H_6Z = manually_adapt_front_end_dialect__999 tr_V5P_6Z
  tr_X5Z_6R = manually_cat_tr_fl_999 tr_X5Y_6R tr_Y5Z_6R
  dat_D_6G = lift_subset_language__999 dat_D_6C
      ==>>:
      tr_X5Y_6G = lift_subset_language__999 tr_X5Y_6C
      vm_V_6G = lift_subset_language__999 vm_V_6C


==>>:
目标:翻译
  长期性目标:翻译诀:tr_X5Y_6Z
  过渡性目标:翻译器:tr_X5Y_999
  辅助性目标:虚拟机:vm_V_999
  辅助性目标:虚拟诀:vm_V_6Z
#下面的『至多一次』表示『局域同类串联可以一步到位』
#下面的『可能多次』导致分支复杂化:
  manually_cat_tr_fl_999
  cat_tr_prg_999
  cat_vm_fl_999
构造器{翻译诀/tr_X5Y_6Z}:
  tr_O5I_6X = exec_tr_tr_999 tr_X5Y_999 tr_O5I_6Y
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
  tr_X5Y_6G = lift_subset_language__999 tr_X5Y_6C
      提升冫翻译诀
      至多一次#一步到位
构造器{翻译器/tr_X5Y_999}:
  tr_X5Y_999 = load_tr_999 vm_Z_999 tr_X5Y_6Z
      装载冫翻译器
      至多一次<<==cat_vm_fl_999
  tr_X5Z_999 = cat_tr_prg_999 tr_X5Y_999 tr_Y5Z_999
      串联冫翻译器
      可能多次
构造器{虚拟机/vm_X_999}:
  vm_V_999 = load_vm_999 vm_Z_999 vm_V_6Z
      运行冫虚拟机
      至多一次<<==cat_vm_fl_999
构造器{虚拟诀/vm_X_6Z}:
  vm_X_6Z = cat_vm_fl_999 vm_X_6Y vm_Y_6Z
      堆叠冫虚拟诀
      可能多次
  vm_V_6X = exec_tr_vm_999 tr_X5Y_999 vm_V_6Y
      翻译冫虚拟诀
      至多一次<<==cat_tr_prg_999
  vm_V_6G = lift_subset_language__999 vm_V_6C
      提升冫虚拟诀
      至多一次#一步到位



-}


type File8VirtualMachine hr fmt nml = File8Data hr fmt (VirtualMachine hr nml)
type File8Translator hr fmt i_fmt o_fmt = File8Data hr fmt (Translator hr i_fmt o_fmt)
class Monad hr => Translation_Hierarchy hr where
    -- *三种文件:
    type File8Data hr :: * -> * -> *
    -- type File8VirtualMachine hr :: * -> * -> *
    -- type File8Translator hr :: * -> * -> * -> *
    -- type File8Data hr fmt dat :: *
    -- type File8VirtualMachine hr fmt nml :: *
    -- type File8Translator hr fmt i_fmt o_fmt :: *

    -- *两种程序:
    type VirtualMachine hr :: * -> *
    type Translator hr :: * -> * -> *
    -- type VirtualMachine hr nml :: *
    -- type Translator hr i_fmt o_fmt :: *

    -- *基本操作:
    load_vm_999 :: VirtualMachine hr _Z -> File8VirtualMachine hr _Z _V -> hr (VirtualMachine hr _V)
      -- vm_V_999_7hr = load_vm_999 vm_Z_999 vm_V_6Z
      -- vm_V_999 <- load_vm_999 vm_Z_999 vm_V_6Z
    load_vm_999 = load_fl_999

    load_tr_999 :: VirtualMachine hr _V -> File8Translator hr _V _Y _X -> hr (Translator hr _Y _X)
      -- tr_X5Y_999_7hr = load_tr_999 vm_Z_999 tr_X5Y_6Z
      -- tr_X5Y_999 <- load_tr_999 vm_Z_999 tr_X5Y_6Z
    load_tr_999 = load_fl_999

    load_fl_999 :: VirtualMachine hr _Z -> File8Data hr _Z _D -> hr _D
      -- dat_D_999_7hr = load_fl_999 vm_Z_999 dat_D_6Z
      -- dat_D_999 <- load_fl_999 vm_Z_999 dat_D_6Z


    cat_vm_fl_999 :: File8VirtualMachine hr _Y _X -> File8VirtualMachine hr _Z _Y -> hr (File8VirtualMachine hr _Z _X)
      -- vm_X_6Z_7hr = cat_vm_fl_999 vm_X_6Y vm_Y_6Z
      -- vm_X_6Z <- cat_vm_fl_999 vm_X_6Y vm_Y_6Z

    cat_tr_prg_999 :: Translator hr _Y _X -> Translator hr _Z _Y -> hr (Translator hr _Z _X)
      -- tr_X5Z_999_7hr = cat_tr_prg_999 tr_X5Y_999 tr_Y5Z_999
      -- tr_X5Z_999 <- cat_tr_prg_999 tr_X5Y_999 tr_Y5Z_999


    exec_tr_tr_999 :: Translator hr _Y _X -> File8Translator hr _Y i_fmt o_fmt -> hr (File8Translator hr _X i_fmt o_fmt)
      -- tr_O5I_6X_7hr = exec_tr_tr_999 tr_X5Y_999 tr_O5I_6Y
      -- tr_O5I_6X <- exec_tr_tr_999 tr_X5Y_999 tr_O5I_6Y
    exec_tr_tr_999 = exec_tr_fl_999

    exec_tr_vm_999 :: Translator hr _Y _X -> File8VirtualMachine hr _Y _V -> hr (File8VirtualMachine hr _X _V)
      -- vm_V_6X_7hr = exec_tr_vm_999 tr_X5Y_999 vm_V_6Y
      -- vm_V_6X <- exec_tr_vm_999 tr_X5Y_999 vm_V_6Y
    exec_tr_vm_999 = exec_tr_fl_999

    exec_tr_fl_999 :: Translator hr _Y _X -> File8Data hr _Y _D -> hr (File8Data hr _X _D)
      -- dat_D_6X_7hr = exec_tr_fl_999 tr_X5Y_999 dat_D_6Y
      -- dat_D_6X <- exec_tr_fl_999 tr_X5Y_999 dat_D_6Y
-- class Monad hr => Translation_Hierarchy hr where




class Is_Similar_Dialect o i where
    --is_similar_dialect
    -- Too many parameters for class ‘Is_Similar_Dialect’
    --  (Enable MultiParamTypeClasses to allow multi-parameter classes)
class (Is_Similar_Dialect o_fmt8o_back_end o_fmt8i_back_end, Translation_Hierarchy hr) => Manually_Adapt_Back_End_Dialect hr fmt i_fmt8io_front_end o_fmt8i_back_end o_fmt8o_back_end where
    manually_adapt_back_end_dialect__999 :: File8Translator hr fmt i_fmt8io_front_end o_fmt8i_back_end -> hr (File8Translator hr fmt i_fmt8io_front_end o_fmt8o_back_end)
      -- tr_M5P_6Z <- manually_adapt_back_end_dialect__999 tr_V5P_6Z
class (Is_Similar_Dialect i_fmt8o_front_end i_fmt8i_front_end, Translation_Hierarchy hr) => Manually_Adapt_Front_End_Dialect hr fmt o_fmt8io_back_end i_fmt8i_front_end i_fmt8o_front_end where
    manually_adapt_front_end_dialect__999 :: File8Translator hr fmt i_fmt8i_front_end o_fmt8io_back_end -> hr (File8Translator hr fmt i_fmt8o_front_end o_fmt8io_back_end)
      -- tr_V5H_6Z <- manually_adapt_front_end_dialect__999 tr_V5P_6Z


{-
class Manually_Cat4File8Script hr fmt output_type middle_type input_type where
    manually_cat_prg_fl_999 :: File8Script hr fmt middle_type output_type -> File8Script hr fmt input_type middle_type -> hr (File8Script hr fmt input_type output_type)
-}



class Manually_Cat4File8Translator hr fmt i_fmt tmp_fmt o_fmt where
    manually_cat_tr_fl_999 :: File8Translator hr fmt tmp_fmt o_fmt -> File8Translator hr fmt i_fmt tmp_fmt -> hr (File8Translator hr fmt i_fmt o_fmt)
      -- tr_X5Z_6R <- manually_cat_tr_fl_999 tr_X5Y_6R tr_Y5Z_6R

class Is_Subset_Language super_fmt sub_fmt where
    --is_subset_language(super_fmt;sub_fmt)
    -- [super_fmt <: sub_fmt]

class Is_Subset_Language super_fmt sub_fmt => Lift_Subset_Language hr super_fmt sub_fmt where
    lift_subset_language__999 :: File8Data hr sub_fmt dat -> hr (File8Data hr super_fmt dat)
      -- dat_D_6G <- lift_subset_language__999 dat_D_6C
      -- ==>>:
      -- tr_X5Y_6G <- lift_subset_language__999 tr_X5Y_6C
      -- vm_V_6G <- lift_subset_language__999 vm_V_6C















{-
-- SECTION:porting
===
:s/\v%(^|\A@<=)(\a)(\a*)/\u\1\L\2/g
    大写化首字母
===
    .+3,$s/runV_6R/vm_V_6R/g
    .+3,$s/runV_9R/vm_V_9R/g
    runW_9R-->vm_W_999
.+3,$s/run\(\u\)_6\(\u\)/vm_\1_6\2/g
.+3,$s/run\(\u\)_9\(\u\)/vm_\1_9\2/g
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
    = Mk_Portable_Interpretive_Compiler_Kit (File8Translator hr _P _P _V, File8Translator hr _V _P _V, File8VirtualMachine hr _P _V)
    -- (tr_V5P_6P,tr_V5P_6V,vm_V_6P)

--newtype Installer4Portable_Interpretive_Compiler_Kit hr vm_code/virtual_machine_bytecode portable_language target_machine_code
newtype Installer4Portable_Interpretive_Compiler_Kit hr _V _P _M
    = Mk_Installer4Portable_Interpretive_Compiler_Kit (Portable_Interpretive_Compiler_Kit hr _V _P, File8VirtualMachine hr _M _V, File8Translator hr _P _P _M)
    -- (portable_interpretive_compiler_kit(V,P),vm_V_6M,tr_M5P_6P)


--newtype Native_Kit4Portable_Interpretive_Compiler_Kit hr vm_code/virtual_machine_bytecode portable_language target_machine_code
newtype Native_Kit4Portable_Interpretive_Compiler_Kit hr _V _P _M
    = Mk_Native_Kit4Portable_Interpretive_Compiler_Kit (Portable_Interpretive_Compiler_Kit hr _V _P, File8VirtualMachine hr _M _V, File8Translator hr _M _P _M)
    -- (portable_interpretive_compiler_kit(V,P),vm_V_6M,tr_M5P_6M)







lift4ma_b :: Monad m => (a -> b -> m c) -> (m a -> b -> m c)
lift4ma_b a2b2mc ma b = flip a2b2mc b =<< ma
lift4ma_b_c :: Monad m => (a -> b -> c -> m d) -> (m a -> b -> c -> m d)
lift4ma_b_c a2b2c2md ma b c = (flip flip c . flip flip b $ a2b2c2md) =<< ma



mk0__translateFL_P_999 :: (Translation_Hierarchy hr) => VirtualMachine hr _P -> (File8Translator hr _P i_fmt o_fmt -> File8Data hr i_fmt dat -> hr (File8Data hr o_fmt dat))
mk0__translateFL_P_999 vm_P_999 = if True then _1_translateFL_P_999 else translateFL_P_999 where
    _1_translateFL_P_999 = lift4ma_b exec_tr_fl_999 . load_tr_999 vm_P_999
    ---------
    ---------
    translateFL_P_999 tr_X5Y_6P dat_D_6Y = do
        tr_X5Y_999 <- load_tr_999 vm_P_999 tr_X5Y_6P
        exec_tr_fl_999 tr_X5Y_999 dat_D_6Y
          -- ->: dat_D_6X
        -- [:def____translateFL_P_999]:here
        -- dat_D_6X <- translateFL_P_999 tr_X5Y_6P dat_D_6Y




mk1__translateFL_P_999 :: (Translation_Hierarchy hr) => File8Translator hr _W _P _W -> VirtualMachine hr _W -> (File8Translator hr _P i_fmt o_fmt -> File8Data hr i_fmt dat -> hr (File8Data hr o_fmt dat))
mk1__translateFL_P_999 tr_W5P_6W vm_W_999 = if True then _1_translateFL_P_999 else translateFL_P_999 where
    _1_translateFL_P_999 = lift4ma_b (mk0__translateFL_P_999 vm_W_999) . (mk0__translateFL_P_999 vm_W_999) tr_W5P_6W
    ---------
    ---------
    translateFL_W_999 = mk0__translateFL_P_999 vm_W_999
    -- translateFL_P_999 = translateFL_W_999 . translateFL_W_999 tr_W5P_6W
    --translateFL_P_999 tr_X5Y_6P dat_D_6Y = do
    translateFL_P_999 tr_X5Y_6P dat_D_6Y = do
      tr_X5Y_6W <- translateFL_W_999 tr_W5P_6W tr_X5Y_6P
      mk0__translateFL_P_999 vm_W_999 tr_X5Y_6W dat_D_6Y
        -- <==>[SHOULD_BE]:translateFL_W_999 tr_X5Y_6W dat_D_6Y
        -- <==>:
        -- dat_D_6X <- mk0__translateFL_P_999 vm_W_999 tr_X5Y_6W dat_D_6Y
        --return dat_D_6X
    --
    -- [:def____translateFL_P_999]:goto
    --





mk2__translateFL_P_999 :: (Translation_Hierarchy hr) => Either (File8VirtualMachine hr _W _P) (File8Translator hr _W _P _W) -> VirtualMachine hr _W -> (File8Translator hr _P i_fmt o_fmt -> File8Data hr i_fmt dat -> hr (File8Data hr o_fmt dat))
    -- either__vm_P_6W__tr_W5P_6W
mk2__translateFL_P_999 (Left vm_P_6W) vm_W_999 = if True then _1_translateFL_P_999 else translateFL_P_999 where
    _1_translateFL_P_999 = lift4ma_b_c mk0__translateFL_P_999 (load_vm_999 vm_W_999 vm_P_6W)
    ---------
    ---------
    translateFL_P_999 tr_X5Y_6P dat_D_6Y = do
        vm_P_999 <- load_vm_999 vm_W_999 vm_P_6W
        mk0__translateFL_P_999 vm_P_999 tr_X5Y_6P dat_D_6Y
          -- ->:  dat_D_6X
mk2__translateFL_P_999 (Right tr_W5P_6W) vm_W_999 = translateFL_P_999 where
    translateFL_P_999 = mk1__translateFL_P_999 tr_W5P_6W vm_W_999






mk3__translateFL_P_999 :: (Translation_Hierarchy hr) => (File8Translator hr _V _P _V) -> Either (File8VirtualMachine hr _W _V) (File8Translator hr _W _P _W) -> VirtualMachine hr _W -> (File8Translator hr _P i_fmt o_fmt -> File8Data hr i_fmt dat -> hr (File8Data hr o_fmt dat))
    -- either__vm_V_6W__tr_W5P_6W
mk3__translateFL_P_999 tr_V5P_6V either__vm_V_6W__tr_W5P_6W vm_W_999 = translateFL_P_999 where
    -- (tr_X5P_6X, vm_X_999) :: (File8Translator hr _W _P _W, VirtualMachine hr _W)
    --translateFL_P_999 tr_X5Y_6P dat_D_6Y = case either__vm_V_6W__tr_W5P_6W of
    translateFL_P_999 = case either__vm_V_6W__tr_W5P_6W of
      (Right tr_W5P_6W) -> mk1__translateFL_P_999 tr_W5P_6W vm_W_999
      (Left vm_V_6W) -> if True
        then lift4ma_b_c (mk1__translateFL_P_999 tr_V5P_6V) (load_vm_999 vm_W_999 vm_V_6W)
        else \ tr_X5Y_6P dat_D_6Y -> do
          vm_V_999 <- load_vm_999 vm_W_999 vm_V_6W
          mk1__translateFL_P_999 tr_V5P_6V vm_V_999 tr_X5Y_6P dat_D_6Y
    -------











-- 辅助起草冫便携式灬
-- [(tr_V5P_6P,vm_V_6P,(vm_P_6W|tr_W5P_6W),vm_W_999) -> portable_interpretive_compiler_kit(V,P)]
prepare4portable_interpretive_compiler_kit :: (Translation_Hierarchy hr) => File8Translator hr _P _P _V -> File8VirtualMachine hr _P _V -> Either (File8VirtualMachine hr _W _P) (File8Translator hr _W _P _W) -> VirtualMachine hr _W -> hr (Portable_Interpretive_Compiler_Kit hr _V _P)
prepare4portable_interpretive_compiler_kit tr_V5P_6P vm_V_6P either__vm_P_6W__tr_W5P_6W vm_W_999 = do
    let translateFL_P_999 = mk2__translateFL_P_999 either__vm_P_6W__tr_W5P_6W vm_W_999
    tr_V5P_6V <- translateFL_P_999 tr_V5P_6P tr_V5P_6P
    let portable_interpretive_compiler_kit = Mk_Portable_Interpretive_Compiler_Kit (tr_V5P_6P,tr_V5P_6V,vm_V_6P)
    return portable_interpretive_compiler_kit







-- 打包生成冫安装包灬
-- [(tr_V5P_6P,tr_V5P_6V,vm_V_6P,{similar(V,M)},manually_V5P_P_back_end_dialectM_999,(vm_V_6W|tr_W5P_6W),vm_W_999) -> (vm_V_6M,tr_M5P_6P)]
prepare4installer4portable_interpretive_compiler_kit :: (Translation_Hierarchy hr, Manually_Adapt_Back_End_Dialect hr _P _P _V _M) => Portable_Interpretive_Compiler_Kit hr _V _P -> Either (File8VirtualMachine hr _W _V) (File8Translator hr _W _P _W) -> VirtualMachine hr _W -> hr (Installer4Portable_Interpretive_Compiler_Kit hr _V _P _M)
prepare4installer4portable_interpretive_compiler_kit portable_interpretive_compiler_kit@(Mk_Portable_Interpretive_Compiler_Kit (tr_V5P_6P,tr_V5P_6V,vm_V_6P)) either__vm_V_6W__tr_W5P_6W vm_W_999 = do
    let translateFL_P_999 = mk3__translateFL_P_999 tr_V5P_6V either__vm_V_6W__tr_W5P_6W vm_W_999
    tr_M5P_6P <- manually_adapt_back_end_dialect__999 tr_V5P_6P
    vm_V_6M <- translateFL_P_999 tr_M5P_6P vm_V_6P
    let installer4portable_interpretive_compiler_kit = Mk_Installer4Portable_Interpretive_Compiler_Kit (portable_interpretive_compiler_kit,vm_V_6M,tr_M5P_6P)
    return installer4portable_interpretive_compiler_kit







-- 安装生成冫本地包灬
prepare4native_kit4portable_interpretive_compiler_kit :: (Translation_Hierarchy hr, Manually_Adapt_Back_End_Dialect hr _P _P _V _M) => Installer4Portable_Interpretive_Compiler_Kit hr _V _P _M -> VirtualMachine hr _M -> hr (Native_Kit4Portable_Interpretive_Compiler_Kit hr _V _P _M)
prepare4native_kit4portable_interpretive_compiler_kit installer4portable_interpretive_compiler_kit@(Mk_Installer4Portable_Interpretive_Compiler_Kit (portable_interpretive_compiler_kit@(Mk_Portable_Interpretive_Compiler_Kit (tr_V5P_6P,tr_V5P_6V,vm_V_6P)),vm_V_6M,tr_M5P_6P)) vm_M_999 = do
    let either__vm_V_6M__tr_M5P_6M = Left vm_V_6M
        translateFL_P_999 = mk3__translateFL_P_999 tr_V5P_6V either__vm_V_6M__tr_M5P_6M vm_M_999
    tr_M5P_6M <- translateFL_P_999 tr_M5P_6P tr_M5P_6P
    let native_kit4portable_interpretive_compiler_kit = Mk_Native_Kit4Portable_Interpretive_Compiler_Kit (portable_interpretive_compiler_kit,vm_V_6M,tr_M5P_6M)
    return native_kit4portable_interpretive_compiler_kit













{-
-}
{-
-}
