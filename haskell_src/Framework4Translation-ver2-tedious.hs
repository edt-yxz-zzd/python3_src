-- __all__:goto
-- SECTION:goto
{-# LANGUAGE KindSignatures #-}
{-# LANGUAGE TypeFamilies #-}
{-# LANGUAGE MultiParamTypeClasses #-}
{- xxx -}
-- {-# LANGUAGE ExplicitForAll #-}
-- {-# LANGUAGE ScopedTypeVariables #-}

{-
__doc__

e ../../python3_src/haskell_src/Framework4Translation.hs
view others/数学/编程/编译/翻译框架设计.txt

view ../lots/NOTE/Haskell/01start.txt
view ../lots/NOTE/Haskell/run_hs_script.txt
runghc ../../python3_src/haskell_src/Framework4Translation.hs
pushd ../../python3_src/haskell_src/ ; runghc ../../python3_src/haskell_src/Framework4Translation.hs ; popd

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
(Label(..)
,Label4VMH ,mk_Label4VMH
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
    -- dat_D_6X = translateFL_P_999 tr_X5Y_6P dat_D_6Y
--
--
--
,Is_Similar_Dialect(..)
,Manually_Adapt_Front_End_Dialect(..)
,Manually_Adapt_Back_End_Dialect(..)
--
,Manually_Cat(..)
,Manually_Cat4Translator4VMH(..)
--
,Is_Subset_Language(..)
,Lift_Subset_Language(..)
--
--
--
,VMH4Translation(..)
-- warning: [-Wduplicate-exports]
    -- ,LoadedData4VMH
    -- ,File4VMH
    -- ,Translation4VMH
,Script4VMH
,Translator4VMH
,VirtualMachine4VMH
--
,VMachine()
,LoadedData()
,File()
,Translation()
,Script
,Translator
,VirtualMachine
,nonprimitive_op__runFL
,nonprimitive_op__translateVM
,nonprimitive_op__translateFL
,nonprimitive_op__load_and_go
,primitive_op__load
,primitive_op__dump
,primitive_op__eval
,primitive_op__exec
,primitive_op__translate4cat
,primitive_op__runVM
)
where

main = print "ok"
-- __all__




data File file_format data_type :: *
    -- Illegal kind signature ‘File’
    -- (Use KindSignatures to allow kind signatures)
    -- [TypeFamilies < KindSignatures]
type Script file_format input_type output_type = File file_format (input_type -> output_type)
    -- Script fmt i o
type Translator file_format input_fmt output_fmt = File file_format (Translation input_fmt output_fmt)
    -- Translator fmt i_fmt o_fmt
type VirtualMachine file_format native_machine_language = File file_format (VMachine native_machine_language)
    -- VirtualMachine fmt nml


data VMachine nml :: *
data LoadedData native_machine_language data_type :: *

data Translation i_fmt o_fmt :: *

{-
data Translation i o where
    MkTranslation :: (forall dat . (File i dat -> File o dat)) -> Translation i o
    -- see:primitive_op__translate4cat
-}

{-
-- SECTION:typing

.+3,$s/runV_6R/vm_V_6R/g
.+3,$s/runV_9R/vm_V_9R/g
.+3,$s/src_/prg_/g
%s/\<vm_[VR]\>/\0_999/g


file vs loaded:
    dat_X_6R prg_X5Y_6R vm_V_6R tr_X5Y_6R
      -- 『6』:file:exchangeable
    dat_X_9R prg_X5Y_9R vm_V_9R tr_X5Y_9R
      -- 『9』:loaded:inexchangeable

typing:
    file:数据/代码
    dat_X_6R :: File R X
      <==>File4VMH vmh R X
    prg_X5Y_6R :: File R (Y -> X)
      <==>File4VMH vmh R (Y -> X)
      <==>Script R Y X
      <==>Script4VMH vmh R Y X
    vm_V_6R :: File R (VMachine V)
      <==>File4VMH vmh R (vmh V)
      <==>VirtualMachine R V
      <==>VirtualMachine4VMH vmh R V
    tr_X5Y_6R :: File R (Translation Y X)
      <==>File R (forall dat . File dat Y -> File dat X)
      <==>Translator R Y X
      <==>Translator4VMH vmh R Y X


    loaded:变量/程序
    dat_X_9R :: LoadedData R X
    prg_X5Y_9R :: LoadedData R (Y -> X)
    vm_V_9R :: LoadedData R (VMachine V)
    tr_X5Y_9R :: LoadedData R (Translation Y X)
      <==>tr_X5Y_9R :: LoadedData R (forall dat . File dat Y -> File dat X)

    拟程序>:伪程序>:机器
    vm_R_999 :: VMachine R
    translateFL_P_999 :: (Translator4VMH vmh _P _Y _X -> File4VMH vmh _Y _D -> File4VMH vmh _X _D)
        dat_D_6X = translateFL_P_999 tr_X5Y_6P dat_D_6Y

重点:
    prg_X5Y_6R-脚本/源文件/源代码纟程序
    tr_X5Y_9R-translator翻译器
        translateFL_P_999
    vm_V_999-virtual_machine虚拟机


分析:得到tr_X5Y_9R的途径:
    * load(tr_X5Y_6R)
        『6』-->『9』
        静态-->动态
    * cat/translate4cat(tr_X5A_9R,tr_A5Y_9R)
        tmp『A』-->『』
        消元
    * runVM/translateVM(vm_V_9R;tr_X5Y_9V)
        『V』-->『R』
        虚拟机<==>动态翻译器/运行期翻译器


分析:得到tr_X5Y_6R的途径:
    ##移植:tr_X5Y_6P用于translateFL_P_999
    * translateVM(tr_R5B_9A;tr_X5Y_6B)
        动态翻译器
        * translateFL(vm_A_999,tr_R5B_6A;tr_X5Y_6B)
            静态翻译器
    #bug:* lift_subset_language([is_subset_language(R;A)][R <: A];tr_X5Y_6A)
    * lift_subset_language([is_subset_language(R;A)][A <: R];tr_X5Y_6A)
        子语言注入#用于 自举？
    * manually_cat4translator(tr_X5A_6R,tr_A5Y_6R)
        人工串联/消元
    * manually_adapt_back_end_dialect([is_similar_dialect(X;A)];tr_A5Y_6R)
        人工适配后端方言
    * manually_adapt_front_end_dialect([is_similar_dialect(Y;A)];tr_X5A_6R)
        人工适配前端方言

-}


-- load,dump,eval
primitive_op__load
    :: VMachine _R
    -> File fmt _X
    -> LoadedData _R (File fmt _X)
primitive_op__dump
    :: VMachine _R
    -> LoadedData _R (File fmt _X)
    -> File fmt _X
primitive_op__eval
    -- [File.fmt === LoadedData.nml]
    :: VMachine _R
    -> LoadedData _R (File _R _X)
    -> LoadedData _R _X

--cat,exec,translate/translate4cat,runVM(nonprimitive_op__runFL)
primitive_op__cat
    :: VMachine _R
    -> LoadedData _R (_Y->_X)
    -> LoadedData _R (_Z->_Y)
    -> LoadedData _R (_Z->_X)
primitive_op__exec
    :: VMachine _R
    -> LoadedData _R (_Y->_X)
    -> LoadedData _R _Y
    -> LoadedData _R _X
primitive_op__translate4cat
    :: VMachine _R
    -> LoadedData _R (Translation _Y _X)
    -> LoadedData _R (File _Y dat -> File _X dat)
nonprimitive_op__translateVM
    :: VMachine _R
    -> LoadedData _R (Translation _Y _X)
    -> File _Y dat
    -> File _X dat
      -- !! load,dump
      -- <==>:
      -- -> LoadedData _R (File _Y dat)
      -- -> LoadedData _R (File _X dat)
primitive_op__runVM
    :: VMachine _R
    -> LoadedData _R (VMachine _V)
    -> VMachine _V
nonprimitive_op__runFL
    :: VMachine _R
    -> File _R (VMachine _V)
      -- !! load,dump
      -- <==>:
      -- -> LoadedData _R (File _R (VMachine _V))
      -- !! eval
      -- <<==:
      -- -> LoadedData _R (VMachine _V)
    -> VMachine _V
nonprimitive_op__runFL vm_R_999 vm_V_6R = vm_V_999 where
    vm_V_999 = primitive_op__runVM vm_R_999 vm_V_9R
    vm_V_9R = primitive_op__eval vm_R_999 $ primitive_op__load vm_R_999 vm_V_6R

primitive_op__load vm_R_999 dat_X_6V = dat_X_6V_9R where
    dat_X_6V_9R = undefined
primitive_op__dump vm_R_999 dat_X_6V_9R = dat_X_6V where
    dat_X_6V = undefined
primitive_op__eval vm_R_999 dat_X_6R_9R = dat_X_9R where
    dat_X_9R = undefined

primitive_op__cat vm_R_999 prg_X5Y_9R prg_Y5Z_9R = prg_X5Z_9R where
    prg_X5Z_9R = undefined
primitive_op__exec vm_R_999 prg_X5Y_9R dat_Y_9R = dat_X_9R where
    dat_X_9R = undefined
primitive_op__translate4cat vm_R_999 tr_X5Y_9R = prg8tr_viaD_X5Y_9R where
    prg8tr_viaD_X5Y_9R = undefined
-- nonprimitive_op__translateVM tr_X5Y_9R dat_D_6Y_9R = dat_D_6X_9R where
    -- dat_D_6X_9R = undefined
nonprimitive_op__translateVM vm_R_999 tr_X5Y_9R dat_D_6Y = dat_D_6X where
    -- dat_D_6X = undefined
    dat_D_6X = primitive_op__dump vm_R_999 dat_D_9X
    dat_D_9X = primitive_op__exec vm_R_999 prg8tr_viaD_X5Y_9R dat_D_9Y
    dat_D_9Y = primitive_op__load vm_R_999 dat_D_6Y
    prg8tr_viaD_X5Y_9R = primitive_op__translate4cat vm_R_999 tr_X5Y_9R
primitive_op__runVM vm_R_999 vm_V_6R = vm_V_999 where
    vm_V_999 = undefined



nonprimitive_op__translateFL
    :: VMachine _R
    -> Translator _R _Y _X
    -> File _Y dat
    -> File _X dat
nonprimitive_op__translateFL vm_R_999 tr_X5Y_6R dat_D_6Y = dat_D_6X where
    tr_X5Y_9R = nonprimitive_op__load_and_go vm_R_999 tr_X5Y_6R
    dat_D_6X = nonprimitive_op__translateVM vm_R_999 tr_X5Y_9R dat_D_6Y
--
nonprimitive_op__load_and_go
    :: VMachine _R
    -> File _R _X
    -> LoadedData _R _X
nonprimitive_op__load_and_go vm_R_999 dat_X_6R = dat_X_9R where
    dat_X_9R = primitive_op__eval vm_R_999 . primitive_op__load vm_R_999 $ dat_X_6R






-- Script,Translator,VirtualMachine
-- Script4VMH,Translator4VMH,VirtualMachine4VMH
type Script4VMH vmh file_format input_type output_type = File4VMH vmh file_format (input_type -> output_type)
    -- Script4VMH vmh fmt i o
type Translator4VMH vmh file_format input_fmt output_fmt = File4VMH vmh file_format (Translation4VMH vmh input_fmt output_fmt)
    -- Translator4VMH vmh fmt i_fmt o_fmt
type VirtualMachine4VMH vmh file_format native_machine_language = File4VMH vmh file_format (vmh native_machine_language)
    -- VirtualMachine4VMH vmh fmt nml


class VMH4Translation vmh where
    -- [virtual_machine===virtual_machine_hierarchy(nml;)]
    --  [nml <: fmt]
    --  nml:native_machine_language
    --  fmt:file_format
    --
    --
    --
    --xxx:type LoadedData4VMH vmh nml var :: *
    --  NB: ‘LoadedData4VMH’ is a non-injective type family
    --  The type variable ‘i0’ is ambiguous
    --
    --
    -- LoadedData,File,Translation
    -- LoadedData4VMH,File4VMH,Translation4VMH
    type LoadedData4VMH vmh nml :: * -> *
    type File4VMH vmh :: * -> * -> *
    type Translation4VMH vmh :: * -> * -> *
    load :: vmh nml -> File4VMH vmh fmt dat -> LoadedData4VMH vmh nml (File4VMH vmh fmt dat)
    dump :: vmh nml -> LoadedData4VMH vmh nml (File4VMH vmh fmt dat) -> File4VMH vmh fmt dat
    eval :: vmh nml -> LoadedData4VMH vmh nml (File4VMH vmh nml dat) -> LoadedData4VMH vmh nml dat
    cat :: vmh nml -> LoadedData4VMH vmh nml (tmp -> o) -> LoadedData4VMH vmh nml (i -> tmp) -> LoadedData4VMH vmh nml (i -> o)
    exec :: vmh nml -> LoadedData4VMH vmh nml (i -> o) -> LoadedData4VMH vmh nml i -> LoadedData4VMH vmh nml o
    translate4cat :: vmh nml -> LoadedData4VMH vmh nml (Translation4VMH vmh i_fmt o_fmt) -> LoadedData4VMH vmh nml (File4VMH vmh i_fmt dat -> File4VMH vmh o_fmt dat)
    runVM :: vmh nml -> LoadedData4VMH vmh nml (vmh nml_V) -> vmh nml_V

    --
    -- runFL :: vmh nml -> File4VMH vmh nml (vmh nml_V) -> vmh nml_V
    runFL :: vmh nml -> VirtualMachine4VMH vmh nml nml_V -> vmh nml_V
    runFL vm_R_999 vm_V_6R = vm_V_999 where
        vm_V_999 = runVM vm_R_999 vm_V_9R
        vm_V_9R = eval vm_R_999 $ load vm_R_999 vm_V_6R

    --
    translateVM :: vmh nml -> LoadedData4VMH vmh nml (Translation4VMH vmh i_fmt o_fmt) -> File4VMH vmh i_fmt dat -> File4VMH vmh o_fmt dat
    translateVM vm_R_999 tr_X5Y_9R dat_D_6Y = dat_D_6X where
        dat_D_6X = dump vm_R_999 dat_D_9X
        dat_D_9X = exec vm_R_999 prg8tr_viaD_X5Y_9R dat_D_9Y
        dat_D_9Y = load vm_R_999 dat_D_6Y
        prg8tr_viaD_X5Y_9R = translate4cat vm_R_999 tr_X5Y_9R

    --
    load_and_go :: vmh nml -> File4VMH vmh nml dat -> LoadedData4VMH vmh nml dat
    load_and_go vm_R_999 dat_X_6R = dat_X_9R where
        dat_X_9R = eval vm_R_999 . load vm_R_999 $ dat_X_6R
    --
    translateFL :: vmh nml -> Translator4VMH vmh nml i_fmt o_fmt -> File4VMH vmh i_fmt dat -> File4VMH vmh o_fmt dat
    translateFL vm_R_999 tr_X5Y_6R dat_D_6Y = dat_D_6X where
        tr_X5Y_9R = load_and_go vm_R_999 tr_X5Y_6R
        dat_D_6X = translateVM vm_R_999 tr_X5Y_9R dat_D_6Y
    --

instance VMH4Translation VMachine where
    type LoadedData4VMH VMachine nml = LoadedData nml
    type File4VMH VMachine = File
    type Translation4VMH VMachine = Translation
    load = primitive_op__load
    dump = primitive_op__dump
    eval = primitive_op__eval
    cat = primitive_op__cat
    exec = primitive_op__exec
    translate4cat = primitive_op__translate4cat
    runVM = primitive_op__runVM
    --
    translateVM = nonprimitive_op__translateVM
    runFL = nonprimitive_op__runFL
    translateFL = nonprimitive_op__translateFL
    load_and_go = nonprimitive_op__load_and_go


data Label a = MkLabel

type Label4VMH vmh = Label (vmh ())
mk_Label4VMH :: vmh nml -> Label4VMH vmh
mk_Label4VMH _ = MkLabel
type Label4NML nml = Label nml
mk_Label4NML :: vmh nml -> Label4NML nml
mk_Label4NML _ = MkLabel

class Is_Similar_Dialect o i where
    --is_similar_dialect
    -- Too many parameters for class ‘Is_Similar_Dialect’
    --  (Enable MultiParamTypeClasses to allow multi-parameter classes)
class (Is_Similar_Dialect o_fmt8o_back_end o_fmt8i_back_end, VMH4Translation vmh) => Manually_Adapt_Back_End_Dialect vmh fmt i_fmt8io_front_end o_fmt8i_back_end o_fmt8o_back_end where
    --manually_adapt_back_end_dialect :: Label4VMH vmh -> Label o_fmt8o_back_end -> Translator4VMH vmh fmt i_fmt8io_front_end o_fmt8i_back_end -> Translator4VMH vmh fmt i_fmt8io_front_end o_fmt8o_back_end
    manually_adapt_back_end_dialect :: Label4VMH vmh -> Translator4VMH vmh fmt i_fmt8io_front_end o_fmt8i_back_end -> Translator4VMH vmh fmt i_fmt8io_front_end o_fmt8o_back_end
class (Is_Similar_Dialect i_fmt8o_front_end i_fmt8i_front_end, VMH4Translation vmh) => Manually_Adapt_Front_End_Dialect vmh fmt o_fmt8io_back_end i_fmt8i_front_end i_fmt8o_front_end where
    manually_adapt_front_end_dialect :: Label4VMH vmh -> Translator4VMH vmh fmt i_fmt8i_front_end o_fmt8io_back_end -> Translator4VMH vmh fmt i_fmt8o_front_end o_fmt8io_back_end


class Manually_Cat vmh fmt output_type middle_type input_type where
    manually_cat :: Label4VMH vmh -> Script4VMH vmh fmt middle_type output_type -> Script4VMH vmh fmt input_type middle_type -> Script4VMH vmh fmt input_type output_type

class Manually_Cat4Translator4VMH vmh fmt o_fmt tmp_fmt i_fmt where
    manually_cat4translator :: Label4VMH vmh -> Translator4VMH vmh fmt tmp_fmt o_fmt -> Translator4VMH vmh fmt i_fmt tmp_fmt -> Translator4VMH vmh fmt i_fmt o_fmt

class Is_Subset_Language super_fmt sub_fmt where
    --is_subset_language

class Is_Subset_Language super_fmt sub_fmt => Lift_Subset_Language vmh super_fmt sub_fmt where
    lift_subset_language :: Label4VMH vmh -> File4VMH vmh sub_fmt dat -> File4VMH vmh super_fmt dat



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

--newtype Portable_Interpretive_Compiler_Kit vmh vm_code/virtual_machine_bytecode portable_language
newtype Portable_Interpretive_Compiler_Kit vmh _V _P
    = Mk_Portable_Interpretive_Compiler_Kit (Translator4VMH vmh _P _P _V, Translator4VMH vmh _V _P _V, VirtualMachine4VMH vmh _P _V)
    -- (tr_V5P_6P,tr_V5P_6V,vm_V_6P)

--newtype Installer4Portable_Interpretive_Compiler_Kit vmh vm_code/virtual_machine_bytecode portable_language target_machine_code
newtype Installer4Portable_Interpretive_Compiler_Kit vmh _V _P _M
    = Mk_Installer4Portable_Interpretive_Compiler_Kit (Portable_Interpretive_Compiler_Kit vmh _V _P, VirtualMachine4VMH vmh _M _V, Translator4VMH vmh _P _P _M)
    -- (portable_interpretive_compiler_kit(V,P),vm_V_6M,tr_M5P_6P)


--newtype Native_Kit4Portable_Interpretive_Compiler_Kit vmh vm_code/virtual_machine_bytecode portable_language target_machine_code
newtype Native_Kit4Portable_Interpretive_Compiler_Kit vmh _V _P _M
    = Mk_Native_Kit4Portable_Interpretive_Compiler_Kit (Portable_Interpretive_Compiler_Kit vmh _V _P, VirtualMachine4VMH vmh _M _V, Translator4VMH vmh _M _P _M)
    -- (portable_interpretive_compiler_kit(V,P),vm_V_6M,tr_M5P_6M)





mk1__translateFL_P_999 :: (VMH4Translation vmh) => (Translator4VMH vmh _W _P _W, vmh _W) -> (Translator4VMH vmh _P i_fmt o_fmt -> File4VMH vmh i_fmt dat -> File4VMH vmh o_fmt dat)
mk1__translateFL_P_999 (tr_W5P_6W, vm_W_999) = translateFL_P_999 where
    translateFL_W_999 = translateFL vm_W_999
    translateFL_P_999 = translateFL vm_W_999 . translateFL vm_W_999 tr_W5P_6W
    --
    -- [:def____translateFL_P_999]:goto
    -- translateFL_P_999 :: (Translator4VMH vmh _P _Y _X -> File4VMH vmh _Y _D -> File4VMH vmh _X _D)
    -- dat_D_6X = translateFL_P_999 tr_X5Y_6P dat_D_6Y
        -- tr_X5Y_6W = translateFL vm_W_999 tr_W5P_6W tr_X5Y_6P
        -- dat_D_6X = translateFL vm_W_999 tr_X5Y_6W dat_D_6Y
    --
    --
    --
    --
    --
    --
    --
    -- vm_V_6M = translateFL_P_999 tr_M5P_6P vm_V_6P
        -- tr_M5P_6W = translateFL vm_W_999 tr_W5P_6W tr_M5P_6P
        -- vm_V_6M = translateFL vm_W_999 tr_M5P_6W vm_V_6P
    --
    --
    --
    -- tr_V5P_6V = translateFL_P_999 tr_V5P_6P tr_V5P_6P
        -- tr_V5P_6W = translateFL_W_999 tr_W5P_6W tr_V5P_6P
        -- tr_V5P_6V = translateFL_W_999 tr_V5P_6W tr_V5P_6P
    --
mk0__translateFL_P_999 :: (VMH4Translation vmh) => vmh _P -> (Translator4VMH vmh _P i_fmt o_fmt -> File4VMH vmh i_fmt dat -> File4VMH vmh o_fmt dat)
mk0__translateFL_P_999 vm_P_999 = translateFL_P_999 where
    translateFL_P_999 = translateFL vm_P_999
        -- [:def____translateFL_P_999]:here





mk2__translateFL_P_999 :: (VMH4Translation vmh) => Either (VirtualMachine4VMH vmh _W _P) (Translator4VMH vmh _W _P _W) -> vmh _W -> (Translator4VMH vmh _P i_fmt o_fmt -> File4VMH vmh i_fmt dat -> File4VMH vmh o_fmt dat)
    -- either__vm_P_6W__tr_W5P_6W
mk2__translateFL_P_999 (Left vm_P_6W) vm_W_999 = translateFL_P_999 where
    vm_P_999 = runFL vm_W_999 vm_P_6W
    translateFL_P_999 = mk0__translateFL_P_999 vm_P_999
mk2__translateFL_P_999 (Right tr_W5P_6W) vm_W_999 = translateFL_P_999 where
    translateFL_P_999 = mk1__translateFL_P_999 (tr_W5P_6W, vm_W_999)
{-
mk2__translateFL_P_999 (Right tr_W5P_6W) vm_W_999 = translateFL_P_999 where
    -- translateFL_W_999 :: Translator4VMH vmh _W i_fmt o_fmt -> File4VMH vmh i_fmt dat -> File4VMH vmh o_fmt dat
    --  Couldn't match type ‘Translation4VMH vmh’
    --                 with ‘Translation4VMH vmh0’
    translateFL_W_999 = translateFL vm_W_999
    -- translateFL_P_999 = translateFL_W_999 . translateFL_W_999 tr_W5P_6W
    --  直接使用translateFL_W_999==>>导致类型固化...#去多态化
    --  ??
    translateFL_P_999 = translateFL vm_W_999 . translateFL vm_W_999 tr_W5P_6W
        -- tr_V5P_6W = translateFL_W_999 tr_W5P_6W tr_V5P_6P
        -- tr_V5P_6V = translateFL_W_999 tr_V5P_6W tr_V5P_6P
-}








mk3__translateFL_P_999 :: (VMH4Translation vmh) => (Translator4VMH vmh _V _P _V) -> Either (VirtualMachine4VMH vmh _W _V) (Translator4VMH vmh _W _P _W) -> vmh _W -> (Translator4VMH vmh _P i_fmt o_fmt -> File4VMH vmh i_fmt dat -> File4VMH vmh o_fmt dat)
    -- either__vm_V_6W__tr_W5P_6W
mk3__translateFL_P_999 tr_V5P_6V either__vm_V_6W__tr_W5P_6W vm_W_999 = translateFL_P_999 where
    -- (tr_X5P_6X, vm_X_999) :: (Translator4VMH vmh _W _P _W, vmh _W)
    translateFL_P_999 = case either__vm_V_6W__tr_W5P_6W of
      (Right tr_W5P_6W) -> mk1__translateFL_P_999 (tr_W5P_6W, vm_W_999)
      (Left vm_V_6W) -> mk1__translateFL_P_999 (tr_V5P_6V, vm_V_999) where
          vm_V_999 = runFL vm_W_999 vm_V_6W
    -------











-- 辅助起草冫便携式灬
-- [(tr_V5P_6P,vm_V_6P,(vm_P_6W|tr_W5P_6W),vm_W_999) -> portable_interpretive_compiler_kit(V,P)]
prepare4portable_interpretive_compiler_kit :: (VMH4Translation vmh) => Translator4VMH vmh _P _P _V -> VirtualMachine4VMH vmh _P _V -> Either (VirtualMachine4VMH vmh _W _P) (Translator4VMH vmh _W _P _W) -> vmh _W -> Portable_Interpretive_Compiler_Kit vmh _V _P
prepare4portable_interpretive_compiler_kit tr_V5P_6P vm_V_6P either__vm_P_6W__tr_W5P_6W vm_W_999 = portable_interpretive_compiler_kit where
    portable_interpretive_compiler_kit = Mk_Portable_Interpretive_Compiler_Kit (tr_V5P_6P,tr_V5P_6V,vm_V_6P)
    translateFL_P_999 = mk2__translateFL_P_999 either__vm_P_6W__tr_W5P_6W vm_W_999
    tr_V5P_6V = translateFL_P_999 tr_V5P_6P tr_V5P_6P





-- 打包生成冫安装包灬
-- [(tr_V5P_6P,tr_V5P_6V,vm_V_6P,{similar(V,M)},manually_V5P_P_back_end_dialectM_999,(vm_V_6W|tr_W5P_6W),vm_W_999) -> (vm_V_6M,tr_M5P_6P)]
prepare4installer4portable_interpretive_compiler_kit :: (VMH4Translation vmh, Manually_Adapt_Back_End_Dialect vmh _P _P _V _M) => Portable_Interpretive_Compiler_Kit vmh _V _P -> Either (VirtualMachine4VMH vmh _W _V) (Translator4VMH vmh _W _P _W) -> vmh _W -> Installer4Portable_Interpretive_Compiler_Kit vmh _V _P _M
prepare4installer4portable_interpretive_compiler_kit portable_interpretive_compiler_kit@(Mk_Portable_Interpretive_Compiler_Kit (tr_V5P_6P,tr_V5P_6V,vm_V_6P)) either__vm_V_6W__tr_W5P_6W vm_W_999 = installer4portable_interpretive_compiler_kit where
    installer4portable_interpretive_compiler_kit = Mk_Installer4Portable_Interpretive_Compiler_Kit (portable_interpretive_compiler_kit,vm_V_6M,tr_M5P_6P)
    label4vmh = mk_Label4VMH vm_W_999
    tr_M5P_6P = manually_adapt_back_end_dialect label4vmh tr_V5P_6P

    translateFL_P_999 = mk3__translateFL_P_999 tr_V5P_6V either__vm_V_6W__tr_W5P_6W vm_W_999
    vm_V_6M = translateFL_P_999 tr_M5P_6P vm_V_6P


    -------
    -- (tr_X5P_6X, vm_X_999) :: (Translator4VMH vmh _W _P _W, vmh _W)
    -- translateFL_X_999 = translateFL vm_X_999
    -- translateFL_P_999 = translateFL vm_X_999 . translateFL vm_X_999 tr_X5P_6X
        -- tr_M5P_6X = translateFL vm_X_999 tr_X5P_6X tr_M5P_6P
        -- vm_V_6M = translateFL vm_X_999 tr_M5P_6X vm_V_6P
    -------






-- 安装生成冫本地包灬
prepare4native_kit4portable_interpretive_compiler_kit :: (VMH4Translation vmh, Manually_Adapt_Back_End_Dialect vmh _P _P _V _M) => Installer4Portable_Interpretive_Compiler_Kit vmh _V _P _M -> vmh _M -> Native_Kit4Portable_Interpretive_Compiler_Kit vmh _V _P _M
prepare4native_kit4portable_interpretive_compiler_kit installer4portable_interpretive_compiler_kit@(Mk_Installer4Portable_Interpretive_Compiler_Kit (portable_interpretive_compiler_kit@(Mk_Portable_Interpretive_Compiler_Kit (tr_V5P_6P,tr_V5P_6V,vm_V_6P)),vm_V_6M,tr_M5P_6P)) vm_M_999 = native_kit4portable_interpretive_compiler_kit where
    native_kit4portable_interpretive_compiler_kit = Mk_Native_Kit4Portable_Interpretive_Compiler_Kit (portable_interpretive_compiler_kit,vm_V_6M,tr_M5P_6M)
    either__vm_V_6M__tr_M5P_6M = Left vm_V_6M
    translateFL_P_999 = mk3__translateFL_P_999 tr_V5P_6V either__vm_V_6M__tr_M5P_6M vm_M_999
    tr_M5P_6M = translateFL_P_999 tr_M5P_6P tr_M5P_6P










