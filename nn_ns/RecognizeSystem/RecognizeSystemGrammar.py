
r'''
data types:
    tokenize :: str -> [token]
    parse__tokens :: [token] -> parse_result
    parse__str :: str -> parse_result
    compile :: parse_result -> compile_result

    token = (token_case, substr)
    token_case in 'keyword digit word_char op comment newline space1s'.split()
    parse_result =
        { alt_id_info_pairs :: [(alt_id, alt_info)]
        , usr_token_set_ids :: [name]
        , usr_predicator_ids :: [name]
        , usr_nullable_recognizer_ids :: [name]
        , usr_nonnull_recognizer_ids :: [name]
        , noise_nonnull_recognizer_ids :: [name]
        }
    compile_result =
        { def_id2alt_id2alt_info :: {def_id : {alt_id : alt_info}}
        , usr_token_set_ids :: {name}
        , usr_predicator_ids :: {name}
        , usr_nullable_recognizer_ids :: {name}
        , usr_nonnull_recognizer_ids :: {name}
        , noise_nonnull_recognizer_ids :: {name}
        }


    alt_id = def_id | '{def_id}-{suffix}'
    def_id = name
    name   is rex'[0-9a-zA-Z_]+'
    suffix is rex'[0-9a-zA-Z]+'
    alt_info =  ( may_unbox_or_prime :: str # int
                , unsingleton :: bool
                , items3s :: ([item], [item], [item])
                )
    may_unbox_or_prime in ['', '*', '&'] # [0,1,2]
    AutoNoise = bool
    item = (may_skip, recognizer_item, may_lookahead) | ('?', name) | ('!', name)
    recognizer_item = (id, may_multi_ex)
    may_multi_ex = (may_sep_by, may_endID, multi) | ()
    may_skip = '' | '-'
    may_lookahead = '' | '&'
    id = name | '@{name}@' # | '`{str}`'
    may_sep_by = () | ('/'|'//', sepID_ex)
    sepID_ex = (AutoNoise, name, AutoNoise)
    may_endID = '' | name
    multi = (uint, uint|None)

    # may_sep_by
    # x/~* -> ()
    # x* -> ('/', (False, '@noise@', False))
    # x/s* -> ('/', (True, s, True))
    # x/~s* -> ('/', (False, s, True))
    # x/~s~* -> ('/', (False, s, False))
    # x/s~* -> ('/', (True, s, False))



'''

















__all__ = '''
    recognize_system_grammar
    TokenizeError
    ParseError
    tokenize_RecognizeSystemGrammar
    iter_tokenize_RecognizeSystemGrammar
    tokens
    _parse_recognize_system_grammar
    parse_result
    alt_id2def_id
    is_skipped_item
    verify_unsingleton

    compile_RecognizeSystemGrammar
    compile_result_RecognizeSystemGrammar
    '''.split()

import re
from itertools import chain
from collections import defaultdict, OrderedDict
from collections.abc import Sequence
from .Utils import (drop_prefix, handle_seq_begin_end
    , end_of, fst, snd, list_map, sum_lists
    , are_elements_all_unique, are_disjoint_sets
    , find_duplicate_elements, find_out_nondisjoint_sets
    , group_to_pairs
    )
from .nullable import left_recur_detect_ex

'''

@token_set_regex__begin@
    # turn-off noise
    # type == [token]
    Rule-Define*
@token_set_regex__end@
@tokens_nullable_recognizer@ # st -> uint
@tokens_nonnull_recognizer@ # st -> pint

open_of_regex_group (
close_of_regex_group )
open_of_regex_choice [
close_of_regex_choice ]

'''

