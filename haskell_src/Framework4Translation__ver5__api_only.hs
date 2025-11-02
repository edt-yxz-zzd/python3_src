-- __all__:goto
-- TODO:goto

{-
e ../../python3_src/haskell_src/Framework4Translation__ver5__api_only.hs
view ../../python3_src/haskell_src/Framework4Translation.hs
view ../lots/NOTE/Haskell/run_hs_script.txt
runghc ../../python3_src/haskell_src/Framework4Translation__ver5__api_only.hs
view others/数学/编程/编译/翻译框架设计.txt



-- ######################
-- 语言昵称讠约定的语言特性:here
-- ######################
-- low_level_lang:m{remote_host},h{curr_host},t{target_host}, u{let mc_u := (mc_m|mc_h|mc_n/(mc_h,vm_n_6h))}
-- low_level_portable_lang:n,e{similar{e,t}},w{used as intermediate language},r{similar{r,n}}
-- high_level_portable_lang:p  ###,q{similar{q,p}}
-- high_level_lang:g,s,z{similar{z,s}},c{c<:s}{s is super_lang of c}
-- ######################


翻译的局限:不论如何翻译tr_x5y_6z，都改变不了核心『x5y』
  ++ManualPortO,ManualPortI,Similar
  ++SuperType,SuperLang

[[
===
关键数据{单段式}:
  mc_h单段式最小下载包([mc_h]:tr_t5s_6s;(tr_h5s_6h|(vm_n_6h,tr_n5s_6n));?tr_n5s_6s) --> tr_t5s_6t
  mc_h单段式开发下载包([mc_h]:tr_t5s_6s,tr_h5s_6h;vm_n_6h,tr_n5s_6s;?tr_n5s_6n) --> tr_t5s_6t
  单段式开发前置下载包(vm_n_6p,tr_n5p_6p,tr_n5p_6n) ~~> vm_n_6h
===
关键数据{双段式}:
  mc_h两段式最小下载包牜甲型([mc_h]:!tr_t5w_6p,!tr_w5s_6s;vm_n_6h,!tr_t5p_6p;((tr_n5p_6n,!tr_n5s_6n)|(tr_n5p_6p,!tr_n5s_6s,([mc_m]:tr_m5p_6m,!tr_m5s_6m)))) --> (tr_t5w_6t,tr_w5s_6t)/trp_t5s_6t
  mc_h两段式最小下载包牜乙型([mc_h]:!tr_t5w_6p,!tr_w5s_6s;vm_n_6h,!tr_t5p_6p,tr_n5w_6n,((tr_w5p_6n,!tr_w5s_6n)|(tr_w5p_6p,([mc_m]:tr_n5w_6w,tr_m5w_6m,tr_m5p_6m,!tr_m5s_6m)))) --> (tr_t5w_6t,tr_w5s_6t)/trp_t5s_6t
  mc_h两段式最小下载包牜丙型([mc_u]:tr_w5p_6p,tr_u5p_6u,tr_u5w_6u,tr_u5s_6u,tr_t5w_6p,tr_w5s_6s) --> (tr_t5w_6t,tr_w5s_6t)/trp_t5s_6t  #[mc_u := (mc_m|mc_h|mc_n/(mc_h,vm_n_6h))]
    #丙型:使用了tr_u5s_6u，可能很麻烦
    #甲型:使用了(tr_n5s_6n|tr_m5s_6m)，可能很麻烦
    #乙型:使用了(tr_w5s_6n|tr_m5s_6m)，可能很麻烦
    #为了避免麻烦，丁型使用:(tr_u5g_6u,tr_w5s_6g)
  mc_h两段式最小下载包牜丁型([mc_u]:tr_w5p_6p,tr_u5p_6u,tr_u5w_6u,tr_u5g_6u,tr_w5s_6g,tr_t5w_6p,tr_w5s_6s) --> (tr_t5w_6t,tr_w5s_6t)/trp_t5s_6t

]]

[[
四基础虚拟封装+二扩展:
  # 串联同文:[tr_t5s_6w == cat_Tr_ tr_t5x_6w tr_x5s_6w]
  # 串联虚拟:[vm_p_6w == cat_Vm_ vm_p_6x vm_x_6w] # [?不太基础?]
  # 虚设格式:[tr_t5s_6w == mock_Tr_ vm_x_6w tr_t5s_6x] #仅限于『程序文件』，其实 串联虚拟cat_Vm_ ~= flip mock_Tr_ 只要 虚设格式 放宽到所有程序而非限于翻译诀
  # 虚设虚拟:[vm_n_6w == mock_Vm_ tr_y5n_6w vm_y_6w]
  #二扩展@20251018:
  # 虚饰入端:[tr_t5s_6w == decorate_I4Tr_ vm_s_6x tr_t5x_6w]
  # 虚饰出端:[tr_t5s_6w == decorate_O4Tr_ vm_x_6t tr_x5s_6w]
    ===
    思考:这几个东西能生成啥样子的系统？
      TODO:
      e script/helper4Framework4Translation__ver5__api_only.py
    ===
    由来的理论支持:
        源代码的两种短程用途:
          + 被宿主机运行后功能等效
          + 被翻译后这两种用途递归功能等效
        归结为一:源代码的递归长程用途:
          + 被多次翻译后被宿主机运行后功能等效
    ===
    虽然相似，但不等同:[vm_n_6w =!= tr_w5n_6w]，也不存在谁替换谁
        不同之处在于:
        * vm_n_6w被翻译成vm_n_6m~?=tr_m5n_6m, 而tr_w5n_6w被翻译成tr_w5n_6m
          =>tr_w5n_6w不能用来替换vm_n_6w
        * tr_w5n_6w用作翻译器 可将dat_v_6n翻译成dat_v_6w，而vm_n_6w启动后只能运行程序并不能翻译文件
          =>vm_n_6w不能用来替换tr_w5n_6w
        相似之处在于:
        + tr_w5n_6w用作翻译器 可将tr_t5s_6n翻译成tr_t5s_6n，而vm_n_6w可以通过 虚设格式 伪作封装 得tr_t5s_6n
          tr_t5s_6n与dat_v_6n的区别在于tr_t5s_6n只强调『函数功能』而非『数据』，所以有『虚设格式』用于『程序文件』而不能用于『数据文件』
===
ls ../../python3_src/haskell_src/Framework4Translation-ver5-images/ -1
串联同文.png
串联虚拟.png
虚设格式.png
虚设虚拟.png
虚饰入端.png
虚饰出端.png
===
e ../../python3_src/haskell_src/Framework4Translation-ver5-images/tools.txt
PxerStudio
com.benny.pxerstudio
===
]]


为了避免循环调用，只调用前面的函数
e ../../python3_src/nn_ns/app/find_forward_calls6haskell_src.py
py_adhoc_call   nn_ns.app.find_forward_calls6haskell_src   ,iter_roughly_find_forward_calls6haskell_src_ :../../python3_src/haskell_src/Framework4Translation__ver5__api_only.hs
('tr2_', 'tr1_')
('main', 'type')


__TrP_版:更有用，应当经可能将输入该为TrP，输出改为Tr
  特别是二进制代码/可执行文件/字节码:以下是应当改的:
      tr_o5i_6m --> trp_o5i_6m
      tr_o5i_6n --> trp_o5i_6n
      tr_o5i_6h --> trp_o5i_6h
  -- 查无: \v<Tr(_\w*)? [^mnhuwtpszg\\xy(b]
  --  #补偿: >)
  -- \v<Tr(_\w*)? [mnhuwt]

版本{whole_picture4porting_相关}:__ver1,__ver2,__ver3,__ver4
  ver1 --[Tr-->TrP]-> ver2
  ver1 --[z-->g]-> ver3
  ???TODO:ver1 --[Tr-->TrP;z-->g]-> ver4

[[useful vim cmds:

左右交换冫函数首行讠赋值语句
  『f a b c = out where』-->『  out = f a b c』
:s/^\v(\w[^=]*\S) *\= *(.*\S) *where$/  \2 = \1

单变量 变成 load_语句
:s/^\v(tr)p?(_\w5\w_6\w)$/  \1p\2 = load_ \1\2


辅助冫新建函数签名丶定义体的首行
  初始类似:『f (tr_o5i_6h,tr_x5y_6z,tr_o5i_6h) -> tr_o5i_6h』
  初始类似:『f tr_o5i_6h tr_x5y_6z tr_o5i_6h = tr_o5i_6h』
  将变量名变成类型名
  类型名根据对称性折叠
:s/ / -> /g
:s/,/ -> /g
:s/ \(::\|->\) / /g
:s/\vtr_(\w)5(\w)_6(\w)/Tr \3 \2 \1/g
:s/\vtrp_(\w)5(\w)_6(\w)/TrP \3 \2 \1/g
:.+1,$s/\v(TrP?) (\w) (\w) (\2)/\1__income \2 \3/g
:.+1,$s/\v(TrP?) (\w) (\2) (\w)/\1__outgo \2 \4/g

检查错误冫剪切代码时函数签名
/^\v(\w+) :: .*\n( *--.*\n)*( *--|\1)@!



搜索特定签名:
/\vMc (\w) -\> TrP__income \1 (\w) -\> Tr__outgo \2 (\w) -\> Tr__income \3 \2$
  tr__port__TrP_ :: Mc m -> TrP__income m s -> Tr__outgo s t -> Tr__income t s
    正常
  update_compile_ :: Mc m -> TrP__income m s -> Tr__outgo s m -> Tr__income m s
    翻译两次
  compile__p2p_A__TrP_ :: Mc h -> TrP__income h s -> Tr__outgo s t -> Tr__income t s
    ===tr__port__TrP_
  mk_tr4old_lang6new_machine_I__A_ :: Mc m -> TrP__income m s -> Tr__outgo s t -> Tr__income t s
    ===tr__port__TrP_
  mk_tr4new_lang_I__TrP_ :: Mc m -> TrP__income m s -> Tr__outgo s m -> Tr__income m s
    [t:=m]
    ===self_resident_translate__TrP_

]]

__all__
[[
主要输出:
  tr__port_/tr__port__TrP_
    #体现出(内向翻译诀,自助翻译诀)的重要性:
    #   接力:内向翻译诀->自助翻译诀->内向翻译诀
    #   tr__port_ :: Mc m -> Tr__income m s -> Tr__outgo s t -> Tr__income t s
重要输出:
  ++cat_Tr_
      #相关:chain_TrP_,cat_BTr_,cat_TrH__
      #     有cat_TrH__但没有cat_TrH_，见下面对此的看法
      ###
      <<==假设牜翻译诀链
      => 双文件可打包为一个虚拟的大文件(翻译诀链)
        即:双文件/(tr_t5w_6t,tr_w5s_6t) --> 单文件/tr_t5s_6t
  ######################
  news@20251018
    decorate_I4Tr_
    decorate_O4Tr_
  ######################
  news@20251008:
    mock_Tr_
    mock_Vm_
    ==>>:
    pseudo_cross_translate_
    pseudo_self_resident_translate_
  ######################
  ++mk_Mc__income_
  ######################
      # 虚设格式:[tr_t5s_6w == mock_Tr_ vm_x_6w tr_t5s_6x]
      # 虚设虚拟:[vm_n_6w == mock_Vm_ tr_y5n_6w vm_y_6w]
      # =>虚拟翻译:[tr_t5s_6w == pseudo_cross_translate_ vm_y_6w tr_y5x_6w tr_t5s_6x == mock_Tr_ (vm_x_6w:=mock_Vm_ tr_y5x_6w vm_y_6w) tr_t5s_6x]
      # =>虚拟翻译牜内向:[tr_t5s_6w == pseudo_self_resident_translate_ vm_y_6w tr_y5x_6y tr_t5s_6x == pseudo_cross_translate_ vm_y_6w (tr_y5x_6w:=mock_Tr_ vm_y_6w tr_y5x_6y) tr_t5s_6x]
      -- ######################

  -- eliminate_Vm:
  eliminate_Vm_via_cat_Vm_
  eliminate_Vm_via_mk_Mc_
  eliminate_Vm_via_mk_remote_TrP_
    cat_Vm_
    mk_Mc_
    mk_remote_TrP_
  # mc_n <<== (mc_h,vm_n_6h)|(mc_m,vm_n_6m)
  # trp_o5i_6n <<== (mc_h,trp_o5i_6h)|(mc_m,trp_o5i_6m)
  #     =>相当于vm拥有宿主机上的所有翻译器
  #     =>统一到虚拟机上
  #     =>统一到同一台机上
  #     =>只有流程性翻译函数才可能用到虚拟机，基础型翻译程序只使用一台机器即不使用虚拟机
  #     ###
  #     =>反向:
  #     trp_o5i_6h <<== (mc_n,trp_o5i_6n)
  #     trp_o5i_6m <<== (mc_n,trp_o5i_6n)
主要输出:
  #流程冫生成编译器纟新语言:单文件,双文件
  mk_tr4new_lang_I__A_
  mk_tr_tr4new_lang_II__A_
  #流程冫生成编译器纟旧语言乊新机器:单文件,双文件
  mk_tr4old_lang6new_machine_I__A_
  mk_tr_tr4old_lang6new_machine_II__A_
  #流程冫生成编译器纟新版本纟旧语言乊旧机器:单文件,双文件
  mk_tr4new_ver4old_lang6old_machine_I__A_
  mk_tr_tr4new_ver4old_lang6old_machine_II__A_
  #流程冫生成编译器纟新算法纟翻译诀乊旧语言乊旧机器:单文件,双文件
  mk_tr4new_ver4algo6old_lang6old_machine_I__A_
  mk_fst4tr_tr4new_ver4algo6old_lang6old_machine_II__A_
  mk_snd4tr_tr4new_ver4algo6old_lang6old_machine_II__A_
主要输出:
  #流程冫生成编译器纟新语言:单文件
  mk_tr4new_lang_I__B_
  mk_tr4new_lang_I__A_
  #流程冫生成编译器纟新语言:双文件
  mk_trp_and_front_end_tr4new_lang_II__B_
  mk_trp_and_front_end_tr4new_lang_II__A_
主要输出:
  #流程冫下载并生成编译器:单文件
  local_compile_I_
  prepare4local_compile_I_
  #流程冫下载并生成编译器:双文件
  local_compile_II_
  prepare4local_compile_II_
主要输出:
  #流程冫移植性翻译:单文件vs双文件
  compile__p2c2p_C1_
    # 双文件模式使用中间层低级语言来中转:避免单文件点对点带来的麻烦
    # 使用另一门语言g(tr_u5g_6u,tr_w5s_6g{vivi:已有的tr_w5s_6s})来避免(tr_u5s_6u|tr_w5s_6u)带来的麻烦

  # -- 点到点:p2p
  # compile__p2p_A_
  # compile__p2p_B_
  # -- 点到中心再到点:p2c2p
  # compile__p2c2p_C__TrP_
  #   compile__p2c2p_C0_
  #   compile__p2c2p_C1_
  # compile__p2c2p_common_
  #   compile__p2c2p_A0_
  #     compile__p2c2p_A1_
  #   compile__p2c2p_B0_
  #     compile__p2c2p_B1_

主要输出:
  #流程冫示例性翻译
  tr7vmIII_
  tr7bootstrap_
主要输出:
  #流程冫示例性翻译
  whole_picture4porting__ver3_
  (Input4Prepare4Port__ver3 (tr_n5p_6g, tr_p5z_6g, tr_e5n_6g, tr_p5g_6m, tr_n5g_6m, manual_portI_z2s__p5_6g, manual_portO_e2t__5n_6g, similar_z_s, similar_e_t))
主要输出:
  #流程冫示例性翻译
  -- 再发现其实没毛病{Tr<:Dat}:xxx:发现porting_的类型有毛病，改为：porting_TrP_,port_Tr_,port_Vm_
  whole_picture4porting__ver2_
  (Input4Prepare4Port__ver2 (tr_p5z_6z, tr_n5p_6z, tr_e5n_6z, tr_m5z_6m, manual_portI_z2s__p5_6z, manual_portO_e2t__5n_6z, similar_z_s, similar_e_t))
    前三项稳定,中三项不稳定,后两项是前提
      #只有两项需人工辅助
<<==:
__all__
@20251004
grep -E '^((data|newtype|type) \w+|\w+ :: )' ../../python3_src/haskell_src/Framework4Translation__ver5__api_only.hs -o | grep '[[:alnum:] _]*\w' -o
  #205:
===
data Lang
data Mc
data Var
data Dat
type Vm
type Tr
type Tr__income
type Tr__outgo
type Tr__echo
type TrP
type TrP__income
type TrP__outgo
type TrP__echo
type TrI_TrO
type TrI_TrO_B
type TrB
type TrB__income
type TrB__outgo
type TrH
data BoxedVirtualMachine
data BoxedTranTranslation
data SuperLang
data SuperType
data ManualPortI
data ManualPortO
data Similar
newtype Input4Prepare4Port__ver1
newtype Input4Prepare4Port__ver2
newtype Input4Prepare4Port__ver3
newtype Input4Prepare4Port__ver4
newtype Output4Prepare4Port
primitive
apply_manual_portI_
apply_manual_portO_
mk_Mc_
mk_Mc__income_
cat_Vm_
pure_load_
load_
dump_
tr__echo
cat_Tr_
mock_Tr_
mock_Vm_
decorate_I4Tr_
decorate_O4Tr_
box_BTr_
unbox_BTr_
apply_Var_
reflexive_similar_
symmetric_similar_
eq_sametype
reflexive_subtype_
transitive_subtype_
simplify_subtype_
leF4Mc_
leF4Var_
leB4Var_
leF4Dat_
leB4Dat_
leF4BVm_
leI4BTr_
leO4BTr_
leF4Vm_
leB4Vm_
leFI4Tr_
leFO4Tr_
leB4Tr_
leFI4TrP_
leFO4TrP_
leB4TrP_
degradeF_Mc_
degradeF_BVm_
upgradeB_Var_
simplifyF_Var_
upgradeB_Dat_
simplifyF_Dat_
degradeFI_BTr_
upgradeFO_BTr_
degradeF_Vm_
upgradeB_Vm_
upgradeB_Tr_
degradeFI_Tr_
upgradeFO_Tr_
upgradeB_TrP_
degradeFI_TrP_
upgradeFO_TrP_
tr__upgrade_
cat_TrB_
load_TrB_
cat_BTr_
sys__unbox_BTr
fmap_Var_
run_TrP_
run_Tr_
pure__cat
tr0_
tr2_
tr1_
tr3_
mk_remote_TrP_
eliminate_Vm_via_mk_Mc_
eliminate_Vm_via_cat_Vm_
eliminate_Vm_via_mk_remote_TrP_
cross_translate__TrP_
cross_translate_
self_resident_translate__TrP_
self_resident_translate_
bootstrapping_translate__TrP_
bootstrapping_translate_
pseudo_cross_translate_
pseudo_self_resident_translate_
cat_TrH__
load_TrH__
mk_cross_translator__TrP_
mk_cross_translator_
two_stage_translate__TrP_
two_stage_translate_
chain_TrP_
chain_TrP_Tr__income_
chain_TrP__L__
chain_TrP__R__
tr__port__TrP_
tr__port_
tr__portII_
update_compile_
local_compile_II__TrP_
local_compile_II_
prepare_vm4local_compile_I__TrP_
prepare_vm4local_compile_I_
prepare4local_compile_II__TrP_
prepare4local_compile_II_
local_compile_I__TrP_
local_compile_I_
prepare4local_compile_I__TrP_
prepare4local_compile_I_
compile__p2p_A__TrP_
compile__p2p_A_
compile__p2p_B__TrP_
compile__p2p_B_
compile__p2c2p_common_
compile__p2c2p_A0__TrP_
compile__p2c2p_A0_
compile__p2c2p_A1__TrP_
compile__p2c2p_A1_
compile__p2c2p_B0__TrP_
compile__p2c2p_B0_
compile__p2c2p_B1__TrP_
compile__p2c2p_B1_
compile__p2c2p_C__TrP_
compile__p2c2p_C0__TrP_
compile__p2c2p_C0_
compile__p2c2p_C1__TrP_
compile__p2c2p_C1_
mk_trp4porting__TrP_
porting__TrP_
porting_
core_prepare4porting_
core_prepare4porting__ver2_
core_prepare4porting__ver3_
low_prepare4porting_
low_prepare4porting__ver2_
low_prepare4porting__ver3_
high_prepare4porting_
high_prepare4porting__ver3_
whole_prepare4porting__ver1_
whole_prepare4porting__ver2_
whole_prepare4porting__ver3_
whole_picture4porting__ver1_
whole_picture4porting__ver2_
whole_picture4porting__ver3_
tr7core_
tr7degenerate_
trp7chain_
tr7vmI__TrP_
tr7vmI_
tr7vmII__TrP_
tr7vmII_
tr7vmIII__TrP_
tr7vmIII_
tr7bootstrap__TrP_
tr7bootstrap_
port_Vm__TrP_
port_Vm_
port_Vm__TrP__ver66_
port_Vm__ver66_
port_Tr__TrP_
port_Tr_
port_Tr__TrP__ver66_
port_Tr__ver66_
porting_TrP_
mk_tr4new_ver4algo6old_lang6old_machine_I__A_
mk_fst4tr_tr4new_ver4algo6old_lang6old_machine_II__A_
mk_snd4tr_tr4new_ver4algo6old_lang6old_machine_II__A_
mk_tr4new_ver4old_lang6old_machine_I__A_
mk_tr_tr4new_ver4old_lang6old_machine_II__A_
mk_tr4old_lang6new_machine_I__A_
prepareA4mk_tr_tr4old_lang6new_machine_II__A_
prepareB4mk_tr_tr4old_lang6new_machine_II__A_
mk_tr_tr4old_lang6new_machine_II__A_
mk_tr4new_lang_I__A_
mk_tr4new_lang_I__TrP_
mk_tr4new_lang_I__B_
mk_tr_tr4new_lang_II__A_
mk_trp_and_front_end_tr4new_lang_II__A_
mk_front_end_tr4new_lang_II__TrP_
mk_trp_and_front_end_tr4new_lang_II__TrP_
mk_trp_and_front_end_tr4new_lang_II__B_
===
]]
__all__


[[
构造器:有限:
  # required GADT
  data Mc where
    -- = McVm (forall h. (Mc h, Vm h t))
    | McVm :: Mc h -> Vm h t            -> Mc t
    | McTr :: Mc h -> Tr__income h n        -> Mc n
    | DegradeF_Mc :: SuperLang subL superL -> Mc superL     -> Mc subL

  data Dat where
    | Dump :: Mc h -> Var h (Dat s v)   -> Dat s v
    | ApplyBTr :: BoxedTranTranslation s t -> Dat s v       -> Dat t v
    | CatVm :: Vm x t -> Vm h x          -> Vm h t
    | MockVm :: Tr w n y -> Vm w y         -> Vm w n
    | MockTr :: Vm w x -> Tr x s t       -> Tr w s t
    | CatTr ::  Tr h a t -> Tr h s a    -> Tr h s t
    | DecorateI4Tr :: Vm x s -> Tr w x t -> Tr w s t
    | DecorateO4Tr :: Vm t x -> Tr w s x -> Tr w s t
    | TrECHO :: Tr h s s
    | ManI :: Similar iA iB -> ManualPortI h o iA iB -> Tr h iA o           -> Tr h iB o)
    | ManO :: Similar oA oB -> ManualPortO h i oA oB -> Tr h i oA           -> Tr h i oB
    | UpgradeB_Dat :: SuperLang subL superL -> Dat subL v       -> Dat superL v
    | SimplifyF_Dat :: SuperType subT superT -> Dat h subT      -> Dat h superT
  data Var where
    | LoadPure :: v         -> Var h v
    | LoadDat :: Dat h v    -> Var h v
    | ApplyVar :: Var h (i -> o) -> Var h i         -> Var h o
    | UpgradeB_Var :: SuperLang subL superL -> Var subL v       -> Var superL v
    | SimplifyF_Var :: SuperType subT superT -> Var h subT      -> Var h superT
<<==:
-- all primitive ops related to Mc;Dat#Tr,Vm;Var#TrP;BoxedTranTranslation
-- .-- ######################
-- .-- Mc
-- .mk_Mc_ :: Mc h -> Vm h t -> Mc t
-- .mk_Mc__income_ :: Mc h -> Tr__income h n -> Mc n
-- .
-- .-- ######################
-- .-- Dat#Tr,Vm
-- .dump_ :: Mc h -> Var h (Dat s v) -> Dat s v
-- .unbox_BTr_ :: BoxedTranTranslation s t -> (Dat s v -> Dat t v)
-- .
-- .cat_Vm_ :: Vm x t -> Vm h x -> Vm h t
-- .mock_Vm_ :: Tr w n y -> Vm w y -> Vm w n
-- .
-- .cat_Tr_ ::  Tr h a t -> Tr h s a -> Tr h s t
-- .mock_Tr_ :: Vm w x -> Tr x s t -> Tr w s t
-- .decorate_I4Tr_ :: Vm x s -> Tr w x t -> Tr w s t
-- .decorate_O4Tr_ :: Vm t x -> Tr w s x -> Tr w s t
-- .tr__echo :: Tr__echo h s
-- .apply_manual_portI_ :: Similar iA iB -> ManualPortI h o iA iB -> (Tr h iA o -> Tr h iB o)
-- .apply_manual_portO_ :: Similar oA oB -> ManualPortO h i oA oB -> (Tr h i oA -> Tr h i oB)
-- .
-- .-- ######################
-- .-- Var#TrP
-- .pure_load_ :: v -> Var h v
-- .load_ :: Dat h v -> Var h v
-- .apply_Var_ :: Var h (i -> o) -> (Var h i -> Var h o)
-- .
-- .-- ######################
-- .box_BTr_ :: (forall v. Dat s v -> Dat t v) -> (BoxedTranTranslation s t)
]]
发现还得算上某些 non-primitive ops:
[[
-- .-- Mc (+h)
-- .degradeF_Mc_ :: SuperLang subL superL -> Mc superL -> Mc subL
-- .
-- .-- Dat (-h) (+v)
-- .upgradeB_Dat_ :: SuperLang subL superL -> Dat subL v -> Dat superL v
-- .simplifyF_Dat_ :: SuperType subT superT -> Dat h subT -> Dat h superT
-- .
-- .-- Var (-h) (+v)
-- .upgradeB_Var_ :: SuperLang subL superL -> Var subL v -> Var superL v
-- .simplifyF_Var_ :: SuperType subT superT -> Var h subT -> Var h superT
-- .
-- .-- BoxedVirtualMachine (+t)
-- .degradeF_BVm_ :: SuperLang subL superL -> BoxedVirtualMachine superL -> BoxedVirtualMachine subL
-- .
-- .-- BoxedTranTranslation (+s) (-t)
-- .degradeFI_BTr_ :: SuperLang subL superL -> BoxedTranTranslation superL t -> BoxedTranTranslation subL t
-- .upgradeFO_BTr_ :: SuperLang subL superL -> BoxedTranTranslation s subL -> BoxedTranTranslation s superL
]]
<<==: 根据 primitive ops 的 类型显化:类似 hs.instance 对 hs.class的 具现化:
[[
-- .-- ######################
-- .simplify_subtype_ :: SuperType subT superT -> (subT -> superT)
-- .
-- .-- ######################
-- .-- Mc
-- .leF4Mc_ :: SuperLang subL superL -> SuperType (Mc superL) (Mc subL)
-- .
-- .-- ######################
-- .-- Dat#Tr,Vm
-- .leF4Dat_ :: SuperType subT superT -> SuperType (Dat h subT) (Dat h superT)
-- .leB4Dat_ :: SuperLang subL superL -> SuperType (Dat subL v) (Dat superL v)
-- .
-- .-- ######################
-- .-- Var#TrP
-- .leF4Var_ :: SuperType subT superT -> SuperType (Var h subT) (Var h superT)
-- .leB4Var_ :: SuperLang subL superL -> SuperType (Var subL v) (Var superL v)
-- .
-- .-- ######################
-- .leF4BVm_ :: SuperLang subL superL -> SuperType (BoxedVirtualMachine superL) (BoxedVirtualMachine subL)
-- .
-- .-- ######################
-- .leI4BTr_ :: SuperLang subL superL -> SuperType (BoxedTranTranslation superL t) (BoxedTranTranslation subL t)
-- .leO4BTr_ :: SuperLang subL superL -> SuperType (BoxedTranTranslation s subL) (BoxedTranTranslation s superL)
-- .
-- .-- ######################

]]



-}

