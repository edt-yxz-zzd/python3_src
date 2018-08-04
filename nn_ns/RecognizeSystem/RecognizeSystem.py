

r'''

target:
    to parse new grammar
    when we try to define a grammar/language,
        it is likely that we would change the grammar/language frequently.
        RecognizeSystem is here to aid tokenization and parse.
        be grammar/language stable, we switch to use formal tools.

steps for user:
    # example: UntypedLambdaGrammar.py
    1) grammarXXX = write a RS grammar
        # see RecognizeSystemGrammar.py for syntax
    2) compile_resultXXX = compileRecognizeSystemGrammar__str(grammarXXX)
    3) class XXX(RecognizeSystem):
        # MUST
        def RS_T_{usr_token_set_id}(self, token) -> bool:
        def RS_P_{usr_predicator_id}(self, st) -> bool:
        def RS_NR_{usr_nullable_recognizer_id}{self, st) -> None|(val, st'):
        def RS_NNR_{usr_nonnull_recognizer_id}{self, st) -> None|(val, st'):
        # MAY_BE
        def RS_Alt2Def_{def_id}(self, alt_val) -> def_val:
        def RS_uncons(self, st)->None|(token, st'):
        def RS_check_st_type(self, st)->bool:
        def RS_have_same_position(self, st, st')->bool:
        # to act as PEG # the cache depents on (self,st), can be anywhere
        def _RS_query_st_cache(self, st, recognizer_item_or_predicater_id):
        def _RS_store_st_cache(self, st, recognizer_item_or_predicater_id, result):
        def RS_clear_st_cache(self, st):
    4) compilerXXX = XXX(**compile_resultXXX)
    5) result, remain_stream = compilerXXX.id2recognizer(start_symbolXXX)(st)
    NOTE:
        0) st is token_streamXXX
        1) stream:
            user can override RS_uncons/RS_check_st_type/RS_have_same_position/mkAltErr/catchAltErr/mkDeadErr/catchDeadErr
                default stream is a Stream_Ops
                a concrete Stream_Ops is ArrayStream
                    ArrayStream(OffsetedArray(tokens))
        2) if want remain_stream be empty:
            *new_start_symbolXXX =* old_start_symbolXXX !@any@
            # now remain_stream should be empty, and we can ignore it
        3) if token is char, then use RecognizeSystem__TokenIsChar
            which offer many char_sets
        4) PEG: there are CachedStream and CachedRecognizeSystem

bug:
    cache[(id(self), id(st))][st.tell()][recognizer_item|predicator_id]
'''













__all__ = '''
    RecognizeSystemBase
    RecognizeSystem
    ICachedStream
    CachedStream
    CachedRecognizeSystem
    '''.split()
'''

        nullable_recognizer may consumed no tokens.
            (always success?) not always
            EOF = !@any@
        nonnull_recognizer should consumed tokens.
            to prevent left_recur
TODO:
    string_named_nullable_...  # '{py_re}...'
    string_named_nonnull_...
    string_named_token_set
        then usr can op on strings directly

    type decl
        DefID/usrID :: Type
        AltID/DefID'-' :: Type # ('alt_id', Type)
        Type = DefID | Type '|' Type | [Type] | '(' Type//','* ')' | ConstantStr | String | ...
PEG/attribute grammar/tokenizer

'''











from abc import abstractmethod, ABCMeta
from collections import defaultdict, OrderedDict
from .Stream_Ops import ArrayStream, Stream_Ops, OffsetedArray
from .Utils import (end_of, id_map
    , drop_prefix, are_disjoint_sets, catch, mkErr
    )
from .RecognizeSystemBase import RecognizeSystemBase





if 0:
    id_recognizer_addr2name = {}
    def log(name, id_recognizer):
        id_recognizer_addr2name[id(id_recognizer)] = name
    def show_id_recognizer(id_recognizer):
        print('show_id_recognizer')
        name = id_recognizer_addr2name[id(id_recognizer)]
        print(name)