recognize_system_grammar = r'''
# RecognizeSystemGrammar = ('RecognizeSystemGrammar', [LogicalBlock])
RecognizeSystemGrammar =* -EmptyLines $$/ LogicalBlock/EmptyLines$EOF*

# LogicalBlock = ('LogicalBlock-RuleLine', Rule) -->> Rule
#              | ('LogicalBlock-TurnOffNoise', Rule) -->> Rule
*LogicalBlock-RuleLine =* $$/ LogicalLine
*LogicalBlock-TurnOffNoise =* $$/ TurnOffNoiseBlock
#LogicalBlock-Regex =* $$/ RegexBlock


*EmptyLines =* EmptyLine*
EmptyLine = -RealSpace1s? LineComment? -newline $$      # nonnull
EmptyTail-comment = -RealSpace1s $$/ LineComment -EOL   # nonnull
EmptyTail-spaces = -RealSpace1s? -EOL                   # nullable
# LogicalLine = Rule
*LogicalLine =* $$/ Rule -EmptyTail                     # nonnull



# Rule  =
#   | ('Rule-Define', ... -->> (Alt_ID, (may_unbox_or_prime, unsingleton, ([Item], [item], [item]))))
#   | (other-cases, [IDBase])
Rule-Alias = DefID -Space1s -eqeq $$ -Space1s AnyID
Rule-Define      = MayOp_Alt_ID ?NoSpace $$/ Alt_ID -Space1s Eq -Space1s ListInserted
Rule-TokenSet   =* -kw_token_set $$ -Space1s UsrTokenSetID/Space1s+
Rule-Predicator =* -kw_predicator $$ -Space1s UsrPredicatorID/Space1s+
Rule-NullableRecognizer =* -kw_nullable_recognizer $$ -Space1s UsrNullableRecognizerID/Space1s+
# to detect left-recur
Rule-NonNullRecognizer =* -kw_nonnull_recognizer $$ -Space1s UsrNonnullRecognizerID/Space1s+
# to omit Space1s and EmbeddedComment
Rule-Noise =* -kw_noise $$ -Space1s NoiseID/Space1s+




# MayOp_Alt_ID = ... -->> '' | '&' | '*'
MayOp_Alt_ID-unbox =* unbox     # -> '*'
MayOp_Alt_ID-prime =* prime     # -> '&'
MayOp_Alt_ID-empty = ?@pass@    # -> ''


# Alt_ID = ('Alt_ID', (DefID, [Suffix])) -->> DefID | '{DefID}-{Suffix}'
# Alt_ID = ... -->> String
Alt_ID = DefID $$/ ?NoSpace Deli_Suffix?
*DefID =* IDBase
# IDBase = [('id_char', Char)] -->> String
*IDBase =* !digit id_char+

# Deli_Suffix = String
*Deli_Suffix =* -deli $$ ?NoSpace Suffix
# Suffix = [('alnum_char', Char)] -->> String
*Suffix =* alnum_char+ # v.s. IDBase: exclude '_'; can start with digit
# Eq = ... -->> Bool
Eq-Normal      =* eq        # -> False
Eq-Unsingleton =* eq_star   # -> True

# ListInserted = ... -->> ([Item], [Item], [Item])
#       # [...,itemA, itemB,...] ==>> [...,itemA, "@noise@", itemB, ...]
#       # remove all ()
*ListInserted =* $$/ List
# List = (AutoItems, AutoItems, AutoItems)
#       the first AutoNoise in first AutoItems if exists, should be False
*List-1ss3 = May_AutoItem1s_Space1s -ss $$ @any@{0,0} May_Space1s_AutoItem1s
*List-1ss23 = May_AutoItem1s_Space1s -ss1 $$ -Space1s AutoItem{1,1} May_Space1s_AutoItem1s
*List-1s2s3 = May_AutoItem1s_Space1s -open_of_ss $$ -Space1s May_AutoItem1s_Space1s -close_of_ss May_Space1s_AutoItem1s
*List-1ss = $$/ AutoItem1s @any@{0,0} @any@{0,0}




# May_Space1s_AutoItem1s = AutoItems
# May_AutoItem1s_Space1s = AutoItems
*May_Space1s_AutoItem1s-just =* -Space1s $$/ AutoItem1s
*May_Space1s_AutoItem1s-none =* @any@{0,0} # ?@pass@ # [] instead of ()
*May_AutoItem1s_Space1s-just =* $$/ AutoItem1s -Space1s
*May_AutoItem1s_Space1s-none =* @any@{0,0} # ?@pass@


# AutoItem = Item | ()
*AutoItem-Item =* $$/ Item
*AutoItem-NoAuto = -no_auto_noise

# AutoItems = [AutoItem]
# AutoItem1s = [AutoItem]
*AutoItems =* $$/ AutoItem/Space1s*
*AutoItem1s =* $$/ AutoItem/Space1s+



# Item  = ItemReco | ItemPred
*Item-pred =* $$/ PredicatorItem
    # ItemPred = ('!'|'?', ID)
*Item-reco =* $$/ WrappedRecognizerItem
    # ItemReco = (MaySkip, RecognizerItem, MayLookAhead)
*PredicatorItem = PredOp $$ ?NoSpace ToBePredicatorID
*WrappedRecognizerItem = MaySkip ?NoSpace $$/ RecognizerItem ?NoSpace MayLookAhead
# RecognizerItem = (ID, MayMultiEx)
*RecognizerItem = RecognizerPositionID $$ ?NoSpace MayMultiEx


# PredOp = ... -->> '!'|'?'
PredOp-not =* not
PredOp-ask =* ask


# MaySkip = ... -->> '' | '-'
MaySkip-True  = skip           # -> '-'
MaySkip-False = ?@pass@        # -> ''
# MayLookAhead = ... -->> '' | '&'
MayLookAhead-True  = lookahead # -> '&'
MayLookAhead-False = ?@pass@   # -> ''

# MayMultiEx = (MaySepBy, MayEndBy, Multi) | ()
*MayMultiEx-just = $[ MaySepBy ?NoSpace MayEndBy ?NoSpace Multi ]$
*MayMultiEx-none = ?@pass@
#### MaySepBy =* Sep RecognizerPositionID # ERROR: =*
# MaySepBy = ... -->> () | ('/' | '//', (AutoNoise, ID, AutoNoise))
MaySepBy-sep = Sep $$ ?NoSpace SepIDEx
    # if ('/'|'//', ()) -> ()
MaySepBy-None = ?@pass@
    # -> ('/', (False, '@noise@', False))
# SepIDEx = (AutoNoise, ID, AutoNoise) | ()
*SepIDEx-ID = StrictAutoNoise ?NoSpace RecognizerPositionID $$ ?NoSpace StrictAutoNoise
*SepIDEx-NoID = -no_auto_noise
# StrictAutoNoise = ... -->> AutoNoise # AutoNoise == bool
*StrictAutoNoise =* no_auto_noise?
# Sep = ... -->> '/'|'//'
Sep-1 =* sep1 # -> '/'
Sep-2 =* sep2 # -> '//'

# MayEndBy = ... -->> String
*MayEndBy-just =* -end $$ ?NoSpace RecognizerPositionID     # -> ID
*MayEndBy-none = ?@pass@                                    # -> ''

# Multi = ... -->> (uint, uint|None)
Multi-star      =* star     # -> (0, None)
Multi-cross     =* cross    # -> (1, None)
Multi-optional  =* optional # -> (0, 1)
Multi-minmax    = -open_of_multi $$ ?NoSpace Min ?NoSpace -comma_of_multi ?NoSpace MayMax ?NoSpace -close_of_multi
                            # -> (min, max)
# Min = UInt
*Min =* $$/ UInt
# MayMax = ... -->> UInt | None
*MayMax =* $$/ UInt?



# UInt = int
*UInt-hex =* $$/ UIntHex !id_char
*UInt-dec =* $$/ UIntDec !id_char
    # dec should be after hex; since '0' is prefix of '0x'
# UIntDec = [char_token] -->> int
# UIntHex = [char_token] -->> int
*UIntHex =* -char_0 -char_x $$ xdigit+  # 0x not 0X
*UIntDec-0 = char_0 $$ !char_x
*UIntDec-pos =* !char_0 digit+          # digitNot0 digit*




# noise
RealSpace1s =* spaceNotNewline+
Space1s-logical = EmptyTail EmptyLines RealSpace1s
#              /* newline + indent ==>> in same logical line */
Space1s-physical = RealSpace1s
#              /* no newline == in same physical line */


LineComment =* -sharp $$ charNotNewline* # @any@$(?EOL)*
EOL-eol = newline
EOL-eof = EOF
EOF = !@any@
NoSpace = ?@pass@











########################### TurnOffNoise
# TurnOffNoiseBlock = [Rule]
*TurnOffNoiseBlock =* $$/ -TurnOffNoiseBegin TurnOffNoise_LogicalLine/EmptyLines$TurnOffNoiseEnd*
TurnOffNoiseBegin = kw_turnoff_noise__begin $$ EmptyTail EmptyLines
TurnOffNoiseEnd = kw_turnoff_noise__end $$ EmptyTail

# TurnOffNoise_LogicalLine = Rule
*TurnOffNoise_LogicalLine =* $$/ TurnOffNoise_Rule -EmptyTail    # nonnull
# TurnOffNoise_Rule = ... -->> ('Rule-Define', _)
TurnOffNoise_Rule-Define = MayOp_Alt_ID ?NoSpace $$/ Alt_ID -Space1s Eq -Space1s TurnOffNoise_List



# TurnOffNoise_List = (Items, Items, Items)
TurnOffNoise_List-1ss3 = TurnOffNoise_May_Item1s_Space1s -ss $$ @any@{0,0} TurnOffNoise_May_Space1s_Item1s
TurnOffNoise_List-1ss23 = TurnOffNoise_May_Item1s_Space1s -ss1 $$ -Space1s TurnOffNoise_Item{1,1} TurnOffNoise_May_Space1s_Item1s
TurnOffNoise_List-1s2s3 = TurnOffNoise_May_Item1s_Space1s -open_of_ss $$ -Space1s TurnOffNoise_May_Item1s_Space1s -close_of_ss TurnOffNoise_May_Space1s_Item1s
TurnOffNoise_List-1ss = $$/ TurnOffNoise_Item1s @any@{0,0} @any@{0,0}




# TurnOffNoise_May_Space1s_Item1s = Items
# TurnOffNoise_May_Item1s_Space1s = Items
*TurnOffNoise_May_Space1s_Item1s-just =* -Space1s $$/ TurnOffNoise_Item1s
*TurnOffNoise_May_Space1s_Item1s-none =* @any@{0,0}
*TurnOffNoise_May_Item1s_Space1s-just =* $$/ TurnOffNoise_Item1s -Space1s
*TurnOffNoise_May_Item1s_Space1s-none =* @any@{0,0}



# TurnOffNoise_Items = [Item]
# TurnOffNoise_Item1s = [Item]
*TurnOffNoise_Items =* $$/ TurnOffNoise_Item/Space1s*
*TurnOffNoise_Item1s =* $$/ TurnOffNoise_Item/Space1s+



# TurnOffNoise_Item = Item
# TurnOffNoise_Item  = ItemReco | ItemPred
*TurnOffNoise_Item-pred =* $$/ PredicatorItem
    # ItemPred = ('!'|'?', ID)
*TurnOffNoise_Item-reco =* $$/ TurnOffNoise_WrappedRecognizerItem
    # ItemReco = (MaySkip, RecognizerItem, MayLookAhead)
*TurnOffNoise_WrappedRecognizerItem = MaySkip ?NoSpace $$/ TurnOffNoise_RecognizerItem ?NoSpace MayLookAhead
# TurnOffNoise_RecognizerItem = (ID, MayMultiEx)
*TurnOffNoise_RecognizerItem = RecognizerPositionID $$ ?NoSpace TurnOffNoise_MayMultiEx

# TurnOffNoise_MayMultiEx = (MaySepBy, MayEndBy, Multi) | ()
*TurnOffNoise_MayMultiEx-just = $[ TurnOffNoise_MaySepBy ?NoSpace MayEndBy ?NoSpace Multi ]$
*TurnOffNoise_MayMultiEx-none = ?@pass@
# TurnOffNoise_MaySepBy = ... -->> () | ('/' | '//', (AutoNoise, ID, AutoNoise))
TurnOffNoise_MaySepBy-sep = Sep $$ ?NoSpace RecognizerPositionID
    # ('/'|'//', id) -> (sep, (False, id, False))
TurnOffNoise_MaySepBy-None = ?@pass@
    # () -> ()
###########################










# IDs
*RecognizerPositionID =* RecognizerID
*AnyID =* ToBePredicatorID
*ToBePredicatorID-1 =* UsrPredicatorID_or_RecognizerID
*ToBePredicatorID-2 =* BuiltinPredicatorID

*NoiseID =* NonnullRecognizerID
*NonnullRecognizerID-1 =* NonnullDefID_or_UsrTokenSetID_or_UsrNonnullRecognizerID
*NonnullRecognizerID-2 =* BuiltinTokenSetID_or_BuiltinNonnullRecognizerID

*RecognizerID-1 =* DefID_or_UsrTokenSetID_or_UsrRecognizerID
*RecognizerID-2 =* BuiltinTokenSetID_or_BuiltinRecognizerID
*BuiltinRecognizerID =* BuiltinNullableRecognizerID_or_BuiltinNonnullRecognizerID
*UsrRecognizerID =* UsrNonnullRecognizerID_or_UsrNullableRecognizerID



*UsrTokenSetID =* IDBase
*UsrPredicatorID =* IDBase
*UsrNonnullRecognizerID  =* IDBase
*UsrNullableRecognizerID =* IDBase


# BuiltinTokenSetID = (_, id) -> id
# BuiltinPredicatorID = (_, id) -> id
# BuiltinNullableRecognizerID = (_, id) -> id
*BuiltinTokenSetID-1 =* kw_any
*BuiltinTokenSetID-2 =* kw_dead
*BuiltinPredicatorID =* kw_pass
*BuiltinNullableRecognizerID =* kw_noise
BuiltinNonnullRecognizerID = @dead@  # not exists


*UsrPredicatorID_or_RecognizerID-1 =* RecognizerID
*UsrPredicatorID_or_RecognizerID-2 =* UsrPredicatorID
*DefID_or_UsrTokenSetID_or_UsrRecognizerID =* IDBase
*UsrNonnullRecognizerID_or_UsrNullableRecognizerID =* IDBase
*NonnullDefID_or_UsrTokenSetID_or_UsrNonnullRecognizerID =* IDBase
*BuiltinTokenSetID_or_BuiltinNonnullRecognizerID-1 =* BuiltinTokenSetID
*BuiltinTokenSetID_or_BuiltinNonnullRecognizerID-2 =* BuiltinNonnullRecognizerID
*BuiltinTokenSetID_or_BuiltinRecognizerID-1 =* BuiltinTokenSetID
*BuiltinTokenSetID_or_BuiltinRecognizerID-2 =* BuiltinRecognizerID
*BuiltinNullableRecognizerID_or_BuiltinNonnullRecognizerID-1 =* BuiltinNullableRecognizerID
*BuiltinNullableRecognizerID_or_BuiltinNonnullRecognizerID-2 =* BuiltinNonnullRecognizerID



# token_set is a predicator
# so one token may present in different token_set
@token_set@ digit  id_char       alnum_char
          # [0-9]  [0-9a-zA-Z_] [0-9a-zA-Z]
@token_set@ char_x char_0 xdigit
          # 'x'    '0'    [0-9a-fA-F]
@token_set@ spaceNotNewline  charNotNewline
          # \S-\n            \.-\n
@token_set@ sharp  newline
          # #      \n
@token_set@ unbox prime deli  eq  eq_star  ss   no_auto_noise eqeq
          # *     &     -     =   =*       $$   ~             ==
@token_set@ skip  sep1  sep2  end  star  cross  optional  not ask lookahead
          # -     /     //    $    *     +      ?         !   ?   &
@token_set@ open_of_multi comma_of_multi close_of_multi
          # {             ,              }
@token_set@ open_of_ss  close_of_ss ss1
          # $[          ]$          $$/
@token_set@ kw_token_set kw_predicator kw_nullable_recognizer kw_nonnull_recognizer kw_noise
          # @token_set@  @predicator@  @nullable_recognizer@  @nonnull_recognizer@  @noise@
@token_set@ kw_pass kw_any kw_dead
          # @pass@  @any@  @dead@
          # @dead@ =/= (!@pass@), since later is nullable
          # no @eof@, since eof === !@any@
@token_set@ kw_turnoff_noise__begin kw_turnoff_noise__end
          # @turnoff_noise__begin@  @turnoff_noise__end@

################################ constraint
# every DefID should be defined
# AltID should be unique; AltID of same DefID should be together
# unsingleton "=*":
#   there should be one and only one non-skipped item in right part
# for any item not [?!] for any id in item:
#   id should not be BuiltinPredicatorID or UsrPredicatorID
# no left-recur
# no nullable{_,None} and no nullable/nullable[$e]{_,None}
# all noise IDs should be nonnull recognizer
################################ explain
# explain
# -- id = symbol = nonterminal | terminal; token = terminal
# -- try alternatives from top to bottom
# each id/alt_id -> ((val, st) | raise IDErr | raise AltErr)
#       token -> ((val, st) | raise AltErr)
#       (!id | ?id) -> (() | raise AltErr)
# (-item | !id | ?id)  ->  no val since they are skipped items
#
# 0) comment; alias
# comment: begin with '#' to end of line
# alias:   "alias_id == ref_id"
# 1) basic:
# # alt_id
# alt_id = x y
#   -> ('alt_id', (x, y))
# alt_id = -x y         # skip
#   -> ('alt_id', (y,))
# alt_id =* -x y        # unsingleton
#   -> ('alt_id', y)
# &alt_id =* -x y       # remove suffix, i.e. alt_id->def_id
#   -> ('def_id', y)
# *alt_id =* -x y       # unbox
#   -> y
# "alt_id = x y" === "alt_id = x y $[ ]$"
# "alt_id = x $$ y" === "alt_id = x $[ ]$ y"
# "alt_id = x... $$/ y z..." === "alt_id = x... $[ y ]$ z..."
# alt_id = x... $[ y... ]$ z...
#   if x... -> raise AltErr|IDErr, then alt_id -> raise AltErr
#   if y... -> raise AltErr|IDErr, then alt_id -> reraise
#   if z... -> raise AltErr|IDErr, then alt_id -> raise IDErr
# # def_id
# id-1 = ...
# id-2 = ...
#   if id-1 -> v, then id -> v
#   if id-1 -> raise IDErr, then id -> raise IDErr
#   if id-1 -> raise AltErr, then id -> try id-2
#   try id-2 ...#like id-1
#   if no alternatives: raise AltErr # no alt matched
# # decl
# @token_set@ x y # decl token_set 'x' 'y'
# @predicator@ x y # decl predicator 'x' 'y'
# @nullable_recognizer@ x y # decl nullable_recognizer 'x' 'y'
# @nonnull_recognizer@ x y # decl nonnull_recognizer 'x' 'y'
# if token_set -> v, then convert to ('token_set', v)
# similar for others
# 2) $$  -- should success
# alt_id = x $$ z
#   if x -> raise IDErr, then alt_id -> raise AltErr
#   if z -> raise AltErr, then logic-error
# alt_id = x y ==>> alt_id = x y $$
# 3) ?x !y -- predicate
# ?x -- if match x then pass else fail
# !x -- if not match x then pass else fail
# 4) x& -- AND; lookahead; v.s. predicate: got result
# x& -- match x, get the result and then go back to input position
# ?x === -x& except when raise DeadErr
# 5) x/s$e+
# if x -> v then x(('/'|'//')s)?('$'e)?('+'|'*'|'?') -> [v]
# * === {0,}
# + === {1,}
# ? === {0,1}
# let S = s | ~s | s~ | ~s~
# x//S = x/S !S
# x//S$e = x/S$e !S
# -- greedy
# x{m,M}
# x/S{m,M}
# -- nongreedy
# x$e{m,M}
# x/S$e{m,M}
#### implement
# x//s$e{m,M} = x/s$e !s
# x$e{m,M} = (!e x){m,M} -e
# x/s$e{m,M} = (!e x -s){m,M} -e = (x -s)$e{m,M}
# x{m,M} = to be implemented = x{m,m} x{0,M-m}
# x/s{m,M} = to be implemented =/= ERROR: x/s$(!x){m,M}
#
##x{m,M}
# x{0,} = avoid_null(x){0,}...
# x{0,M} = ...
# x{m,m} = ...
# x{m,M} = x{m,m} x{0,M-m}
##x/s{m,M}
# x/s{0,0} = ...
# x/s{0,M} = x/s{1,M} | x/s{0,0}
# x/s{m,M} = x (-s x){m-1,M-1}
#
# 6) @noise@
# # decl
# @noise@ x y   # @noise@ = -(x|y)*  # default to "@pass@"
#   # @noise@ can appear anywhere between "two" items except "~"
#   @noise@ space1s comment
# # insert @noise@ between items
# x y === inserted"x -@noise@ y" === x ~ -@noise@ ~ y
# x ~ y === inserted"x y" # do not insert @noise@ between x y
# x* === inserted"x/(@noise@)*"
# x/~* === inserted"x*"
# x/s* === inserted"x/(@noise@ s @noise@)*"
# x/~s* === inserted"x/(s @noise@)*"
# x/s~* === inserted"x/(@noise@ s)*"
# x/~s~* === inserted"x/s*"
# e.g. ID = id_char/~+
#
# 7) TurnOffNoise
# @turnoff_noise__begin@
# ID = id_char+ # compare with "ID = id_char/~+" where noise turn on
# @turnoff_noise__end@

'''


