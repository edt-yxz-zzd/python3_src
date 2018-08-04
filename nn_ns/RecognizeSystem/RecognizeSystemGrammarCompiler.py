


__all__ = '''
    RecognizeSystemBase
    RecognizeSystem
    RecognizeSystemGrammarCompiler
    compileRecognizeSystemGrammar__str
    '''.split()





from .Stream_Ops import ArrayStream, Stream_Ops, OffsetedArray
from .Utils import (end_of
    , even_lines_of_paired_words_to_odict
    , drop_prefix
    , list_join, list_split__by_is
    )
from .RecognizeSystemGrammar import (
    compile_result_RecognizeSystemGrammar
    , compile_RecognizeSystemGrammar
    , tokenize_RecognizeSystemGrammar
    )
from .RecognizeSystemBase import RecognizeSystemBase
from .RecognizeSystem import RecognizeSystem






class RecognizeSystemGrammarCompiler(RecognizeSystem):
    # token2bool
    def RS_T_char_0(self, t):
        case, val = t
        return case == 'digit' and val == '0'
    def RS_T_char_x(self, t):
        case, val = t
        return case == 'word_char' and val == 'x'
    def RS_T_xdigit(self, t):
        case, val = t
        if case == 'digit':
            return True
        if case != 'word_char':
            return False
        return 'a' <= val <= 'f' or 'A' <= val <= 'F'
    def RS_T_digit(self, t):
        case, val = t
        return case == 'digit'
    def RS_T_id_char(self, t):
        case, val = t
        return case in ('digit', 'word_char')
    def RS_T_alnum_char(self, t):
        case, val = t
        return self.RS_T_id_char(t) and val != '_'
    def RS_T_spaceNotNewline(self, t):
        case, val = t
        return case == 'space1s'
    def RS_T_charNotNewline(self, t):
        return False
    def RS_T_sharp(self, t):
        case, val = t
        return case == 'comment'
    def RS_T_newline(self, t):
        case, val = t
        return case == 'newline'
    def mk_RS_T_op(self, op):
        def RS_T_op(t):
            case, val = t
            return case == 'op' and val == op
        return RS_T_op
    def mk_RS_T_kw(self, kw):
        def RS_T_kw(t):
            case, val = t
            return case == 'keyword' and val == kw
        return RS_T_kw
    name2op = even_lines_of_paired_words_to_odict('''\
unbox prime deli  eq  eq_star  ss
*     &     -     =   =*       $$
open_of_multi comma_of_multi close_of_multi lookahead no_auto_noise
{             ,              }              &         ~
eqeq    open_of_ss  close_of_ss ss1
==      $[          ]$          $$/
skip  sep1  sep2  end  star  cross  optional  not  ask 
-     /     //    $    *     +      ?         !    ?\
''')
    name2kw = even_lines_of_paired_words_to_odict('''\
kw_token_set kw_predicator kw_nullable_recognizer kw_nonnull_recognizer
@token_set@  @predicator@  @nullable_recognizer@  @nonnull_recognizer@
kw_turnoff_noise__begin kw_turnoff_noise__end
@turnoff_noise__begin@  @turnoff_noise__end@
kw_noise kw_dead
@noise@  @dead@
kw_pass kw_any
@pass@  @any@\
''')


    def __getattr__(self, attr):
        suffix = drop_prefix(attr, 'RS_T_')
        if suffix is not None:
            op = self.name2op.get(suffix)
            if op is not None:
                return self.mk_RS_T_op(op)
            kw = self.name2kw.get(suffix)
            if kw is not None:
                return self.mk_RS_T_kw(kw)
        return getattr(super(), attr)
        return super().__getattr__(attr)




    def main_recognize_result2parse_result(self, alt_val):
        alt_case, rules = alt_val
        assert alt_case == 'RecognizeSystemGrammar'
        alt_id_info_pairs = []
        alias_list = []
        usr_token_set_ids = []
        usr_predicator_ids = []
        usr_nullable_recognizer_ids = []
        usr_nonnull_recognizer_ids = []
        noise_nonnull_recognizer_ids = []
        #rint(alt_val)
        for rule_case, rule in rules:
            if rule_case == 'Rule-Define':
                alt_id, alt_info = rule
                alt_id_info_pairs.append((alt_id, alt_info))
            elif rule_case == 'Rule-TokenSet':
                usr_token_set_ids.extend(rule)
            elif rule_case == 'Rule-Predicator':
                usr_predicator_ids.extend(rule)
            elif rule_case == 'Rule-NullableRecognizer':
                usr_nullable_recognizer_ids.extend(rule)
            elif rule_case == 'Rule-NonNullRecognizer':
                usr_nonnull_recognizer_ids.extend(rule)
            elif rule_case == 'Rule-Noise':
                noise_nonnull_recognizer_ids.extend(rule)
            elif rule_case == 'Rule-Alias':
                alias_list.append(rule)
            else:
                raise logic-error
        parse_result = dict(
            alt_id_info_pairs = alt_id_info_pairs
            , alias_list = alias_list
            , usr_token_set_ids = usr_token_set_ids
            , usr_predicator_ids = usr_predicator_ids
            , usr_nullable_recognizer_ids = usr_nullable_recognizer_ids
            , usr_nonnull_recognizer_ids = usr_nonnull_recognizer_ids
            , noise_nonnull_recognizer_ids = noise_nonnull_recognizer_ids
            )
        return parse_result
    def main_recognize_result2compile_result(self, alt_val):
        parse_result = self.main_recognize_result2parse_result(alt_val)
        compile_result = compile_RecognizeSystemGrammar(parse_result)
        return compile_result

    ########################
    def RS_Alt2Def_Rule(self, alt_val):
        rule_case, rule = alt_val
        if rule_case == 'Rule-Define':
            may_unbox_or_prime, alt_id, unsingleton, items3s = rule
            assert type(unsingleton) is bool
            alt_info = may_unbox_or_prime, unsingleton, items3s
            return (rule_case, (alt_id, alt_info))
        return alt_val
    def RS_Alt2Def_MayOp_Alt_ID(self, alt_val):
        alt_case, _ = alt_val
        d = {'MayOp_Alt_ID-unbox':'*', 'MayOp_Alt_ID-prime':'&', 'MayOp_Alt_ID-empty':''}
        return d[alt_case]

    def RS_Alt2Def_Alt_ID(self, alt_val):
        alt_case, (def_id, may_suffix) = alt_val
        if may_suffix:
            [suffix] = may_suffix
            alt_id = '{}-{}'.format(def_id, suffix)
        else:
            alt_id = def_id
        return alt_id


    def char_tokens2str(self, char_tokens):
        return ''.join(char for _case, char in char_tokens)
    def RS_Alt2Def_IDBase(self, tokens):
        return self.char_tokens2str(tokens)
    def RS_Alt2Def_Suffix(self, tokens):
        return self.char_tokens2str(tokens)


    def RS_Alt2Def_Eq(self, alt_val):
        alt_case, _ = alt_val
        return {'Eq-Normal':False, 'Eq-Unsingleton':True}[alt_case]


    '''
    def auto_items2items(self, auto_items):
        ls = []
        noiseID = '@noise@'
        for auto, item in auto_items:
            if auto:
                ls.append(noiseID)
            ls.append(item)
        return ls
    '''
    def RS_Alt2Def_ListInserted(self, v):
        auto_itemss = v
        auto_items = list_join([...], auto_itemss)
        prev_one_is_item = False
        noise = ('-', ('@noise@', ()), '')
        items = []
        for auto_item in auto_items:
            if auto_item is ...:
                items.append(...)
            elif auto_item:
                # is_item
                item = auto_item
                if prev_one_is_item:
                    items.append(noise)
                items.append(item)
                prev_one_is_item = True
            else:
                try:
                    assert auto_item == ()
                except:
                    print(auto_item)
                    raise
                # not item
                # "~"
                prev_one_is_item = False
        itemss = list_split__by_is(items, ...)
        assert len(itemss) == len(auto_itemss)
        return tuple(itemss)


    def RS_Alt2Def_PredOp(self, alt_val):
        alt_case, _ = alt_val
        return {'PredOp-not':'!', 'PredOp-ask':'?'}[alt_case]
    def RS_Alt2Def_MaySkip(self, alt_val):
        alt_case, _ = alt_val
        return {'MaySkip-True':'-', 'MaySkip-False':''}[alt_case]
    def RS_Alt2Def_MayLookAhead(self, alt_val):
        alt_case, _ = alt_val
        return {'MayLookAhead-True':'&', 'MayLookAhead-False':''}[alt_case]
    def RS_Alt2Def_MaySepBy(self, alt_val):
        alt_case, v = alt_val
        if alt_case == 'MaySepBy-None':
            return ('/', (False, '@noise@', False))
        elif alt_case == 'MaySepBy-sep':
            sep, may_sepID_ex = v
            if not may_sepID_ex:
                return ()
            sepID_ex = may_sepID_ex
            return sep, sepID_ex
        raise logic-error
    def RS_Alt2Def_StrictAutoNoise(self, no_auto):
        return bool(not no_auto)
    def RS_Alt2Def_Sep(self, alt_val):
        alt_case, _ = alt_val
        return {'Sep-1':'/', 'Sep-2':'//'}[alt_case]
    def RS_Alt2Def_MayEndBy(self, v):
        if not v: v = ''
        return v
    def RS_Alt2Def_Multi(self, alt_val):
        alt_case, v = alt_val
        return {'Multi-star':(0,None), 'Multi-cross':(1,None), 'Multi-optional':(0,1), 'Multi-minmax':v}[alt_case]
    def RS_Alt2Def_MayMax(self, v):
        if not v:
            v = None
        else:
            [v] = v
        return v
    def RS_Alt2Def_UIntDec(self, tokens):
        s = self.char_tokens2str(tokens)
        return int(s)
    def RS_Alt2Def_UIntHex(self, tokens):
        s = self.char_tokens2str(tokens)
        return int(s, 16)