{-# LANGUAGE DataKinds #-}

main = print "ok"

{-
  type Lang = (* -> *)
  data Dat (h :: Lang)  (v :: *)
  • Type constructor ‘Lang’ cannot be used here
          (perhaps you intended to use DataKinds)
      • In the kind ‘Lang’
        In the data type declaration for ‘Dat’
-}

-- ######################
data Lang
  -- <<==DataKinds

-- (Mc h) asif real machine
-- (Var h v) asif inexchangeable variable in memory
-- (Dat h v), (Tr h s t), (Vm h t) ... asif exchangeable file
  -- host,source,target
-- 目标:
--  临时用的目标:TrP
--  通用的目标:Tr
data Mc (h :: Lang)
  -- h:power        :+h
data Var (h :: Lang)  (v :: *)
  -- 不可交换的内存变量
  -- h:requirement  :-h
data Dat (h :: Lang)  (v :: *)
  -- 可交换的数据文件
  -- h:requirement  :-h

-- data Vm (h :: Lang) (t :: Lang)
type Vm (h :: Lang) (t :: Lang) = Dat h (BoxedVirtualMachine t)
  -- 虚拟机的源代码
  -- h:requirement  :-h
  -- t:power        :+t

-- .type TrS (h :: Lang) (s :: Lang) (t :: Lang) = Dat h (BoxedTranTranslationChain s t)
-- .  -- 翻译诀链
-- data Tr (h :: Lang) (s :: Lang) (t :: Lang)
type Tr (h :: Lang) (s :: Lang) (t :: Lang) = Dat h (BoxedTranTranslation s t)
  -- 翻译诀/翻译器的源代码
  -- 翻译诀链#假设牜翻译诀链
  -- 跨机翻译诀/外向翻译诀/他助翻译诀/cross_translator/tr_X5Y_6Z
  -- h:requirement  :-h
  -- s:power        :+s
  -- t:requirement  :-t
type Tr__income (h :: Lang) (s :: Lang) = Tr h s h
  -- 内向翻译诀/self_resident_translator/tr_Z5Y_6Z
type Tr__outgo (s :: Lang) (t :: Lang) = Tr s s t
  -- 自助翻译诀/tr_X5Z_6Z
  --    [自举翻译诀/bootstrapping_translator <: 自助翻译诀]
type Tr__echo (h :: Lang) (s :: Lang) = Tr h s s
  -- 恒等翻译诀/tr_X5X_6Z


type TrP (h :: Lang) (s :: Lang) (t :: Lang) = Var h (BoxedTranTranslation s t)
  -- 翻译器/内存形式的翻译程序
  -- P - program
type TrP__income (h :: Lang) (s :: Lang) = TrP h s h
type TrP__outgo (s :: Lang) (t :: Lang) = TrP s s t
type TrP__echo (h :: Lang) (s :: Lang) = TrP h s s

-- :.+1,$s/\v(TrP?) (\w) (\w) (\2)/\1__income \2 \3/g
-- :.+1,$s/\v(TrP?) (\w) (\2) (\w)/\1__outgo \2 \4/g

type TrI_TrO m s p = (Tr__income m s, Tr__outgo s p)
  --trtr_s62m_p65s
  -- old-mkr:newtype TrI_TrO
type TrI_TrO_B n p = TrI_TrO n p n -- (Tr__income n p, Tr__outgo p n)
  --trtr_p62n_n65p

type TrB  (w :: Lang) (h :: Lang) (s :: Lang) (t :: Lang) = (Tr h w t, Tr h s w)
  -- 双文件
  -- B - 『bi-』
  -- <==> (tr_t5w_6h,tr_w5s_6h)
  -- old-mkr:newtype Tr_Tr

type TrB__income (w :: Lang) (h :: Lang) (s :: Lang) = TrB w h s h
type TrB__outgo (w :: Lang) (s :: Lang) (t :: Lang) = TrB w s s t
-- .type TrB__echo (w :: Lang) (h :: Lang) (s :: Lang) = TrB w h s s


type TrH  (w :: Lang) (h :: Lang) (s :: Lang) = (Tr__income h w, Tr__income w s)
  -- 双文件的第二种形式:堆叠式:pile
  -- H - I-I - income-income
  -- <==> (tr_h5w_6h,tr_w5s_6w)



data BoxedVirtualMachine (t :: Lang)
  -- t:power        :+t
data BoxedTranTranslation (s :: Lang) (t :: Lang)
  -- <==> (forall v. Dat s v -> Dat t v)
  -- s:power        :+s
  -- t:requirement  :-t


data SuperLang (sublang :: Lang) (superlang :: Lang)
data SuperType (subtype :: *) (supertype :: *)
-- ######################
data ManualPortI h o iA iB
data ManualPortO h i oA oB
data Similar :: Lang -> Lang -> *

-- ######################
newtype Input4Prepare4Port__ver1 p n z e m s t = Input4Prepare4Port__ver1 (Tr__outgo z p, Tr z p n, Tr z n e, Tr m z p, Tr m z n, ManualPortI z p z s, ManualPortO z n e t, Similar z s, Similar e t)
  -- (Input4Prepare4Port__ver1 (tr_p5z_6z, tr_n5p_6z, tr_e5n_6z, tr_p5z_6m, tr_n5z_6m, manual_portI_z2s__p5_6z, manual_portO_e2t__5n_6z, similar_z_s, similar_e_t))
--  (tr_p5z_6m, tr_n5z_6m) <-- tr_m5z_6m
newtype Input4Prepare4Port__ver2 p n z e m s t = Input4Prepare4Port__ver2 (Tr__outgo z p, Tr z p n, Tr z n e, Tr__income m z, ManualPortI z p z s, ManualPortO z n e t, Similar z s, Similar e t)
  -- (Input4Prepare4Port__ver2 (tr_p5z_6z, tr_n5p_6z, tr_e5n_6z, tr_m5z_6m, manual_portI_z2s__p5_6z, manual_portO_e2t__5n_6z, similar_z_s, similar_e_t))
newtype Input4Prepare4Port__ver3 p n g z e m s t = Input4Prepare4Port__ver3 (Tr g p n, Tr g z p, Tr g n e, Tr m g p, Tr m g n, ManualPortI g p z s, ManualPortO g n e t, Similar z s, Similar e t)
  -- (Input4Prepare4Port__ver3 (tr_n5p_6g, tr_p5z_6g, tr_e5n_6g, tr_p5g_6m, tr_n5g_6m, manual_portI_z2s__p5_6g, manual_portO_e2t__5n_6g, similar_z_s, similar_e_t))
newtype Input4Prepare4Port__ver4 p n g z e m s t = Input4Prepare4Port__ver4 (Tr g p n, Tr g z p, Tr g n e, Tr__outgo g p, Tr__outgo g n, Tr__income m g, ManualPortI g p z s, ManualPortO g n e t, Similar z s, Similar e t)
  -- (Input4Prepare4Port__ver4 (tr_n5p_6g, tr_p5z_6g, tr_e5n_6g, tr_p5g_6g, tr_n5g_6g, tr_m5g_6m, manual_portI_z2s__p5_6g, manual_portO_e2t__5n_6g, similar_z_s, similar_e_t))
newtype Output4Prepare4Port p n s t = Output4Prepare4Port (Tr__income p s, Tr__income n p, Tr__outgo n t)
  -- (Output4Prepare4Port (tr_p5s_6p, tr_n5p_6n, tr_t5n_6n))











-- __all__




-- ##################################
-- ############primitive:begin:
-- ##################################

-- ######################
primitive :: a
primitive = error "api_only"

-- ######################
apply_manual_portI_ :: Similar iA iB -> ManualPortI h o iA iB -> (Tr h iA o -> Tr h iB o)
apply_manual_portI_ = primitive

apply_manual_portO_ :: Similar oA oB -> ManualPortO h i oA oB -> (Tr h i oA -> Tr h i oB)
apply_manual_portO_ = primitive

-- ######################
-- vivi:cat_Vm_
mk_Mc_ :: Mc h -> Vm h t -> Mc t
mk_Mc_ = primitive
cat_Vm_ :: Vm x t -> Vm h x -> Vm h t
cat_Vm_ = primitive

-- vivi:mock_Vm_
mk_Mc__income_ :: Mc h -> Tr__income h n -> Mc n
mk_Mc__income_ = primitive


-- ######################
pure_load_ :: v -> Var h v
pure_load_ = primitive
load_ :: Dat h v -> Var h v
load_ = primitive
dump_ :: Mc h -> Var h (Dat s v) -> Dat s v
dump_ = primitive
  -- eliminate 『h』 in 『(Var h ...)』 ==>> required 『Mc h』
  -- 数据具现化；保存为文件

tr__echo :: Tr__echo h s
tr__echo = primitive
--tr__echo = ???mk_Dat_??? $ box_BTr_ id

cat_Tr_ ::  Tr h a t -> Tr h s a -> Tr h s t
-- cat_Tr_ tr_t5a_h tr_a5s_h = tr_t5s_h
cat_Tr_ = primitive
  -- 假设牜翻译诀链
  -- vs:cat_Tr_,cat_BTr_

-- ######################
-- news@20251008:
--  mock_Tr_
--  mock_Vm_
--  ==>>:
--  pseudo_cross_translate_
--  pseudo_self_resident_translate_
-- ######################
mock_Tr_ :: Vm w x -> Tr x s t -> Tr w s t
mock_Tr_ = primitive
  -- [tr_t5s_6w == mock_Tr_ vm_x_6w tr_t5s_6x]
mock_Vm_ :: Tr w n y -> Vm w y -> Vm w n
mock_Vm_ = primitive
  -- [vm_n_6w == mock_Vm_ tr_y5n_6w vm_y_6w]


-- ######################
-- news@20251018:
-- decorate_I4Tr_
-- decorate_O4Tr_
decorate_I4Tr_ :: Vm x s -> Tr w x t -> Tr w s t
decorate_I4Tr_ = primitive
  -- [tr_t5s_6w == decorate_I4Tr_ vm_s_6x tr_t5x_6w]
decorate_O4Tr_ :: Vm t x -> Tr w s x -> Tr w s t
decorate_O4Tr_ = primitive
  -- [tr_t5s_6w == decorate_O4Tr_ vm_x_6t tr_x5s_6w]



-- ######################
box_BTr_ :: (forall v. Dat s v -> Dat t v) -> (BoxedTranTranslation s t)
--fail:box_BTr_ = primitive
box_BTr_ = \f -> primitive
unbox_BTr_ :: BoxedTranTranslation s t -> (Dat s v -> Dat t v)
unbox_BTr_ = primitive
apply_Var_ :: Var h (i -> o) -> (Var h i -> Var h o)
apply_Var_ = primitive

-- ######################
reflexive_similar_ :: Similar a a
reflexive_similar_ = primitive
symmetric_similar_ :: Similar a b -> Similar b a
symmetric_similar_ = primitive
-- xxx:transitive_similar_ :: Similar a b -> Similar b c -> Similar a c
-- xxx:transitive_similar_ = primitive

-- ######################
eq_sametype :: SuperType a a
eq_sametype = primitive

-- xxx:symmetric_subtype_
reflexive_subtype_ :: SuperType a a
reflexive_subtype_ = primitive
transitive_subtype_ :: SuperType a b -> SuperType b c -> SuperType a c
transitive_subtype_ = primitive

-- %s/upgrade_subtype_/simplify_subtype_/g
simplify_subtype_ :: SuperType subT superT -> (subT -> superT)
simplify_subtype_ = primitive



-- ######################
-- all-data-type:Mc,Var,Dat,BoxedVirtualMachine,BoxedTranTranslation,SuperLang,SuperType
-- real-data-type:Mc,Var,Dat,BoxedVirtualMachine,BoxedTranTranslation

-- [M ... (+fmt) ... => degrade :: M ... superL ... -> M ... subL ...]
--      #offers weaker format
-- [M ... (-fmt) ... => upgrade :: M ... subL ... -> M ... superL ...]
--      #requires more powerful machine
-- [M ... (+typ) ... => simplify :: M ... subT ... -> M ... superT ...]
--      #offers weaker type
-- [M ... (-typ) ... => complicate :: M ... superT ... -> M ... subT ...]
--      #requires more complex type
--widen,narrow,simplify,complicate

-- F,B:frontend vs backend
-- Mc (+h)
leF4Mc_ :: SuperLang subL superL -> SuperType (Mc superL) (Mc subL)
leF4Mc_ = primitive

-- Var (-h) (+v)
-- =>Var ... (+v)
leF4Var_ :: SuperType subT superT -> SuperType (Var h subT) (Var h superT)
leF4Var_ = primitive
-- =>Var (-h) ...
leB4Var_ :: SuperLang subL superL -> SuperType (Var subL v) (Var superL v)
leB4Var_ = primitive

-- Dat (-h) (+v)
-- =>Dat ... (+v)
leF4Dat_ :: SuperType subT superT -> SuperType (Dat h subT) (Dat h superT)
leF4Dat_ = primitive
-- =>Dat (-h) ...
leB4Dat_ :: SuperLang subL superL -> SuperType (Dat subL v) (Dat superL v)
leB4Dat_ = primitive

-- BoxedVirtualMachine (+t)
leF4BVm_ :: SuperLang subL superL -> SuperType (BoxedVirtualMachine superL) (BoxedVirtualMachine subL)
leF4BVm_ = primitive

-- I,O:input vs output
-- BoxedTranTranslation (--s) (+-t)
--      #外层(->) => 『-』『+』
--      #里层Dat再反转一次
-- BoxedTranTranslation (+s) (-t)
-- =>BoxedTranTranslation (+s) ...
leI4BTr_ :: SuperLang subL superL -> SuperType (BoxedTranTranslation superL t) (BoxedTranTranslation subL t)
leI4BTr_ = primitive
-- =>BoxedTranTranslation ... (-t)
leO4BTr_ :: SuperLang subL superL -> SuperType (BoxedTranTranslation s subL) (BoxedTranTranslation s superL)
leO4BTr_ = primitive

-- ##################################
-- ############primitive:end
-- ##################################

-- __all__


-- ######################
-- ==>>:
leF4Vm_ :: SuperLang subL superL -> SuperType (Vm h superL) (Vm h subL)
leF4Vm_ = leF4Dat_ . leF4BVm_
leB4Vm_ :: SuperLang subL superL -> SuperType (Vm subL t) (Vm superL t)
leB4Vm_ = leB4Dat_

leFI4Tr_ :: SuperLang subL superL -> SuperType (Tr h superL t) (Tr h subL t)
leFI4Tr_ = leF4Dat_ . leI4BTr_
leFO4Tr_ :: SuperLang subL superL -> SuperType (Tr h s subL) (Tr h s superL)
leFO4Tr_ = leF4Dat_ . leO4BTr_
leB4Tr_ :: SuperLang subL superL -> SuperType (Tr subL s t) (Tr superL s t)
leB4Tr_ = leB4Dat_

leFI4TrP_ :: SuperLang subL superL -> SuperType (TrP h superL t) (TrP h subL t)
leFI4TrP_ = leF4Var_ . leI4BTr_
leFO4TrP_ :: SuperLang subL superL -> SuperType (TrP h s subL) (TrP h s superL)
leFO4TrP_ = leF4Var_ . leO4BTr_
leB4TrP_ :: SuperLang subL superL -> SuperType (TrP subL s t) (TrP superL s t)
leB4TrP_ = leB4Var_



-- ######################
-- eliminate 『superL』 in 『(Zzz superL ...)』 ==>> required 『Mc superL』
-- degrade power  vs  upgrade requirement
-- ==>>:
-- F,B:frontend vs backend
-- I,O:input vs output

-- Mc (+h)
degradeF_Mc_ :: SuperLang subL superL -> Mc superL -> Mc subL
degradeF_Mc_ = simplify_subtype_ . leF4Mc_

-- BoxedVirtualMachine (+t)
degradeF_BVm_ :: SuperLang subL superL -> BoxedVirtualMachine superL -> BoxedVirtualMachine subL
degradeF_BVm_ = simplify_subtype_ . leF4BVm_


-- Var (-h) (+v)
upgradeB_Var_ :: SuperLang subL superL -> Var subL v -> Var superL v
upgradeB_Var_ = simplify_subtype_ . leB4Var_
simplifyF_Var_ :: SuperType subT superT -> Var h subT -> Var h superT
simplifyF_Var_ = simplify_subtype_ . leF4Var_

-- Dat (-h) (+v)
upgradeB_Dat_ :: SuperLang subL superL -> Dat subL v -> Dat superL v
upgradeB_Dat_ = simplify_subtype_ . leB4Dat_
simplifyF_Dat_ :: SuperType subT superT -> Dat h subT -> Dat h superT
simplifyF_Dat_ = simplify_subtype_ . leF4Dat_


-- BoxedTranTranslation (+s) (-t)
degradeFI_BTr_ :: SuperLang subL superL -> BoxedTranTranslation superL t -> BoxedTranTranslation subL t
degradeFI_BTr_ le super2t = box_BTr_ $ \subv -> unbox_BTr_ super2t (upgradeB_Dat_ le subv)
upgradeFO_BTr_ :: SuperLang subL superL -> BoxedTranTranslation s subL -> BoxedTranTranslation s superL
upgradeFO_BTr_ le s2sub = box_BTr_ $ \sv -> upgradeB_Dat_ le (unbox_BTr_ s2sub sv)


-- Vm (-h) (+t)
degradeF_Vm_ :: SuperLang subL superL -> Vm h superL -> Vm h subL
degradeF_Vm_ = simplify_subtype_ . leF4Vm_
upgradeB_Vm_ :: SuperLang subL superL -> Vm subL t -> Vm superL t
upgradeB_Vm_ = upgradeB_Dat_


-- Tr (-h) (+s) (-t)
upgradeB_Tr_ :: SuperLang subL superL -> Tr subL s t -> Tr superL s t
upgradeB_Tr_ = upgradeB_Dat_

degradeFI_Tr_ :: SuperLang subL superL -> Tr h superL t -> Tr h subL t
degradeFI_Tr_ = simplify_subtype_ . leFI4Tr_
upgradeFO_Tr_ :: SuperLang subL superL -> Tr h s subL -> Tr h s superL
upgradeFO_Tr_ = simplify_subtype_ . leFO4Tr_


-- TrP (-h) (+s) (-t)
upgradeB_TrP_ :: SuperLang subL superL -> TrP subL s t -> TrP superL s t
upgradeB_TrP_ = upgradeB_Var_
degradeFI_TrP_ :: SuperLang subL superL -> TrP h superL t -> TrP h subL t
degradeFI_TrP_ = simplify_subtype_ . leFI4TrP_
upgradeFO_TrP_ :: SuperLang subL superL -> TrP h s subL -> TrP h s superL
upgradeFO_TrP_ = simplify_subtype_ . leFO4TrP_


-- ######################
--tr__echo = ???mk_Dat_??? $ box_BTr_ id
tr__upgrade_ :: SuperLang subL superL -> Tr h subL superL
tr__upgrade_ le = upgradeFO_Tr_ le tr__echo

-- ######################
cat_TrB_ :: TrB w h s t -> Tr h s t
  -- 双文件->单文件
  -- 双文件讠单文件
  -- 单文件巛双文件
  -- vs:cat_TrB_,cat_TrH__
cat_TrB_ (tr_t5w_6h,tr_w5s_6h) = tr_t5s_6h where
  tr_t5s_6h = cat_Tr_ tr_t5w_6h tr_w5s_6h

load_TrB_ :: TrB w h s t -> TrP h s t
  -- vs:load_TrB_,load_TrH__
load_TrB_ = load_ . cat_TrB_
-- .load_TrB_ (tr_t5w_6h,tr_w5s_6h) = trp_t5s_6h where
-- .  tr_t5s_6h = cat_TrB_ (tr_t5w_6h,tr_w5s_6h)
-- .  trp_t5s_6h = load_ tr_t5s_6h


cat_BTr_ ::  BoxedTranTranslation a t -> BoxedTranTranslation s a -> BoxedTranTranslation s t
  -- vs:cat_Tr_,cat_BTr_
cat_BTr_ t5a a5s = box_BTr_ (\s -> (unbox_BTr_ t5a) . (unbox_BTr_ a5s) $ s)

sys__unbox_BTr :: Var h    (BoxedTranTranslation s t -> (Dat s v -> Dat t v))
sys__unbox_BTr = pure_load_ unbox_BTr_

fmap_Var_ :: (i -> o) -> (Var h i -> Var h o)
fmap_Var_ = apply_Var_ . pure_load_

-- bug:apply_Dat_ :: Dat h (i -> o) -> (Dat h i -> Dat h o)
-- bug:apply_Dat_ = primitive
-- bug:fmap_Dat_ :: (i -> o) -> (Dat h i -> Dat h o)
-- bug:fmap_Dat_ f i = apply_Dat_ (pure_load_ f)

-- ######################
run_TrP_ :: TrP h s t -> Var h (Dat s v -> Dat t v)
run_TrP_ = apply_Var_ sys__unbox_BTr

run_Tr_ :: Tr h s t -> Var h (Dat s v -> Dat t v)
run_Tr_ = run_TrP_ . load_

-- ######################
pure__cat :: Var h     ((b->c) -> (a->b) -> (a->c))
pure__cat = pure_load_ (.)


-- __all__

-- ######################
-- (... -> Dat fmt v)
--      apply Tr,TrP:apply_Var_,apply_Dat_,unbox_BTr_,sys__unbox_BTr,run_Tr_,run_TrP_
--      save:dump_
--      typing upgrade/degrade:upgradeB_Dat_,simplifyF_Dat_
tr0_ :: Mc h -> TrP h s t -> (Dat s v -> Dat t v)
tr0_ mc trp sv = dump_ mc . apply_Var_ (run_TrP_ trp) $ pure_load_ sv
tr2_ :: Mc h -> Tr h s t -> (Dat s v -> Dat t v)
tr2_ mc tr sv = tr0_ mc (tr1_ tr) sv



{-
\(::\|->\) Dat [^>]*$
\(::\|->\) Var [^>]*$
\(::\|->\) Tr\(_\w*\)\? [^>]*$
\(::\|->\) TrP [^>]*$
-}
-- ######################
-- (... -> Tr h s t)
--      as Dat:tr0_,tr2_
--      constant:tr__echo,tr__port_,cat_Tr_
--      manual:apply_manual_portI_,apply_manual_portO_
--      typing upgrade/degrade:upgradeB_Tr_,degradeFI_Tr_,upgradeFO_Tr_,tr__upgrade_


-- ######################
-- (... -> Var fmt v)
--      build:pure_load_,load_,apply_Var_,fmap_Var_
--      typing upgrade/degrade:upgradeB_Var_,simplifyF_Var_

-- ######################
-- (... -> TrP h s t)
--      as Var:pure_load_,load_
--      build:apply_Var_,box_BTr_/unbox_BTr_,chain_TrP_,chain_TrP_Tr__income_,mk_remote_TrP_/eliminate_Vm_via_mk_remote_TrP_
--      typing upgrade/degrade:upgradeB_TrP_,degradeFI_TrP_,upgradeFO_TrP_
--      #见下面:tr7bootstrap_:串联tr_n5x_6n,tr_x5y_6x,tr_y5s_6y可得trp_n5s_6n__verCHAIN，串联tr_t5n_6n,tr_n5s_6n可得trp_t5s_6n
tr1_ :: Tr h s t -> TrP h s t
tr1_ = load_
tr3_ :: (forall v. Dat s v -> Dat t v) -> (TrP h s t)
tr3_ f = pure_load_ (box_BTr_ f)
--fail:tr3_ = pure_load_ . box_BTr_
--  • Couldn't match type ‘a0’ with ‘forall v. Dat s v -> Dat t v’


-- ######################
mk_remote_TrP_ :: Mc n -> TrP n s t -> TrP h s t
  -- 消去n => 需要 mc_n
mk_remote_TrP_ mc_n trp_t5s_6n = trp_t5s_6h where
  -- tr0_,cross_translate__TrP_ :: Mc h -> TrP h s t -> (Dat s v -> Dat t v)
  -- box_BTr_ :: (forall v. Dat s v -> Dat t v) -> (BoxedTranTranslation s t)
  trp_t5s_6h = pure_load_ $ box_BTr_ (tr0_ mc_n trp_t5s_6n)

eliminate_Vm_via_mk_Mc_ :: Mc h -> Vm h t -> Mc t
eliminate_Vm_via_mk_Mc_ = mk_Mc_

eliminate_Vm_via_cat_Vm_ :: Vm x t -> Vm h x -> Vm h t
eliminate_Vm_via_cat_Vm_ = cat_Vm_

eliminate_Vm_via_mk_remote_TrP_ :: Mc n -> TrP n s t -> TrP h s t
eliminate_Vm_via_mk_remote_TrP_ = mk_remote_TrP_


-- ######################
cross_translate__TrP_ :: Mc h -> TrP h s t -> (Dat s v -> Dat t v)
cross_translate__TrP_ = tr0_
cross_translate_ :: Mc h -> Tr h s t -> (Dat s v -> Dat t v)
cross_translate_ = tr2_

self_resident_translate__TrP_ :: Mc h -> TrP__income h s -> (Dat s v -> Dat h v)
self_resident_translate__TrP_ = tr0_
self_resident_translate_ :: Mc h -> Tr__income h s -> (Dat s v -> Dat h v)
self_resident_translate_ = tr2_

bootstrapping_translate__TrP_ :: Mc h -> TrP__outgo h t -> (Dat h v -> Dat t v)
bootstrapping_translate__TrP_ = tr0_
bootstrapping_translate_ :: Mc h -> Tr__outgo h t -> (Dat h v -> Dat t v)
bootstrapping_translate_ = tr2_
-- ######################




-- ######################
-- news@20251008:
-- ######################
pseudo_cross_translate_ :: Vm w y -> Tr w x y -> Tr x s t -> Tr w s t
pseudo_cross_translate_ vm_y_6w tr_y5x_6w tr_t5s_6x = tr_t5s_6w where
  vm_x_6w = mock_Vm_ tr_y5x_6w vm_y_6w
  tr_t5s_6w = mock_Tr_ vm_x_6w tr_t5s_6x

pseudo_self_resident_translate_ :: Vm w y -> Tr__income y x -> Tr x s t -> Tr w s t
pseudo_self_resident_translate_ vm_y_6w tr_y5x_6y tr_t5s_6x = tr_t5s_6w where
  tr_y5x_6w = mock_Tr_ vm_y_6w tr_y5x_6y
  tr_t5s_6w = pseudo_cross_translate_ vm_y_6w tr_y5x_6w tr_t5s_6x

-- ######################
cat_TrH__ :: Mc h -> TrH w h s -> Tr__income h s
  -- vs:cat_TrB_,cat_TrH__
  -- ???是否可以有cat_TrH_:『tr_h5s_6h = cat_TrH_ (tr_h5w_6h,tr_w5s_6w)』
  --    此构造 支持tr_h5s_6h的 两种主要用法:load_,cross_translate_{#可能需要包含不定数量的Mc#}
  --    但毕竟 内部 不再是 统一语言，还是有不少毛病:
  --        ManualPortO 可能非常不平凡
  --        不断cat_TrH_=>一摞厚厚的(tr_h5w_6h,tr_w5p_6w,tr_p5g_6p,tr_g5s_6g)
  --            ++mc_h => tr_h5p_6h,tr_h5g_6h,tr_h5s_6h
  --        被翻译后无法运行除非包含所有中间层参数与机器:
  --            『tr_p5s_6h = cross_translate_ mc_m tr_h5p_6m tr_p5s_6p{:=cat_TrH_ (tr_p5g_6p,tr_g5s_6g)}』
  --            『tr_p5s_6h{至多包含:(mc_m,tr_h5p_6m;tr_p5g_6p,tr_g5s_6g)}』
  --            『?无法运行?:cross_translate_ mc_h tr_p5s_6h dat_v_s』
  --            『可以允许但需所有数据:(mc_h,dat_v_s;mc_m,tr_h5p_6m;tr_p5g_6p,tr_g5s_6g)』
  --            『无法运行的简化数据:(mc_h,dat_v_s;(...删去中间层...);tr_p5g_6h,tr_g5s_6g)』
  --
  -- ######################
  -- 再讨论:
  -- ######################
  --  同文串联:[tr_t5s_6h == tr_t5x_6h . tr_x5s_6h]
  --  其余操作 需要 机器参与
  --  若允许:[tr_t5s_6h == tr_h5x_6h <$< tr_t5s_6x]
  --    但:
  --      !! [tr_t5s_6m == mc_n trp_m5h_6n tr_t5s_6h]
  --      [mc_m tr_t5s_6m dat_v_6s ~~== ffffff mc_m tr_h5x_6m (...mc_n trp_m5h_6n...) tr_h5x_6h tr_t5s_6x dat_v_6s]
  --      删去中间的程序(...mc_n trp_m5h_6n...)
  --      剩下的机器只有mc_m，唯一『_6m』文件是tr_h5x_6m，只能生成tr_t5s_6h，无法更进一步
  --      行不通！
  --  若允许:[tr_t5s_6h == cat3 vm_h_6h tr_h5x_6h tr_t5s_6x]
  --      !! [tr_t5s_6m == mc_n trp_m5h_6n tr_t5s_6h]
  --      [mc_m tr_t5s_6m dat_v_6s ~~== ffffff mc_m vm_h_6m (...mc_n trp_m5h_6n...) vm_h_6h tr_h5x_6h tr_t5s_6x dat_v_6s]
  --      删去中间的程序(...mc_n trp_m5h_6n...)
  --      剩下的机器只有mc_m，加上虚拟机的mc_n
  --      可行！！
  --      证明:每一次翻译，只翻译虚拟机的源文件，保证在实机上构建虚拟机！
  -- [tr_t5s_6w == cat3_special vm_w_6w tr_w5x_6w tr_t5s_6x]
  -- [tr_t5s_6w == cat2 vm_x_6w tr_t5s_6x]
  -- [tr_t5s_6w == cat4 vm_z_6w vm_y_6w tr_z5x_6y tr_t5s_6x]
  --    !! cat2:
  --    [tr_t5s_6w == cat4_3 vm_z_6w tr_z5x_6w tr_t5s_6x]
  --    => [tr_t5s_6w == cat3 vm_y_6w tr_y5x_6w tr_t5s_6x]
  -- ==>>:
  -- 虚设格式:mock_Tr_:cat2__8Tr_:[tr_t5s_6w == cat2__8Tr_ vm_x_6w tr_t5s_6x]
  -- 虚设虚拟:mock_Vm_:cat2__8Vm_:[vm_n_6w == cat2__8Vm_ tr_y5n_6w vm_y_6w]
  -- =>虚拟翻译:pseudo_cross_translate_:cat3:[tr_t5s_6w == cat3 vm_y_6w tr_y5x_6w tr_t5s_6x == cat2__8Tr_ (vm_x_6w:=cat2__8Vm_ tr_y5x_6w vm_y_6w) tr_t5s_6x]
  -- =>虚拟翻译牜内向:pseudo_self_resident_translate_:cat3_income:[tr_t5s_6w == cat3_income vm_y_6w tr_y5x_6y tr_t5s_6x == cat3 vm_y_6w (tr_y5x_6w:=cat2__8Tr_ vm_y_6w tr_y5x_6y) tr_t5s_6x       == (cat2__8Tr_ (vm_x_6w:=cat2__8Vm_ (tr_y5x_6w:=cat2__8Tr_ vm_y_6w tr_y5x_6y) vm_y_6w) tr_t5s_6x)]
  --
  -- 泛化: (Mc h -> Dats a -> Tr w s t) -> (Vm w h -> Dats a -> Tr w s t)
  --    where [Dats =[def]= Empty | (Dat, Dats)]
  --        def__Dats:here
cat_TrH__ mc_h (tr_h5w_6h,tr_w5s_6w) = tr_h5s_6h where
  tr_w5s_6h = self_resident_translate_ mc_h tr_h5w_6h tr_w5s_6w
  tr_h5s_6h = cat_Tr_ tr_h5w_6h tr_w5s_6h
load_TrH__ :: Mc h -> TrH w h s -> TrP__income h s
  -- vs:load_TrB_,load_TrH__
load_TrH__ mc_h (tr_h5w_6h,tr_w5s_6w) = trp_h5s_6h where
  tr_h5s_6h = cat_TrH__ mc_h (tr_h5w_6h,tr_w5s_6w)
  trp_h5s_6h = load_ tr_h5s_6h

-- ######################
mk_cross_translator__TrP_ :: Mc h -> TrP__income h s -> Tr__outgo s t -> Tr h s t
mk_cross_translator__TrP_ = self_resident_translate__TrP_
  -- tr_t5s_6h = self_resident_translate__TrP_ mc trp_h5s_6h tr_t5s_6s

mk_cross_translator_ :: Mc h -> Tr__income h s -> Tr__outgo s t -> Tr h s t
mk_cross_translator_ = self_resident_translate_
  -- tr_t5s_6h = self_resident_translate_ mc tr_h5s_6h tr_t5s_6s

two_stage_translate__TrP_ :: Mc h -> TrP__income h s -> Tr__outgo s t -> (Dat s v -> Dat t v)
two_stage_translate__TrP_ mc trp_h5s_6h tr_t5s_6s = fn_t5s where
  --tr_t5s_6h = self_resident_translate__TrP_ mc trp_h5s_6h tr_t5s_6s
  tr_t5s_6h = mk_cross_translator__TrP_ mc trp_h5s_6h tr_t5s_6s
  fn_t5s = cross_translate_ mc tr_t5s_6h

two_stage_translate_ :: Mc h -> Tr__income h s -> Tr__outgo s t -> (Dat s v -> Dat t v)
two_stage_translate_ mc tr_h5s_6h tr_t5s_6s = fn_t5s where
  trp_h5s_6h = load_ tr_h5s_6h
  fn_t5s = two_stage_translate__TrP_ mc trp_h5s_6h tr_t5s_6s





-- ######################
chain_TrP_ :: TrP h s a -> TrP h a t -> TrP h s t
chain_TrP_ trp_a5s_6h trp_t5a_6h = apply_Var_ (apply_Var_ (pure_load_ cat_BTr_) trp_t5a_6h) trp_a5s_6h
  --串联
  --    =>自举
chain_TrP_Tr__income_ :: Mc a -> TrP__income a b -> Tr__income b c -> TrP__income a c
chain_TrP_Tr__income_ mc_a trp_a5b_6a tr_b5c_6b = trp_a5c_6a where
  tr_b5c_6a = self_resident_translate__TrP_ mc_a trp_a5b_6a tr_b5c_6b
  trp_b5c_6a = load_ tr_b5c_6a
  trp_a5c_6a = chain_TrP_ trp_b5c_6a trp_a5b_6a




chain_TrP__L__ :: Mc h -> TrP n s a -> TrP h a t -> TrP n s t
  -- 消去h => 需要 mc_h
chain_TrP__L__ mc_h trp_a5s_6n trp_t5a_6h = trp_t5s_6n where
  trp_t5a_6n = mk_remote_TrP_ mc_h trp_t5a_6h
  trp_t5s_6n = chain_TrP_ trp_a5s_6n trp_t5a_6n

chain_TrP__R__ :: Mc n -> TrP n s a -> TrP h a t -> TrP h s t
  -- 消去n => 需要 mc_n
chain_TrP__R__ mc_n trp_a5s_6n trp_t5a_6h = trp_t5s_6h where
  trp_a5s_6h = mk_remote_TrP_ mc_n trp_a5s_6n
  trp_t5s_6h = chain_TrP_ trp_a5s_6h trp_t5a_6h




tr__port__TrP_ :: Mc m -> TrP__income m s -> Tr__outgo s t -> Tr__income t s
tr__port__TrP_ mc_m trp_m5s_6m tr_t5s_6s = tr_t5s_6t where
  tr_t5s_6m = self_resident_translate__TrP_ mc_m trp_m5s_6m tr_t5s_6s
  tr_t5s_6t = cross_translate_ mc_m tr_t5s_6m tr_t5s_6s


tr__port_ :: Mc m -> Tr__income m s -> Tr__outgo s t -> Tr__income t s
tr__port_ mc_m tr_m5s_6m tr_t5s_6s = tr_t5s_6t where
  trp_m5s_6m = load_ tr_m5s_6m
  tr_t5s_6t = tr__port__TrP_ mc_m trp_m5s_6m tr_t5s_6s


tr__portII_ :: Mc m -> TrI_TrO m s p -> Tr__income p s
tr__portII_ mc_m (tr_m5s_6m, tr_p5s_6s) = tr_p5s_6p where
  tr_p5s_6p = tr__port_ mc_m tr_m5s_6m tr_p5s_6s

update_compile_ :: Mc m -> TrP__income m s -> Tr__outgo s m -> Tr__income m s
update_compile_ mc_m trp_m5s_6m tr_m5s_6s = tr_m5s_6m where
  _0_tr_m5s_6m = tr__port__TrP_ mc_m trp_m5s_6m tr_m5s_6s
  tr_m5s_6m = tr__port_ mc_m _0_tr_m5s_6m tr_m5s_6s



-- tr__port_
  -- tr_p5s_6p = tr__port_ mc_m tr_m5s_6m tr_p5s_6s
  -- #体现出(内向翻译诀,自助翻译诀)的重要性:
  -- #   接力:内向翻译诀->自助翻译诀->内向翻译诀
  -- vm_n_6m=>(tr_n5p_6n,tr_n5p_6p;tr_t5p_6p,tr_t5n_6n,tr_t5n_6p)
  -- mc_m=>(tr_m5g_6m,tr_m5g_6g)
  --        tr_m5g_6m=>本机当下可用
  --        tr_m5g_6g=>跨机移植用
  -- mc_m*vm_n_6m=>(tr_n5g_6g,tr_n5g_6m,tr_n5p_6g,tr_n5p_6m;tr_m5n_6n,tr_m5n_6m,tr_m5p_6p,tr_m5p_6m,tr_m5n_6g,tr_m5n_6p;tr_p5g_6p,tr_p5g_6g):
  --
  -- m,n,p,g=>6=C(4;2):m5n,m5p,m5g,n5p,n5g,p5g
  -- m,n,p,g=>24=6*4:tr_x5y_6[mnpg]
  --
  -- m,g=>1=C(2;2):m5g
  -- m,g=>2=1*2:tr_m5g_6m,tr_m5g_6g#trtr_g62m_m65g
  --
  -- n,p=>1=C(2;2):n5p
  -- n,p=>2=1*2:tr_n5p_6n,tr_n5p_6p#trtr_p62n_n65p
  --
  -- #mn,ns
  -- mc_m
  -- vm_n_6m
  -- trtr_n62m_m65n
  -- #?trtr_p62n_n65p
  -- trtr_s62n_n65s
  -- fail:???=>trtr_s62m_m65s
  -- =>trp_m5s_6n,trp_m5s_6m
  -- ++tr_m5s_6s
  -- =>tr_m5s_6m #hence trtr_s62m_m65s
  --
  --
  -- 翻译的局限:不论如何翻译tr_x5y_6z，都改变不了核心『x5y』
  --    ++ManualPortO,ManualPortI,Similar
  --    ++SuperType,SuperLang
  --
  -- ++manual_portO_n2m__5s_6s,similar_n_m
  -- =>trtr_s62m_m65s
  --
  -- ###############################
  -- 考虑移植时的相关操作:
  -- ###############################
  -- tr7vmX_
  -- #n,p;m,g;h~k;e~t,z~s;
  -- 『!(低级5...|...6低级)#生成下载#不是源代码』进一步展开:同名#同一角色定位场景
  -- 『?(低级5...|...6低级)#生成下载#不是源代码』可能进一步展开:异名#不同场景不同角色
  -- #vm_n_6h在mc_m上生成
  -- mc_n <--:
  --    | mc_m ?vm_n_6m
  -- vm_n_6h <--:
  --    | vm_n_6p,!tr_h5p_6p,!trp_n5p_6n,?mc_n
  --    | vm_n_6p,!tr_h5p_6p,!trp_n5p_6m,mc_m
  --    | vm_n_6g,!tr_h5g_6g,?tr_m5g_6m,mc_m
  -- tr_h5p_6p <--:
  --    | ?tr_k5p_6p,manual_portO_k2h__5p_6p,?similar_k_h
  -- trp_n5p_6n/tr_n5p_6n <--:
  --    | tr_n5p_6p,?trp_m5p_6m,mc_m
  -- trp_n5p_6m/tr_n5p_6m <--:
  --    | tr_n5p_6g,?trp_m5g_6m,mc_m
  -- tr_h5g_6g <--:
  --    | ?tr_k5g_6g,manual_portO_k2h__5g_6g,?similar_k_h
  -- end:vm_n_6h
  --
  --  #以下在(mc_h,vm_n_6h)/mc_n上生成#没有m,g;也没有h,k#只有#n,p;e~t,z~s;
  -- tr_?5?_6t <--:
  -- tr_?5?_6n <--:
  -- trp_?5?_6n <--:
  --
  -- mc_n <--:
  --    | mc_h ?vm_n_6h
  -- tr_t5s_6t <--:
  --    | !tr_t5s_6s !trp_t5s_6n ?mc_n
  --    | !tr_t5s_6p !trp_t5p_6n ?mc_n
  -- tr_t5s_6s <--:
  --    #xxx: | ?tr_t5z_6s manual_portI_z2s__t5_6s ?similar_z_s
  --    | ?tr_e5s_6s manual_portO_e2t__5s_6s ?similar_e_t
  --    | !tr_t5s_6z !trp_s5z_6n ?mc_n
  -- tr_t5s_6z <--:
  --    | !tr_t5z_6z manual_portI_z2s__t5_6z ?similar_z_s
  --
  -- tr_t5z_6z <--:
  --    | ?tr_e5z_6z manual_portO_e2t__5z_6z ?similar_e_t
  --
  --
  -- tr_t5s_6p <--:
  --    | !tr_t5z_6p manual_portI_z2s__t5_6p ?similar_z_s
  --
  -- tr_t5z_6p <--:
  --    | ?tr_e5z_6p manual_portO_e2t__5z_6p ?similar_e_t
  --
  --
  -- trp_t5s_6n <--:
  --    | !tr_t5s_6s !trp_n5s_6n ?mc_n
  --    | !tr_t5s_6p !trp_n5p_6n ?mc_n
  --    ###
  --    | !trp_t5n_6n !trp_n5s_6n ?mc_n
  --    | !trp_t5e_6n !trp_e5z_6n !trp_z5s_6n ?mc_n
  -- trp_t5p_6n <--:
  --    | !tr_t5p_6p !trp_n5p_6n ?mc_n
  --    ###
  --    | !trp_t5n_6n !trp_n5p_6n ?mc_n
  --    | !trp_t5e_6n !trp_e5p_6n ?mc_n
  -- trp_s5z_6n <--:
  -- trp_n5s_6n <--:
  -- trp_t5n_6n <--:
  -- trp_t5e_6n <--:
  -- trp_e5z_6n <--:
  -- trp_e5p_6n <--:
  -- trp_z5s_6n <--:
  -- trp_n5p_6n <--:
  -- tr_t5p_6p <--:
  --    cancel:TODO
  --
  --
  --
  -- ###############################
  -- 从头再来:目标:tr_t5s_6t
  -- ###############################
  -- 目标:tr_t5s_6t
  -- 已有:tr_t5s_6s
  -- 还需:
  --    mc_h,trp_h5s_6h/tr_h5s_6h #<<==tr__port__TrP_
  --    mc_h,vm_n_6h,trp_n5s_6n/tr_n5s_6n
  --    mc_h,vm_n_6h,(tr_n5s_6s,trp_m5s_6m/tr_m5s_6m,mc_m)
  --        #mc_h,vm_n_6h,(tr_n5s_6s,trp_h5s_6h/tr_h5s_6h) 被前面覆盖:
  --        #mc_h,trp_h5s_6h/tr_h5s_6h
  -- mc_h单段式最小下载包([mc_h]:tr_t5s_6s;(tr_h5s_6h|(vm_n_6h,tr_n5s_6n));?tr_n5s_6s) --> tr_t5s_6t
  -- mc_h单段式开发下载包([mc_h]:tr_t5s_6s,tr_h5s_6h;vm_n_6h,tr_n5s_6s;?tr_n5s_6n) --> tr_t5s_6t
  -- 去h:单段式开发下载包(tr_t5s_6s,tr_n5s_6s,tr_n5s_6n,...)
  -- 去h,t:单段式开发前置下载包(tr_n5s_6s,tr_n5s_6n,...)
  -- 去h,t,s:单段式开发前置下载包(...)
  -- vm_n_6h <--:
  --    | vm_n_6p,!tr_h5p_6p,!trp_n5p_6n,?mc_n
  -- 去h,t,s:单段式开发前置下载包(vm_n_6p,tr_n5p_6p,tr_n5p_6n,...) ~~> vm_n_6h
  --    #vm_n_6p ~~> mc_n/(mc_m,vm_n_6m)
  --    #tr_n5p_6p ~~> tr_h5p_6p
  --    #tr_n5p_6n ~~> trp_n5p_6n
  --
  -- ###综上:
  -- mc_h单段式最小下载包([mc_h]:tr_t5s_6s;(tr_h5s_6h|(vm_n_6h,tr_n5s_6n));?tr_n5s_6s) --> tr_t5s_6t
  -- mc_h单段式开发下载包([mc_h]:tr_t5s_6s,tr_h5s_6h;vm_n_6h,tr_n5s_6s;?tr_n5s_6n) --> tr_t5s_6t
  -- 单段式开发前置下载包(vm_n_6p,tr_n5p_6p,tr_n5p_6n) ~~> vm_n_6h
  --
  --
  --
  -- ###############################
  -- 从头再来:目标:(tr_t5w_6t,tr_w5s_6t)
  -- ###############################
  -- 目标:(tr_t5w_6t,tr_w5s_6t)/trp_t5s_6t
  -- 已有:tr_t5w_6p,tr_w5s_6s
  -- 还需:
  --    mc_h,trp_t5p_6h,trp_t5s_6h
  --    mc_h,trp_t5p_6h,trp_t5w_6h,trp_w5s_6h
  --    mc_h,trp_t5p_6h,trp_h5p_6h,trp_h5s_6h
  --    mc_h,vm_n_6h,trp_t5p_6n,trp_n5p_6n,trp_n5s_6n
  --    mc_h,vm_n_6h,tr_t5p_6p,trp_n5p_6n,trp_n5s_6n
  --    ---A:
  --    mc_h,vm_n_6h,tr_t5p_6p,tr_n5p_6n,tr_n5s_6n
  --    mc_h,vm_n_6h,tr_t5p_6p,tr_n5p_6p,tr_n5s_6s,(mc_m,tr_m5p_6m,tr_m5s_6m)
  --    ---B:
  --    mc_h,vm_n_6h,tr_t5p_6p,(trp_n5w_6n,trp_w5p_6n)/trp_n5p_6n,(trp_n5w_6n,trp_w5s_6n)/trp_n5s_6n
  --    mc_h,vm_n_6h,tr_t5p_6p,trp_n5w_6n,trp_w5p_6n,trp_w5s_6n
  --    mc_h,vm_n_6h,tr_t5p_6p,tr_n5w_6n,trp_w5p_6n,trp_w5s_6n
  --    mc_h,vm_n_6h,tr_t5p_6p,tr_n5w_6n,tr_w5p_6n,tr_w5s_6n
  --    mc_h,vm_n_6h,tr_t5p_6p,tr_n5w_6n,tr_w5p_6p,(mc_m,trp_n5p_6m,trp_n5s_6m)
  --    mc_h,vm_n_6h,tr_t5p_6p,tr_n5w_6n,tr_w5p_6p,(mc_m,(trp_n5w_6m,trp_w5p_6m)/trp_n5p_6m,(trp_n5w_6m,trp_w5s_6m)/trp_n5s_6m)
  --    mc_h,vm_n_6h,tr_t5p_6p,tr_n5w_6n,tr_w5p_6p,(mc_m,trp_n5w_6m,trp_w5p_6m,trp_w5s_6m)
  --    mc_h,vm_n_6h,tr_t5p_6p,tr_n5w_6n,tr_w5p_6p,(mc_m,tr_n5w_6w,trp_m5w_6m,trp_m5p_6m,trp_m5s_6m)
  --    mc_h,vm_n_6h,tr_t5p_6p,tr_n5w_6n,tr_w5p_6p,(mc_m,tr_n5w_6w,tr_m5w_6m,tr_m5p_6m,tr_m5s_6m)
  --        #本:,tr_t5p_6p,tr_w5p_6p,(,tr_n5w_6w)
  --        #程:,tr_n5w_6n,(,tr_m5w_6m,tr_m5p_6m,tr_m5s_6m)
  --        #杂:mc_h,vm_n_6h,(mc_m)
  --        ---
  --        #本:t5p,w5p,(,n5w)
  --        #程:,n5w,(,m5w,m5p,m5s)
  --        ---
  --
  -- mc_h两段式最小下载包牜甲型([mc_h]:!tr_t5w_6p,!tr_w5s_6s;vm_n_6h,!tr_t5p_6p;((tr_n5p_6n,!tr_n5s_6n)|(tr_n5p_6p,!tr_n5s_6s,([mc_m]:tr_m5p_6m,!tr_m5s_6m)))) --> (tr_t5w_6t,tr_w5s_6t)/trp_t5s_6t
  -- mc_h两段式最小下载包牜乙型([mc_h]:!tr_t5w_6p,!tr_w5s_6s;vm_n_6h,!tr_t5p_6p,tr_n5w_6n,((tr_w5p_6n,!tr_w5s_6n)|(tr_w5p_6p,([mc_m]:tr_n5w_6w,tr_m5w_6m,tr_m5p_6m,!tr_m5s_6m)))) --> (tr_t5w_6t,tr_w5s_6t)/trp_t5s_6t
  --
  --
  --
  -- s,t相关:甲型([mc_h]:!tr_t5w_6p,!tr_w5s_6s;!tr_t5p_6p;(!tr_n5s_6n|(!tr_n5s_6s,([mc_m]:!tr_m5s_6m))))
  -- s,t相关:乙型([mc_h]:!tr_t5w_6p,!tr_w5s_6s;!tr_t5p_6p,(!tr_w5s_6n|([mc_m]:!tr_m5s_6m)))
  --    共同:tr_t5w_6p,tr_w5s_6s,tr_t5p_6p,(...|(...,([mc_m]:!tr_m5s_6m)))
  --    不同:((tr_n5s_6n~tr_w5s_6n)|(tr_n5s_6s~<None>))
  --    !! 已有:w5s(tr_w5s_6s)
  --    => tr_w5s_6n比tr_n5s_6n更容易获得
  --    => 乙型更优秀@{s,t相关}
  --
  --
  -- s,t无关:甲型([mc_h]:vm_n_6h;(tr_n5p_6n|(tr_n5p_6p,([mc_m]:tr_m5p_6m))))
  -- s,t无关:乙型([mc_h]:vm_n_6h,tr_n5w_6n,(tr_w5p_6n|(tr_w5p_6p,([mc_m]:tr_n5w_6w,tr_m5w_6m,tr_m5p_6m))))
  --    共同:([mc_h]:vm_n_6h|(...|([mc_m]:tr_m5p_6m)))
  --    不同:(<None>~tr_n5w_6n),(tr_n5p_6n~tr_w5p_6n|(tr_n5p_6p~tr_w5p_6p,(<None>~([mc_m]:tr_n5w_6w,tr_m5w_6m))))
  --    => 乙型含更多常量项@{s,t无关}
  --
  --
  -- ###############################
  -- 回顾重审:目标:(tr_t5w_6t,tr_w5s_6t)
  -- ###############################
  -- 目标:(tr_t5w_6t,tr_w5s_6t)/trp_t5s_6t
  -- 已有:tr_t5w_6p,tr_w5s_6s
  --    # let [mc_u := (mc_m|mc_h|mc_n/(mc_h,vm_n_6h))]
  --    ++!tr_w5p_6p,(!tr_u5p_6u,mc_u) => (-tr_w5p_6u, +tr_t5w_6w)
  --
  --    ++^tr_t5w_6w,(!tr_u5w_6u,mc_u) => (+tr_t5w_6u, +tr_t5w_6t) # !fst!
  --
  --    ++(!tr_u5s_6u,mc_u) => (-tr_w5s_6u, +tr_w5s_6w)
  --
  --    ++^tr_w5s_6w,(^tr_t5w_6u,mc_u) => (+tr_w5s_6t) # !snd!
  --
  -- => 还需:(mc_u,tr_w5p_6p,tr_u5p_6u,tr_u5w_6u,tr_u5s_6u)
  -- => 总需求:(mc_u,tr_w5p_6p,tr_u5p_6u,tr_u5w_6u,tr_u5s_6u,tr_t5w_6p,tr_w5s_6s)
  --
  -- mc_h两段式最小下载包牜丙型([mc_u]:tr_w5p_6p,tr_u5p_6u,tr_u5w_6u,tr_u5s_6u,tr_t5w_6p,tr_w5s_6s) --> (tr_t5w_6t,tr_w5s_6t)/trp_t5s_6t  #[mc_u := (mc_m|mc_h|mc_n/(mc_h,vm_n_6h))]
  --    #丙型:使用了tr_u5s_6u，可能很麻烦
  --    #甲型:使用了(tr_n5s_6n|tr_m5s_6m)，可能很麻烦
  --    #乙型:使用了(tr_w5s_6n|tr_m5s_6m)，可能很麻烦
  --    #为了避免麻烦，丁型使用:(tr_u5g_6u,tr_w5s_6g)
  --
  -- ###############################
  -- 回顾重审:补丁:目标:(trp_u5s_6u)
  -- ###############################
  -- 目标:trp_u5s_6u
  -- 已有:tr_w5s_6s
  --    # let [mc_u := (mc_m|mc_h|mc_n/(mc_h,vm_n_6h))]
  --    ++!tr_w5s_6g,(!tr_u5g_6u,mc_u) => (+tr_w5s_6u)
  --    xxx:++(^tr_w5s_6u,mc_u) => (tr_w5s_6u)
  --    ++!tr_u5w_6u,(^tr_w5s_6u,mc_u) => (+trp_u5s_6u)
  -- => 还需:(mc_u,tr_u5w_6u,tr_u5g_6u,tr_w5s_6g)
  -- => 总需求:(mc_u,tr_u5w_6u,tr_u5g_6u,tr_w5s_6g,tr_w5s_6s) --> trp_u5s_6u
  -- => 双段式丁型总需求:(mc_u,tr_w5p_6p,tr_u5p_6u,tr_u5w_6u,tr_u5g_6u,tr_w5s_6g,tr_t5w_6p,tr_w5s_6s)
  --
  -- mc_h两段式最小下载包牜丁型([mc_u]:tr_w5p_6p,tr_u5p_6u,tr_u5w_6u,tr_u5g_6u,tr_w5s_6g,tr_t5w_6p,tr_w5s_6s) --> (tr_t5w_6t,tr_w5s_6t)/trp_t5s_6t
  --    compile__p2c2p_C1_:goto
  --
  -- ###############################
  -- 本地化:单文件:目标:(tr_h5s_6h)
  -- ###############################
  -- 目标:tr_h5s_6h
  -- 已有:mc_h,vm_n_6h,tr_h5s_6s
  -- 还需:
  --    trp_n5s_6n
  --        !! tr__port__TrP_
  --        => tr_h5s_6h
  -- (tr_h5s_6h) <<== (mc_h,vm_n_6h,tr_h5s_6s,trp_n5s_6n)
  -- ###############################
  -- 预备下载包纟本地化牜虚拟机:目标:(vm_n_6t)/vm_n_6h
  -- ###############################
  -- 目标:vm_n_6t
  -- 已有:mc_m,vm_n_6p
  -- 还需:
  --    trp_t5p_6m
  --    tr_t5p_6m
  --    tr_t5p_6p,tr_m5p_6m
  -- (vm_n_6t)/vm_n_6h <<== (mc_m,vm_n_6p,tr_t5p_6p,tr_m5p_6m)
  --    (vm_n_6h) <<== (mc_m,vm_n_6p,tr_h5p_6p,tr_m5p_6m)
  -- ###############################
  -- 预备下载包纟本地化牜翻译诀:目标:(tr_t5s_6s)/tr_h5s_6s/tr_t5p_6p(tr_h5p_6p)/tr_n5s_6s
  -- ###############################
  -- 目标:tr_t5s_6s
  -- 已有:tr_e5s_6s
  -- 还需:
  --    manual_portO_e2t__5s_6s,similar_e_t
  -- (tr_t5s_6s)/tr_h5s_6s/tr_t5p_6p(tr_h5p_6p)/tr_n5s_6s <<== (tr_e5s_6s,manual_portO_e2t__5s_6s,similar_e_t){(t,s)<-{(h,s),(h,p),(n,s)}}
  --    (tr_h5s_6s) <<== (tr_k5s_6s,manual_portO_k2h__5s_6s,similar_k_h) # s,h,k
  --    (tr_h5p_6p) <<== (tr_k5p_6p,manual_portO_k2h__5p_6p,similar_k_h) # p,h,k
  --    (tr_n5s_6s) <<== (tr_r5s_6s,manual_portO_r2n__5s_6s,similar_r_n) # s,n,r
  -- ###############################
  -- 预备下载包纟本地化牜翻译器牜虚拟版:目标:(tr_n5s_6n)/trp_n5s_6n
  -- ###############################
  -- 目标:tr_n5s_6n
  -- xxx:已有:mc_n,tr_n5s_6n
  -- 已有:mc_m,tr_n5s_6s
  -- 还需:
  --    tr_m5s_6m
  -- (tr_n5s_6n)/trp_n5s_6n <<== (mc_m,tr_n5s_6s,tr_m5s_6m)
  -- ###############################
  -- 本地化:单文件:
  -- (tr_h5s_6h) <<== (mc_h,%vm_n_6h,%tr_h5s_6s,%trp_n5s_6n)
  --
  -- local_compile_I_:goto
  --
  --
  -- 总结{预备下载包纟本地化:单文件}:
  -- (vm_n_6t)/vm_n_6h <<== (mc_m,vm_n_6p,%tr_t5p_6p,tr_m5p_6m)
  --    (vm_n_6h) <<== (mc_m,vm_n_6p,%tr_h5p_6p,tr_m5p_6m)
  -- (tr_t5s_6s)/tr_h5s_6s/tr_t5p_6p(tr_h5p_6p)/tr_n5s_6s <<== (tr_e5s_6s,manual_portO_e2t__5s_6s,similar_e_t){(t,s)<-{(h,s),(h,p),(n,s)}}
  --    (tr_h5s_6s) <<== (tr_k5s_6s,manual_portO_k2h__5s_6s,similar_k_h) # s,h,k
  --    (tr_h5p_6p) <<== (tr_k5p_6p,manual_portO_k2h__5p_6p,similar_k_h) # p,h,k
  --    (tr_n5s_6s) <<== (tr_r5s_6s,manual_portO_r2n__5s_6s,similar_r_n) # s,n,r
  -- (tr_n5s_6n)/trp_n5s_6n <<== (mc_m,%tr_n5s_6s,tr_m5s_6m)
  --
  --
  -- 需求{预备下载包纟本地化:单文件}:
  --  (mc_m,vm_n_6p,tr_m5p_6m,tr_m5s_6m,similar_k_h,similar_r_n,(tr_k5s_6s,manual_portO_k2h__5s_6s),(tr_k5p_6p,manual_portO_k2h__5p_6p),(tr_r5s_6s,manual_portO_r2n__5s_6s))
  --
  --
  -- 输出{预备下载包纟本地化:单文件}:
  -- (vm_n_6h,tr_n5s_6n,tr_h5s_6s;tr_n5s_6s,tr_h5p_6p)
  --    #前三项必要，后两项是中间输出
  -- prepare4local_compile_I_:goto
  --
  --
  --
  --
  --
  --
  --
  -- ###############################
  -- 本地化:双文件:目标:(tr_h5w_6h,tr_w5s_6h)
  -- ###############################
  -- 目标:(tr_h5w_6h,tr_w5s_6h)
  -- 已有:mc_h,vm_n_6h,tr_h5w_6p,tr_w5s_6s
  -- 还需:
  --    trp_h5p_6n,trp_h5s_6n
  --    trp_h5w_6n,trp_w5p_6n,trp_w5s_6n
  --    tr_h5w_6n,tr_w5p_6n,tr_w5s_6n
  -- (tr_h5w_6h,tr_w5s_6h) <<== (mc_h,vm_n_6h,tr_w5p_6n,tr_w5s_6n,tr_h5w_6n,tr_h5w_6p,tr_w5s_6s)
  -- ###############################
  -- 预备下载包纟本地化牜翻译诀:目标:(tr_h5w_6p) # 而tr_w5s_6s,tr_w5p_6p,tr_n5w_6p不予考虑
  -- ###############################
  -- 目标:(tr_h5w_6p)
  -- 已有:  #tr_n5w_6p
  -- 还需:
  --    tr_k5w_6p,manual_portO_k2h__5w_6p,similar_k_h
  -- (tr_h5w_6p) <<== (tr_k5w_6p,manual_portO_k2h__5w_6p,similar_k_h)
  -- ###############################
  -- 预备下载包纟本地化牜虚拟机:目标:(vm_n_6t)/vm_n_6h
  -- ###############################
  -- # prepare_vm4local_compile_I_:goto
  -- 见上面:
  --    (tr_h5p_6p) <<== (tr_k5p_6p,manual_portO_k2h__5p_6p,similar_k_h) # p,h,k
  --    !! (vm_n_6h) <<== (mc_m,vm_n_6p,tr_h5p_6p,tr_m5p_6m)
  --    (vm_n_6h,vm_n_6m) <<== (mc_m,vm_n_6p,tr_h5p_6p,tr_m5p_6m)
  -- ###############################
  -- 预备下载包纟本地化牜翻译器牜虚拟版:目标:(tr_w5p_6n,tr_w5s_6n,tr_h5w_6n)
  -- ###############################
  -- 目标:(tr_w5p_6n,tr_w5s_6n,tr_h5w_6n)
  -- 已有:mc_m,tr_w5p_6p,tr_w5s_6s,tr_h5w_6p
  -- 还需:
  --    vm_n_6m,trp_n5p_6n,(trp_n5s_6n|trp_n5s_6m)
  --    # 同时分化_6n,_6m可行！
  --    #   !! mk_remote_TrP_:goto
  --    #   !! chain_TrP__L__:goto
  --    vm_n_6m,tr_n5p_6n,trp_n5w_6n,trp_w5s_6m
  --    vm_n_6m,tr_n5p_6n,tr_n5w_6n,tr_w5s_6m
  --    vm_n_6m,tr_n5p_6n,tr_n5w_6p,tr_m5s_6m
  --
  -- (tr_w5p_6n,tr_w5s_6n,tr_h5w_6n) <<== (mc_m,vm_n_6m,tr_n5p_6n,tr_m5s_6m,tr_w5s_6s,tr_w5p_6p,tr_n5w_6p,tr_h5w_6p)
  -- ###############################
  -- 本地化:双文件:
  -- (tr_h5w_6h,tr_w5s_6h) <<== (mc_h,%vm_n_6h,%tr_w5p_6n,%tr_w5s_6n,%tr_h5w_6n,%tr_h5w_6p,tr_w5s_6s)
  --    local_compile_II_:goto
  --
  --
  -- 总结{预备下载包纟本地化:双文件}:
  --    (tr_h5w_6p) <<== (tr_k5w_6p,manual_portO_k2h__5w_6p,similar_k_h)
  --    (vm_n_6h,vm_n_6m) <<== (mc_m,vm_n_6p,%tr_h5p_6p,tr_m5p_6m)
  --    (tr_h5p_6p) <<== (tr_k5p_6p,manual_portO_k2h__5p_6p,similar_k_h) # p,h,k
  --    (tr_w5p_6n,tr_w5s_6n,tr_h5w_6n) <<== (mc_m,%vm_n_6m,tr_n5p_6n,tr_m5s_6m,tr_w5s_6s,tr_w5p_6p,tr_n5w_6p,%tr_h5w_6p)
  --
  --
  -- 需求{预备下载包纟本地化:双文件}:
  -- (mc_m,tr_m5s_6m,tr_m5p_6m,vm_n_6p,tr_n5p_6n,tr_n5w_6p,tr_w5p_6p,tr_w5s_6s, similar_k_h, (tr_k5w_6p,manual_portO_k2h__5w_6p), (tr_k5p_6p,manual_portO_k2h__5p_6p))
  --
  --
  -- 输出{预备下载包纟本地化:双文件}:
  -- (vm_n_6h,tr_w5p_6n,tr_w5s_6n,tr_h5w_6n,tr_h5w_6p;tr_w5s_6s;tr_h5p_6p,vm_n_6m)
  --    #前五项是真输出，倒数第三的tr_w5s_6s只是必需，最后两项是中间输出
  --    prepare4local_compile_II_:goto
  --
  --
  --
  -- ###############################
  --
  --
  --
  -- ###############################





-- __all__


-- 本地化:双文件
local_compile_II__TrP_ :: Mc h -> Vm h n -> TrP n p w -> TrP n s w -> TrP n w h -> Tr p w h -> Tr__outgo s w -> (Tr__income h w,Tr h s w)
local_compile_II__TrP_ mc_h vm_n_6h trp_w5p_6n trp_w5s_6n trp_h5w_6n tr_h5w_6p tr_w5s_6s = (tr_h5w_6h,tr_w5s_6h) where
  trp_h5p_6n = chain_TrP_ trp_w5p_6n trp_h5w_6n
  trp_h5s_6n = chain_TrP_ trp_w5s_6n trp_h5w_6n

  mc_n = mk_Mc_ mc_h vm_n_6h
  tr_h5w_6h = cross_translate__TrP_ mc_n trp_h5p_6n tr_h5w_6p
  tr_w5s_6h = cross_translate__TrP_ mc_n trp_h5s_6n tr_w5s_6s


local_compile_II_ :: Mc h -> Vm h n -> Tr n p w -> Tr n s w -> Tr n w h -> Tr p w h -> Tr__outgo s w -> (Tr__income h w,Tr h s w)
  -- local_compile_II__TrP_
local_compile_II_ mc_h vm_n_6h tr_w5p_6n tr_w5s_6n tr_h5w_6n tr_h5w_6p tr_w5s_6s = (tr_h5w_6h,tr_w5s_6h) where
  trp_h5w_6n = load_ tr_h5w_6n
  trp_w5p_6n = load_ tr_w5p_6n
  trp_w5s_6n = load_ tr_w5s_6n

  (tr_h5w_6h,tr_w5s_6h) = local_compile_II__TrP_ mc_h vm_n_6h trp_w5p_6n trp_w5s_6n trp_h5w_6n tr_h5w_6p tr_w5s_6s




-- 预备下载包纟本地化:虚拟机:单文件&双文件
prepare_vm4local_compile_I__TrP_ :: Mc m -> TrP__income m p -> Tr__outgo p t -> Vm p n -> Vm t n
prepare_vm4local_compile_I__TrP_ mc_m trp_m5p_6m tr_t5p_6p vm_n_6p = vm_n_6t where
  --    trp_t5p_6m
  --    tr_t5p_6m
  --    tr_t5p_6p,trp_m5p_6m
  tr_t5p_6m = self_resident_translate__TrP_ mc_m trp_m5p_6m tr_t5p_6p
  vm_n_6t = cross_translate_ mc_m tr_t5p_6m vm_n_6p

-- .prepare_vm4local_compile_I_ :: Mc m -> Tr__income m p -> Tr__outgo p h -> Vm p n -> Vm h n
-- .prepare_vm4local_compile_I_ mc_m tr_m5p_6m tr_h5p_6p vm_n_6p = vm_n_6h where
prepare_vm4local_compile_I_ :: Mc m -> Tr__income m p -> Tr__outgo p t -> Vm p n -> Vm t n
  -- prepare_vm4local_compile_I__TrP_
prepare_vm4local_compile_I_ mc_m tr_m5p_6m tr_t5p_6p vm_n_6p = vm_n_6t where
  trp_m5p_6m = load_ tr_m5p_6m
  vm_n_6t = prepare_vm4local_compile_I__TrP_ mc_m trp_m5p_6m tr_t5p_6p vm_n_6p




-- 预备下载包纟本地化:双文件
prepare4local_compile_II__TrP_ :: Mc m -> TrP__income m s -> TrP__income m p -> Vm p n -> TrP__income n p -> Tr p w n -> Tr__outgo p w -> Tr__outgo s w ->  Similar k h -> (Tr p w k,ManualPortO p w k h) -> (Tr__outgo p k,ManualPortO p p k h) -> (Vm h n,Tr n p w,Tr n s w,Tr n w h,Tr p w h,   Tr__outgo s w,   Tr__outgo p h,Vm m n)
prepare4local_compile_II__TrP_ mc_m trp_m5s_6m trp_m5p_6m vm_n_6p trp_n5p_6n tr_n5w_6p tr_w5p_6p tr_w5s_6s  similar_k_h (tr_k5w_6p,manual_portO_k2h__5w_6p) (tr_k5p_6p,manual_portO_k2h__5p_6p) = (vm_n_6h,tr_w5p_6n,tr_w5s_6n,tr_h5w_6n,tr_h5w_6p,   tr_w5s_6s,   tr_h5p_6p,vm_n_6m) where
  tr_h5p_6p = apply_manual_portO_ similar_k_h manual_portO_k2h__5p_6p tr_k5p_6p
  vm_n_6h = prepare_vm4local_compile_I__TrP_ mc_m trp_m5p_6m tr_h5p_6p vm_n_6p
  vm_n_6m = self_resident_translate__TrP_ mc_m trp_m5p_6m vm_n_6p

  tr_h5w_6p = apply_manual_portO_ similar_k_h manual_portO_k2h__5w_6p tr_k5w_6p



  mc_n = mk_Mc_ mc_m vm_n_6m

  tr_n5w_6n = self_resident_translate__TrP_ mc_n trp_n5p_6n tr_n5w_6p
  tr_w5s_6m = self_resident_translate__TrP_ mc_m trp_m5s_6m tr_w5s_6s

  trp_n5w_6n = load_ tr_n5w_6n
  trp_w5s_6m = load_ tr_w5s_6m

  trp_n5s_6m = chain_TrP__L__ mc_n trp_w5s_6m trp_n5w_6n
  -- .trp_n5p_6n = load_ tr_n5p_6n

  tr_w5p_6n = self_resident_translate__TrP_ mc_n trp_n5p_6n tr_w5p_6p
  tr_h5w_6n = self_resident_translate__TrP_ mc_n trp_n5p_6n tr_h5w_6p
  tr_w5s_6n = cross_translate__TrP_ mc_m trp_n5s_6m tr_w5s_6s



prepare4local_compile_II_ :: Mc m -> Tr__income m s -> Tr__income m p -> Vm p n -> Tr__income n p -> Tr p w n -> Tr__outgo p w -> Tr__outgo s w ->  Similar k h -> (Tr p w k,ManualPortO p w k h) -> (Tr__outgo p k,ManualPortO p p k h) -> (Vm h n,Tr n p w,Tr n s w,Tr n w h,Tr p w h,   Tr__outgo s w,   Tr__outgo p h,Vm m n)
  -- prepare4local_compile_II__TrP_
prepare4local_compile_II_ mc_m tr_m5s_6m tr_m5p_6m vm_n_6p tr_n5p_6n tr_n5w_6p tr_w5p_6p tr_w5s_6s  similar_k_h (tr_k5w_6p,manual_portO_k2h__5w_6p) (tr_k5p_6p,manual_portO_k2h__5p_6p) = (vm_n_6h,tr_w5p_6n,tr_w5s_6n,tr_h5w_6n,tr_h5w_6p,   tr_w5s_6s,   tr_h5p_6p,vm_n_6m) where
  trp_m5s_6m = load_ tr_m5s_6m
  trp_m5p_6m = load_ tr_m5p_6m
  trp_n5p_6n = load_ tr_n5p_6n
  (vm_n_6h,tr_w5p_6n,tr_w5s_6n,tr_h5w_6n,tr_h5w_6p,   tr_w5s_6s,   tr_h5p_6p,vm_n_6m) = prepare4local_compile_II__TrP_ mc_m trp_m5s_6m trp_m5p_6m vm_n_6p trp_n5p_6n tr_n5w_6p tr_w5p_6p tr_w5s_6s  similar_k_h (tr_k5w_6p,manual_portO_k2h__5w_6p) (tr_k5p_6p,manual_portO_k2h__5p_6p)









-- 本地化:单文件
local_compile_I__TrP_ :: Mc h -> Vm h n -> TrP__income n s -> Tr__outgo s h -> Tr__income h s
local_compile_I__TrP_ mc_h vm_n_6h trp_n5s_6n tr_h5s_6s = tr_h5s_6h where
  mc_n = mk_Mc_ mc_h vm_n_6h
  tr_h5s_6h = tr__port__TrP_ mc_n trp_n5s_6n tr_h5s_6s

local_compile_I_ :: Mc h -> Vm h n -> Tr__income n s -> Tr__outgo s h -> Tr__income h s
local_compile_I_ mc_h vm_n_6h tr_n5s_6n tr_h5s_6s = tr_h5s_6h where
  trp_n5s_6n = load_ tr_n5s_6n
  tr_h5s_6h = local_compile_I__TrP_ mc_h vm_n_6h trp_n5s_6n tr_h5s_6s




-- 预备下载包纟本地化:单文件
prepare4local_compile_I__TrP_ :: Mc m -> Vm p n -> TrP__income m p -> TrP__income m s -> Similar k h -> Similar r n -> (Tr__outgo s k, ManualPortO s s k h) -> (Tr__outgo p k, ManualPortO p p k h) -> (Tr__outgo s r, ManualPortO s s r n) -> (Vm h n,Tr__income n s,Tr__outgo s h,Tr__outgo s n,Tr__outgo p h)
prepare4local_compile_I__TrP_ mc_m vm_n_6p trp_m5p_6m trp_m5s_6m similar_k_h similar_r_n (tr_k5s_6s, manual_portO_k2h__5s_6s) (tr_k5p_6p, manual_portO_k2h__5p_6p) (tr_r5s_6s, manual_portO_r2n__5s_6s) = (vm_n_6h,tr_n5s_6n,tr_h5s_6s,   tr_n5s_6s,tr_h5p_6p) where
  tr_h5p_6p = apply_manual_portO_ similar_k_h manual_portO_k2h__5p_6p tr_k5p_6p
  vm_n_6h = prepare_vm4local_compile_I__TrP_ mc_m trp_m5p_6m tr_h5p_6p vm_n_6p

  tr_n5s_6s = apply_manual_portO_ similar_r_n manual_portO_r2n__5s_6s tr_r5s_6s
  tr_n5s_6n = tr__port__TrP_ mc_m trp_m5s_6m tr_n5s_6s

  tr_h5s_6s = apply_manual_portO_ similar_k_h manual_portO_k2h__5s_6s tr_k5s_6s


prepare4local_compile_I_ :: Mc m -> Vm p n -> Tr__income m p -> Tr__income m s -> Similar k h -> Similar r n -> (Tr__outgo s k, ManualPortO s s k h) -> (Tr__outgo p k, ManualPortO p p k h) -> (Tr__outgo s r, ManualPortO s s r n) -> (Vm h n,Tr__income n s,Tr__outgo s h,Tr__outgo s n,Tr__outgo p h)
  -- prepare4local_compile_I__TrP_
prepare4local_compile_I_ mc_m vm_n_6p tr_m5p_6m tr_m5s_6m similar_k_h similar_r_n (tr_k5s_6s, manual_portO_k2h__5s_6s) (tr_k5p_6p, manual_portO_k2h__5p_6p) (tr_r5s_6s, manual_portO_r2n__5s_6s) = (vm_n_6h,tr_n5s_6n,tr_h5s_6s,   tr_n5s_6s,tr_h5p_6p) where
  trp_m5p_6m = load_ tr_m5p_6m
  trp_m5s_6m = load_ tr_m5s_6m
  (vm_n_6h,tr_n5s_6n,tr_h5s_6s,   tr_n5s_6s,tr_h5p_6p) = prepare4local_compile_I__TrP_ mc_m vm_n_6p trp_m5p_6m trp_m5s_6m similar_k_h similar_r_n (tr_k5s_6s, manual_portO_k2h__5s_6s) (tr_k5p_6p, manual_portO_k2h__5p_6p) (tr_r5s_6s, manual_portO_r2n__5s_6s)





-- mc_h单段式最小下载包([mc_h]:tr_t5s_6s;(tr_h5s_6h|(vm_n_6h,tr_n5s_6n));?tr_n5s_6s) --> tr_t5s_6t
-- 点到点:p2p
compile__p2p_A__TrP_ :: Mc h -> TrP__income h s -> Tr__outgo s t -> Tr__income t s
compile__p2p_A__TrP_ = tr__port__TrP_

compile__p2p_A_ :: Mc h -> Tr__income h s -> Tr__outgo s t -> Tr__income t s
compile__p2p_A_ = tr__port_
-- .compile__p2p_A_ mc_h tr_h5s_6h tr_t5s_6s = tr_t5s_6t where
-- .  tr_t5s_6t = tr__port_ mc_n tr_n5s_6n tr_t5s_6s


compile__p2p_B__TrP_ :: Mc h -> Vm h n -> TrP__income n s -> Tr__outgo s t -> Tr__income t s
compile__p2p_B__TrP_ mc_h vm_n_6h trp_n5s_6n tr_t5s_6s = tr_t5s_6t where
  mc_n = mk_Mc_ mc_h vm_n_6h
  tr_t5s_6t = compile__p2p_A__TrP_ mc_n trp_n5s_6n tr_t5s_6s

compile__p2p_B_ :: Mc h -> Vm h n -> Tr__income n s -> Tr__outgo s t -> Tr__income t s
compile__p2p_B_ mc_h vm_n_6h tr_n5s_6n tr_t5s_6s = tr_t5s_6t where
  mc_n = mk_Mc_ mc_h vm_n_6h
  tr_t5s_6t = compile__p2p_A_ mc_n tr_n5s_6n tr_t5s_6s



-- 两段式
-- 点到中心再到点:p2c2p
compile__p2c2p_common_ :: Mc h -> Vm h n -> Tr p w t -> Tr__outgo s w -> Tr__outgo p t -> TrP__income n p -> TrP__income n s -> (Tr__income t w,Tr t s w)
compile__p2c2p_common_ mc_h vm_n_6h tr_t5w_6p tr_w5s_6s tr_t5p_6p trp_n5p_6n trp_n5s_6n = (tr_t5w_6t,tr_w5s_6t) where
  --    mc_h,vm_n_6h,tr_t5p_6p,trp_n5p_6n,trp_n5s_6n

  mc_n = mk_Mc_ mc_h vm_n_6h
  tr_t5p_6n = self_resident_translate__TrP_ mc_n trp_n5p_6n tr_t5p_6p
  trp_t5p_6n = load_ tr_t5p_6n
  --    mc_n,trp_t5p_6n,trp_n5p_6n,trp_n5s_6n

  tr_t5w_6n = self_resident_translate__TrP_ mc_n trp_n5p_6n tr_t5w_6p
  tr_w5s_6n = self_resident_translate__TrP_ mc_n trp_n5s_6n tr_w5s_6s

  trp_t5w_6n = load_ tr_t5w_6n
  trp_w5s_6n = load_ tr_w5s_6n
  --    mc_n,trp_t5p_6n,trp_t5w_6n,trp_w5s_6n

  trp_t5s_6n = chain_TrP_ trp_w5s_6n trp_t5w_6n
  --    mc_n,trp_t5p_6n,trp_t5s_6n

  tr_t5w_6t = cross_translate__TrP_ mc_n trp_t5p_6n tr_t5w_6p
  tr_w5s_6t = cross_translate__TrP_ mc_n trp_t5s_6n tr_w5s_6s



-- mc_h两段式最小下载包牜甲型([mc_h]:!tr_t5w_6p,!tr_w5s_6s;vm_n_6h,!tr_t5p_6p;((tr_n5p_6n,!tr_n5s_6n)|(tr_n5p_6p,!tr_n5s_6s,([mc_m]:tr_m5p_6m,!tr_m5s_6m)))) --> (tr_t5w_6t,tr_w5s_6t)/trp_t5s_6t
-- 点到中心再到点:p2c2p
compile__p2c2p_A0__TrP_ :: Mc h -> Vm h n -> (TrP__income n p,TrP__income n s) -> Tr p w t -> Tr__outgo s w -> Tr__outgo p t -> (Tr__income t w,Tr t s w)
compile__p2c2p_A0__TrP_ mc_h vm_n_6h (trp_n5p_6n,trp_n5s_6n) tr_t5w_6p tr_w5s_6s tr_t5p_6p = (tr_t5w_6t,tr_w5s_6t) where
  --    mc_h,vm_n_6h,tr_t5p_6p,trp_n5p_6n,trp_n5s_6n
  (tr_t5w_6t,tr_w5s_6t) = compile__p2c2p_common_ mc_h vm_n_6h tr_t5w_6p tr_w5s_6s tr_t5p_6p trp_n5p_6n trp_n5s_6n

compile__p2c2p_A0_ :: Mc h -> Vm h n -> (Tr__income n p,Tr__income n s) -> Tr p w t -> Tr__outgo s w -> Tr__outgo p t -> (Tr__income t w,Tr t s w)
  -- compile__p2c2p_A0__TrP_
compile__p2c2p_A0_ mc_h vm_n_6h (tr_n5p_6n,tr_n5s_6n) tr_t5w_6p tr_w5s_6s tr_t5p_6p = (tr_t5w_6t,tr_w5s_6t) where
  --    mc_h,vm_n_6h,tr_t5p_6p,tr_n5p_6n,tr_n5s_6n
  trp_n5p_6n = load_ tr_n5p_6n
  trp_n5s_6n = load_ tr_n5s_6n
  --    mc_h,vm_n_6h,tr_t5p_6p,trp_n5p_6n,trp_n5s_6n
  (tr_t5w_6t,tr_w5s_6t) = compile__p2c2p_A0__TrP_ mc_h vm_n_6h (trp_n5p_6n,trp_n5s_6n) tr_t5w_6p tr_w5s_6s tr_t5p_6p



compile__p2c2p_A1__TrP_ :: Mc h -> Vm h n -> (Tr__outgo p n,Tr__outgo s n,(Mc m,TrP__income m p,TrP__income m s)) -> Tr p w t -> Tr__outgo s w -> Tr__outgo p t -> (Tr__income t w,Tr t s w)
compile__p2c2p_A1__TrP_ mc_h vm_n_6h (tr_n5p_6p,tr_n5s_6s,(mc_m,trp_m5p_6m,trp_m5s_6m)) tr_t5w_6p tr_w5s_6s tr_t5p_6p = (tr_t5w_6t,tr_w5s_6t) where
  --    mc_h,vm_n_6h,tr_t5p_6p,tr_n5p_6p,tr_n5s_6s,(mc_m,trp_m5p_6m,trp_m5s_6m)
  tr_n5s_6n = tr__port__TrP_ mc_m trp_m5s_6m tr_n5s_6s
  tr_n5p_6n = tr__port__TrP_ mc_m trp_m5p_6m tr_n5p_6p
  --    mc_h,vm_n_6h,tr_t5p_6p,tr_n5p_6n,tr_n5s_6n
  (tr_t5w_6t,tr_w5s_6t) = compile__p2c2p_A0_ mc_h vm_n_6h (tr_n5p_6n,tr_n5s_6n) tr_t5w_6p tr_w5s_6s tr_t5p_6p


compile__p2c2p_A1_ :: Mc h -> Vm h n -> (Tr__outgo p n,Tr__outgo s n,(Mc m,Tr__income m p,Tr__income m s)) -> Tr p w t -> Tr__outgo s w -> Tr__outgo p t -> (Tr__income t w,Tr t s w)
  -- compile__p2c2p_A1__TrP_
compile__p2c2p_A1_ mc_h vm_n_6h (tr_n5p_6p,tr_n5s_6s,(mc_m,tr_m5p_6m,tr_m5s_6m)) tr_t5w_6p tr_w5s_6s tr_t5p_6p = (tr_t5w_6t,tr_w5s_6t) where
  --    mc_h,vm_n_6h,tr_t5p_6p,tr_n5p_6p,tr_n5s_6s,(mc_m,tr_m5p_6m,tr_m5s_6m)
  trp_m5p_6m = load_ tr_m5p_6m
  trp_m5s_6m = load_ tr_m5s_6m
  --    mc_h,vm_n_6h,tr_t5p_6p,tr_n5p_6p,tr_n5s_6s,(mc_m,trp_m5p_6m,trp_m5s_6m)
  (tr_t5w_6t,tr_w5s_6t) = compile__p2c2p_A1__TrP_ mc_h vm_n_6h (tr_n5p_6p,tr_n5s_6s,(mc_m,trp_m5p_6m,trp_m5s_6m)) tr_t5w_6p tr_w5s_6s tr_t5p_6p




-- mc_h两段式最小下载包牜乙型([mc_h]:!tr_t5w_6p,!tr_w5s_6s;vm_n_6h,!tr_t5p_6p,tr_n5w_6n,((tr_w5p_6n,!tr_w5s_6n)|(tr_w5p_6p,([mc_m]:tr_n5w_6w,tr_m5w_6m,tr_m5p_6m,!tr_m5s_6m)))) --> (tr_t5w_6t,tr_w5s_6t)/trp_t5s_6t
-- 点到中心再到点:p2c2p
compile__p2c2p_B0__TrP_ :: Mc h -> Vm h n -> (TrP n p w,TrP n s w) -> Tr p w t -> Tr__outgo s w -> Tr__outgo p t -> TrP__income n w -> (Tr__income t w,Tr t s w)
compile__p2c2p_B0__TrP_ mc_h vm_n_6h (trp_w5p_6n,trp_w5s_6n) tr_t5w_6p tr_w5s_6s tr_t5p_6p trp_n5w_6n = (tr_t5w_6t,tr_w5s_6t) where
  trp_n5p_6n = chain_TrP_ trp_w5p_6n trp_n5w_6n
  trp_n5s_6n = chain_TrP_ trp_w5s_6n trp_n5w_6n

  (tr_t5w_6t,tr_w5s_6t) = compile__p2c2p_common_ mc_h vm_n_6h tr_t5w_6p tr_w5s_6s tr_t5p_6p trp_n5p_6n trp_n5s_6n

compile__p2c2p_B0_ :: Mc h -> Vm h n -> (Tr n p w,Tr n s w) -> Tr p w t -> Tr__outgo s w -> Tr__outgo p t -> Tr__income n w -> (Tr__income t w,Tr t s w)
  -- compile__p2c2p_B0__TrP_
compile__p2c2p_B0_ mc_h vm_n_6h (tr_w5p_6n,tr_w5s_6n) tr_t5w_6p tr_w5s_6s tr_t5p_6p tr_n5w_6n = (tr_t5w_6t,tr_w5s_6t) where
  trp_w5p_6n = load_ tr_w5p_6n
  trp_w5s_6n = load_ tr_w5s_6n

  trp_n5w_6n = load_ tr_n5w_6n

  (tr_t5w_6t,tr_w5s_6t) = compile__p2c2p_B0__TrP_ mc_h vm_n_6h (trp_w5p_6n,trp_w5s_6n) tr_t5w_6p tr_w5s_6s tr_t5p_6p trp_n5w_6n



compile__p2c2p_B1__TrP_ :: Mc h -> Vm h n -> (Tr__outgo p w,(Mc m,Tr__outgo w n,TrP__income m w,TrP__income m p,TrP__income m s)) -> Tr p w t -> Tr__outgo s w -> Tr__outgo p t -> TrP__income n w -> (Tr__income t w, Tr t s w)
  -- tr_n5w_6w is used as src not binary in this func
compile__p2c2p_B1__TrP_ mc_h vm_n_6h (tr_w5p_6p,(mc_m,tr_n5w_6w,trp_m5w_6m,trp_m5p_6m,trp_m5s_6m)) tr_t5w_6p tr_w5s_6s tr_t5p_6p trp_n5w_6n = (tr_t5w_6t,tr_w5s_6t) where
  tr_n5w_6m = self_resident_translate__TrP_ mc_m trp_m5w_6m tr_n5w_6w
  tr_w5p_6m = self_resident_translate__TrP_ mc_m trp_m5p_6m tr_w5p_6p
  tr_w5s_6m = self_resident_translate__TrP_ mc_m trp_m5s_6m tr_w5s_6s

  trp_n5w_6m = load_ tr_n5w_6m
  trp_w5p_6m = load_ tr_w5p_6m
  trp_w5s_6m = load_ tr_w5s_6m

  trp_n5p_6m = chain_TrP_ trp_w5p_6m trp_n5w_6m
  trp_n5s_6m = chain_TrP_ trp_w5s_6m trp_n5w_6m

  tr_w5p_6n = cross_translate__TrP_ mc_m trp_n5p_6m tr_w5p_6p
  tr_w5s_6n = cross_translate__TrP_ mc_m trp_n5s_6m tr_w5s_6s

  trp_w5p_6n = load_ tr_w5p_6n
  trp_w5s_6n = load_ tr_w5s_6n

  (tr_t5w_6t,tr_w5s_6t) = compile__p2c2p_B0__TrP_ mc_h vm_n_6h (trp_w5p_6n,trp_w5s_6n) tr_t5w_6p tr_w5s_6s tr_t5p_6p trp_n5w_6n


compile__p2c2p_B1_ :: Mc h -> Vm h n -> (Tr__outgo p w,(Mc m,Tr__outgo w n,Tr__income m w,Tr__income m p,Tr__income m s)) -> Tr p w t -> Tr__outgo s w -> Tr__outgo p t -> Tr__income n w -> (Tr__income t w, Tr t s w)
  -- compile__p2c2p_B1__TrP_
compile__p2c2p_B1_ mc_h vm_n_6h (tr_w5p_6p,(mc_m,tr_n5w_6w,tr_m5w_6m,tr_m5p_6m,tr_m5s_6m)) tr_t5w_6p tr_w5s_6s tr_t5p_6p tr_n5w_6n = (tr_t5w_6t,tr_w5s_6t) where
  trp_m5w_6m = load_ tr_m5w_6m
  trp_m5p_6m = load_ tr_m5p_6m
  trp_m5s_6m = load_ tr_m5s_6m

  trp_n5w_6n = load_ tr_n5w_6n

  (tr_t5w_6t,tr_w5s_6t) = compile__p2c2p_B1__TrP_ mc_h vm_n_6h (tr_w5p_6p,(mc_m,tr_n5w_6w,trp_m5w_6m,trp_m5p_6m,trp_m5s_6m)) tr_t5w_6p tr_w5s_6s tr_t5p_6p trp_n5w_6n







-- 两段式:共通:丙型&丁型
-- 点到中心再到点:p2c2p
compile__p2c2p_C__TrP_ :: Mc u -> Tr__outgo p w -> TrP__income u p -> TrP__income u w -> TrP__income u s -> Tr p w t -> Tr__outgo s w -> (Tr__income t w, Tr t s w)
  -- tr_u5s_6u --> trp_u5s_6u
compile__p2c2p_C__TrP_ mc_u tr_w5p_6p trp_u5p_6u trp_u5w_6u trp_u5s_6u tr_t5w_6p tr_w5s_6s = (tr_t5w_6t,tr_w5s_6t) where
  tr_w5p_6u = self_resident_translate__TrP_ mc_u trp_u5p_6u tr_w5p_6p
  tr_t5w_6w = cross_translate_ mc_u tr_w5p_6u tr_t5w_6p
  tr_t5w_6u = self_resident_translate__TrP_ mc_u trp_u5w_6u tr_t5w_6w
  tr_t5w_6t = cross_translate_ mc_u tr_t5w_6u tr_t5w_6w

  --tr_w5s_6u = self_resident_translate_ mc_u tr_u5s_6u tr_w5s_6s
  tr_w5s_6u = self_resident_translate__TrP_ mc_u trp_u5s_6u tr_w5s_6s
  tr_w5s_6w = cross_translate_ mc_u tr_w5s_6u tr_w5s_6s
  tr_w5s_6t = cross_translate_ mc_u tr_t5w_6u tr_w5s_6w




-- mc_h两段式最小下载包牜丙型([mc_u]:tr_w5p_6p,tr_u5p_6u,tr_u5w_6u,tr_u5s_6u,tr_t5w_6p,tr_w5s_6s) --> (tr_t5w_6t,tr_w5s_6t)/trp_t5s_6t  #[mc_u := (mc_m|mc_h|mc_n/(mc_h,vm_n_6h))]
-- 点到中心再到点:p2c2p
compile__p2c2p_C0__TrP_ :: Mc u -> Tr__outgo p w -> TrP__income u p -> TrP__income u w -> TrP__income u s -> Tr p w t -> Tr__outgo s w -> (Tr__income t w, Tr t s w)
compile__p2c2p_C0__TrP_ mc_u tr_w5p_6p trp_u5p_6u trp_u5w_6u trp_u5s_6u tr_t5w_6p tr_w5s_6s = (tr_t5w_6t,tr_w5s_6t) where
  (tr_t5w_6t,tr_w5s_6t) = compile__p2c2p_C__TrP_ mc_u tr_w5p_6p trp_u5p_6u trp_u5w_6u trp_u5s_6u tr_t5w_6p tr_w5s_6s

compile__p2c2p_C0_ :: Mc u -> Tr__outgo p w -> Tr__income u p -> Tr__income u w -> Tr__income u s -> Tr p w t -> Tr__outgo s w -> (Tr__income t w, Tr t s w)
  -- compile__p2c2p_C0__TrP_
compile__p2c2p_C0_ mc_u tr_w5p_6p tr_u5p_6u tr_u5w_6u tr_u5s_6u tr_t5w_6p tr_w5s_6s = (tr_t5w_6t,tr_w5s_6t) where
  trp_u5p_6u = load_ tr_u5p_6u
  trp_u5w_6u = load_ tr_u5w_6u
  trp_u5s_6u = load_ tr_u5s_6u

  (tr_t5w_6t,tr_w5s_6t) = compile__p2c2p_C0__TrP_ mc_u tr_w5p_6p trp_u5p_6u trp_u5w_6u trp_u5s_6u tr_t5w_6p tr_w5s_6s




-- mc_h两段式最小下载包牜丁型([mc_u]:tr_w5p_6p,tr_u5p_6u,tr_u5w_6u,tr_u5g_6u,tr_w5s_6g,tr_t5w_6p,tr_w5s_6s) --> (tr_t5w_6t,tr_w5s_6t)/trp_t5s_6t
-- compile__p2c2p_C1__TrP_:发现多余参数:tr_u5s_6u:已删除
compile__p2c2p_C1__TrP_ :: Mc u -> Tr__outgo p w -> TrP__income u p -> TrP__income u w -> TrP__income u g -> Tr g s w -> Tr p w t -> Tr__outgo s w -> (Tr__income t w, Tr t s w)
compile__p2c2p_C1__TrP_ mc_u tr_w5p_6p trp_u5p_6u trp_u5w_6u trp_u5g_6u tr_w5s_6g tr_t5w_6p tr_w5s_6s = (tr_t5w_6t,tr_w5s_6t) where
  tr_w5s_6u = self_resident_translate__TrP_ mc_u trp_u5g_6u tr_w5s_6g
  trp_w5s_6u = load_ tr_w5s_6u
  trp_u5s_6u = chain_TrP_ trp_w5s_6u trp_u5w_6u
  (tr_t5w_6t,tr_w5s_6t) = compile__p2c2p_C__TrP_ mc_u tr_w5p_6p trp_u5p_6u trp_u5w_6u trp_u5s_6u tr_t5w_6p tr_w5s_6s

compile__p2c2p_C1_ :: Mc u -> Tr__outgo p w -> Tr__income u p -> Tr__income u w -> Tr__income u g -> Tr g s w -> Tr p w t -> Tr__outgo s w -> (Tr__income t w, Tr t s w)
  -- compile__p2c2p_C1__TrP_
compile__p2c2p_C1_ mc_u tr_w5p_6p tr_u5p_6u tr_u5w_6u tr_u5g_6u tr_w5s_6g tr_t5w_6p tr_w5s_6s = (tr_t5w_6t,tr_w5s_6t) where
  trp_u5p_6u = load_ tr_u5p_6u
  trp_u5w_6u = load_ tr_u5w_6u
  trp_u5g_6u = load_ tr_u5g_6u

  (tr_t5w_6t,tr_w5s_6t) = compile__p2c2p_C1__TrP_ mc_u tr_w5p_6p trp_u5p_6u trp_u5w_6u trp_u5g_6u tr_w5s_6g tr_t5w_6p tr_w5s_6s









-- ######################
-- 语言昵称讠约定的语言特性:goto
-- ######################
--
-- ~mc_h
-- ~vm_n_6h
-- #!tr_p5s_6s
-- !tr_p5s_6p
-- #.tr_n5p_6p
-- .tr_n5p_6n
-- !tr_t5n_6n
-- porting_ :: ... -> (dat_v_6s -> dat_v_6t)
--  (tr_n5p_6n,tr_p5s_6p) => tr_p5s_6n
--  (tr_p5s_6n,dat_v_6s) => dat_v_6p
--  (tr_n5p_6n,dat_v_6p) => dat_v_6n
--  (tr_t5n_6n,dat_v_6n) => dat_v_6t
--
-- 再发现其实没毛病{Tr<:Dat}:xxx:发现porting_的类型有毛病，改为：
-- porting_TrP_ :: ... -> trp_t5s_6h
-- port_Tr_ :: ... -> tr_t5s_6h
-- port_Vm_ :: ... -> vm_n_6h
--
-- core_prepare4porting_ :: ... -> tr_n5p_6n
--  =>core_prepare4porting_ :: mc_m -> tr_n5z_6m -> tr_n5p_6z -> tr_n5p_6n
--  =>core_prepare4porting_ :: mc_m -> tr_n5g_6m -> tr_n5p_6g -> tr_n5p_6n
--
-- low_prepare4porting_ :: ... -> tr_t5n_6n
--  =>low_prepare4porting_ :: mc_m -> tr_n5z_6m -> tr_t5n_6z -> tr_t5n_6n
--  =>low_prepare4porting_ :: mc_m -> tr_n5z_6m -> tr_e5n_6z -> manual_portO_e2t__5n_6z -> tr_t5n_6n
--  =>low_prepare4porting_ :: mc_m -> tr_n5g_6m -> tr_e5n_6g -> manual_portO_e2t__5n_6g -> tr_t5n_6n
--
-- high_prepare4porting_ :: ... -> tr_p5s_6s -> tr_p5s_6p
--  =>high_prepare4porting_ :: mc_m -> tr_p5z_6m -> tr_p5z_6z -> manual_portI_z2s__p5_6z -> tr_p5s_6p
--  =>high_prepare4porting_ :: mc_m -> tr_p5g_6m -> tr_p5z_6g -> manual_portI_z2s__p5_6g -> tr_p5s_6p
--


mk_trp4porting__TrP_ :: Mc n -> TrP__income n p -> Tr__income p s -> TrP__outgo n t -> TrP n s t
mk_trp4porting__TrP_ mc_n trp_n5p_6n tr_p5s_6p trp_t5n_6n = trp_t5s_6n where
  -- chain_TrP_Tr__income_ :: Mc a -> TrP__income a b -> Tr__income b c -> TrP__income a c
  trp_n5s_6n = chain_TrP_Tr__income_ mc_n trp_n5p_6n tr_p5s_6p
  trp_t5s_6n = chain_TrP_ trp_n5s_6n trp_t5n_6n





porting__TrP_ :: Mc h -> Vm h n -> TrP__income n p -> Tr__income p s -> TrP__outgo n t -> (Dat s v -> Dat t v)
porting__TrP_ mc_h vm_n_6h trp_n5p_6n tr_p5s_6p trp_t5n_6n dat_v_6s = dat_v_6t where
  mc_n = mk_Mc_ mc_h vm_n_6h

  trp_t5s_6n = mk_trp4porting__TrP_ mc_n trp_n5p_6n tr_p5s_6p trp_t5n_6n
  dat_v_6t = cross_translate__TrP_ mc_n trp_t5s_6n dat_v_6s

  -- .tr_p5s_6n = self_resident_translate__TrP_ mc_n trp_n5p_6n tr_p5s_6p
  -- .dat_v_6p = cross_translate_ mc_n tr_p5s_6n dat_v_6s
  -- .dat_v_6n = self_resident_translate__TrP_ mc_n trp_n5p_6n dat_v_6p
  -- .dat_v_6t = bootstrapping_translate__TrP_ mc_n trp_t5n_6n dat_v_6n

porting_ :: Mc h -> Vm h n -> Tr__income n p -> Tr__income p s -> Tr__outgo n t -> (Dat s v -> Dat t v)
  -- porting_TrP_
  -- porting__TrP_
porting_ mc_h vm_n_6h tr_n5p_6n tr_p5s_6p tr_t5n_6n dat_v_6s = dat_v_6t where
  trp_n5p_6n = load_ tr_n5p_6n
  trp_t5n_6n = load_ tr_t5n_6n
  dat_v_6t = porting__TrP_ mc_h vm_n_6h trp_n5p_6n tr_p5s_6p trp_t5n_6n dat_v_6s







-- __all__
core_prepare4porting_ :: Mc m -> Tr m z n -> Tr z p n -> Tr__income n p
core_prepare4porting_ = cross_translate_
--core_prepare4porting_ mc_m tr_n5z_6m tr_n5p_6z = tr_n5p_6n where
--  tr_n5p_6n = cross_translate_ mc_m tr_n5z_6m tr_n5p_6z

core_prepare4porting__ver2_ :: Mc m -> TrP m z n -> Tr z p n -> Tr__income n p
core_prepare4porting__ver2_ = cross_translate__TrP_
--core_prepare4porting__ver2_ mc_m trp_n5z_6m tr_n5p_6z = tr_n5p_6n where
--  tr_n5p_6n = cross_translate__TrP_ mc_m trp_n5z_6m tr_n5p_6z


core_prepare4porting__ver3_ :: Mc m -> Tr m g n -> Tr g p n -> Tr__income n p
core_prepare4porting__ver3_ = core_prepare4porting_



low_prepare4porting_ :: Mc m -> Tr m z n -> Tr z n e -> ManualPortO z n e t -> Similar e t -> Tr__outgo n t
low_prepare4porting_ mc_m tr_n5z_6m tr_e5n_6z manual_portO_e2t__5n_6z similar_e_t = tr_t5n_6n where
  tr_t5n_6z = apply_manual_portO_ similar_e_t manual_portO_e2t__5n_6z tr_e5n_6z
  tr_t5n_6n = cross_translate_ mc_m tr_n5z_6m tr_t5n_6z


low_prepare4porting__ver2_ :: Mc m -> TrP m z n -> Tr z n e -> ManualPortO z n e t -> Similar e t -> Tr__outgo n t
low_prepare4porting__ver2_ mc_m trp_n5z_6m tr_e5n_6z manual_portO_e2t__5n_6z similar_e_t = tr_t5n_6n where
  tr_t5n_6z = apply_manual_portO_ similar_e_t manual_portO_e2t__5n_6z tr_e5n_6z
  tr_t5n_6n = cross_translate__TrP_ mc_m trp_n5z_6m tr_t5n_6z


low_prepare4porting__ver3_ :: Mc m -> Tr m g n -> Tr g n e -> ManualPortO g n e t -> Similar e t -> Tr__outgo n t
low_prepare4porting__ver3_ = low_prepare4porting_





high_prepare4porting_ :: Mc m -> Tr m z p -> Tr__outgo z p -> ManualPortI z p z s -> Similar z s -> Tr__income p s
high_prepare4porting_ mc_m tr_p5z_6m tr_p5z_6z manual_portI_z2s__p5_6z similar_z_s = tr_p5s_6p where
  tr_p5s_6z = apply_manual_portI_ similar_z_s manual_portI_z2s__p5_6z tr_p5z_6z
  tr_p5s_6p = cross_translate_ mc_m tr_p5z_6m tr_p5s_6z


high_prepare4porting__ver3_ :: Mc m -> Tr m g p -> Tr g z p -> ManualPortI g p z s -> Similar z s -> Tr__income p s
high_prepare4porting__ver3_ mc_m tr_p5g_6m tr_p5z_6g manual_portI_z2s__p5_6g similar_z_s = tr_p5s_6p where
  tr_p5s_6g = apply_manual_portI_ similar_z_s manual_portI_z2s__p5_6g tr_p5z_6g
  tr_p5s_6p = cross_translate_ mc_m tr_p5g_6m tr_p5s_6g





whole_prepare4porting__ver1_ :: Mc m -> Input4Prepare4Port__ver1 p n z e m s t -> Output4Prepare4Port p n s t
whole_prepare4porting__ver1_ mc_m (Input4Prepare4Port__ver1 (tr_p5z_6z, tr_n5p_6z, tr_e5n_6z, tr_p5z_6m, tr_n5z_6m, manual_portI_z2s__p5_6z, manual_portO_e2t__5n_6z, similar_z_s, similar_e_t)) = Output4Prepare4Port (tr_p5s_6p, tr_n5p_6n, tr_t5n_6n) where
  tr_n5p_6n = core_prepare4porting_ mc_m tr_n5z_6m tr_n5p_6z
  tr_t5n_6n = low_prepare4porting_ mc_m tr_n5z_6m tr_e5n_6z manual_portO_e2t__5n_6z similar_e_t
  tr_p5s_6p = high_prepare4porting_ mc_m tr_p5z_6m tr_p5z_6z manual_portI_z2s__p5_6z similar_z_s



whole_prepare4porting__ver2_ :: Mc m -> Input4Prepare4Port__ver2 p n z e m s t -> Output4Prepare4Port p n s t
whole_prepare4porting__ver2_ mc_m (Input4Prepare4Port__ver2 (tr_p5z_6z, tr_n5p_6z, tr_e5n_6z, tr_m5z_6m, manual_portI_z2s__p5_6z, manual_portO_e2t__5n_6z, similar_z_s, similar_e_t)) = Output4Prepare4Port (tr_p5s_6p, tr_n5p_6n, tr_t5n_6n) where
  tr_p5z_6m = self_resident_translate_ mc_m tr_m5z_6m tr_p5z_6z
  tr_n5p_6m = self_resident_translate_ mc_m tr_m5z_6m tr_n5p_6z
  trp_n5z_6m = chain_TrP_ (load_ tr_p5z_6m) (load_ tr_n5p_6m)
  tr_n5p_6n = core_prepare4porting__ver2_ mc_m trp_n5z_6m tr_n5p_6z
  tr_t5n_6n = low_prepare4porting__ver2_ mc_m trp_n5z_6m tr_e5n_6z manual_portO_e2t__5n_6z similar_e_t
  tr_p5s_6p = high_prepare4porting_ mc_m tr_p5z_6m tr_p5z_6z manual_portI_z2s__p5_6z similar_z_s


whole_prepare4porting__ver3_ :: Mc m -> Input4Prepare4Port__ver3 p n g z e m s t -> Output4Prepare4Port p n s t
whole_prepare4porting__ver3_ mc_m (Input4Prepare4Port__ver3 (tr_n5p_6g, tr_p5z_6g, tr_e5n_6g, tr_p5g_6m, tr_n5g_6m, manual_portI_z2s__p5_6g, manual_portO_e2t__5n_6g, similar_z_s, similar_e_t)) = Output4Prepare4Port (tr_p5s_6p, tr_n5p_6n, tr_t5n_6n) where
  tr_n5p_6n = core_prepare4porting__ver3_ mc_m tr_n5g_6m tr_n5p_6g
  tr_t5n_6n = low_prepare4porting__ver3_ mc_m tr_n5g_6m tr_e5n_6g manual_portO_e2t__5n_6g similar_e_t
  tr_p5s_6p = high_prepare4porting__ver3_ mc_m tr_p5g_6m tr_p5z_6g manual_portI_z2s__p5_6g similar_z_s









whole_picture4porting__ver1_ :: Mc m -> Mc h -> Vm h n -> Input4Prepare4Port__ver1 p n z e m s t -> (Dat s v -> Dat t v)
whole_picture4porting__ver1_ mc_m mc_h vm_n_6h input4prepare4port__ver1 dat_v_6s = dat_v_6t where
  Output4Prepare4Port (tr_p5s_6p, tr_n5p_6n, tr_t5n_6n) = whole_prepare4porting__ver1_ mc_m input4prepare4port__ver1
  dat_v_6t = porting_ mc_h vm_n_6h tr_n5p_6n tr_p5s_6p tr_t5n_6n dat_v_6s




whole_picture4porting__ver2_ :: Mc m -> Mc h -> Vm h n -> Input4Prepare4Port__ver2 p n z e m s t -> (Dat s v -> Dat t v)
whole_picture4porting__ver2_ mc_m mc_h vm_n_6h input4prepare4port__ver2 dat_v_6s = dat_v_6t where
  Output4Prepare4Port (tr_p5s_6p, tr_n5p_6n, tr_t5n_6n) = whole_prepare4porting__ver2_ mc_m input4prepare4port__ver2
  dat_v_6t = porting_ mc_h vm_n_6h tr_n5p_6n tr_p5s_6p tr_t5n_6n dat_v_6s


whole_picture4porting__ver3_ :: Mc m -> Mc h -> Vm h n -> Input4Prepare4Port__ver3 p n g z e m s t -> (Dat s v -> Dat t v)
whole_picture4porting__ver3_ mc_m mc_h vm_n_6h input4prepare4port__ver3 dat_v_6s = dat_v_6t where
  Output4Prepare4Port (tr_p5s_6p, tr_n5p_6n, tr_t5n_6n) = whole_prepare4porting__ver3_ mc_m input4prepare4port__ver3
  dat_v_6t = porting_ mc_h vm_n_6h tr_n5p_6n tr_p5s_6p tr_t5n_6n dat_v_6s




-- ######################
-- 再发现其实没毛病{Tr<:Dat}:xxx:发现porting_的类型有毛病，改为：porting_TrP_,port_Tr_,port_Vm_
-- porting_TrP_ :: ... -> trp_t5s_6h
-- port_Tr_ :: ... -> tr_t5s_6h
-- port_Vm_ :: ... -> vm_n_6h
--
-- vs:(vm_n_6g|vm_n_6p|vm_n_6n)
-- [n足够简单][p不过于低级] => [vm_n_6p容易手写]
-- [n,p足够简单][g足够高级] => [tr_n5p_6g容易手写]
-- [g太复杂][任意x] => [tr_x5g_6g不容易手写] # 否决:vm_n_6g
-- [tr_m5g_6m已存在与mc_m上]
--
-- port_Vm_ :: mc_m -> tr_h5n_6m -> vm_n_6n -> vm_n_6h
--  !! vm_n_6n <-- (vm_n_6p,tr_n5p_6m)
--  !! tr_n5p_6m <-- (tr_n5p_6g,tr_m5g_6m)
--  => vm_n_6n <-- (vm_n_6p,tr_n5p_6g,tr_m5g_6m)
--
--  !! tr_h5n_6m <-- (tr_h5n_6g,tr_m5g_6m)
--  !! tr_h5n_6g <-- (tr_k5n_6g,manual_portO_k2h__5n_6g,similar_k_h)
--  => tr_h5n_6m <-- (tr_k5n_6g,manual_portO_k2h__5n_6g,similar_k_h,tr_m5g_6m)
--
-- port_Vm__ver66_ :: mc_m -> tr_m5g_6m -> tr_k5n_6g -> manual_portO_k2h__5n_6g -> similar_k_h -> tr_n5p_6g -> vm_n_6p -> vm_n_6h
--
--
-- port_Tr_ :: mc_m -> tr_h5n_6m -> tr_t5s_6n -> tr_t5s_6h
--  !! tr_t5s_6n <-- (tr_t5s_6p,tr_n5p_6m)
--  !! tr_t5s_6p <-- (tr_t5z_6p,manual_portI_z2s__t5_6p,similar_z_s)
--  !! tr_t5z_6p <-- (tr_e5z_6p,manual_portO_e2t__5z_6p,similar_e_t)
--  !! tr_n5p_6m <-- (tr_n5p_6g,tr_m5g_6m)
--  => tr_t5s_6n <-- (tr_e5z_6p,manual_portO_e2t__5z_6p,similar_e_t,manual_portI_z2s__t5_6p,similar_z_s,tr_n5p_6g,tr_m5g_6m)
--  !! 见上面: tr_h5n_6m <-- (tr_k5n_6g,manual_portO_k2h__5n_6g,similar_k_h,tr_m5g_6m)
-- port_Tr__ver66_ :: mc_m -> tr_m5g_6m -> tr_k5n_6g -> manual_portO_k2h__5n_6g -> similar_k_h -> tr_n5p_6g -> manual_portO_e2t__5z_6p -> similar_e_t -> manual_portI_z2s__t5_6p -> similar_z_s -> tr_e5z_6p -> tr_t5s_6h
--
--
-- porting_TrP_ :: trp_t5e_6n -> trp_e5z_6n -> trp_z5s_6n -> trp_t5s_6n
--
--
--
-- :s/,/ -> /g
-- :s/ \(::\|->\) / /g
-- :s/\vtr_(\w)5(\w)_6(\w)/Tr \3 \2 \1/g
-- :s/\vtrp_(\w)5(\w)_6(\w)/TrP \3 \2 \1/g
--
-- tr7degenerate_   #=== tr7core_{g:=s;h:=t}
-- Output: tr_t5s_6t
--  => Input: tr_t5s_6s,trp_t5s_6m,mc_m
--
-- tr7core_
-- Output: tr_t5s_6h
--  => Input: tr_t5s_6g,trp_h5g_6m,mc_m
--
-- trp7chain_       #生成tr7core_的参数{翻译器}
-- Output: trp_t5s_6n
--  => Input: mc_h,vm_n_6h,trp_t5n_6n,trp_n5s_6n
--
-- tr7vmI_
-- Output: tr_n5s_6n
--  => Input: tr_n5s_6s,tr_n5s_6p,tr_n5p_6n,vm_n_6m,mc_m
--
-- tr7vmII_
-- Output: (tr_p5s_6n,trp_n5s_6n)
--  => Input: tr_p5s_6p,tr_n5p_6n,vm_n_6m,mc_m
--
-- tr7vmIII_
-- Output: (tr_p5s_6p,tr_p5s_6n,trp_n5s_6n)
--  => Input: tr_p5s_6s,tr_m5s_6m,tr_n5p_6n,vm_n_6m,mc_m
--
-- tr7bootstrap_
-- Output: (tr_n5s_6n,trp_t5s_6n)
--  => Input: tr_n5x_6n,tr_x5y_6x,tr_y5s_6y,tr_n5s_6s,tr_t5n_6n,vm_n_6m,mc_m  #useless:『x_le_y,y_le_s,』
--
--
-- ######################
-- __all__
tr7core_ :: Mc m -> TrP m g h -> Tr g s t -> Tr h s t
tr7core_ = cross_translate__TrP_
-- .tr7core_ mc_m trp_h5g_6m tr_t5s_6g = tr_t5s_6h where
-- .  tr_t5s_6h = cross_translate__TrP_ mc_m trp_h5g_6m tr_t5s_6g

tr7degenerate_ :: Mc m -> TrP m s t -> Tr__outgo s t -> Tr__income t s
tr7degenerate_ = cross_translate__TrP_
-- .tr7degenerate_ mc_m trp_t5s_6m tr_t5s_6s = tr_t5s_6t where
-- .  tr_t5s_6t = cross_translate__TrP_ mc_m trp_t5s_6m tr_t5s_6s


trp7chain_ :: TrP__outgo n t -> TrP__income n s -> TrP n s t
trp7chain_ = flip chain_TrP_
-- .trp7chain_ trp_t5n_6n trp_n5s_6n = trp_t5s_6n where
-- .  trp_t5s_6n = chain_TrP_ trp_n5s_6n trp_t5n_6n


tr7vmI__TrP_ :: Mc m -> Vm m n -> TrP__income n p -> Tr p s n -> Tr__outgo s n -> Tr__income n s
tr7vmI__TrP_ mc_m vm_n_6m trp_n5p_6n tr_n5s_6p tr_n5s_6s = tr_n5s_6n where
  mc_n = mk_Mc_ mc_m vm_n_6m
  tr_n5s_6n__verP = self_resident_translate__TrP_ mc_n trp_n5p_6n tr_n5s_6p
  tr_n5s_6n__verS = self_resident_translate_ mc_n tr_n5s_6n__verP tr_n5s_6s
  tr_n5s_6n = if False then tr_n5s_6n__verP else tr_n5s_6n__verS

tr7vmI_ :: Mc m -> Vm m n -> Tr__income n p -> Tr p s n -> Tr__outgo s n -> Tr__income n s
  -- tr7vmI__TrP_
tr7vmI_ mc_m vm_n_6m tr_n5p_6n tr_n5s_6p tr_n5s_6s = tr_n5s_6n where
  trp_n5p_6n = load_ tr_n5p_6n
  tr_n5s_6n = tr7vmI__TrP_ mc_m vm_n_6m trp_n5p_6n tr_n5s_6p tr_n5s_6s



tr7vmII__TrP_ :: Mc m -> Vm m n -> TrP__income n p -> Tr__income p s -> (Tr n s p, TrP__income n s)
tr7vmII__TrP_ mc_m vm_n_6m trp_n5p_6n tr_p5s_6p = (tr_p5s_6n, trp_n5s_6n) where
  mc_n = mk_Mc_ mc_m vm_n_6m
  tr_p5s_6n = self_resident_translate__TrP_ mc_n trp_n5p_6n tr_p5s_6p
  trp_p5s_6n = load_ tr_p5s_6n
  -- trp_n5p_6n = load_ tr_n5p_6n
  trp_n5s_6n = chain_TrP_ trp_p5s_6n trp_n5p_6n

tr7vmII_ :: Mc m -> Vm m n -> Tr__income n p -> Tr__income p s -> (Tr n s p, TrP__income n s)
  -- tr7vmII__TrP_
tr7vmII_ mc_m vm_n_6m tr_n5p_6n tr_p5s_6p = (tr_p5s_6n, trp_n5s_6n) where
  trp_n5p_6n = load_ tr_n5p_6n
  (tr_p5s_6n, trp_n5s_6n) = tr7vmII__TrP_ mc_m vm_n_6m trp_n5p_6n tr_p5s_6p



tr7vmIII__TrP_ :: Mc m -> Vm m n -> TrP__income n p -> Tr__outgo s p -> TrP__income m s -> (Tr__income p s, Tr n s p, TrP__income n s)
tr7vmIII__TrP_ mc_m vm_n_6m trp_n5p_6n tr_p5s_6s trp_m5s_6m = (tr_p5s_6p, tr_p5s_6n, trp_n5s_6n) where
  tr_p5s_6p = tr__port__TrP_ mc_m trp_m5s_6m tr_p5s_6s
      -- .tr_p5s_6m = self_resident_translate_ mc_m tr_m5s_6m tr_p5s_6s
      -- .tr_p5s_6p = cross_translate_ mc_m tr_p5s_6m tr_p5s_6s
  (tr_p5s_6n, trp_n5s_6n) = tr7vmII__TrP_ mc_m vm_n_6m trp_n5p_6n tr_p5s_6p

tr7vmIII_ :: Mc m -> Vm m n -> Tr__income n p -> Tr__outgo s p -> Tr__income m s -> (Tr__income p s, Tr n s p, TrP__income n s)
  -- tr7vmIII__TrP_
tr7vmIII_ mc_m vm_n_6m tr_n5p_6n tr_p5s_6s tr_m5s_6m = (tr_p5s_6p, tr_p5s_6n, trp_n5s_6n) where
  trp_m5s_6m = load_ tr_m5s_6m
  trp_n5p_6n = load_ tr_n5p_6n
  (tr_p5s_6p, tr_p5s_6n, trp_n5s_6n) = tr7vmIII__TrP_ mc_m vm_n_6m trp_n5p_6n tr_p5s_6s trp_m5s_6m





tr7bootstrap__TrP_ :: Mc m -> Vm m n -> TrP__income n x -> Tr__income x y -> Tr__income y s -> Tr__outgo s n -> TrP__outgo n t -> (Tr__income n s, TrP n s t)
tr7bootstrap__TrP_ mc_m vm_n_6m trp_n5x_6n tr_x5y_6x tr_y5s_6y tr_n5s_6s trp_t5n_6n = if False then result__via_Tr else result__via_TrP where
  result__via_Tr = (tr_n5s_6n,trp_t5s_6n) where
    mc_n = mk_Mc_ mc_m vm_n_6m
    tr_x5y_6n = self_resident_translate__TrP_ mc_n trp_n5x_6n tr_x5y_6x

    tr_y5s_6x = cross_translate_ mc_n tr_x5y_6n tr_y5s_6y
    tr_y5s_6n = self_resident_translate__TrP_ mc_n trp_n5x_6n tr_y5s_6x

    tr_n5s_6y = cross_translate_ mc_n tr_y5s_6n tr_n5s_6s
    tr_n5s_6x = cross_translate_ mc_n tr_x5y_6n tr_n5s_6y
    tr_n5s_6n = self_resident_translate__TrP_ mc_n trp_n5x_6n tr_n5s_6x

    trp_n5s_6n = load_ tr_n5s_6n
    trp_t5s_6n = chain_TrP_ trp_n5s_6n trp_t5n_6n
    -- .trp_t5s_6n = chain_TrP_ (load_ tr_n5s_6n) (load_ tr_t5n_6n)


  result__via_TrP = (tr_n5s_6n,trp_t5s_6n) where
    -- 串联tr_n5x_6n,tr_x5y_6x,tr_y5s_6y可得trp_n5s_6n__verCHAIN
    -- 串联tr_t5n_6n,tr_n5s_6n可得trp_t5s_6n
    mc_n = mk_Mc_ mc_m vm_n_6m
    --trp_n5x_6n = load_ tr_n5x_6n

    trp_n5y_6n = chain_TrP_Tr__income_ mc_n trp_n5x_6n tr_x5y_6x
        -- .tr_x5y_6n = self_resident_translate__TrP_ mc_n trp_n5x_6n tr_x5y_6x
        -- .trp_x5y_6n = load_ tr_x5y_6n
        -- .trp_n5y_6n = chain_TrP_ trp_x5y_6n trp_n5x_6n

    trp_n5s_6n__verCHAIN = chain_TrP_Tr__income_ mc_n trp_n5y_6n tr_y5s_6y
        -- .tr_y5s_6n = self_resident_translate__TrP_ mc_n trp_n5y_6n tr_y5s_6y
        -- .trp_y5s_6n = load_ tr_y5s_6n
        -- .trp_n5s_6n__verCHAIN = chain_TrP_ trp_y5s_6n trp_n5y_6n

    tr_n5s_6n = self_resident_translate__TrP_ mc_n trp_n5s_6n__verCHAIN tr_n5s_6s
    trp_n5s_6n__verLOAD = load_ tr_n5s_6n

    trp_n5s_6n = if False then trp_n5s_6n__verCHAIN else trp_n5s_6n__verLOAD

    --trp_t5n_6n = load_ tr_t5n_6n
    trp_t5s_6n = chain_TrP_ trp_n5s_6n trp_t5n_6n


tr7bootstrap_ :: Mc m -> Vm m n -> Tr__income n x -> Tr__income x y -> Tr__income y s -> Tr__outgo s n -> Tr__outgo n t -> (Tr__income n s, TrP n s t)
  -- tr7bootstrap__TrP_
--tr7bootstrap_ mc_m vm_n_6m tr_n5x_6n tr_x5y_6x tr_y5s_6y tr_n5s_6s tr_t5n_6n = (tr_n5s_6n,trp_t5s_6n) where
  -- useless:『SuperLang x y -> SuperLang y s -> 』『x_le_y y_le_s 』
tr7bootstrap_ mc_m vm_n_6m tr_n5x_6n tr_x5y_6x tr_y5s_6y tr_n5s_6s tr_t5n_6n = (tr_n5s_6n,trp_t5s_6n) where
  trp_n5x_6n = load_ tr_n5x_6n
  trp_t5n_6n = load_ tr_t5n_6n

  (tr_n5s_6n,trp_t5s_6n) = tr7bootstrap__TrP_ mc_m vm_n_6m trp_n5x_6n tr_x5y_6x tr_y5s_6y tr_n5s_6s trp_t5n_6n






-- ######################
port_Vm__TrP_ :: Mc m -> TrP m n h -> Vm n n -> Vm h n
port_Vm__TrP_ = cross_translate__TrP_
port_Vm_ :: Mc m -> Tr m n h -> Vm n n -> Vm h n
port_Vm_ = cross_translate_
-- .port_Vm_ mc_m tr_h5n_6m vm_n_6n = vm_n_6h where
-- .  vm_n_6h = cross_translate_ mc_m tr_h5n_6m vm_n_6n

port_Vm__TrP__ver66_ :: Mc m -> TrP__income m g -> Tr g n k -> ManualPortO g n k h -> Similar k h -> Tr g p n -> Vm p n -> Vm h n
port_Vm__TrP__ver66_ mc_m trp_m5g_6m tr_k5n_6g manual_portO_k2h__5n_6g similar_k_h tr_n5p_6g vm_n_6p = vm_n_6h where
  tr_n5p_6m = self_resident_translate__TrP_ mc_m trp_m5g_6m tr_n5p_6g
  vm_n_6n = cross_translate_ mc_m tr_n5p_6m vm_n_6p

  tr_h5n_6g = apply_manual_portO_ similar_k_h manual_portO_k2h__5n_6g tr_k5n_6g
  tr_h5n_6m = self_resident_translate__TrP_ mc_m trp_m5g_6m tr_h5n_6g

  vm_n_6h = port_Vm_ mc_m tr_h5n_6m vm_n_6n

port_Vm__ver66_ :: Mc m -> Tr__income m g -> Tr g n k -> ManualPortO g n k h -> Similar k h -> Tr g p n -> Vm p n -> Vm h n
  -- port_Vm__TrP__ver66_
port_Vm__ver66_ mc_m tr_m5g_6m tr_k5n_6g manual_portO_k2h__5n_6g similar_k_h tr_n5p_6g vm_n_6p = vm_n_6h where
  trp_m5g_6m = load_ tr_m5g_6m
  vm_n_6h = port_Vm__TrP__ver66_ mc_m trp_m5g_6m tr_k5n_6g manual_portO_k2h__5n_6g similar_k_h tr_n5p_6g vm_n_6p



-- ######################

port_Tr__TrP_ :: Mc m -> TrP m n h -> Tr n s t -> Tr h s t
port_Tr__TrP_ = cross_translate__TrP_
port_Tr_ :: Mc m -> Tr m n h -> Tr n s t -> Tr h s t
port_Tr_ = cross_translate_
-- .port_Tr_ mc_m tr_h5n_6m tr_t5s_6n = tr_t5s_6h where
-- .  tr_t5s_6h = cross_translate_ mc_m tr_h5n_6m tr_t5s_6n


port_Tr__TrP__ver66_ :: Mc m -> TrP__income m g -> Tr g n k -> ManualPortO g n k h -> Similar k h -> Tr g p n -> ManualPortO p z e t -> Similar e t -> ManualPortI p t z s -> Similar z s -> Tr p z e -> Tr h s t
port_Tr__TrP__ver66_ mc_m trp_m5g_6m tr_k5n_6g manual_portO_k2h__5n_6g similar_k_h tr_n5p_6g manual_portO_e2t__5z_6p similar_e_t manual_portI_z2s__t5_6p similar_z_s tr_e5z_6p = tr_t5s_6h where
  tr_t5z_6p = apply_manual_portO_ similar_e_t manual_portO_e2t__5z_6p tr_e5z_6p
  tr_t5s_6p = apply_manual_portI_ similar_z_s manual_portI_z2s__t5_6p tr_t5z_6p

  tr_n5p_6m = self_resident_translate__TrP_ mc_m trp_m5g_6m tr_n5p_6g

  tr_t5s_6n = cross_translate_ mc_m tr_n5p_6m tr_t5s_6p

  tr_h5n_6g = apply_manual_portO_ similar_k_h manual_portO_k2h__5n_6g tr_k5n_6g
  tr_h5n_6m = self_resident_translate__TrP_ mc_m trp_m5g_6m tr_h5n_6g

  tr_t5s_6h = port_Tr_ mc_m tr_h5n_6m tr_t5s_6n

port_Tr__ver66_ :: Mc m -> Tr__income m g -> Tr g n k -> ManualPortO g n k h -> Similar k h -> Tr g p n -> ManualPortO p z e t -> Similar e t -> ManualPortI p t z s -> Similar z s -> Tr p z e -> Tr h s t
  --port_Tr__TrP__ver66_
port_Tr__ver66_ mc_m tr_m5g_6m tr_k5n_6g manual_portO_k2h__5n_6g similar_k_h tr_n5p_6g manual_portO_e2t__5z_6p similar_e_t manual_portI_z2s__t5_6p similar_z_s tr_e5z_6p = tr_t5s_6h where
  trp_m5g_6m = load_ tr_m5g_6m
  tr_t5s_6h = port_Tr__TrP__ver66_ mc_m trp_m5g_6m tr_k5n_6g manual_portO_k2h__5n_6g similar_k_h tr_n5p_6g manual_portO_e2t__5z_6p similar_e_t manual_portI_z2s__t5_6p similar_z_s tr_e5z_6p


-- ######################
porting_TrP_ :: TrP n e t -> TrP n z e -> TrP n s z -> TrP n s t
  -- porting_TrP_ vs porting__TrP_
porting_TrP_ trp_t5e_6n trp_e5z_6n trp_z5s_6n = trp_t5s_6n where
  trp_e5s_6n = chain_TrP_ trp_z5s_6n trp_e5z_6n
  trp_t5s_6n = chain_TrP_ trp_e5s_6n trp_t5e_6n



-- ######################
-- ######################
-- 旧语言vs新语言:
--
-- ***他助编译:新语言起步 依赖 旧语言乊旧机器 编译
--  他助编译
--  单文件:(tr_m5s_6m) <<== (tr_m5s_6g,trp_m5g_6m,mc_m)
--      #tr_m5s_6m = mk_tr4new_lang_I__A_ mc_m trp_m5g_6m tr_m5s_6g
--  双文件:(tr_m5w_6m,tr_w5s_6m) <<== (tr_m5w_6m,tr_w5s_6g,trp_m5g_6m,mc_m)
--      #(tr_m5w_6m,tr_w5s_6m) = mk_tr_tr4new_lang_II__A_ mc_m tr_m5w_6m trp_m5g_6m tr_w5s_6g
-- ***移植编译:旧语言乊新机器 依赖 旧机器上的跨机翻译器 编译
--  移植编译
--  单文件:(tr_t5s_6t) <<== (tr_t5s_6s,trp_m5s_6m,mc_m)
--      #tr_t5s_6t = mk_tr4old_lang6new_machine_I__A_ mc_m trp_m5s_6m tr_t5s_6s
--  双文件:(tr_t5w_6t,tr_w5s_6t) <<== (tr_t5w_6w,tr_w5s_6s,trp_m5w_6m,trp_m5s_6m,mc_m)
--      #(tr_t5w_6t,tr_w5s_6t) = mk_tr_tr4old_lang6new_machine_II__A_ mc_m trp_m5w_6m trp_m5s_6m tr_t5w_6w tr_w5s_6s
--  双文件牜预备:(tr_t5w_6w) <<== (tr_t5w_6p,tr_w5p_6p,trp_m5p_6m,mc_m)
--      #tr_t5w_6w = prepareA4mk_tr_tr4old_lang6new_machine_II__A_ mc_m trp_w5p_6m tr_t5w_6p
--      #tr_t5w_6w = prepareB4mk_tr_tr4old_lang6new_machine_II__A_ mc_m trp_m5p_6m tr_w5p_6p tr_t5w_6p
-- ***变体编译:新版本纟旧语言乊旧机器 依赖 旧版本纟旧语言乊旧机器:
--  变体编译
--      发现:useless:superlang_c_s
--      =>也可以是 更新补丁、方言、相似度高的语法族类
--  单文件:(tr_m5s_6m) <<== (?superlang_c_s?,tr_c5s_6c,tr_m5c_6m,mc_m)
--      #tr_m5c_6m:用于cat_Tr_
--      #tr_m5s_6m = mk_tr4new_ver4old_lang6old_machine_I__A_ mc_m tr_m5c_6m ?superlang_c_s? tr_c5s_6c
--  双文件:(tr_m5w_6m,tr_w5s_6m) <<== (tr_m5w_6m,?superlang_c_s?,tr_c5s_6c,tr_w5c_6m,mc_m)
--      #tr_w5c_6m:用于cat_Tr_
--      #(tr_m5w_6m,tr_w5s_6m) = mk_tr_tr4new_ver4old_lang6old_machine_II__A_ mc_m tr_m5w_6m tr_w5c_6m ?superlang_c_s? tr_c5s_6c
-- ***更新编译:新算法纟翻译诀乊旧语言乊旧机器 依赖 旧算法纟翻译诀乊旧语言乊旧机器:
--      #翻译诀:更新补丁，添加特性
--  单文件:(new-tr_m5s_6m) <<== (new-tr_m5s_6s,old-trp_m5s_6m,mc_m)
--      #tr_m5s_6m = mk_tr4new_ver4algo6old_lang6old_machine_I__A_ mc_m trp_m5s_6m tr_m5s_6s
--  双文件:fst:(new-tr_m5w_6m) <<== (new-tr_m5w_6w,old-trp_m5w_6m,?old-trp_w5s_6m?,mc_m)
--      #tr_m5w_6m = mk_fst4tr_tr4new_ver4algo6old_lang6old_machine_II__A_ mc_m trp_m5w_6m ?trp_w5s_6m? tr_m5w_6w
--  双文件:snd:(new-tr_w5s_6m) <<== (new-tr_w5s_6s,old-trp_m5w_6m,old-trp_w5s_6m,mc_m)
--      #tr_w5s_6m = mk_snd4tr_tr4new_ver4algo6old_lang6old_machine_II__A_ mc_m trp_m5w_6m trp_w5s_6m tr_w5s_6s
--  ***跨机编译:嵌入式系统，宿主机不含编译器，依赖 外部编译
--      ???TODO
--
-- ######################
-- w旧语言，则 假设已有:tr_m5w_6m/trp_m5w_6m,?tr_m5w_6w
-- g旧语言，则 假设已有:tr_m5g_6m/trp_m5g_6m,?tr_w5g_6g,?tr_m5g_6g
--
-- s新语言起步时，还未有:tr_m5s_6m/trp_m5s_6m
--  先依赖其他高级语言:tr_w5s_6g
--  双文件:目标:(trp_m5s_6m,tr_w5s_6m)
--      已有:mc_m, trp_m5w_6m, trp_m5g_6m, tr_w5s_6g, ?tr_w5s_6s
--      front_end_tr:tr_w5s_6m
--      back_end_tr:tr_m5w_6m#trp_m5w_6m
--  单文件:目标:(trp_m5s_6m/tr_m5s_6m)
--      已有:mc_m, trp_m5g_6m, tr_m5s_6g, ?tr_m5s_6s
--
--




-- 更新编译:新算法纟翻译诀乊旧语言乊旧机器:单文件
mk_tr4new_ver4algo6old_lang6old_machine_I__A_ :: Mc m -> TrP__income m s -> Tr__outgo s m -> Tr__income m s
  -- 单文件:(new-tr_m5s_6m) <<== (new-tr_m5s_6s,old-trp_m5s_6m,mc_m)
mk_tr4new_ver4algo6old_lang6old_machine_I__A_ = self_resident_translate__TrP_
-- .mk_tr4new_ver4algo6old_lang6old_machine_I__A_ mc_m trp_m5s_6m tr_m5s_6s = tr_m5s_6m where
-- .  tr_m5s_6m = self_resident_translate__TrP_ mc_m trp_m5s_6m tr_m5s_6s



-- 更新编译:新算法纟翻译诀乊旧语言乊旧机器:双文件.fst
mk_fst4tr_tr4new_ver4algo6old_lang6old_machine_II__A_ :: Mc m -> TrP__income m w -> Tr__outgo w m -> Tr__income m w
  -- 双文件:fst:(new-tr_m5w_6m) <<== (new-tr_m5w_6w,old-trp_m5w_6m,?old-trp_w5s_6m?,mc_m)
mk_fst4tr_tr4new_ver4algo6old_lang6old_machine_II__A_ = self_resident_translate__TrP_
-- .mk_fst4tr_tr4new_ver4algo6old_lang6old_machine_II__A_ mc_m trp_m5w_6m tr_m5w_6w = tr_m5w_6m where
-- .  tr_m5w_6m = self_resident_translate__TrP_ mc_m trp_m5w_6m tr_m5w_6w



-- 更新编译:新算法纟翻译诀乊旧语言乊旧机器:双文件.snd
mk_snd4tr_tr4new_ver4algo6old_lang6old_machine_II__A_ :: Mc m -> TrP__income m w -> TrP m s w -> Tr__outgo s w -> Tr m s w
  -- 双文件:snd:(new-tr_w5s_6m) <<== (new-tr_w5s_6s,old-trp_m5w_6m,old-trp_w5s_6m,mc_m)
mk_snd4tr_tr4new_ver4algo6old_lang6old_machine_II__A_ mc_m trp_m5w_6m trp_w5s_6m tr_w5s_6s = tr_w5s_6m where
  trp_m5s_6m = chain_TrP_ trp_w5s_6m trp_m5w_6m
  tr_w5s_6m = self_resident_translate__TrP_ mc_m trp_m5s_6m tr_w5s_6s





-- 变体编译:新版本纟旧语言乊旧机器:单文件
-- .mk_tr4new_ver4old_lang6old_machine_I__A_ :: Mc m -> Tr__income m c -> SuperLang c s -> Tr__income c s -> Tr__income m s
-- .mk_tr4new_ver4old_lang6old_machine_I__A_ mc_m tr_m5c_6m superlang_c_s tr_c5s_6c = tr_m5s_6m where
  -- useless:superlang_c_s
mk_tr4new_ver4old_lang6old_machine_I__A_ :: Mc m -> Tr__income m c -> Tr__income c s -> Tr__income m s
  -- tr_m5c_6m:用于cat_Tr_
mk_tr4new_ver4old_lang6old_machine_I__A_ mc_m tr_m5c_6m tr_c5s_6c = tr_m5s_6m where
  tr_c5s_6m = self_resident_translate_ mc_m tr_m5c_6m tr_c5s_6c
  tr_m5s_6m = cat_Tr_ tr_m5c_6m tr_c5s_6m
  -- xxx:tr_c5s_6s = upgradeB_Tr_ superlang_c_s tr_c5s_6c
  -- xxx:tr_c5s_6c = cross_translate_ mc_m tr_c5s_6m tr_c5s_6s


-- 变体编译:新版本纟旧语言乊旧机器:双文件
-- .mk_tr_tr4new_ver4old_lang6old_machine_II__A_ :: Mc m -> Tr__income m w -> Tr m c w -> SuperLang c s -> Tr__income c s -> (Tr__income m w,Tr m s w)
-- .mk_tr_tr4new_ver4old_lang6old_machine_II__A_ mc_m tr_m5w_6m tr_w5c_6m superlang_c_s tr_c5s_6c = (tr_m5w_6m,tr_w5s_6m) where
  -- useless:superlang_c_s
mk_tr_tr4new_ver4old_lang6old_machine_II__A_ :: Mc m -> Tr__income m w -> Tr m c w -> Tr__income c s -> (Tr__income m w,Tr m s w)
  --tr_w5c_6m:用于cat_Tr_
mk_tr_tr4new_ver4old_lang6old_machine_II__A_ mc_m tr_m5w_6m tr_w5c_6m tr_c5s_6c = (tr_m5w_6m,tr_w5s_6m) where
  tr_m5c_6m = cat_Tr_ tr_m5w_6m tr_w5c_6m
  tr_c5s_6m = self_resident_translate_ mc_m tr_m5c_6m tr_c5s_6c
  tr_w5s_6m = cat_Tr_ tr_w5c_6m tr_c5s_6m




-- 移植编译:旧语言乊新机器:单文件
mk_tr4old_lang6new_machine_I__A_ :: Mc m -> TrP__income m s -> Tr__outgo s t -> Tr__income t s
mk_tr4old_lang6new_machine_I__A_ = tr__port__TrP_
-- .mk_tr4old_lang6new_machine_I__A_ mc_m trp_m5s_6m tr_t5s_6s = tr_t5s_6t where
-- .  tr_t5s_6t = tr__port__TrP_ mc_m trp_m5s_6m tr_t5s_6s

-- 移植编译:旧语言乊新机器:双文件
prepareA4mk_tr_tr4old_lang6new_machine_II__A_ :: Mc m -> TrP m p w -> Tr p w t -> Tr__outgo w t
prepareA4mk_tr_tr4old_lang6new_machine_II__A_ = cross_translate__TrP_
-- .prepareA4mk_tr_tr4old_lang6new_machine_II__A_ mc_m trp_w5p_6m tr_t5w_6p = tr_t5w_6w where
-- .  tr_t5w_6w = cross_translate__TrP_ mc_m trp_w5p_6m tr_t5w_6p
prepareB4mk_tr_tr4old_lang6new_machine_II__A_ :: Mc m -> TrP__income m p -> Tr__outgo p w -> Tr p w t -> Tr__outgo w t
prepareB4mk_tr_tr4old_lang6new_machine_II__A_ mc_m trp_m5p_6m tr_w5p_6p tr_t5w_6p = tr_t5w_6w where
  tr_w5p_6m = self_resident_translate__TrP_ mc_m trp_m5p_6m tr_w5p_6p
  trp_w5p_6m = load_ tr_w5p_6m
  tr_t5w_6w = prepareA4mk_tr_tr4old_lang6new_machine_II__A_ mc_m trp_w5p_6m tr_t5w_6p

mk_tr_tr4old_lang6new_machine_II__A_ :: Mc m -> TrP__income m w -> TrP__income m s -> Tr__outgo w t -> Tr__outgo s w -> (Tr__income t w,Tr t s w)
mk_tr_tr4old_lang6new_machine_II__A_ mc_m trp_m5w_6m trp_m5s_6m tr_t5w_6w tr_w5s_6s = (tr_t5w_6t,tr_w5s_6t) where
  tr_t5w_6m = self_resident_translate__TrP_ mc_m trp_m5w_6m tr_t5w_6w
  tr_t5w_6t = cross_translate_ mc_m tr_t5w_6m tr_t5w_6w

  tr_w5s_6m = self_resident_translate__TrP_ mc_m trp_m5s_6m tr_w5s_6s

  trp_t5w_6m = load_ tr_t5w_6m
  trp_w5s_6m = load_ tr_w5s_6m

  trp_t5s_6m = chain_TrP_ trp_w5s_6m trp_t5w_6m

  tr_w5s_6t = cross_translate__TrP_ mc_m trp_t5s_6m tr_w5s_6s

-- 他助编译:新语言起步:单文件
mk_tr4new_lang_I__A_ :: Mc m -> TrP__income m g -> Tr g s m -> Tr__income m s
mk_tr4new_lang_I__A_ mc_m trp_m5g_6m tr_m5s_6g = tr_m5s_6m where
  tr_m5s_6m = cross_translate__TrP_ mc_m trp_m5g_6m tr_m5s_6g

mk_tr4new_lang_I__TrP_ :: Mc m -> TrP__income m s -> Tr__outgo s m -> Tr__income m s
mk_tr4new_lang_I__TrP_ = self_resident_translate__TrP_
-- .mk_tr4new_lang_I__TrP_ mc_m _0_trp_m5s_6m tr_m5s_6s = tr_m5s_6m where
-- .  tr_m5s_6m = self_resident_translate__TrP_ mc_m _0_trp_m5s_6m tr_m5s_6s

mk_tr4new_lang_I__B_ :: Mc m -> TrP__income m g -> Tr g s m -> Tr__outgo s m -> Tr__income m s
mk_tr4new_lang_I__B_ mc_m trp_m5g_6m tr_m5s_6g tr_m5s_6s = tr_m5s_6m where
  _0_tr_m5s_6m = mk_tr4new_lang_I__A_ mc_m trp_m5g_6m tr_m5s_6g
  -- tr_m5s_6m = self_resident_translate_ mc_m _0_tr_m5s_6m tr_m5s_6s
  _0_trp_m5s_6m = load_ _0_tr_m5s_6m
  tr_m5s_6m = mk_tr4new_lang_I__TrP_ mc_m _0_trp_m5s_6m tr_m5s_6s



-- 他助编译:新语言起步:双文件
mk_tr_tr4new_lang_II__A_ :: Mc m -> Tr__income m w -> TrP__income m g -> Tr g s w -> (Tr__income m w,Tr m s w)
mk_tr_tr4new_lang_II__A_ mc_m tr_m5w_6m trp_m5g_6m tr_w5s_6g = (tr_m5w_6m,tr_w5s_6m) where
  tr_w5s_6m = self_resident_translate__TrP_ mc_m trp_m5g_6m tr_w5s_6g
  -- tr_m5w_6m = ...echo SELF...

mk_trp_and_front_end_tr4new_lang_II__A_ :: Mc m -> TrP__income m w -> TrP__income m g -> Tr g s w -> (TrP__income m s,Tr m s w)
mk_trp_and_front_end_tr4new_lang_II__A_ mc_m trp_m5w_6m trp_m5g_6m tr_w5s_6g = (trp_m5s_6m,tr_w5s_6m) where
  tr_w5s_6m = self_resident_translate__TrP_ mc_m trp_m5g_6m tr_w5s_6g
  -- xxx:tr_w5s_6m = cross_translate_ mc_m tr_w5s_6m tr_w5s_6s
  trp_w5s_6m = load_ tr_w5s_6m
  trp_m5s_6m = chain_TrP_ trp_w5s_6m trp_m5w_6m


mk_front_end_tr4new_lang_II__TrP_ :: Mc m -> TrP__income m s -> Tr__outgo s w -> Tr m s w
mk_front_end_tr4new_lang_II__TrP_ mc_m trp_m5s_6m tr_w5s_6s = tr_w5s_6m where
  tr_w5s_6m = self_resident_translate__TrP_ mc_m trp_m5s_6m tr_w5s_6s

mk_trp_and_front_end_tr4new_lang_II__TrP_ :: Mc m -> TrP__income m w -> TrP__income m s -> Tr__outgo s w -> (TrP__income m s,Tr m s w)
mk_trp_and_front_end_tr4new_lang_II__TrP_ mc_m trp_m5w_6m _0_trp_m5s_6m tr_w5s_6s = (trp_m5s_6m,tr_w5s_6m) where
  tr_w5s_6m = mk_front_end_tr4new_lang_II__TrP_ mc_m _0_trp_m5s_6m tr_w5s_6s
  trp_w5s_6m = load_ tr_w5s_6m
  trp_m5s_6m = chain_TrP_ trp_w5s_6m trp_m5w_6m


mk_trp_and_front_end_tr4new_lang_II__B_ :: Mc m -> TrP__income m w -> TrP__income m g -> Tr g s w -> Tr__outgo s w -> (TrP__income m s,Tr m s w)
mk_trp_and_front_end_tr4new_lang_II__B_ mc_m trp_m5w_6m trp_m5g_6m tr_w5s_6g tr_w5s_6s = (trp_m5s_6m,tr_w5s_6m) where
  (_0_trp_m5s_6m,_0_tr_w5s_6m) = mk_trp_and_front_end_tr4new_lang_II__A_ mc_m trp_m5w_6m trp_m5g_6m tr_w5s_6g
  (trp_m5s_6m,tr_w5s_6m) = mk_trp_and_front_end_tr4new_lang_II__TrP_ mc_m trp_m5w_6m _0_trp_m5s_6m tr_w5s_6s




-- ######################