'''
'''

# keyword | digit | word_char | op | comment | newline | space1s
pattern = (r'(?m-s:'
    r'(@token_set@|@predicator@|@nullable_recognizer@|@nonnull_recognizer@'
        r'|@turnoff_noise__begin@|@turnoff_noise__end@'
        r'|@noise@|@dead@|@pass@|@any@)'
    r'|([0-9])'
    r'|([a-zA-Z_])'
    r'|(\$\$/|\$\[|\]\$|\$\$|==|=\*|//|[{,}~&=/$*+?!-])'
    r'|(#.*)'
    r'|(\n)'
    r'|((?:(?!\n)\s)+)'
    ')')

rex = re.compile(pattern)
class TokenizeError(Exception):pass
class ParseError(Exception):pass
def tokenize_RecognizeSystemGrammar(s, begin=None, end=None):
    # str -> [(case, substr)]
    # where case in [keyword, digit, word_char, op, comment, newline, space1s]
    return tuple(iter_tokenize_RecognizeSystemGrammar(s, begin, end))
def iter_tokenize_RecognizeSystemGrammar(s, begin=None, end=None):
    s, begin, end = handle_seq_begin_end(s, begin, end)
    while begin < end:
        m = rex.match(s, begin, end)
        if not m:
            if 1:
                print(s[:begin])
                print('#'*20)
                print(s[begin:end])
            raise TokenizeError(s, begin, end)
        if begin == m.end():
            # bad rex
            raise logic-error
        begin = m.end()
        groups = m.groups()
        # [keyword, digit, word_char, op, comment, newline, space1s]
        names = 'keyword digit word_char op comment newline space1s'.split()
        assert len(names) == len(groups)
        for name, val in zip(names, groups):
            if val is not None:
                yield name, val
                break
        else:
            raise logic-error