# BuiltinTokenSetID = (_, id) -> id
# BuiltinPredicatorID = (_, id) -> id
# BuiltinNullableRecognizerID = (_, id) -> id
    def RS_Alt2Def_BuiltinTokenSetID(self, kw_token):
        return self.kw_token2val(kw_token)
    def RS_Alt2Def_BuiltinPredicatorID(self, kw_token):
        return self.kw_token2val(kw_token)
    def RS_Alt2Def_BuiltinNullableRecognizerID(self, kw_token):
        return self.kw_token2val(kw_token)
    def kw_token2val(self, kw_token):
        _case, id = kw_token
        return id





    ######### TurnOffNoise
    '''
    def RS_Alt2Def_ LogicalBlock(self, alt_val):
        alt_case, v = alt_val
    '''
    def RS_Alt2Def_TurnOffNoise_Rule(self, alt_val):
        alt_case, v = alt_val
        alt_case = 'Rule-Define'
        alt_val = alt_case, v
        return self.RS_Alt2Def_Rule(alt_val)
    def RS_Alt2Def_TurnOffNoise_MaySepBy(self, alt_val):
        alt_case, v = alt_val
        if alt_case == 'TurnOffNoise_MaySepBy-sep':
            sep, id = v
            return (sep, (False, id, False))
        elif alt_case == 'TurnOffNoise_MaySepBy-None':
            return ()
        raise logic-error