else:
    def show_id_recognizer(id_recognizer):pass
    def log(name, id_recognizer):pass



################


class RecognizeSystem(RecognizeSystemBase):
    class BothErr(Exception):
        def __init__(self, RS, st, name, *args, pos):
            super().__init__(RS, st, name, *args)
            self.pos = pos
            self.name = (name, pos, *args)
            self.names = (name, [])
            self.max_pos = pos
            self.max_pos_errs = [self]
        @property
        def max_pos_err(self):
            r = self.__max_pos_err
            if r is None:
                return self
            return r
        def merge(self, other):
            #rint('self:{:X}, other:{:X}'.format(id(self), id(other)))
            if 0:
                if self.max_pos == 3 and other.max_pos == 45:
                    import traceback
                    traceback.print_exception(type(self), self, None)
                    traceback.print_exception(type(other), other, None)
                    raise logic-error
            if self.max_pos < other.max_pos:
                self.max_pos = other.max_pos
                self.max_pos_errs = other.max_pos_errs
                self.names = (self.name, [other.names])
            elif self.max_pos == other.max_pos:
                self.max_pos_errs.extend(other.max_pos_errs)
                self.names[1].append(other.names)
        def merges(self, others):
            #rint('self', self.max_pos)
            for other in others:
                #rint('other', other.max_pos)
                self.merge(other)
        def _str_(self):
            return str(self.name) # super().__str__()
        def __str__(self):
            s = '\n\t'.join(e._str_() for e in self.max_pos_errs)
            return '{}: {}\n\t@max_pos[{}]\n\t@stack[{}]\n\t{}'.format(
                type(self).__name__, self._str_()
                #super().__str__()
                , self.max_pos, self.names, s)
    class AltErr(BothErr):pass
    class DeadErr(BothErr):pass
    def catchBothErr(self, f, handler, otherwise=None):
        return catch(self.BothErr, f, handler, otherwise=otherwise)
    def catchDeadErr(self, f, handler, otherwise=None):
        return catch(self.DeadErr, f, handler, otherwise=otherwise)
    def catchAltErr(self, f, handler, otherwise=None):
        return catch(self.AltErr, f, handler, otherwise=otherwise)
    def mkDeadErr(self, st, id, *args, **kwargs):
        return mkErr(self.DeadErr, self, st, id
            , pos=st.tell(), *args, **kwargs)
    def mkAltErr(self, st, alt_id, *args, **kwargs):
        return mkErr(self.AltErr, self, st, alt_id
            , pos=st.tell(), *args, **kwargs)
    def _merge_Err_from_Errs(self, err, from_errs):
        len(from_errs)
        max_pos = max(err.max_pos, 0, *[e.max_pos for e in from_errs])
        err.merges(from_errs)
        assert err.max_pos == max_pos
        return err
    def _merge_Err_from_Err(self, err, from_err):
        #err.__cause__ = from_err
        max_pos = max(err.max_pos, from_err.max_pos)
        err.merge(from_err)
        assert err.max_pos == max_pos
        return err




    def RS_uncons(self, st):
        # st -> None | (token, st)
        assert self.RS_check_st_type(st)
        #return st.uncons()
        r = st.uncons()
        if r is not None:
            a, ts = r
            assert st.tell() < ts.tell()
        return r
    def RS_check_st_type(self, st):
        # st -> bool
        return isinstance(st, Stream_Ops)
    def RS_have_same_position(self, st, ts):
        # (st, st') -> bool
        return st.tell() == ts.tell()





    fmt_UsrPredicatorID2st2bool = 'RS_P_{usr_predicator_id}'
    fmt_UsrTokenSetID2token2bool = 'RS_T_{usr_token_set_id}'
    fmt_UsrNullableRecognizerID2st2may_val_st = 'RS_NR_{usr_nullable_recognizer_id}'
    fmt_UsrNonNullRecognizerID2st2may_val_st = 'RS_NNR_{usr_nonnull_recognizer_id}'
    prefix_DefID2alt_result2final_result = 'RS_Alt2Def_'


    @property
    def fmt_DefID2alt_result2final_result(self):
        return self.prefix_DefID2alt_result2final_result + '{def_id}'
    def attr_DefID2alt_result2final_result2may_def_id(self, attr):
        prefix = self.prefix_DefID2alt_result2final_result
        may_def_id = drop_prefix(attr, prefix)
        assert may_def_id is None or attr.endswith(may_def_id)
        return may_def_id

    def isDefID(self, id):
        return id in self.__def_id2alt_id2alt_info
    def isUsrTokenSetID(self, id):
        return id in self.__usr_token_set_ids
    def isUsrPredicatorID(self, id):
        return id in self.__usr_predicator_ids
    def isUsrNullableRecognizerID(self, id):
        return id in self.__usr_nullable_recognizer_ids
    def isUsrNonNullRecognizerID(self, id):
        return id in self.__usr_nonnull_recognizer_ids
    def usr_predicator_id2predicator(self, id):
        attr = self.fmt_UsrPredicatorID2st2bool.format(usr_predicator_id=id)
        st2bool = getattr(self, attr)
        def predicator(st):
            if st2bool(st):
                return ()
            raise self.mkExpectedAltErr(st, id)
        return predicator
    def usr_token_set_id2recognizer(self, id):
        attr = self.fmt_UsrTokenSetID2token2bool.format(usr_token_set_id=id)
        token2bool = getattr(self, attr)
        def recognizer(st):
            (_any_, t), ts = self.any_token_recognizer(st)
            if token2bool(t):
                return t, ts
            raise self.mkExpectedAltErr(st, id)
        return recognizer

    def usr_nonnull_recognizer_id2recognizer(self, id):
        attr = self.fmt_UsrNonNullRecognizerID2st2may_val_st.format(usr_nonnull_recognizer_id=id)
        st2may_v_st = getattr(self, attr)
        def recognizer(st):
            r = st2may_v_st(st)
            if r is None:
                raise self.mkExpectedAltErr(id)
            v, ts = r
            if self.RS_have_same_position(st, ts):
                raise ValueError('not nonnull_recognizer: {!r}'.format(id))
            return v, ts
        return recognizer
    def usr_nullable_recognizer_id2recognizer(self, id):
        attr = self.fmt_UsrNullableRecognizerID2st2may_val_st.format(usr_nullable_recognizer_id=id)
        st2may_v_st = getattr(self, attr)
        def recognizer(st):
            r = st2may_v_st(st)
            if r is None:
                raise self.mkExpectedAltErr(id)
            v, st = r
            return v, st
        return recognizer

    def def_id2result_translater(self, def_id):
        attr = self.fmt_DefID2alt_result2final_result.format(def_id=def_id)
        return getattr(self, attr, id_map)

    def __init__(self
        , def_id2alt_id2alt_info
        , usr_token_set_ids
        , usr_predicator_ids
        , usr_nullable_recognizer_ids
        , usr_nonnull_recognizer_ids
        , noise_nonnull_recognizer_ids
        ):
        # let Map k v = OrderedDict k v or [(k,v)]
        # def_id2alt_id2alt_info :: Map def_id (Map alt_id alt_info)
        # alt_info = (may_unbox_or_prime, unsingleton:bool, [item], [item])
        # item = ( '' | '-'
        #        , recognizer_item
        #        , '' | '&'
        #        )
        #      | ( '!', predicator_id)
        #      | ( '?', predicator_id)
        # recognizer_item = # see RecognizeSystemGrammar.py
        #
        # usr_token_set_ids :: [token_set_id]
        # usr_predicator_ids :: [predicator_id]
        # usr_nullable_recognizer_ids :: [recognizer_id]
        # usr_nonnull_recognizer_ids :: [recognizer_id]
        # noise_nonnull_recognizer_ids :: [recognizer_id]
        super().__init__()

        d = OrderedDict(def_id2alt_id2alt_info)
        d = OrderedDict((k, OrderedDict(v)) for k,v in d.items())
        self.__def_id2alt_id2alt_info = d

        ls = [usr_token_set_ids, usr_predicator_ids
            , usr_nullable_recognizer_ids, usr_nonnull_recognizer_ids]
            #, noise_nonnull_recognizer_ids]
        ls = list(map(frozenset, ls))
        assert are_disjoint_sets(ls)
        [usr_token_set_ids, usr_predicator_ids
            , usr_nullable_recognizer_ids, usr_nonnull_recognizer_ids
            ] = ls #, noise_nonnull_recognizer_ids] = ls
        noise_nonnull_recognizer_ids =\
            frozenset(noise_nonnull_recognizer_ids)

        self.__usr_token_set_ids = usr_token_set_ids
        self.__usr_predicator_ids = usr_predicator_ids
        self.__usr_nullable_recognizer_ids = usr_nullable_recognizer_ids
        self.__usr_nonnull_recognizer_ids = usr_nonnull_recognizer_ids
        self.__noise_nonnull_recognizer_ids = noise_nonnull_recognizer_ids

    def iter_noise_nonnull_recognizer_ids(self):
        return iter(self.__noise_nonnull_recognizer_ids)
    def def_id2alt_ids(self, def_id):
        # def_id -> [alt_id]
        return self.__def_id2alt_id2alt_info[def_id].keys()
    def alt_id2alt_info(self, alt_id):
        # alt_id -> (may_unbox_or_prime:[012], unsingleton:bool, items before $$, items after $$)
        def_id = self.alt_id2def_id(alt_id)
        return self.__def_id2alt_id2alt_info[def_id][alt_id]