tokens = tokenize_RecognizeSystemGrammar(recognize_system_grammar)
#rint(list(tokens))
def _parse_recognize_system_grammar(s):
    '''\
[token] ->  { alt_id_info_pairs :: [(alt_id, alt_info)]
            , alias_list :: [(def_id, name)]
            , usr_token_set_ids :: [name]
            , usr_predicator_ids :: [name]
            , usr_nullable_recognizer_ids :: [name]
            , usr_nonnull_recognizer_ids :: [name]
            , noise_nonnull_recognizer_ids :: [name]
            }
token = (token_case, substr)
token_case in [keyword, digit, word_char, op, comment, newline, space1s]


'''
    def fix_items_first_AutoNoise(*itemss):
        for items in itemss:
            if items:
                auto_noise, item = items[0]
                items[0] = False, item
                break
    def parse_items(s):
        # not support "~"
        item_strs = s.split()
        items = list(map(parse_item, item_strs))
        return items
        items = [(True, parse_item(item_str)) for item_str in item_strs]
    def parse_item(s):
        # stripped
        # not support "~"
        assert s
        if s[0] in '?!':
            return (s[0], s[1:])
        if s[0] == '-':
            s = s[1:]
            may_skip = '-'
        else:
            may_skip = ''
        if not s: raise ParseError("error: {!r}".format(org_line))

        if s[-1] == '&':
            s = s[:-1]
            may_lookahead = '&'
        else:
            may_lookahead = ''
        if not s: raise ParseError("error: {!r}".format(org_line))

        def str2int(s):
            if 'x' in s:
                return int(s, 16)
            return int(s)
        if s[-1] == '}':
            s = s[:-1]
            s, mM = s.split('{')
            m, M = mM.split(',')
            M = None if M == '' else str2int(M)
            m = str2int(m)
            multi = (m, M)
        elif s[-1] in '?*+': # not support "{,}"
            multi = s[-1]
            s = s[:-1]
            multi = {'?':(0,1), '*':(0,None), '+':(1,None)}[multi]
        else:
            multi = None
        if multi is not None:
            # not support "//"
            # not support "~"
            if '$' in s:
                s, endID = s.split('$')
                may_endID = endID
            else:
                may_endID = ''
            if '/' in s:
                id, sepID = s.split('/')
            else:
                sepID = '@noise@'
                id = s
            may_sep_by = ('/', (True, sepID, True))
            may_multi_ex = (may_sep_by, may_endID, multi)
        else:
            may_multi_ex = ()
            id = s
        recognizer_item = (id, may_multi_ex)
        item = may_skip, recognizer_item, may_lookahead
        assert type(id) is str
        return item

    def parse_assign(s):
        assign = '=*' if '=*' in s else '==' if '==' in s else '='
        L, R = s.split(assign)
        L = L.strip(); R = R.strip()
        if assign == '==':
            [alias_id] = L.split()
            [orginial_id] = R.split()
            alias_list.append((alias_id, orginial_id))
            return

        # Middle
        unsingleton = assign == '=*'

        # Left
        if L[0] in '*&':
            may_unbox_or_prime = L[0]
            L = L[1:]
        else:
            may_unbox_or_prime = ''

        alt_id = L
        def_id = L.split('-')[0]

        # Right
        if '$$/' in R.split():
            items1, items23 = R.split('$$/')
            items2_3 = items23.split(maxsplit=1)
            items2_3.extend(['']*(2-len(items2_3)))
            items2, items3 = items2_3
        elif '$$' in R.split():
            items1, items3 = R.split('$$')
            items2 = ''
        elif '$[' in R.split():
            items1, items23 = R.split('$[')
            items2, items3 = items23.split(']$')
        else:
            items1, items2, items3 = R, '', ''
        ls = [items1, items2, items3]
        items3s = tuple(map(parse_items, ls))
        #fix_items_first_AutoNoise(items1, items2)
        alt_info = may_unbox_or_prime, unsingleton, items3s
        d[def_id][alt_id] = alt_info
        alt_id_info_pairs.append((alt_id, alt_info))
        return
    def parse_decl_names(s, kw, out_names):
        s = drop_prefix(s, kw)
        names = s.split()
        out_names.extend(names)
    ###########
    d = defaultdict(OrderedDict)
    # [(alt_id, (may_unbox_or_prime, unsingleton, items1, items2))]
    alt_id_info_pairs = []
    alias_list = []
    usr_token_set_ids = []
    usr_predicator_ids = []
    usr_nullable_recognizer_ids = []
    usr_nonnull_recognizer_ids = []
    noise_nonnull_recognizer_ids = []
    decl_kw_outnames_pairs =\
        [('@token_set@',  usr_token_set_ids)
        ,('@predicator@', usr_predicator_ids)
        ,('@nullable_recognizer@', usr_nullable_recognizer_ids)
        ,('@nonnull_recognizer@', usr_nonnull_recognizer_ids)
        ,('@noise@', noise_nonnull_recognizer_ids)
        ]

    for line in s.split('\n'):
        org_line = line
        line = line.strip()
        if not line or line[0] == '#': continue
        if '#' in line:
            i = line.index('#')
            line = line[:i].strip()
        assert line
        if '=' in line:
            parse_assign(line)
        else:
            for kw, out_names in decl_kw_outnames_pairs:
                if line.startswith(kw): break
            else:
                raise ParseError("error: {!r}".format(org_line))
            parse_decl_names(line, kw, out_names)

    def_id2alt_id2alt_info = d
    return dict ( alt_id_info_pairs = alt_id_info_pairs
                , alias_list = alias_list
                , usr_token_set_ids = usr_token_set_ids
                , usr_predicator_ids = usr_predicator_ids
                , usr_nullable_recognizer_ids = usr_nullable_recognizer_ids
                , usr_nonnull_recognizer_ids = usr_nonnull_recognizer_ids
                , noise_nonnull_recognizer_ids = noise_nonnull_recognizer_ids
                )