end_of(RecognizeSystemGrammarCompiler)







compilerRecognizeSystemGrammar = \
    RecognizeSystemGrammarCompiler(**compile_result_RecognizeSystemGrammar)
def compileRecognizeSystemGrammar__str(grammar:str):
    compiler = compilerRecognizeSystemGrammar
    tokens = tokenize_RecognizeSystemGrammar(grammar)
    st = ArrayStream(OffsetedArray(tokens))
    main_recognizer = compiler.id2recognizer('RecognizeSystemGrammar')
    def handler(e):
        pos = e.max_pos
        print('\n'*3)
        print(tokens[:pos])
        print('\n')
        print(tokens[pos:])
        print('\n'*3)
        raise
    recognizer_result, _empty_st = compiler.catchBothErr(
        lambda:main_recognizer(st), handler)
    compile_result = compiler.main_recognize_result2compile_result(recognizer_result)
    return compile_result


def test():
    from .RecognizeSystemGrammar import (
        compile_result_RecognizeSystemGrammar
        , tokenize_RecognizeSystemGrammar, recognize_system_grammar \
        , )

    rs = RecognizeSystemGrammarCompiler(**compile_result_RecognizeSystemGrammar)
    tokens = tokenize_RecognizeSystemGrammar(recognize_system_grammar)
    st = ArrayStream(OffsetedArray(tokens))
    from pprint import pprint
    #pprint(tokens)
    if 0:
        st = ArrayStream(OffsetedArray([('digit', '0')]))
        id_char = rs.id2recognizer('id_char')
        v, st = id_char(st)
        print(v, st.uncons())
        return
    main = rs.id2recognizer('RecognizeSystemGrammar')
    v, st = main(st)
    pprint(v)

def test():
    from pprint import pprint
    from .RecognizeSystemGrammar import recognize_system_grammar
    v = compileRecognizeSystemGrammar__str(recognize_system_grammar)
    pprint(v)

if __name__ == '__main__':
    test()



#rint_lines(globals())