'''
    def __getattr__(self, attr):
        may_def_id = self.attr_DefID2alt_result2final_result2may_def_id(attr)
        if may_def_id is not None:
            if self.isDefID(may_def_id):
                def_id = may_def_id
                return id_map
        raise AttributeError(attr)

        return __class__.__mro__[1].__getattr__(self, attr)
        print(__class__.__mro__)
        print(super(__class__, self).__class__)
        return super(__class__, self).__getattr__(attr)
'''
end_of(RecognizeSystem)
###########################






class ICachedStream(Stream_Ops):
    @property
    @abstractmethod
    def cache(self):
        pass
class CachedStream(ICachedStream):
    def __init__(self, st, *, cache=None):
        assert isinstance(st, Stream_Ops)
        self.__st = st
        if cache is None:
            cache = {}
        self.__cache = cache
    @property
    def cache(self):
        return self.__cache
    @classmethod
    def mkCachedStream(cls, st, cache):
        return cls(st, cache=cache)
    def uncons(self):
        r = self.__st.uncons()
        if r is None:
            return r
        a, ts = r
        return a, self.mkCachedStream(ts, self.cache)
    def tell(self):
        return self.__st.tell()
    def seek(self, pos):
        ts = self.__st.seek(pos)
        return self.mkCachedStream(ts, self.cache)


class CachedRecognizeSystem(RecognizeSystem):
    def RS_check_st_type(self, st):
        return isinstance(st, ICachedStream)
    def _RS_query_st_cache(self, st, recognizer_item_or_predicater_id):
        d = st.cache.get(st.tell())
        if d is None: return None
        return d.get(recognizer_item_or_predicater_id)
    def _RS_store_st_cache(self, st, recognizer_item_or_predicater_id, result):
        pos = st.tell()
        d = st.cache.get(pos)
        if d is None:
            d = st.cache[pos] = {}
        d[recognizer_item_or_predicater_id] = result
    def RS_clear_st_cache(self, st):
        st.cache.clear()
end_of(CachedRecognizeSystem)

