end_of(_parse_recognize_system_grammar)
parse_result = _parse_recognize_system_grammar(recognize_system_grammar)





















def alt_id2def_id(alt_id):
    def_id, suffix = split_alt_id(alt_id)
    return def_id
def split_alt_id(alt_id):
    ls = alt_id.split('-')
    assert len(ls) <= 2
    if len(ls) < 2:
        ls.append('')
    def_id, suffix = ls
    return def_id, suffix



def is_alt_id(alt_id):
    def_id, suffix = split_alt_id(alt_id)
    return is_def_id(def_id) and is_suffix(suffix)
def is_suffix(suffix):
    return not suffix or (is_name(suffix) and '_' not in suffix)
def is_alt_info(alt_info):
    # (may_unbox_or_prime :: str, unsingleton :: bool, items3s)
    if not is_tuple(alt_info, 3):
        return False
    may_unbox_or_prime, unsingleton, items3s = alt_info
    return (is_may_unbox_or_prime(may_unbox_or_prime)
        and is_bool(unsingleton)
        and are_itemss(items3s, 3)
        )

def is_may_unbox_or_prime(x):
    return is_str(x) and x in ('', '&', '*')
def are_itemss(itemss, L):
    return is_tuple(itemss, L) and all(map(are_items, itemss))

def are_items(items):
    return hasattr(items, '__len__') and all(map(is_item, items))
def is_tuple(x, L=None):
    return type(x) is tuple and (L is None or len(x) == L)
def is_int(x):
    return type(x) is int
def is_uint(x):
    return is_int(x) and x >= 0
def is_bool(x):
    return type(x) is bool
def is_str(x):
    return type(x) is str
def int_between(x, min, max):
    return is_int(x) and min <= x <= max

def is_auto_item(auto_item):
    if is_tuple(auto_item, 2):
        auto_noise, item = auto_item
        return is_bool(auto_noise) and is_item(item)
    return False

def is_item(item):
    return is_predicater_item(item) or is_wrapped_recognizer_item(item)
def is_predicater_item(item):
    # ('?', name) | ('!', name)
    if is_tuple(item, 2):
        case, name = item
        return case and case in '?!' and is_name(name)
    return False
