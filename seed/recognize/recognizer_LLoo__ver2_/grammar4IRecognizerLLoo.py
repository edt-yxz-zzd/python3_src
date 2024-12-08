#__all__:goto
#TODO
#TODO:_4result4rgnz
#TODO?@_4Unpack:rgnr7uc = _apply_unpack_case(rgnr, unpack_case)
#DONE:INameResolver:cenv_var,nm4spost,nm4spost6elem <<== IEnvironment.param2setting_
#   --> Either sym<env.param2setting_> value
#   8个可能变成:lazy_alias_/RecognizerLLoo__lazy_alias
#DONE:fixed:xctx_view@-whether_default
#DONE:always tkd_/tkey2rgnr4tkd_  # cooperate with subscript_ .@(idx/0/1)
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/grammar4IRecognizerLLoo.py

py -m seed.recognize.recognizer_LLoo__ver2_.grammar4IRecognizerLLoo
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo__ver2_.grammar4IRecognizerLLoo -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo__ver2_.grammar4IRecognizerLLoo:__doc__ -ht


[[
grammar<IRecognizerLLoo>:

:%s/\([$+]+ *\)'\(\w*\)'/\1"\2"
    # tkey_str  == ' ... '
    # value_str == " ... "

=====
#begin-grammar4IRecognizerLLoo
[[[
^^^grammar4rgnr
; grammar4rgnr := (<
    ;-'^^^'
    ,goal
    ,-';'.+
    ,stmt9.*
    ,-'$$$'
    >)
; goal := rgnr_ref
; rgnr_ref := 'rgnr_var' .@1
; stmt9 := (< ;stmt ,-';'.+ >) =!
; stmt := assignment
; assignment := (< ,rgnr_nmd ;-':=' ,rgnr_expr >)
; rgnr_nmd := 'rgnr_var' .@1
; rgnr_expr := (< ,prefix.? ;rgnr_atom ,suffix.* >)
; rgnr_atom := {/
    / rgnr_ref $+"ref"  # rgnr_var
    / builtin_rgnr_ref $+"std_ref" # @rgnr_var
    / rgnr_group $+"group"  # ( ... )
    / rgnr_tuple $+"tuple"  # (< ... >)
    / rgnr_list $+"list"    # [~ ...,~]
    / rgnr_choice $+"choice" # {/ ... /}
    / rgnr_router $+"router" # {| ... |}
    / rgnr_tkey $+"tkey"    # ' ... '
    / rgnr_loader $+"loader"
    /}
; builtin_rgnr_ref := (< ;-'@' ,'rgnr_var' .@1 >) =!
; rgnr_group := (< ;-'(' ,ex_rgnr_expr ,-')' >) =!
; ex_rgnr_expr := {/
    / assignment $+"assign"
    / rgnr_expr $+"expr"
    /}
; rgnr_tuple := (< ;-'(<' ,g_rgnr_expr[.. //-';'] ,rgnr_expr[.. %%-',' //-'>)' ] >)
; rgnr_list := (< ;-'[~' ,g_rgnr_expr[.. //-';'] ,rgnr_expr[.. %%-',' //-'~]' ] >)
; rgnr_choice := (< ;-'{/' ,j_rgnr_expr[.. //-'/}'] >) =!
; rgnr_router := (< ;-'{|' ,i_proposition[.. //-'|}'] >) =!
; rgnr_loader := (< ;-'++' ,value >) =!
; g_rgnr_expr := (< ;-',' ,rgnr_expr >) =!
; j_rgnr_expr := (< ;-'/' ,rgnr_expr >) =!
; i_rgnr_expr := (< ;-'|' ,rgnr_expr >) =!
; i_proposition := (< ;-'|' ,rgnr_tkey.* ,-'=>' ,rgnr_expr >)
; prefix := {/ /'-' /'==' /'!=' /'*=' /'*~' /'.=' /'.~' /} .@0
    # ++unpack '*=' '*~'
    # ++pack '.=' '.~'
; suffix_op := {/
    / '.*'
    / '.+'
    / '^^'
    / '^$'
    / ':?'
    / '.?'
    / ':&'
    / '.&'
    / '<<'
    / '<>'
    / '=!'
    / '~!'
    / '$-'
    /}
; suffix := {/
    / (< ;suffix_op .@0 >) # no: =!
    / (< ;'=$' .@0  ,nm4spost >)
    / (< ;'~$' .@0  ,nm4spost >)
    / (< ;'$+' .@0  ,value >)
    / (< ;'.@' .@0  ,value >)
    / (< ;'=*$'.@0  ,nm4spost6elem >)
    / (< ;'~*$'.@0  ,nm4spost6elem >)
    / (< ;'=>' .@0  ,-'{' ,v_rgnr_expr[.. %%-',' //-'}' ] >)
    / (< ;'['  .@0  ,min.? ,op_max.? ,op_rgnr8sep.? ,op_rgnr8end.? ,']' >) # cancel:$+"gsep_end_by_"
        # ++"gsep_end_by_"
        # not ignore '[' ']'
    /}
    # cancel:no 『.@0』 for any tkey ==>> to at once
; nm4spost := 'value_str' .@1
; nm4spost6elem := 'value_str' .@1
; rgnr_tkey := 'tkey_str' .@1
    # tkey_str  == ' ... '
    # value_str == " ... "
; v_rgnr_expr := (< ;value ,-':' ,rgnr_expr >)
; op_max := (< ;-'..' ,max.? >) =!
; op_rgnr8sep := (< ;-'%%' ,rgnr8sep >) =!
; op_rgnr8end := (< ;-'//' ,rgnr8end >) =!
; min := 'uint' .@1
; max := 'uint' .@1
; rgnr8sep := rgnr_expr
; rgnr8end := rgnr_expr
; value := {/
    / 'value_str'
    / 'uint'
    / 'bool' #0b/1b #(or 0false/0true)
    / 'null' #0_ #(or 0null)
    / 'cenv_var' #3nm4var6cenv
        # cancel:rgnr8cenv_var->_EnvVar
    /} # no 『.@1』
    #5nm4func /...
; $$$

]]]
#end-grammar4IRecognizerLLoo

=====
tkeys:terminals:
    #see:grep_between
    #_keyword_tkeys_
    'bool' 'cenv_var' 'uint' 'null' 'rgnr_var' 'tkey_str' 'value_str' '!=' '$$$' '$+' '$-' '%%' '(' '(<' ')' '*=' '*~' '++' ',' '-' '.&' '.*' '.+' '..' '.=' '.?' '.@' '.~' '/' '//' '/}' ':&' ':' ':=' ':?' ';' '<<' '<>' '=!' '=$' '=*$' '==' '=>' '>)' '@' '[' '[~' ']' '^$' '^^' '^^^' '{' '{/' '{|' '|' '|}' '}' '~!' '~$' '~*$'

=====
nmd_rgnrs:nonterminals:
    #see:grep_between
    assignment builtin_rgnr_ref ex_rgnr_expr g_rgnr_expr goal i_rgnr_expr j_rgnr_expr max min nm4spost nm4spost6elem op_max op_rgnr8end op_rgnr8sep prefix i_proposition rgnr8end rgnr8sep rgnr_atom rgnr_choice rgnr_expr rgnr_group rgnr_list rgnr_loader rgnr_nmd rgnr_ref rgnr_router rgnr_tkey rgnr_tuple stmt stmt9 suffix suffix_op v_rgnr_expr value

=====
tags:constant_strings:
    #see:grep_between
    "assign" "choice" "expr" "group" "list" "loader" "ref" "router" "std_ref" "tkey" "tuple"

=====
]]

[[
view others/app/termux/shell_string_quoting.txt
"!..." --> '!'"..."
$ echo "!..."
bash: !...: event not found
$ echo '!'"..."
!...
<<==:
fail:grep_between -s -u -ptn "(?<!['\"#]|# *\+\+|# *@?)(?!\d)\w+(?=\s*:=)" -begin '#begin-grammar4IRecognizerLLoo' -end '#end-grammar4IRecognizerLLoo' -i ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/grammar4IRecognizerLLoo.py
    ??? "<![" has special meanings in bash shell ???
fail:grep_between -s -u -ptn "(?<!# *\+\+|# *@?|['\"#])(?!\d)\w+(?=\s*:=)" -begin '#begin-grammar4IRecognizerLLoo' -end '#end-grammar4IRecognizerLLoo' -i ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/grammar4IRecognizerLLoo.py
    ??? "<!#" has special meanings in bash shell ???
]]
[[
all-names:
    total:35
echo '(?<!# \+\+|# @|# |['"'"'"#])'
    (?<!# \+\+|# @|# |['"#])
    re.error: look-behind requires fixed-width pattern
echo '(?<!# \+\+|.# @|..# |...['"'"'"#])'
    (?<!# \+\+|.# @|..# |...#|...['"#])
grep_between -s -u -ptn '(?<!# \+\+|.# @|..# |...['"'"'"#])''(?!\d)\w+(?=\s*:=)' -begin '#begin-grammar4IRecognizerLLoo' -end '#end-grammar4IRecognizerLLoo' -i ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/grammar4IRecognizerLLoo.py
assignment
builtin_rgnr_ref
ex_rgnr_expr
g_rgnr_expr
goal
i_proposition
i_rgnr_expr
j_rgnr_expr
max
min
nm4spost
nm4spost6elem
op_max
op_rgnr8end
op_rgnr8sep
prefix
rgnr8end
rgnr8sep
rgnr_atom
rgnr_choice
rgnr_expr
rgnr_group
rgnr_list
rgnr_loader
rgnr_nmd
rgnr_ref
rgnr_router
rgnr_tkey
rgnr_tuple
stmt
stmt9
suffix
suffix_op
v_rgnr_expr
value
]]


[[
assigned-names
    total:35
grep_between -s -u -ptn '\w+(?=\s*:=)' -begin '#begin-grammar4IRecognizerLLoo' -end '#end-grammar4IRecognizerLLoo' -i ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/grammar4IRecognizerLLoo.py
assignment
builtin_rgnr_ref
ex_rgnr_expr
g_rgnr_expr
goal
grammar4rgnr
i_proposition
i_rgnr_expr
j_rgnr_expr
max
min
nm4spost
nm4spost6elem
op_max
op_rgnr8end
op_rgnr8sep
prefix
rgnr8end
rgnr8sep
rgnr_atom
rgnr_choice
rgnr_expr
rgnr_group
rgnr_list
rgnr_loader
rgnr_nmd
rgnr_ref
rgnr_router
rgnr_tkey
rgnr_tuple
stmt
stmt9
suffix
suffix_op
v_rgnr_expr
value
]]

[[
tkey_str == ' ... '
    total:60
grep_between -s -u -ptn "'[^ ']*'" -begin '#begin-grammar4IRecognizerLLoo' -end '#end-grammar4IRecognizerLLoo' -i ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/grammar4IRecognizerLLoo.py
'bool'
'cenv_var'
'uint'
'null'
'rgnr_var'
'tkey_str'
'value_str'
'!='
'$$$'
'$+'
'$-'
'%%'
'('
'(<'
')'
'*='
'*~'
'++'
','
'-'
'.&'
'.*'
'.+'
'..'
'.='
'.?'
'.@'
'.~'
'/'
'//'
'/}'
':&'
':'
':='
':?'
';'
'<<'
'<>'
'=!'
'=$'
'=*$'
'=='
'=>'
'>)'
'@'
'['
'[~'
']'
'^$'
'^^'
'^^^'
'{'
'{/'
'{|'
'|'
'|}'
'}'
'~!'
'~$'
'~*$'

]]
[[
value_str == " ... "
    total:11
grep_between -s -u -ptn '"[^ "]*"' -begin '#begin-grammar4IRecognizerLLoo' -end '#end-grammar4IRecognizerLLoo' -i ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/grammar4IRecognizerLLoo.py
"assign"
"choice"
"expr"
"group"
"list"
"loader"
"ref"
"router"
"std_ref"
"tkey"
"tuple"

]]





py_adhoc_call   seed.recognize.recognizer_LLoo__ver2_.grammar4IRecognizerLLoo   @f
from seed.recognize.recognizer_LLoo__ver2_.grammar4IRecognizerLLoo import *

#]]]'''
__all__ = r'''
grammar4all_method_names
    all_method_names

INameResolver
    DummyNameResolver
        dummy_name_resolver

prepare4parse__7grammar_
    grp4nm4rgnr4parse__7grammar
    name2may_gpostprocess6ok4parse__7grammar
    name2rgnr4parse__7grammar
    main_rgnr4parse__7grammar
    env4parse__7grammar
    max_num_tokens6backward4parse__7grammar



prepare4tokenize__7grammar_
    main_rgnr4tknz__7grammar
    tkeys8noise4tknz__7grammar
    may_env4tknz__7grammar








_xpostprocess_group7grammar
    constant_loader__Right_
    switch_cased__flat_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.types.Either import Cased, Either
from seed.types.Either import mk_Left, mk_Right


from seed.tiny import fst, snd
from seed.tiny_.check import check_type_is, check_type_le, check_int_ge_le, check_int_ge
from seed.tiny_.dict__add_fmap_filter import dict_add__new# fmap4dict_value, filter4dict_value, dict_add__is, dict_add__eq, group4dict_value
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper
    #def __repr__(sf, /):
    #    return repr_helper(sf, *args, **kwargs)

from seed.types.FrozenOrderedSet import FrozenOrderedSet, FrozenOrderedDict
from seed.types.StackStyleSet import StackStyleSet
from collections import OrderedDict
frozenset

from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import BaseRecognizerLLoo__main__split_teardown__default_mixins, BaseRecognizerLLoo__alias__default_mixins
from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import mk_group_pair4rgnr_ref, Makers4IRecognizerLLoo
mkrs = Makers4IRecognizerLLoo

from seed.helper.str2__all__ import str2__all__

from seed.recognize.recognizer_LLoo__ver2_.tokenize_utils import (
ns4common_rgnr4tknz
,   all_name_set4common_rgnr4tknz
,   xqset2rgnr4tdat_
,   xqset2rgnr4tkey_
,   tkey2rgnr4tdat_
,   tkey2rgnr4tkey_
#
,   xqset2both_rgnrs4tdat_
,   xqset2both_rgnrs4tkey_
,   tkey2both_rgnrs4tdat_
,   tkey2both_rgnrs4tkey_
#
,   xqset2rgnr4tkd_
,   tkey2rgnr4tkd_
#
,IHelper4Tokenization
,   BaseHelper4Tokenization
,   whether_default
,       whether_default_
,       remove_default_methods_
,   extract_info5hlpr4tknz_
,   prepare4tokenize_
)
from seed.recognize.recognizer_LLoo__ver2_.tokenize_utils import mk_rgnr4words_, mk_rgnr4enum_type_
___end_mark_of_excluded_global_names__0___ = ...


def _mk_all_method_names():
    #all_method_names = tuple(sorted({**Makers4IRecognizerLLoo}))
    all_method_names = tuple(sorted(Makers4IRecognizerLLoo))
    return all_method_names
def _show_all_method_names():
    all_method_names = _mk_all_method_names()
    print('\n'.join(all_method_names))
all_method_names = tuple(sorted(str2__all__(
grammar4all_method_names:=r'''
named_              #   nm = ...
ref_                #   ... = ...nm...
empty8header_       #   rgnr^^
whole8header_       #   rgnr^$
optional__forgivable_#  rgnr:?
optional__strict_   #   rgnr.?
lift__forgivable_   #   rgnr:&
lift__strict_       #   rgnr.&
lookahead_          #   rgnr<<
protect_header_     #   rgnr<>
rgnr__eof           #   @eof
rgnr__any_tkd       #   @any
                    #   ===(spost__tkn2tkd_ . rgnr__any_token)
ignore_             #   -rgnr
followed_by_        #   ==rgnr
not_followed_by_    #   !=rgnr
    # ++unpack '*=' '*~'
    # ++pack '.=' '.~'
    # pack/unpack only inside serial_/gsep_end_by_
spost__unbox_       #   rgnr ~!
unbox_tuple_        #?? (< ... >) =!
    # [ignore:=True] cause diff
    # (< >) tuple never ignore
    # =! unbox never ignore
spostprocess_       #   rgnr =$nm4spost
                    #   rgnr ~$nm4spost #ignorable
serial_             #   [~ ... ~] #ignorable
                    #   (< ... >) #non_ignorable
                    #   ... ::= ,rgnr... ;...
many_               #   rgnr[ min .. max ]
                    #   rgnr.*
                    #   rgnr.+
end_by_             #   rgnr[ min .. max //rgnr8end]
sep_by_             #   rgnr[ min .. max %%rgnr8sep]
sep_end_by_         #   rgnr[ min .. max %%rgnr8sep //rgnr8end]
(lookahead_<tkey_prefix_tree_> ~> switch_branches_)
                    #   {| tkey... => rgnr | ... |}
priority_parallel_  #   {/ rgnr / ... /}
tag_rgnr_           #   rgnr $+(val)
constant_loader_    #   ++(val)
none8oresult_if_ignore_
                    #   rgnr $-
(spost__tkn2tkd_ . token_)
                    #   'tkey' # cooperate with subscript_ .@(idx/0/1)
switch_cased_       #   rgnr => {(val):rgnr,...}
subscript_          #   rgnr .@(val)
spost__fmap4tuple_  #   rgnr =*$nm4spost6elem
                    #   rgnr ~*$nm4spost6elem



######################
# no direct syntax support
######################
rgnr__any_tkey
rgnr__any_tdat
rgnr__any_token
any_token_
not_eof_
eof_
not_ignore_
rgnr__not_eof       #=> !@eof
repetition_         #   replaced by many_
protect_whole_      #=> rgnr ^$ <>

between_            #=> (< ,-open ;body ,-end >) =! #NOTE:『;』
tag_                #== rgnr $+(val)
trial_and_error_    #== rgnr<>
token_seq_          #=> (< 'tkey' ... >)
try_except_else_    #=> rgnr8fail{? rgnr8trial => rgnr8else ?}
try_except_else__spost_
                    #   rgnr8fail{? $$nm4spost6trial_else rgnr8trial => rgnr8else ?}
                    #=> {/ (< ;rgnr8trial ,rgnr8else >) =$ nm4spost6trial_else / rgnr8fail /}
                    # therefore cancelled
dependent_pair_     #~= rgnr => {(val):rgnr,...}
switch_branches_    #=> (rgnr => {(val):rgnr,...}) .@1




gprepostprocess_
gsep_end_by_

light_wrap_
light_wrap_rgnr_

spost__fmap4tuple__tkd2tdat_
spost__fmap4tuple__tkd2tkey_
spost__fmap4tuple__tkn2tdat_
spost__fmap4tuple__tkn2tkd_
spost__fmap4tuple__tkn2tkey_
                #=> rgnr =*$"tkn2tkey_"
                #=> rgnr ~*$"tkn2tkey_"
spost__tkd2tdat_
spost__tkd2tkey_
spost__tkn2tdat_
spost__tkn2tkd_
spost__tkn2tkey_
                #=> rgnr =$"tkn2tkey_"
                #=> rgnr ~$"tkn2tkey_"

main_
main__split_teardown_
lazy_alias_
lazy_alias_rgnr__human_

'''#'''
)))
#end-all_method_names

assert (__:=_mk_all_method_names()) == all_method_names, (_show_all_method_names(), {*__}-{*all_method_names}, {*all_method_names}-{*__})













class _4par_:
    'see:par_'
    def __init__(sf, /, *args):
        if not args:
            sf._may_pair = None
        else:
            ot, rgnr = args
            assert type(ot) is __class__
            sf._may_pair = args
    def __truediv__(sf, rgnr, /):
        return __class__(sf, rgnr)
    def collect_(sf, /):
        ls = []
        while (pair := sf._may_pair):
            sf, rgnr = pair
            ls.append(rgnr)
        ls.reverse()
        return ls
_4par = _4par_()

def prepare4parse__7grammar_(name_resolver, /):
    '-> (grp4nm4rgnr4parse__7grammar, name2may_gpostprocess6ok4parse__7grammar, name2rgnr4parse__7grammar, main_rgnr4parse__7grammar, env4parse__7grammar, max_num_tokens6backward4parse__7grammar)'
    ######################
    from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import mk_name2may_gpostprocess6ok_
    from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import collect_namess5rgnrs_# mk_group_pair4rgnr_ref# Makers4IRecognizerLLoo, collect_namess5locals_
    #from seed.types.IToken import TokenKeyQuerySet5xqset
    #from seed.types.Tester import Tester__eq_obj
    from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import mk_Environment
    ######################
    #tkn_qset5xqset_ = TokenKeyQuerySet5xqset
    #mkrs = Makers4IRecognizerLLoo
    ######################
    #tkey2rgnr4tdat_ = lambda tkey:mkrs.spost__tkn2tdat_(mkrs.token_(tkn_qset5xqset_(Tester__eq_obj(tkey))))
        # tkn -> tdat
    #tkey2rgnr4tkey_ = lambda tkey:mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(Tester__eq_obj(tkey))))
        # tkn -> tkey
    ######################
    ######################
    ######################

    ######################
    (grp4nm4rgnr, grp4rgnr_ref) = mk_group_pair4rgnr_ref()
    assert grp4nm4rgnr is grp4rgnr_ref[:].get_grp4nm4rgnr_()
    ######################
    #ls4rgnr_ref
    #:.+1,.+36s/^\w\+$/ref__\0 = grp4rgnr_ref.\0
    ref__assignment = grp4rgnr_ref.assignment
    ref__builtin_rgnr_ref = grp4rgnr_ref.builtin_rgnr_ref
    ref__ex_rgnr_expr = grp4rgnr_ref.ex_rgnr_expr
    ref__g_rgnr_expr = grp4rgnr_ref.g_rgnr_expr
    ref__goal = grp4rgnr_ref.goal
    ref__grammar4rgnr = grp4rgnr_ref.grammar4rgnr
    ref__i_proposition = grp4rgnr_ref.i_proposition
    ref__i_rgnr_expr = grp4rgnr_ref.i_rgnr_expr
    ref__j_rgnr_expr = grp4rgnr_ref.j_rgnr_expr
    ref__max = grp4rgnr_ref.max
    ref__min = grp4rgnr_ref.min
    ref__nm4spost = grp4rgnr_ref.nm4spost
    ref__nm4spost6elem = grp4rgnr_ref.nm4spost6elem
    ref__op_max = grp4rgnr_ref.op_max
    ref__op_rgnr8end = grp4rgnr_ref.op_rgnr8end
    ref__op_rgnr8sep = grp4rgnr_ref.op_rgnr8sep
    ref__prefix = grp4rgnr_ref.prefix
    ref__rgnr8end = grp4rgnr_ref.rgnr8end
    ref__rgnr8sep = grp4rgnr_ref.rgnr8sep
    ref__rgnr_atom = grp4rgnr_ref.rgnr_atom
    ref__rgnr_choice = grp4rgnr_ref.rgnr_choice
    ref__rgnr_expr = grp4rgnr_ref.rgnr_expr
    ref__rgnr_group = grp4rgnr_ref.rgnr_group
    ref__rgnr_list = grp4rgnr_ref.rgnr_list
    ref__rgnr_loader = grp4rgnr_ref.rgnr_loader
    ref__rgnr_nmd = grp4rgnr_ref.rgnr_nmd
    ref__rgnr_ref = grp4rgnr_ref.rgnr_ref
    ref__rgnr_router = grp4rgnr_ref.rgnr_router
    ref__rgnr_tkey = grp4rgnr_ref.rgnr_tkey
    ref__rgnr_tuple = grp4rgnr_ref.rgnr_tuple
    ref__stmt = grp4rgnr_ref.stmt
    ref__stmt9 = grp4rgnr_ref.stmt9
    ref__suffix = grp4rgnr_ref.suffix
    ref__suffix_op = grp4rgnr_ref.suffix_op
    ref__v_rgnr_expr = grp4rgnr_ref.v_rgnr_expr
    ref__value = grp4rgnr_ref.value
    ######################
    grp4nm4rgnr[:].frozen_()
    nm2sym4rgnr = grp4rgnr_ref[:].view_grp4nm4rgnr_as_mapping_()
    ######################
    #init:ls4rgnr4rule
    ######################
    tpl_ = lambda *xs:mkrs.serial_(xs, _not_ignore_toplvl_=True)
    par_ = lambda _4par:mkrs.priority_parallel_(_4par.collect_())
    ig_ = lambda x:(x, 0)
    tag_ = mkrs.tag_
    sep_end_by_ = mkrs.sep_end_by_
        # (rgnr8sep, rgnr8end, rgnr8body)
    end_by_ = mkrs.end_by_
    m0_ = mkrs.many_
    m1_ = lambda x:mkrs.many_(x, 1)
    opt_ = lambda x:mkrs.optional__strict_(x)
    force_unbox_ = lambda x:mkrs.spost__unbox_(x, _force_postprocess_when_ignore_=True)
    tkd_ = tkey2rgnr4tkd_
    tkey_ = tkey2rgnr4tkey_
    tdat_ = tkey2rgnr4tdat_
    ######################
    # vim cmd :: grammar -> ls4rgnr4rule
    ######################
    # .,.+89s/ (</ tpl_(/g
    # .,.+89s/ >)/ )/g
    # .,.+89s/ {\// par_(/g
    # .,.+89s/ \/}/ )/g
    # .,.+89s/\(.[=;,/$-] *\)\(\a\w*\)\>(\@!/\1ref__\2/g
    # .,.+89s/\([;,/%]\)-\(\S\+\)/\1ig_(\2)/g
    # .,.+89s/\('\w*'\)/tdat_(\1)/g
    # .,.+89s/\('[^'' a-zA-Z0-9]*'\)/tkey_(\1)/g
    # /[.][*+?]
    #     .* --> m0_
    #     .+ --> m1_
    #     .? --> opt_

    # .,.+89s/ ;/ ,True ,/g
    # .,.+89s/tpl_(/\0*[]/g
    # .,.+89s/par_(/\0_4par/g
    #     )))
    # .,.+89s/:= \(tpl_(.*)\) =!$/:= force_unbox_(\1)/g
    # .,.+89s/; \(\w\+\) := /77; \1 = /
    # .,.+89s/\(\w\+\) \$+\("\w*"\)/tag_(\1, \2)
    #     $+
    # .,.+89s/,\(\w\+\)\[\.\. *%%ig_(\(\S*\)) *\/\/ig_(\(\S*\)) *\]/,sep_end_by_(\2, \3, \1)/g
    #     [.. %% //]
    # .,.+89s/,\(\w\+\)\[\.\. *\/\/ig_(\(\S*\)) *\]/,end_by_(\2, \1)/g
    #     [.. //]
    # 缩进
    # 人工修改
    # /tpl_(\(\(True\)\@!.\)*$
    #         )
    #     miss ,True
    # fix-bugs@end_by_()
    # ++『.@0』++『.@1』 <<== always:tkd
    #   but already distinguished by tkey_/tdat_
    #   fixed:cenv_var,value_str using tkd_
    #       #cancel:_EnvVar
    #       #=>using:tkd_
    #
    ######################
    #ls4rgnr4rule
    77; grammar4rgnr = tpl_(*[]
        ,True ,ig_(tkey_('^^^'))
        ,ref__goal
        ,ig_(m1_(tkey_(';')))
        ,m0_(ref__stmt9)
        ,ig_(tkey_('$$$'))
        )
    77; goal = ref__rgnr_ref
    77; rgnr_ref = tdat_('rgnr_var')
    77; stmt9 = force_unbox_(tpl_(*[] ,True ,ref__stmt ,ig_(m1_(tkey_(';'))) ))
    77; stmt = ref__assignment
    77; assignment = tpl_(*[] ,ref__rgnr_nmd ,True ,ig_(tkey_(':=')) ,ref__rgnr_expr )
    77; rgnr_nmd = tdat_('rgnr_var')
    77; rgnr_expr = tpl_(*[] ,opt_(ref__prefix) ,True ,ref__rgnr_atom ,m0_(ref__suffix) )
    77; rgnr_atom = par_(_4par
        / tag_(ref__rgnr_ref, "ref")  # rgnr_var
        / tag_(ref__builtin_rgnr_ref, "std_ref") # @rgnr_var
        / tag_(ref__rgnr_group, "group")  # ( ... )
        / tag_(ref__rgnr_tuple, "tuple")  # tpl_(*[] ... )
        / tag_(ref__rgnr_list, "list")    # [~ ...,~]
        / tag_(ref__rgnr_choice, "choice") # par_(_4par ... )
        / tag_(ref__rgnr_router, "router") # {| ... |}
        / tag_(ref__rgnr_tkey, "tkey")    # ' ... '
        / tag_(ref__rgnr_loader, "loader")
        )
    77; builtin_rgnr_ref = force_unbox_(tpl_(*[] ,True ,ig_(tkey_('@')) ,tdat_('rgnr_var') ))
    77; rgnr_group = force_unbox_(tpl_(*[] ,True ,ig_(tkey_('(')) ,ref__ex_rgnr_expr ,ig_(tkey_(')')) ))
    77; ex_rgnr_expr = par_(_4par
        / tag_(ref__assignment, "assign")
        / tag_(ref__rgnr_expr, "expr")
        )
    ######################
    #77; rgnr_tuple = tpl_(*[] ,True ,ig_(tkey_('(<')) ,end_by_(tkey_(';', ref__g_rgnr_expr)) ,sep_end_by_(tkey_(','), tkey_('>)'), ref__rgnr_expr) )
    77; rgnr_tuple = tpl_(*[] ,True ,ig_(tkey_('(<')) ,end_by_(tkey_(';'), ref__g_rgnr_expr) ,sep_end_by_(tkey_(','), tkey_('>)'), ref__rgnr_expr) )
    ######################
    77; rgnr_list = tpl_(*[] ,True ,ig_(tkey_('[~')) ,end_by_(tkey_(';'), ref__g_rgnr_expr) ,sep_end_by_(tkey_(','), tkey_('~]'), ref__rgnr_expr) )
    77; rgnr_choice = force_unbox_(tpl_(*[] ,True ,ig_(tkey_('{/')) ,end_by_(tkey_('/}'), ref__j_rgnr_expr) ))
    77; rgnr_router = force_unbox_(tpl_(*[] ,True ,ig_(tkey_('{|')) ,end_by_(tkey_('|}'), ref__i_proposition) ))
    77; rgnr_loader = force_unbox_(tpl_(*[] ,True ,ig_(tkey_('++')) ,ref__value ))
    77; g_rgnr_expr = force_unbox_(tpl_(*[] ,True ,ig_(tkey_(',')) ,ref__rgnr_expr ))
    77; j_rgnr_expr = force_unbox_(tpl_(*[] ,True ,ig_(tkey_('/')) ,ref__rgnr_expr ))
    77; i_rgnr_expr = force_unbox_(tpl_(*[] ,True ,ig_(tkey_('|')) ,ref__rgnr_expr ))
    77; i_proposition = tpl_(*[] ,True ,ig_(tkey_('|')) ,m0_(ref__rgnr_tkey) ,ig_(tkey_('=>')) ,ref__rgnr_expr )
    77; prefix = par_(_4par /tkey_('-') /tkey_('==') /tkey_('!=') /tkey_('*=') /tkey_('*~') /tkey_('.=') /tkey_('.~') )
        # ++unpack tkey_('*=') tkey_('*~')
        # ++pack tkey_('.=') tkey_('.~')
    77; suffix_op = par_(_4par
        / tkey_('.*')
        / tkey_('.+')
        / tkey_('^^')
        / tkey_('^$')
        / tkey_(':?')
        / tkey_('.?')
        / tkey_(':&')
        / tkey_('.&')
        / tkey_('<<')
        / tkey_('<>')
        / tkey_('=!')
        / tkey_('~!')
        / tkey_('$-')
        )
    77; suffix = par_(_4par
        / tpl_(*[] ,True ,ref__suffix_op )
        / tpl_(*[] ,True ,tkey_('=$') ,ref__nm4spost )
        / tpl_(*[] ,True ,tkey_('~$') ,ref__nm4spost )
        / tpl_(*[] ,True ,tkey_('$+') ,ref__value )
        / tpl_(*[] ,True ,tkey_('.@') ,ref__value )
        / tpl_(*[] ,True ,tkey_('=*$') ,ref__nm4spost6elem )
        / tpl_(*[] ,True ,tkey_('~*$') ,ref__nm4spost6elem )
        / tpl_(*[] ,True ,tkey_('=>') ,ig_(tkey_('{')) ,sep_end_by_(tkey_(','), tkey_('}'), ref__v_rgnr_expr) )
        / tpl_(*[] ,True ,(tkey_('[')) ,opt_(ref__min) ,opt_(ref__op_max) ,opt_(ref__op_rgnr8sep) ,opt_(ref__op_rgnr8end) ,(tkey_(']')) )
            #cancel:ig_ []
        )
    77; nm4spost = tdat_('value_str')
    77; nm4spost6elem = tdat_('value_str')
    77; rgnr_tkey = tdat_('tkey_str')
        # tkey_str  == ' ... '
        # value_str == " ... "
    77; v_rgnr_expr = tpl_(*[] ,True ,ref__value ,ig_(tkey_(':')) ,ref__rgnr_expr )
    77; op_max = force_unbox_(tpl_(*[] ,True ,ig_(tkey_('..')) ,opt_(ref__max) ))
    77; op_rgnr8sep = force_unbox_(tpl_(*[] ,True ,ig_(tkey_('%%')) ,ref__rgnr8sep ))
    77; op_rgnr8end = force_unbox_(tpl_(*[] ,True ,ig_(tkey_('//')) ,ref__rgnr8end ))
    77; min = tdat_('uint')
    77; max = tdat_('uint')
    77; rgnr8sep = ref__rgnr_expr
    77; rgnr8end = ref__rgnr_expr
    77; value = par_(_4par
        / tkd_('value_str')
        / tkd_('uint')
        / tkd_('bool') #0b/1b #(or 0false/0true)
        / tkd_('null') #0_ #(or 0null)
        / tkd_('cenv_var') #3nm4var6cenv
            #cancel:_EnvVar
            #=>using:tkd_ instead of tdat_
        )
        #5nm4func /...
    #; $$$

    ######################
    nms4rgnr4rule = sorted(nm2sym4rgnr)
    #_d = {*locals()} # generate locals diff...
    ls4rgnr4rule = [*map(locals().__getitem__, nms4rgnr4rule)]
    ls4rgnr_ref = [getattr(grp4rgnr_ref, nm) for nm in nms4rgnr4rule]
    ls4rgnr_nmd = [rgnr_ref.mk_named_rgnr_(rgnr4rule) for rgnr4rule, rgnr_ref in zip(ls4rgnr4rule, ls4rgnr_ref)]
    all_rgnrs = (*ls4rgnr_ref, *ls4rgnr4rule, *ls4rgnr_nmd)
    (name2rgnr, nms4ref, nms6ref) = collect_namess5rgnrs_(all_rgnrs, _no_check__vs__ge__vs__eq_=2)
    nmd__grammar4rgnr = name2rgnr[grp4nm4rgnr.grammar4rgnr]
    #   main_rgnr #should be rgnr_nmd instead rgnr4rule which without spostprocess_
    ######################
    name2may_gpostprocess6ok = mk_name2may_gpostprocess6ok_(r'{}', grp4nm4rgnr, _xpostprocess_group7grammar)
        #see:mk_gpostprocess6ok__5xpost_
        #   [num_args{xpostprocess6ok} <- {1,2,3,7}]
        #   [xpostprocess6ok :: ((oresult)|(env, oresult)|(env, xctx_view, oresult)|(rgnr, env, xctx_view, ignore, st, ext_info8end, oresult)) -> oresult]
        #
    assert 14 == len(name2may_gpostprocess6ok), (name2may_gpostprocess6ok.keys(), len(name2may_gpostprocess6ok))
        # AssertionError: (dict_keys([nm4rgnr_.assignment, nm4rgnr_.builtin_rgnr_ref, nm4rgnr_.ex_rgnr_expr, nm4rgnr_.goal, nm4rgnr_.rgnr_atom, nm4rgnr_.rgnr_choice, nm4rgnr_.rgnr_expr, nm4rgnr_.rgnr_list, nm4rgnr_.rgnr_loader, nm4rgnr_.rgnr_ref, nm4rgnr_.rgnr_router, nm4rgnr_.rgnr_tkey, nm4rgnr_.rgnr_tuple, nm4rgnr_.value]), 14)
    ######################
    name2rgnr4parse__7grammar = name2rgnr
    rgnr4parse__7grammar = nmd__grammar4rgnr
        # must be named_rgnr
    name2may_gpostprocess6ok4parse__7grammar = name2may_gpostprocess6ok
    grp4nm4rgnr4parse__7grammar = grp4nm4rgnr
    777;    grp4nm4rgnr[:].frozen_()
    ######################
    env4parse__7grammar = mk_Environment(param2setting:={}, name2rgnr:=name2rgnr4parse__7grammar, name2may_gpreprocess:={}, name2may_gpostprocess6err:={}, name2may_gpostprocess6ok:=name2may_gpostprocess6ok4parse__7grammar, name2force_postprocess_when_ignore:={})
    cenv4parse__7grammar = env4parse__7grammar.core_env
    max_num_tokens6backward4parse__7grammar = rgnr4parse__7grammar.required_num_tokens6backward6cenv_(cenv4parse__7grammar)
    assert max_num_tokens6backward4parse__7grammar == 0
    ######################
    check_type_le(mkrs.named_, rgnr4parse__7grammar)
    #.main_rgnr4parse__7grammar = mkrs.main_(rgnr4parse__7grammar)
    main_rgnr4parse__7grammar = _RecognizerLLoo__main4parse__7grammar(rgnr4parse__7grammar, name_resolver)
    ######################
    return (grp4nm4rgnr4parse__7grammar, name2may_gpostprocess6ok4parse__7grammar, name2rgnr4parse__7grammar, main_rgnr4parse__7grammar, env4parse__7grammar, max_num_tokens6backward4parse__7grammar)
    ######################
#end-def prepare4parse__7grammar_():


class _RecognizerLLoo__main4parse__7grammar(BaseRecognizerLLoo__main__split_teardown__default_mixins):
    def __init__(sf, rgnr, name_resolver, /):
        check_type_le(INameResolver, name_resolver)
        super().__init__(rgnr)
        sf._reset4repr((rgnr, name_resolver))
        sf.name_resolver = name_resolver
    @override
    def _may_setup_(sf, env, gctx, ctx, sym8id4curr_rgnz, ignore, /):
        st4main_rgnr = sym8id4curr_rgnz[_st4main_rgnr] = _st4main_rgnr(sf.name_resolver)
        return st4main_rgnr
    @override
    def _may_teardown6rpostprocess_(sf, env, gctx, ctx, sym8id4curr_rgnz, ignore, st4main_rgnr, reply, /):
        '[only called iff [sf as main_rgnr][entering recognize_()]]: => env->gctx->ctx->sym8id4curr_rgnz->ignore->st4main_rgnr->reply->result4rgnz'
        if reply.ok:
            oresult = reply.oresult
            st4main_rgnr = sym8id4curr_rgnz[_st4main_rgnr]
                #st4main_rgnr = _get_st4main_rgnr(xctx_view)

            (grp4nm4rgnr, grp4rgnr_ref, nm2rgnr_nmd, keyword_tkeys, nms4cenv_var, tags, nms4spost, nms4spost6elem, nm4goal_rgnr) = st4main_rgnr.get_data()
            oresult = _4result4rgnz(oresult, grp4nm4rgnr, grp4rgnr_ref, nm2rgnr_nmd, keyword_tkeys, nms4cenv_var, tags, nms4spost, nms4spost6elem, nm4goal_rgnr)
            reply = reply.ireplace(eresult=mk_Right(oresult))
        result4rgnz = reply
        return result4rgnz
def _get_st4main_rgnr(xctx_view, /):
    xctx_view.sym8id4curr_rgnz
    st4main_rgnr = xctx_view.sym8id4curr_rgnz[_st4main_rgnr]
    return st4main_rgnr
def _get_name_resolver(xctx_view, /):
    st4main_rgnr = _get_st4main_rgnr(xctx_view)
    return st4main_rgnr.name_resolver
def _4result4rgnz(oresult, grp4nm4rgnr, grp4rgnr_ref, nm2rgnr_nmd, keyword_tkeys, nms4cenv_var, tags, nms4spost, nms4spost6elem, nm4goal_rgnr, /):
    del oresult
    grp4rgnr_ref[:].frozen_()
    grp4nm4rgnr[:].frozen_()
    ns4rgnr_ref = grp4rgnr_ref[:].as_immutable_namespace()
    ns4nm4rgnr = grp4nm4rgnr[:].as_immutable_namespace()
    data = (grp4nm4rgnr, grp4rgnr_ref, nm2rgnr_nmd, keyword_tkeys, nms4cenv_var, tags, nms4spost, nms4spost6elem, nm4goal_rgnr)
    rgnr4goal = nm2rgnr_nmd[nm4goal_rgnr]
        #but not IRecognizerLLoo__main yet
    new_oresult = (rgnr4goal, keyword_tkeys, ns4nm4rgnr, ns4rgnr_ref, data)
    #raise 000-TODO
    return new_oresult

class INameResolver(ABC):
    'name_resolver'
    r'''[[[
#DONE:fixed:xctx_view@-whether_default
#   def mk_gpostprocess6ok__5xpost_(xpostprocess6ok, /):
#       'xpostprocess6ok -> gpostprocess6ok # [xpostprocess6ok :: ((oresult)|(env, oresult)|(env, xctx_view, oresult)|(rgnr, env, xctx_view, ignore, st4ppp, ext_info8end, oresult)) -> oresult][num_args{xpostprocess6ok} <- {1,2,3,7}]'

#DONE:INameResolver:cenv_var,nm4spost,nm4spost6elem <<== IEnvironment.param2setting_
#   --> Either sym<env.param2setting_> value
#   8个可能变成:lazy_alias_/RecognizerLLoo__lazy_alias
#; rgnr_loader := (< ;-'++' ,value >) =!
#; v_rgnr_expr := (< ;value ,-':' ,rgnr_expr >)
#    / (< ;'=$' .@0  ,nm4spost >)
#    / (< ;'~$' .@0  ,nm4spost >)
#    / (< ;'$+' .@0  ,value >)
#    / (< ;'.@' .@0  ,value >)
#    / (< ;'=*$'.@0  ,nm4spost6elem >)
#    / (< ;'~*$'.@0  ,nm4spost6elem >)
#    / (< ;'=>' .@0  ,-'{' ,v_rgnr_expr[.. %%-',' //-'}' ] >)
##   'see:IRecognizerLLoo__gprepostprocess6cenv or using:IEnvironment.(name2may_gpreprocess_|name2may_gpostprocess6err_|name2may_gpostprocess6ok_|name2force_postprocess_when_ignore_) or using:lazy_alias_/RecognizerLLoo__lazy_alias'

    #]]]'''#'''
    __slots__ = ()
    #___no_slots_ok___ = True
    @abstractmethod
    def lookup__nm4spost(sf, nm4spost:str, /):
        'str -> Either sym<env.param2setting_> spostprocess/(oresult->oresult) | ^LookupError'
    @abstractmethod
    def lookup__nm4spost6elem(sf, nm4spost6elem:str, /):
        'str -> Either sym<env.param2setting_> spostprocess6elem/(oresult[i]->oresult[i]) | ^LookupError'
    @abstractmethod
    def lookup__cenv_var(sf, cenv_var:str, /):
        'str -> Either sym<env.param2setting_> value | ^LookupError'
class DummyNameResolver(INameResolver):
    'dummy_name_resolver/name_resolver'
    __slots__ = ()
    @override
    def lookup__nm4spost(sf, nm4spost:str, /):
        raise LookupError(nm4spost)
    @override
    def lookup__nm4spost6elem(sf, nm4spost6elem:str, /):
        raise LookupError(nm4spost6elem)
    @override
    def lookup__cenv_var(sf, cenv_var:str, /):
        raise LookupError(cenv_var)
dummy_name_resolver = DummyNameResolver()
    #name_resolver

class _st4main_rgnr:
    def __init__(sf, name_resolver, /):
        check_type_le(INameResolver, name_resolver)

        (grp4nm4rgnr, grp4rgnr_ref) = mk_group_pair4rgnr_ref()

        sf.name_resolver = name_resolver
        sf.grp4nm4rgnr = grp4nm4rgnr
        sf.grp4rgnr_ref = grp4rgnr_ref
        sf.nm2rgnr_nmd = OrderedDict()
        sf.keyword_tkeys = StackStyleSet()
        sf.nms4cenv_var = StackStyleSet()
        sf.tags = StackStyleSet()
        sf.nms4spost = StackStyleSet()
        sf.nms4spost6elem = StackStyleSet()
        sf.nm4goal_rgnr = None
    def get_data(sf, /):
        assert not sf.nm4goal_rgnr is None
        return (
        (sf.grp4nm4rgnr
        ,sf.grp4rgnr_ref
        ,sf.nm2rgnr_nmd
        ,sf.keyword_tkeys
        ,sf.nms4cenv_var
        ,sf.tags
        ,sf.nms4spost
        ,sf.nms4spost6elem
        ,sf.nm4goal_rgnr
        ))
#_nm2std_rgnr = dict(any=mkrs.spost__tkn2tkd_(mkrs.rgnr__any_token), eof=mkrs.rgnr__eof)
_nm2std_rgnr = dict(any=mkrs.rgnr__any_tkd, eof=mkrs.rgnr__eof)
def _4rgnr_serial(oresult, /, _not_ignore_toplvl_):
    rgnrs4header, rgnrs4neck_body = oresult
    rgnrs4header = map(_4unpack, rgnrs4header)
    rgnrs4neck_body = map(_4unpack, rgnrs4neck_body)
    rgnr = mkrs.serial_([*rgnrs4header, True, *rgnrs4neck_body], _not_ignore_toplvl_=_not_ignore_toplvl_)
    return rgnr


class _4Unpack(BaseRecognizerLLoo__alias__default_mixins):
    # [unpack_case :: (0/ignore|1/ignorable_normal|2/ignorable_unpack|-1/non_ignorable_normal|-2/non_ignorable_unpack)]
    def __init__(sf, rgnr, unpack_case, /):
        check_int_ge_le(-2, 2, unpack_case)
        #TODO?:rgnr7uc = _apply_unpack_case(rgnr, unpack_case)
        rgnr7uc = rgnr #...???
        super().__init__(rgnr7uc)
        sf._reset4repr((rgnr, unpack_case))
        sf._uc = unpack_case
    @property
    def _unpack_case_(sf, /):
        return sf._uc
class _4ToktenKeyedData(BaseRecognizerLLoo__alias__default_mixins):
    #tkey2rgnr4tkd_
    def __init__(sf, tkey, /):
        rgnr4tkd = tkey2rgnr4tkd_(tkey)
        super().__init__(rgnr4tkd)
        sf._reset4repr((tkey,))
        sf._tkey = tkey
    @property
    def _tkey_(sf, /):
        return sf._tkey
def _4unpack(rgnr8serial_elem, /):
    '-> (rgnr, 0/1/2) #ig_-->0'
    check_type_is(_4Unpack, rgnr8serial_elem)
    return (rgnr8serial_elem, rgnr8serial_elem._unpack_case_)
def _4unbox_tkey_seq5rgnrs(rgnrs4tdat, /):
    ls = []
    for rgnr4tkd in rgnrs4tdat:
        check_type_is(_4ToktenKeyedData, rgnr4tkd)
        tkey = rgnr4tkd._tkey_
        ls.append(tkey)
    return (tkey_seq:=tuple(ls))
_prefix2unpack_case = {'-':0, '.~':1, '*~':2, '.=':-1, '*=':-2}
    #; prefix := {/ /'-' /'==' /'!=' /'*=' /'*~' /'.=' /'.~' /} .@0
    # [unpack_case :: (0/ignore|1/ignorable_normal|2/ignorable_unpack|-1/non_ignorable_normal|-2/non_ignorable_unpack)]
def _4prefix(prefix, rgnr, /):
    match prefix:
        case '==':
            unpack_case = 0
            rgnr = mkrs.followed_by_(rgnr)
        case '!=':
            unpack_case = 0
            rgnr = mkrs.not_followed_by_(rgnr)
        case _:
            unpack_case = _prefix2unpack_case.get(prefix)
            rgnr
    return _4Unpack(rgnr, unpack_case)
def _4suffix(xctx_view, rgnr, suffix, /):
    check_type_is(tuple, suffix)
    op = suffix[0]
    check_type_is(str, op)
        #tkey not tkd
    rgnr
    ######################
    if len(suffix)==1:
     match op:
      #suffix_op
      case '.*':
        rgnr = mkrs.many_(rgnr, 0)
      case '.+':
        rgnr = mkrs.many_(rgnr, 1)
      case '^^':
        rgnr = mkrs.empty8header_(rgnr)
      case '^$':
        rgnr = mkrs.whole8header_(rgnr)
      case ':?':
        rgnr = mkrs.optional__forgivable_(rgnr)
      case '.?':
        rgnr = mkrs.optional__strict_(rgnr)
      case ':&':
        rgnr = mkrs.lift__forgivable_(rgnr)
      case '.&':
        rgnr = mkrs.lift__strict_(rgnr)
      case '<<':
        rgnr = mkrs.lookahead_(rgnr)
      case '<>':
        rgnr = mkrs.protect_header_(rgnr)
      case '=!':
        rgnr = mkrs.spost__unbox_(rgnr, _force_postprocess_when_ignore_=True)
      case '~!':
        rgnr = mkrs.spost__unbox_(rgnr, _force_postprocess_when_ignore_=False)
      case '$-':
        rgnr = mkrs.none8oresult_if_ignore_(rgnr)
      case _:
        raise Exception(op)
     #end-match op:
     if 1:
        return rgnr
    #end-if len(suffix)==1:
    ######################
    rgnr
    ######################
    #.+1,.+9s/\/ (< ;\('[^'']*'\) *\.@0 *,\(.*\S\) *>)$/  case (\1, \2):
    # case ('=$', nm4spost):
    # case ('~$', nm4spost):
    # case ('$+', value):
    # case ('.@', value):
    # case ('=*$', nm4spost6elem):
    # case ('~*$', nm4spost6elem):
    # case ('=>', case_rgnr_pairs):
    # case ('[', tmay_min, tmay_max, tmay_rgnr8sep, tmay_rgnr8end, ']'):
    ######################
    rgnr
    ######################
    assert len(suffix) >= 2
    #name_resolver = _get_name_resolver(xctx_view)
        #INameResolver
    rgnr
    match suffix:
      #except:suffix_op
      case ('=$', nm4spost):
        name_resolver = _get_name_resolver(xctx_view)
        xf = name_resolver.lookup__nm4spost(nm4spost)
        rgnr = _mk_lazy_alias('spostprocess_', rgnr, xf, _force_postprocess_when_ignore_:=True)
            #rgnr = mkrs.spostprocess_(rgnr, None, f, _force_postprocess_when_ignore_=True)
      case ('~$', nm4spost):
        name_resolver = _get_name_resolver(xctx_view)
        xf = name_resolver.lookup__nm4spost(nm4spost)
        rgnr = _mk_lazy_alias('spostprocess_', rgnr, xf, _force_postprocess_when_ignore_:=False)
            #rgnr = mkrs.spostprocess_(rgnr, None, f, _force_postprocess_when_ignore_=False)
      case ('$+', xvalue):
      #case ('$+', value):
        rgnr = _mk_lazy_alias('tag_', rgnr, xvalue)
            #rgnr = mkrs.tag_(rgnr, value)
      case ('.@', xvalue):
      #case ('.@', value):
        rgnr = _mk_lazy_alias('subscript_', rgnr, xvalue)
            #rgnr = mkrs.subscript_(rgnr, value)
      case ('=*$', nm4spost6elem):
        name_resolver = _get_name_resolver(xctx_view)
        xf = name_resolver.lookup__nm4spost6elem(nm4spost6elem)
        rgnr = _mk_lazy_alias('spost__fmap4tuple_', rgnr, xf, _force_postprocess_when_ignore_:=True)
            #rgnr = mkrs.spost__fmap4tuple_(rgnr, f, _force_postprocess_when_ignore_=True)
      case ('~*$', nm4spost6elem):
        name_resolver = _get_name_resolver(xctx_view)
        xf = name_resolver.lookup__nm4spost6elem(nm4spost6elem)
        rgnr = _mk_lazy_alias('spost__fmap4tuple_', rgnr, xf, _force_postprocess_when_ignore_:=False)
            #rgnr = mkrs.spost__fmap4tuple_(rgnr, f, _force_postprocess_when_ignore_=False)
      case ('=>', xcase_rgnr_pairs):
      #case ('=>', case_rgnr_pairs):
        #; v_rgnr_expr := (< ;value ,-':' ,rgnr_expr >)
        #; suffix := {/
        #    ...
        #    / (< ;'=>' .@0  ,-'{' ,v_rgnr_expr[.. %%-',' //-'}' ] >)
        #    ...
        #    /}
        # => [xcase_rgnr_pairs :: [(xvalue, rgnr)]]
        rgnr8case = rgnr
        rgnr = _mk_lazy_alias(switch_cased__flat_, rgnr8case, *(x for (xcase, rgnr) in xcase_rgnr_pairs for x in (xcase, rgnr)))
            #rgnr8case = rgnr
            #case2rgnr8payload = dict(case_rgnr_pairs)
            #rgnr = mkrs.switch_cased_(rgnr8case, case2rgnr8payload)
      case ('[', tmay_min, tmay_max, tmay_rgnr8sep, tmay_rgnr8end, ']'):
        [_min] = tmay_min if tmay_min else [0]
        [may_max] = tmay_max if tmay_max else [None]
        [may_rgnr8sep] = tmay_rgnr8sep if tmay_rgnr8sep else [None]
        [may_rgnr8end] = tmay_rgnr8end if tmay_rgnr8end else [None]
        rgnr8body = rgnr
        match (may_rgnr8sep, may_rgnr8end):
          case (None, None):
            rgnr = mkrs.many_(rgnr8body, _min, may_max)
          case (None, rgnr8end):
            rgnr = mkrs.end_by_(rgnr8end, rgnr8body, _min, may_max)
          case (rgnr8sep, None):
            rgnr = mkrs.sep_by_(rgnr8sep, rgnr8body, _min, may_max)
          case (rgnr8sep, rgnr8end):
            rgnr = mkrs.sep_end_by_(rgnr8sep, rgnr8end, rgnr8body, _min, may_max)
          case _:
              raise 000
        #end-match (may_rgnr8sep, may_rgnr8end):
        rgnr
      case _:
          raise Exception(suffix)
    #end-match suffix:
    rgnr
    return rgnr
    ######################
_mk_lazy_alias = mkrs.lazy_alias_rgnr__human_
def constant_loader__Right_(oresult, /):
    return mkrs.constant_loader_(mk_Right(oresult))
def switch_cased__flat_(rgnr8case, *ls4case_vs_rgnr):
    assert len(ls4case_vs_rgnr)&1 == 0
    def __():
        it = iter(ls4case_vs_rgnr)
        for case in it:
            rgnr = next(it)
            yield (case, rgnr)
    case2rgnr8payload = dict(case_rgnr_pairs:=__())
    return mkrs.switch_cased_(rgnr8case, case2rgnr8payload)

@remove_default_methods_
class _xpostprocess_group7grammar:
    r'''[[[
    see:mk_gpostprocess6ok__5xpost_
        [num_args{xpostprocess6ok} <- {1,2,3,7}]
        [xpostprocess6ok :: ((oresult)|(env, oresult)|(env, xctx_view, oresult)|(rgnr, env, xctx_view, ignore, st, ext_info8end, oresult)) -> oresult]
    ==>>:
    [g_symXXX :: Symbol4GlobalVarable]
    -->[ug_symXXX :: Symbol4UnrestrictedGlobalVarable]

    ==>>:
    ++xctx_view.sym8id4curr_rgnz
        mk a fresh sym8id4curr_rgnz for each call recognize_()
    ==>>:
    ++main_rgnr/rgnr._may_setup_
        [_may_setup_ :: may (env->gctx->ctx->sym8id4curr_rgnz->ignore->st4main_rgnr)]
        [sym8id4curr_rgnz :: WeakKeyHalfMap8AnonymousWeakableSymbol <: (WeakKeyHalfMap & AnonymousWeakableSymbol)]


    ==>>:
    setup&access global variables@gctx@xctx_view*[sym8id4curr_rgnz,ug_symXXX]:
        #@st4main_rgnr
        # AnonymousWeakableSymbol
        .grp4rgnr_ref
            grp4nm4rgnr = grp4rgnr_ref[:].get_grp4nm4rgnr_()
            nm2sym4rgnr = grp4rgnr_ref[:].view_grp4nm4rgnr_as_mapping_()
            =>grp4nm4rgnr
            =>nms6ref
        .nm2rgnr_nmd
            =>nms4ref
        .keyword_tkeys
        .nms4cenv_var
        .tags
        .nms4spost
        .nms4spost6elem
        .nm4goal_rgnr

TODO:_4result4rgnz
DONE:_may_setup_
DONE:mk rgnr bottom up
%grammar4rgnr$echo
/goal:main_/main__split_teardown_
    main_rgnr4parse__7xxx = mkrs.main_(rgnr4parse__7xxx)
    main_rgnr4tknz__7xxx = mkrs.main_(rgnr4tknz__7xxx)
    but _may_setup_ unknown yet...

/assignment -> rgnr
    !! ex_rgnr_expr

/rgnr_atom $snd
/ex_rgnr_expr $snd

/rgnr_ref
/builtin_rgnr_ref
    eof
    any
    => _nm2std_rgnr
    ?++?pass/None #<<== rgnr_loader

%rgnr_group$echo
/rgnr_tuple
/rgnr_list
/rgnr_choice
/rgnr_router
/rgnr_tkey
/rgnr_loader
/value
    -> xvalue/Either sym<env.param2setting_> value
/rgnr_expr

    #]]]'''#'''
    #
    # .+1,.+36s/^\w\+$/@+whether_default\rdef \0(sf, oresult, \/):\r    'oresult -> oresult'\r    return oresult
    @-whether_default
    def assignment(sf, env, xctx_view, oresult, /):
        'oresult -> oresult'
        st4main_rgnr = _get_st4main_rgnr(xctx_view)
        lhs_nm, rhs_rgnr = (_rgnr_nmd, _rgnr_expr) = oresult
        rgnr_nmd = st4main_rgnr.grp4rgnr_ref[lhs_nm].mk_named_rgnr_(rhs_rgnr)
        dict_add__new(st4main_rgnr.nm2rgnr_nmd, rgnr_nmd)
        return rgnr_nmd # << ex_rgnr_expr
    @-whether_default
    def builtin_rgnr_ref(sf, env, xctx_view, oresult, /):
        'oresult -> oresult'
        st4main_rgnr = _get_st4main_rgnr(xctx_view)
        nm4std_rgnr = oresult
        std_rgnr = _nm2std_rgnr[nm4std_rgnr]
        return std_rgnr
    @-whether_default
    def ex_rgnr_expr(sf, oresult, /):
        'oresult -> oresult'
        return oresult.payload
    @+whether_default
    def g_rgnr_expr(sf, oresult, /):
        'oresult -> oresult'
        return oresult
    @-whether_default
    def goal(sf, env, xctx_view, oresult, /):
        'oresult -> oresult'
        st4main_rgnr = _get_st4main_rgnr(xctx_view)
        rgnr_ref = oresult
        assert sf.nm4goal_rgnr is None
        st4main_rgnr.nm4goal_rgnr = nm4goal_rgnr = rgnr_ref.name6ref
        assert not nm4goal_rgnr is None
        return nm4goal_rgnr
    @+whether_default
    def grammar4rgnr(sf, oresult, /):
        'oresult -> oresult'
        return oresult
    @+whether_default
    def i_proposition(sf, oresult, /):
        'oresult -> oresult'
        return oresult
    @+whether_default
    def i_rgnr_expr(sf, oresult, /):
        'oresult -> oresult'
        return oresult
    @+whether_default
    def j_rgnr_expr(sf, oresult, /):
        'oresult -> oresult'
        return oresult
    @+whether_default
    def max(sf, oresult, /):
        'oresult -> oresult'
        return oresult
    @+whether_default
    def min(sf, oresult, /):
        'oresult -> oresult'
        return oresult
    @+whether_default
    def nm4spost(sf, oresult, /):
        'oresult -> oresult'
        return oresult
    @+whether_default
    def nm4spost6elem(sf, oresult, /):
        'oresult -> oresult'
        return oresult
    @+whether_default
    def op_max(sf, oresult, /):
        'oresult -> oresult'
        return oresult
    @+whether_default
    def op_rgnr8end(sf, oresult, /):
        'oresult -> oresult'
        return oresult
    @+whether_default
    def op_rgnr8sep(sf, oresult, /):
        'oresult -> oresult'
        return oresult
    @+whether_default
    def prefix(sf, oresult, /):
        'oresult -> oresult'
        return oresult
    @+whether_default
    def rgnr8end(sf, oresult, /):
        'oresult -> oresult'
        return oresult
    @+whether_default
    def rgnr8sep(sf, oresult, /):
        'oresult -> oresult'
        return oresult
    @-whether_default
    def rgnr_atom(sf, oresult, /):
        'oresult -> oresult'
        return oresult.payload
    @-whether_default
    def rgnr_choice(sf, oresult, /):
        'oresult -> oresult'
        rgnrs = oresult
        rgnr = mkrs.priority_parallel_(rgnrs)
        return rgnr
    @-whether_default
    def rgnr_expr(sf, env, xctx_view, oresult, /):
        'oresult -> oresult'
        tmay_prefix, rgnr, suffixes = oresult
        for suffix in suffixes:
            rgnr = _4suffix(xctx_view, rgnr, suffix)
        ######################
        #prefix after suffixes
        ######################
        if tmay_prefix:
            [prefix] = tmay_prefix
            rgnr = _4prefix(prefix, rgnr)
        return rgnr
    @+whether_default
    def rgnr_group(sf, oresult, /):
        'oresult -> oresult'
        return oresult
    @-whether_default
    def rgnr_list(sf, oresult, /):
        'oresult -> oresult'
        return _4rgnr_serial(oresult, _not_ignore_toplvl_=False)
    @-whether_default
    def rgnr_loader(sf, oresult, /):
        'oresult -> oresult'
        ######################
        xvalue = oresult
        check_type_is(Either, xvalue)
        rgnr = _mk_lazy_alias(constant_loader__Right_, xvalue)
        return rgnr
        ######################
        #.xvalue = oresult
        #.if xvalue.is_right:
        #.    value = xvalue.right
        #.    rgnr = mkrs.constant_loader_(eresult:=xvalue)
        #.else:
        #.    sym8value = xvalue.left
        #.    rgnr = mkrs.lazy_alias_(constant_loader__Right_, [sym8value])
        #.rgnr
        #.return rgnr
        #.######################
        #.value = oresult
        #.rgnr = mkrs.constant_loader_(eresult:=mk_Right(value))
        #.return rgnr
    @+whether_default
    def rgnr_nmd(sf, oresult, /):
        'oresult -> oresult'
        return oresult
    @-whether_default
    def rgnr_ref(sf, env, xctx_view, oresult, /):
        'oresult -> oresult'
        st4main_rgnr = _get_st4main_rgnr(xctx_view)
        nm6ref = oresult
        rgnr_ref = st4main_rgnr.grp4rgnr_ref[nm6ref]
        return rgnr_ref
    @-whether_default
    def rgnr_router(sf, oresult, /):
        'oresult -> oresult'
        ps = pairs4__ls4rgnr_tkey__rgnr8body = oresult
        #for ls4rgnr_tkey, rgnr8body in ps
        keyed_tkey_seq_pairs = tuple(enumerate(map(_4unbox_tkey_seq5rgnrs, map(fst, ps))))
        # [key4word/case :: idx]
        rgnr8case = mkrs.tkey_prefix_tree_(keyed_tkey_seq_pairs)
        rgnr8case = mkrs.lookahead_(rgnr8case)
        case2rgnr8payload = dict(enumerate(map(snd, ps)))
        rgnr = mkrs.switch_branches_(rgnr8case, case2rgnr8payload)
        return rgnr
    @-whether_default
    def rgnr_tkey(sf, env, xctx_view, oresult, /):
        'oresult -> oresult'
        st4main_rgnr = _get_st4main_rgnr(xctx_view)
        tkey_str = oresult
        check_type_is(str, tkey_str)
        tkey = tkey_str
        st4main_rgnr.keyword_tkeys.add(tkey)
        #rgnr4tkd = tkey2rgnr4tkd_(tkey)
        rgnr4tkd = _4ToktenKeyedData(tkey)
            #mkrs.token_
            #tkd_
        return rgnr4tkd
        #.rgnr4tdat = tkey2rgnr4tdat_(tkey)
        #.return rgnr4tdat
    @-whether_default
    def rgnr_tuple(sf, oresult, /):
        'oresult -> oresult'
        return _4rgnr_serial(oresult, _not_ignore_toplvl_=True)
    @+whether_default
    def stmt(sf, oresult, /):
        'oresult -> oresult'
        return oresult
    @+whether_default
    def stmt9(sf, oresult, /):
        'oresult -> oresult'
        return oresult
    @+whether_default
    def suffix(sf, oresult, /):
        'oresult -> oresult'
        return oresult
    @+whether_default
    def suffix_op(sf, oresult, /):
        'oresult -> oresult'
        return oresult
    @+whether_default
    def v_rgnr_expr(sf, oresult, /):
        'oresult -> oresult'
        return oresult
        #; v_rgnr_expr := (< ;value ,-':' ,rgnr_expr >)
        #; suffix := {/
        #    ...
        #    / (< ;'=>' .@0  ,-'{' ,v_rgnr_expr[.. %%-',' //-'}' ] >)
        #    ...
        #    /}
        # => [xcase_rgnr_pairs :: [(xvalue, rgnr)]]
    @-whether_default
    def value(sf, env, xctx_view, oresult, /):
        'oresult -> oresult/xvalue/Either sym<env.param2setting_> value'
        ######################
        tkd = oresult
        assert type(tkd) is Cased
        case, value = tkd
        if case == 'cenv_var':
            cenv_var = value
            name_resolver = _get_name_resolver(xctx_view)
            xvalue = name_resolver.lookup__cenv_var(cenv_var)
                #INameResolver
        else:
            xvalue = mk_Right(value)
        xvalue
        check_type_is(Either, xvalue)
        return xvalue
        ######################
        #.'oresult -> oresult/value'
        ######################
        # !! cancel:_EnvVar
        #.if type(oresult) is _EnvVar:
        #.    cenv_var = oresult
        #.    name_resolver = _get_name_resolver(xctx_view)
        #.    value = name_resolver.lookup__cenv_var(cenv_var)
        #.        #INameResolver
        #.    oresult = value
        #.return oresult
#end-class _xpostprocess_group7grammar:
_xpostprocess_group7grammar = _xpostprocess_group7grammar()

######################
######################
######################
#class _EnvVar(str):pass
@remove_default_methods_
class _Helper4Tokenization4Grammar(BaseHelper4Tokenization):
    #@override
    _keyword_tkeys_ = frozenset('!= $$$ $+ $- %% ( (< ) *= *~ ++ , - .& .* .+ .. .= .? .@ .~ / // /} :& : := :? ; << <> =! =$ =*$ == => >) @ [ [~ ] ^$ ^^ ^^^ { {/ {| | |} } ~! ~$ ~*$'.split())


    _noise_tkeys_ = frozenset(['spaces1', 'comment'])

    ######################
    ns = ns4common_rgnr4tknz
    #mkrs = Makers4IRecognizerLLoo
    ######################
    rgnr8spaces1 = ns.rgnr8spaces1
    rgnr8comment = ns.rgnr8comment
    ######################
    rgnr8rgnr_var = ns.rgnr8identifier
    #cancel:_EnvVar:rgnr8cenv_var = mkrs.spostprocess_(mkrs.unbox_tuple_(1, 1, True, [tkey2rgnr4tkey_('3'), ns.rgnr8identifier]), None, _EnvVar)
    rgnr8cenv_var = mkrs.unbox_tuple_(1, 1, True, [tkey2rgnr4tkey_('3'), ns.rgnr8identifier])
    rgnr8tkey_str = ns.rgnr8squot_str
    rgnr8value_str = ns.rgnr8dquot_str
    rgnr8uint = ns.rgnr8uint

    #.rgnr8bool = mk_rgnr4enum_type_('bool', '0b 1b 0false 0true'.split())
    #.rgnr8null = mk_rgnr4enum_type_('null', '0null'.split())
    rgnr8bool = mk_rgnr4words_('0b 1b 0false 0true'.split())
    rgnr8null = mk_rgnr4words_('0null'.split())

    ######################
    del ns
    #del mkrs
    ######################

    #@override
    _prefix4attr4rgnr_ = ''#rgnr8
    _prefix4attr4mk4tkd_ = '_tkd5'
    _prefix4attr4spost_ = '_spost4'


    @-whether_default
    def _spost4rgnr8uint(sf, s, /):
        'str -> uint'
        return int(s)
    @-whether_default
    def _spost4rgnr8tkey_str(sf, s, /):
        'str -> str'
        return eval(s)
    @-whether_default
    def _spost4rgnr8value_str(sf, s, /):
        'str -> str'
        return eval(s)
    @-whether_default
    def _spost4rgnr8bool(sf, s, /):
        'str -> str'
        return s in '1b 0true'
    @-whether_default
    def _spost4rgnr8null(sf, s, /):
        'str -> str'
        return None

    @+whether_default
    def f(sf, /):
        'default'

_Helper4Tokenization4Grammar()
def prepare4tokenize__7grammar_():

    ((keyword_tkeys, tkey2rgnr_mmk4tkd_mspost, noise_tkeys),  (num_nonkeyword_rgnrs, num_mk4tkds, num_sposts)) = extract_info5hlpr4tknz_(_Helper4Tokenization4Grammar(), extra=True)
    assert (num_nonkeyword_rgnrs, num_mk4tkds, num_sposts) == (9, 0, 5), (num_nonkeyword_rgnrs, num_mk4tkds, num_sposts)
    #######
    rgnr4tknz__7grammar = prepare4tokenize_(keyword_tkeys, tkey2rgnr_mmk4tkd_mspost)
    #may_tkeys8noise4tknz = noise_tkeys#if len(noise_tkeys) else None
    tkeys8noise4tknz__7grammar = noise_tkeys
    may_env4tknz__7grammar = None
    main_rgnr4tknz__7grammar = mkrs.main_(rgnr4tknz__7grammar)
    return (main_rgnr4tknz__7grammar, tkeys8noise4tknz__7grammar, may_env4tknz__7grammar)
if 1:
    (grp4nm4rgnr4parse__7grammar, name2may_gpostprocess6ok4parse__7grammar, name2rgnr4parse__7grammar, main_rgnr4parse__7grammar, env4parse__7grammar, max_num_tokens6backward4parse__7grammar) = prepare4parse__7grammar_(dummy_name_resolver)
    (main_rgnr4tknz__7grammar, tkeys8noise4tknz__7grammar, may_env4tknz__7grammar) = prepare4tokenize__7grammar_()

def __(pseudo_fname, src, may_tkey2tdat2tdat__7high_lvl_tkd, /):
    #input:
    ######################
    ######################
    from seed.recognize.recognizer_LLoo__ver2_.tokenize_utils import tokenize__chars_
    from seed.types.IToken import mk_chr_tgbegin5fname_
    ######################
    chr_tgbegin6pseudo_fname = mk_chr_tgbegin5fname_(pseudo_fname)
    ######################
    return tokenize__chars_(may_tkey2tdat2tdat__7high_lvl_tkd, tkeys8noise4tknz__7grammar, main_rgnr4tknz__7grammar, chr_tgbegin6pseudo_fname, src, to_flatten=False, max_num_tokens6backward4high_lvl=max_num_tokens6backward4parse__7grammar, may_env4tknz=may_env4tknz__7grammar)
    ######################
######################
######################
######################
__all__
from seed.recognize.recognizer_LLoo__ver2_.grammar4IRecognizerLLoo import *