def is_wrapped_recognizer_item(item):
    # (''|'-', recognizer_item, ''|'&')
    if is_tuple(item, 3):
        may_skip, recognizer_item, may_lookahead = item
        return may_skip in '-' and may_lookahead in '&'\
            and is_recognizer_item(recognizer_item)
    return False
def is_recognizer_item(recognizer_item):
    # (id, may_multi_ex)
    if is_tuple(recognizer_item, 2):
        id, may_multi_ex = recognizer_item
        return is_name(id) and is_may_multi_ex(may_multi_ex)
    return False
def is_may_multi_ex(x):
    # () | (may_sep_by, may_endID, multi)
    if is_tuple(x, 0): return True
    if not is_tuple(x, 3): return False
    may_sep_by, may_endID, multi = x
    return (is_may_sep_by(may_sep_by)
        and is_may_name(may_endID)
        and is_multi(multi)
        )
def is_may_name(x):
    return is_str(x) and (not x or is_name(x))
def is_may_sep_by(x):
    # () | ('/'|'//', AutoNoise, ''|ID, AutoNoise)
    if is_tuple(x, 0): return True
    if not is_tuple(x, 2): return False
    sep, sepID_ex = x
    return sep in ('/', '//') and is_sepID_ex(sepID_ex)
def is_sepID_ex(x):
    if not is_tuple(x, 3): return False
    b1, id, b2 = x
    return is_bool(b1) and is_bool(b2) and is_name(id)

def is_multi(x):
    if not is_tuple(x, 2): return False
    m, M = x
    if not is_uint(m): return False
    if M is None: return True
    if not is_uint(M): return False
    return m <= M

def is_name(id):
    if not is_str(id):
        return False
        print(id)
        raise TypeError
    if len(id) > 2 and id[0] == '@' == id[-1]:
        id = id[1:-1]
    return is_def_id(id)
def is_def_id(id):
    if not is_str(id):
        return False
    if not id:
        return False
    #id = ''.join(id.split('_'))
    id = id.replace('_', '')
    return not id or id.isalnum()


assert is_name('@any@')
assert is_item(('!', '@any@'))























def is_skipped_item(item):
    # item = (skip, recognizer_item, lookahead) | ('?', name) | ('!', name)
    # skip or ask or not
    if is_wrapped_recognizer_item(item):
        may_skip, recognizer_item, may_lookahead = item
        return may_skip == '-'
    if is_predicater_item(item):
        return True
    raise logic-error

def verify_unsingleton(alt_info):
    _, unsingleton, items3s = alt_info
    if not unsingleton:
        return True
    bools = chain.from_iterable(
        list_map(is_skipped_item, items) for items in items3s)
    bools = list(bools)
    return bools.count(False) == 1

def collect_ids__alt_infos(alt_infos, write):
    # write(('PR'|'R'), id)
    for alt_info in alt_infos:
        collect_ids__alt_info(alt_info, write)
def collect_ids__alt_info(alt_info, write):
    _, _, items3s = alt_info
    for items in items3s:
        collect_ids__items(items, write)
def collect_ids__items(items, write):
    for item in items:
        collect_ids__item(item, write)
def collect_ids__item(item, write):
    # item = (skip, id, sep, end, multi::str) | ('?', name) | ('!', name)
    P = "PR" # predicator_id
    R = "R" # recognizer_id
    if is_predicater_item(item):
        not_or_ask, id = item
        write(P, id)
    elif is_wrapped_recognizer_item(item):
        _skip, recognizer_item, _lookahead = item
        id, may_multi_ex = recognizer_item
        write(R, id)
        if not may_multi_ex: return
        may_sep_by, may_endID, multi = may_multi_ex
        if may_endID:
            write(R, may_endID)
        if not may_sep_by: return
        _sep, (auto1, sepID, auto2) = may_sep_by
        write(R, sepID)
        if auto1 or auto2:
            write(R, '@noise@')
    else:
        raise logic-error

def find_alias_target(alias_list):
    L = len(alias_list)
    alias2id = dict(alias_list)
    if len(alias2id) != L:
        raise ValueError('duplicate alias')
    for alias in list(alias2id):
        ls = []
        s = set()
        id = alias
        while id in alias2id:
            if id in s:
                i = ls.index(id)
                ls = ls[i:]
                raise ValueError('recur defined alias: {}'.format(ls))

            s.add(id); ls.append(id)
            id = alias2id[id]
        for alias in ls:
            alias2id[alias] = id
    return alias2id

class _ReplaceAlias:
    def __init__(self, alias2id):
        self.alias2id = alias2id
    def replace(self, alt_id_info_pairs):
        return self.__alt_id_info_pairs(alt_id_info_pairs)
    def __alt_id_info_pairs(self, alt_id_info_pairs):
        r = [(alt_id, self.__alt_info(alt_info))
             for alt_id, alt_info in alt_id_info_pairs]
        check_type__alt_id_info_pairs(r)
        return r
    def __alt_info(self, alt_info):
        may_unbox_or_prime, unsingleton, items3s = alt_info
        items3s = tuple(map(self.__items, items3s))
        return may_unbox_or_prime, unsingleton, items3s
    def __items(self, items):
        return list_map(self.__item, items)
    def __replace(self, id):
        return self.alias2id.get(id, id)
    def __item(self, item):
        if is_predicater_item(item):
            op, predicator_id = item
            return op, self.__replace(predicator_id)
        elif is_wrapped_recognizer_item(item):
            may_skip, recognizer_item, may_lookahead = item
            recognizer_item = self.__recognizer_item(recognizer_item)
            return may_skip, recognizer_item, may_lookahead
        raise logic-error
    def __recognizer_item(self, recognizer_item):
        id, may_multi_ex = recognizer_item
        id = self.__replace(id)
        may_multi_ex = self.__may_multi_ex(may_multi_ex)
        return id, may_multi_ex
    def __may_multi_ex(self, may_multi_ex):
        if not may_multi_ex:
            return may_multi_ex
        may_sep_by, may_endID, multi = may_multi_ex
        may_sep_by = self.__may_sep_by(may_sep_by)
        may_endID = self.__replace(may_endID)
        return may_sep_by, may_endID, multi
    def __may_sep_by(self, may_sep_by):
        if not may_sep_by:
            return may_sep_by
        sep, (auto1, sepID, auto2) = may_sep_by
        sepID = self.__replace(sepID)
        return sep, (auto1, sepID, auto2)
def replace_alias(alt_id_info_pairs, alias2id):
    return _ReplaceAlias(alias2id).replace(alt_id_info_pairs)


def is_pair(x):
    return is_tuple(x, 2)
def is_seq(x):
    return isinstance(x, Sequence)
def is_pair_seq(x):
    return is_seq(x) and all(map(is_pair, x))
def check_type__alt_id_info_pairs(alt_id_info_pairs):
    if not is_pair_seq(alt_id_info_pairs):
        raise TypeError('alt_id_info_pairs should be [(a,b)]')
    for alt_id, alt_info in alt_id_info_pairs:
        if not is_alt_id(alt_id):
            raise ValueError('not alt_id: {!r}'.format(alt_id))
        if not is_alt_info(alt_info):
            raise ValueError('not all alt_info: {!r}->{!r}'.format(
                alt_id, alt_info))
def compile_RecognizeSystemGrammar(parse_result):
    return __compile_RecognizeSystemGrammar(**parse_result)
def id2item(id):
    may_skip = ''
    may_lookahead = ''
    may_multi_ex = ()
    recognizer_item = id, may_multi_ex
    item = wrapped_recognizer_item = may_skip, recognizer_item, may_lookahead
    return item
def __compile_RecognizeSystemGrammar(
    alt_id_info_pairs
    , alias_list
    , usr_token_set_ids
    , usr_predicator_ids
    , usr_nullable_recognizer_ids
    , usr_nonnull_recognizer_ids
    , noise_nonnull_recognizer_ids
    , *
    , __BuiltinTokenSetIDs = ['@any@', '@dead@']
    , __BuiltinPredicatorIDs = ['@pass@']
    , __BuiltinNullableRecognizerIDs = ['@noise@']
    , __BuiltinNonNullRecognizerIDs = []
    ):
    # not itererator
    ls = [alt_id_info_pairs , alias_list
        , usr_token_set_ids, usr_predicator_ids
        , usr_nullable_recognizer_ids, usr_nonnull_recognizer_ids
        , noise_nonnull_recognizer_ids
        , __BuiltinTokenSetIDs, __BuiltinPredicatorIDs
        , __BuiltinNullableRecognizerIDs, __BuiltinNonNullRecognizerIDs
        ]
    list_map(len, ls)
    del ls

    # check type
    check_type__alt_id_info_pairs(alt_id_info_pairs)

    for alias_id, id in alias_list:
        if not is_def_id(alias_id):
            raise ValueError('not alias_id: {!r}'.format(alias_id))
        if not is_name(id):
            raise ValueError('not name: {!r} in "{} == {}"'
                                .format(id, alias_id, id))

    ############
    alt_ids = list_map(fst, alt_id_info_pairs)
    def_ids = list_map(alt_id2def_id, alt_ids)
    alias_ids = list_map(fst, alias_list)
    # alt_id with same def_id should be together
    if 1:
        def_id_group_pairs = group_to_pairs(def_ids)
        should_be_unque_def_ids = list_map(fst, def_id_group_pairs)
        if not are_elements_all_unique(should_be_unque_def_ids):
            raise ValueError('alt_id with same def_id should be together: '
                '{}'.format(
                find_duplicate_elements(should_be_unque_def_ids)
                ))
        del def_id_group_pairs, should_be_unque_def_ids

    name2ls = dict(
        alt_ids = alt_ids
        , alias_ids = alias_ids
        , usr_token_set_ids = usr_token_set_ids
        , usr_predicator_ids = usr_predicator_ids
        , usr_nullable_recognizer_ids = usr_nullable_recognizer_ids
        , usr_nonnull_recognizer_ids = usr_nonnull_recognizer_ids
        , noise_nonnull_recognizer_ids = noise_nonnull_recognizer_ids
        , __BuiltinTokenSetIDs = __BuiltinTokenSetIDs
        , __BuiltinPredicatorIDs = __BuiltinPredicatorIDs
        , __BuiltinNullableRecognizerIDs = __BuiltinNullableRecognizerIDs
        , __BuiltinNonNullRecognizerIDs = __BuiltinNonNullRecognizerIDs
        )

    # each name in names should be unique
    for name, ls in name2ls.items():
        if not are_elements_all_unique(ls):
            raise ValueError('not all {!r} unique: {}'.format(
                name, find_duplicate_elements(ls)
                ))

    # name_sets should be disjoint
    ls = [def_ids, alias_ids
        , usr_token_set_ids, usr_predicator_ids
        , usr_nullable_recognizer_ids, usr_nonnull_recognizer_ids
        , noise_nonnull_recognizer_ids
        , __BuiltinTokenSetIDs, __BuiltinPredicatorIDs
        , __BuiltinNullableRecognizerIDs, __BuiltinNonNullRecognizerIDs
        ]
    ls = list_map(set, ls)
    [def_ids, alias_ids
        , usr_token_set_ids, usr_predicator_ids
        , usr_nullable_recognizer_ids, usr_nonnull_recognizer_ids
        , noise_nonnull_recognizer_ids
        , __BuiltinTokenSetIDs, __BuiltinPredicatorIDs
        , __BuiltinNullableRecognizerIDs, __BuiltinNonNullRecognizerIDs
        ] = ls
    name2set = dict(
        def_ids = def_ids
        , alias_ids = alias_ids
        , usr_token_set_ids = usr_token_set_ids
        , usr_predicator_ids = usr_predicator_ids
        , usr_nullable_recognizer_ids = usr_nullable_recognizer_ids
        , usr_nonnull_recognizer_ids = usr_nonnull_recognizer_ids
        # except:
        #   , noise_nonnull_recognizer_ids = noise_nonnull_recognizer_ids
        , __BuiltinTokenSetIDs = __BuiltinTokenSetIDs
        , __BuiltinPredicatorIDs = __BuiltinPredicatorIDs
        , __BuiltinNullableRecognizerIDs = __BuiltinNullableRecognizerIDs
        , __BuiltinNonNullRecognizerIDs = __BuiltinNonNullRecognizerIDs
        )
    if not are_disjoint_sets(name2set.values()):
        raise ValueError('not are_disjoint_sets({})'.format(
            find_out_nondisjoint_sets(name2set)
            ))
        raise ValueError('not are_disjoint_sets({})'.format(
        '[def_ids, alias_ids usr_token_set_ids, usr_predicator_ids, usr_nullable_recognizer_ids, usr_nonnull_recognizer_ids, noise_nonnull_recognizer_ids, __BuiltinTokenSetIDs, __BuiltinPredicatorIDs, __BuiltinNullableRecognizerIDs, __BuiltinNonNullRecognizerIDs]'
        ))
    #replace all aliases in alt_id_info_pairs
    alias2id = find_alias_target(alias_list)
    alt_id_info_pairs = replace_alias(alt_id_info_pairs, alias2id)

    ############3
    all_known_ids = set().union(*ls)
    all_known_predicator_only_ids = set().union(
        usr_predicator_ids, __BuiltinPredicatorIDs)

    # except defined_nonnull_recognizer_ids
    all_known_nonnull_recognizer_ids = set().union(
        usr_token_set_ids, usr_nonnull_recognizer_ids
        , __BuiltinTokenSetIDs, __BuiltinNonNullRecognizerIDs
        )
    ''' bugs: see below all_known_nonnull_recognizer_ids_ver2
    if not noise_nonnull_recognizer_ids <= all_known_nonnull_recognizer_ids:
        raise ValueError('noise should be nonnull_recognizer: {!r}'.format(
            noise_nonnull_recognizer_ids - all_known_nonnull_recognizer_ids
            ))
    '''


    ########### collect ids in right part
    predicator_position_ids = set()
    recognizer_position_ids = set()
    def write(case, id):
        if case == 'PR':
            predicator_position_ids.add(id)
        elif case == 'R':
            recognizer_position_ids.add(id)
        else:
            raise logic-error
        return
        # bug:
        if case == 'PR':
            all_used_ids.add(id)
            recognizer_position_ids.add(id) # should be removed
        elif case == 'R':
            # should add: all_used_ids.add(id)
            recognizer_position_ids.add(id)
        else:
            raise logic-error
    collect_ids__alt_infos(map(snd, alt_id_info_pairs), write)
    all_used_ids = predicator_position_ids | recognizer_position_ids
    # right part ids should be known
    if not all_used_ids <= all_known_ids:
        unknown_ids = all_used_ids - all_known_ids
        raise ValueError('unknown ids: {!r}'.format(unknown_ids))
    #rint('here')
    #rint('char_RIGHT_PARENTHESIS' in all_used_ids)
    #rint('char_RIGHT_PARENTHESIS' in all_known_ids)

    # right part recognizer_id should not be predicator_id
    if not recognizer_position_ids.isdisjoint(all_known_predicator_only_ids):
        predicators_used_as_recognizer = \
            recognizer_position_ids & all_known_predicator_only_ids
        raise ValueError('use predicator_id as recognizer_id: {!r}'.format(
            predicators_used_as_recognizer))


    # verify_unsingleton
    for alt_id, alt_info in alt_id_info_pairs:
        if not verify_unsingleton(alt_info):
            raise ValueError('alt_id {!r}: cannot unsingleton : {!r}'
                .format(alt_id, alt_info))


    # construct compile_result
    d = defaultdict(OrderedDict)
    for alt_id, alt_info in alt_id_info_pairs:
        def_id = alt_id2def_id(alt_id)
        d[def_id][alt_id] = alt_info
    def_id2alt_id2alt_info = d
    result = dict(
        def_id2alt_id2alt_info = def_id2alt_id2alt_info
        , usr_predicator_ids = usr_predicator_ids
        , usr_token_set_ids = usr_token_set_ids
        , usr_nullable_recognizer_ids = usr_nullable_recognizer_ids
        , usr_nonnull_recognizer_ids = usr_nonnull_recognizer_ids
        , noise_nonnull_recognizer_ids = noise_nonnull_recognizer_ids
        )
    #return result




    # no-left-recur
    # treat @noise@ as a def_id!
    def_id_ex2itemss = {def_id :
        # itemss
        [sum_lists(items3s) for _, _, items3s in alt_id2alt_info.values()]
        for def_id, alt_id2alt_info in def_id2alt_id2alt_info.items()
        }
    def_id_ex2itemss['@noise@'] = [[id2item(id)] for id in noise_nonnull_recognizer_ids]
    def_id_ex2itemss['@noise@'].append([])
    def_id_exs = set(def_id_ex2itemss)
    assert len(def_id_exs) == len(def_ids) + 1
    def id2nullable(id, def_id2nullable):
        if id in def_id2nullable:
            return def_id2nullable[id]
        if id in all_known_nonnull_recognizer_ids:
            return False
        if id in usr_nullable_recognizer_ids:
            return True
        if id in __BuiltinNullableRecognizerIDs:
            return True
        if id in usr_predicator_ids:
            raise logic-error
        if id in __BuiltinPredicatorIDs:
            raise logic-error
        raise logic-error
    def item_nullable(item, def_id2nullable):
        L = len(item)
        if L == 2: return True
        if L != 3:
            print(item)
        may_skip, recognizer_item, may_lookahead = item
        if may_lookahead:
            return True
        id, may_multi_ex = recognizer_item
        id_nullable = id2nullable(id, def_id2nullable)
        if not may_multi_ex:
            return id_nullable
        may_sep_by, may_endID, multi = may_multi_ex
        m, M = multi

        def mayID2nullable(mayID):
            if mayID:
                nullable = id2nullable(mayID, def_id2nullable)
            else:
                nullable = True
            return nullable

        end_nullable = mayID2nullable(may_endID)

        if may_sep_by:
            _sep, (auto1, sepID, auto2) = may_sep_by
            sep_nullable = id2nullable(sepID, def_id2nullable)
        else:
            sep_nullable = True

        if M is None and id_nullable and sep_nullable:
            raise ValueError('"nullable[/nullable][$end]{_,}" is forbidden')

        if m == 0:
            return end_nullable
        if not id_nullable:
            return False
        if may_endID:
            return end_nullable and sep_nullable
        elif m == 1:
            return True
        else:
            return sep_nullable
        raise logic-error

    def item_heads__maynot_def_ids(item, def_id2nullable):
        L = len(item)
        if L == 2:
            _, id = item
            return [id]
        may_skip, recognizer_item, may_lookahead = item
        id, may_multi_ex = recognizer_item
        if not may_multi_ex:
            return [id]

        id_nullable = id2nullable(id, def_id2nullable)
        may_sep_by, may_endID, multi = may_multi_ex
        m, M = multi
        ls = []
        if M is None or M != 0:
            ls.append(id)

        def mayID2nullable(mayID):
            if mayID:
                nullable = id2nullable(mayID, def_id2nullable)
            else:
                nullable = True
            return nullable

        end_nullable = mayID2nullable(may_endID)

        if may_sep_by:
            _sep, (auto1, sepID, auto2) = may_sep_by
            sep_nullable = id2nullable(sepID, def_id2nullable)
        else:
            sep_nullable = True


        if may_endID:
            # (!e x s)* e
            if m == 0 or (id_nullable and sep_nullable):
                ls.append(may_endID)
        if may_sep_by and id_nullable:
            if M is None or M >= 2 or (M == 1 and may_endID):
                ls.append(sepID)
                if auto1 or (sep_nullable and auto2):
                    ls.append('@noise@')
        return ls
        raise logic-error
    def item_heads(item, def_id2nullable):
        heads = item_heads__maynot_def_ids(item, def_id2nullable)
        heads = set(heads)
        heads &= def_id_exs
        return list(heads)

    left_recur_def_id_exs, _def_id2nullable = left_recur_detect_ex(
        def_id_ex2itemss, item_nullable, item_heads)
    assert _def_id2nullable['@noise@']
    if left_recur_def_id_exs:
        raise ValueError('left_recur_def_id_exs: {!r}'.format(left_recur_def_id_exs))


    # all noises should be nonnull
    def_nonnull_recognizer_ids = {def_id
        for def_id, nullable in def_id_ex2itemss.items() if not nullable}
    assert '@noise@' not in def_nonnull_recognizer_ids
    all_known_nonnull_recognizer_ids_ver2 =\
        all_known_nonnull_recognizer_ids | def_nonnull_recognizer_ids
    if not noise_nonnull_recognizer_ids <= all_known_nonnull_recognizer_ids_ver2:
        raise ValueError('noise should be nonnull_recognizer: {!r}'.format(
            noise_nonnull_recognizer_ids - all_known_nonnull_recognizer_ids_ver2
            ))
    return result
end_of(compile_RecognizeSystemGrammar)
compile_result_RecognizeSystemGrammar =\
    compile_RecognizeSystemGrammar(parse_result)

#rint(compile_result)


#rint('\n'.join(globals().keys()))
