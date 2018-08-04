








__all__ = '''
    RecognizeSystemBase
    '''.split()











#import re
from abc import abstractmethod, ABCMeta
from itertools import compress
from .Lazy import Lazy
from .Utils import (end_of, betweenFromTo, iterFromTo, cached, list_map)
from .RecognizeSystemGrammar import (alt_id2def_id
    , is_tuple, is_bool, is_recognizer_item
    )


class RecognizeSystemBase(metaclass=ABCMeta):
    # st - immutable
    # recognize_result val = (val, st) | raise DeadErr && not raise AltErr
    # recognizer val = st -> recognize_result val
    # item_recognizer val = st -> (() | (st,) | recognize_result val)
    #                               () - predicator; (st,) - skipped
    # alt_id_recognizer 'alt_id' val = recognizer ('alt_id', val)



    # f :: () -> result
    # handler :: (exception) -> result'
    # otherwise :: (result) -> result'
    @abstractmethod
    def catchAltErr(self, f, handler, otherwise=None):pass
    @abstractmethod
    def catchDeadErr(self, f, handler, otherwise=None):pass
    @abstractmethod
    def catchBothErr(self, f, handler, otherwise=None):pass
    @abstractmethod
    def mkAltErr(self, st, name, *args, **kwargs):pass
    @abstractmethod
    def mkDeadErr(self, st, id, *args, **kwargs):pass
    def mkExpectedDeadErr(self, st, id, **kwargs):
        return self.mkDeadErr(st, id, 'expected', **kwargs)
    def mkUnexpectedDeadErr(self, st, id):
        return self.mkDeadErr(st, id, 'unexpected')
    def mkExpectedAltErr(self, st, id, **kwargs):
        return self.mkAltErr(st, id, 'expected', **kwargs)
    def mkUnexpectedAltErr(self, st, id):
        return self.mkAltErr(st, id, 'unexpected')
    def merge_AltErr_from_AltErrs(self, err, from_errs):
        return self._merge_Err_from_Errs(err, from_errs)
    def _merge_Err_from_Errs(self, err, from_errs):
        if from_errs:
            err.__cause__ = from_errs[-1]
        return err
    def _merge_Err_from_Err(self, err, from_err):
        err.__cause__ = from_err
        return err
    def merge_AltErr_from_BothErr(self, err, from_err):
        return self._merge_Err_from_Err(err, from_err)
    def merge_AltErr_from_AltErr(self, err, from_err):
        return self._merge_Err_from_Err(err, from_err)
    def merge_DeadErr_from_AltErr(self, err, from_err):
        return self._merge_Err_from_Err(err, from_err)
    def merge_AltErr_from_DeadErr(self, err, from_err):
        return self._merge_Err_from_Err(err, from_err)





    @abstractmethod
    def iter_noise_nonnull_recognizer_ids(self):
        # () -> [noise_nonnull_recognizer_id]
        raise NotImplementedError
    @abstractmethod
    def def_id2alt_ids(self, def_id):
        # def_id -> [alt_id]
        raise NotImplementedError
    @abstractmethod
    def alt_id2alt_info(self, alt_id):
        # alt_id -> (may_unbox_or_prime, unsingleton:bool, items before $$, items after $$)
        raise NotImplementedError



    @abstractmethod
    def isDefID(self, id):pass
    @abstractmethod
    def isUsrTokenSetID(self, id):pass
    @abstractmethod
    def isUsrPredicatorID(self, id):pass
    @abstractmethod
    def isUsrNullableRecognizerID(self, id):pass
    @abstractmethod
    def isUsrNonNullRecognizerID(self, id):pass
    @abstractmethod
    def isBuiltinTokenSetID(self, id):pass
    @abstractmethod
    def isBuiltinPredicatorID(self, id):pass
    @abstractmethod
    def isBuiltinNullableRecognizerID(self, id):pass
    @abstractmethod
    def isBuiltinNonNullRecognizerID(self, id):pass

    # usr_predicator_id -> (st -> (() | raise IDArr))
    @abstractmethod
    def usr_predicator_id2predicator(self, id):pass
    # usr_token_set_id -> (st -> ((token, st) | raise IDArr))
    @abstractmethod
    def usr_token_set_id2recognizer(self, id):pass
    # usr_recognizer_id -> (st -> ((val, st) | raise IDArr))
    @abstractmethod
    def usr_nullable_recognizer_id2recognizer(self, id):pass
    @abstractmethod
    def usr_nonnull_recognizer_id2recognizer(self, id):pass
    # def_id -> (v->v') where v = ('alt_id', val)
    @abstractmethod
    def def_id2result_translater(self, def_id):pass




    def __init__(self):
        # for cache
        self.__id2recognizer = {}
        self.__id2predicator = {}
        self.__id2indirect_recognizer = {}
        self.__id2indirect_predicator = {}

    # override RS_uncons/RS_check_st_type/RS_have_same_position/mkAltErr at same time
    @abstractmethod
    def RS_uncons(self, st):
        # st -> None | (token, st)
        pass
    @abstractmethod
    def RS_check_st_type(self, st):
        # st -> bool
        pass
    @abstractmethod
    def RS_have_same_position(self, st, ts):
        # (st, st') -> bool
        pass
    # st or self has a cache:
    #   (self,st)->{recognizer_item|predicator_id : (v,st')|bool|err|None|...}
    # (v,st') - recognizer_item result
    # () - predicator_id result
    #       ; recognizer_id should be wrapped as recognizer_item
    # err - AltErr/DeadErr
    # None - not cached yet
    # ... - computing; forbidden result dependent on itself
    def RS_query_st_cache_or_set_computing(
        self, st, recognizer_item_or_predicater_id):
        # -> (v,st') | () | err | None | ...
        # default no cache
        r = self._RS_query_st_cache(st, recognizer_item_or_predicater_id)
        if r is None:
            self._RS_store_st_cache(st, recognizer_item_or_predicater_id, ...)
        return r
    def _RS_query_st_cache(self, st, recognizer_item_or_predicater_id):
        return None
    def RS_store_st_cache(self, st, recognizer_item_or_predicater_id, result):
        # not allow override, except: None -> ... -> others
        # default no cache
        assert result is not None
        assert result is not ...
        r = self._RS_query_st_cache(st, recognizer_item_or_predicater_id)
        assert r is ... or r is None
        self._RS_store_st_cache(st, recognizer_item_or_predicater_id, result)
        r = self._RS_query_st_cache(st, recognizer_item_or_predicater_id)
        assert r is result or r is None
    def _RS_store_st_cache(self, st, recognizer_item_or_predicater_id, result):
        return None
    def RS_clear_st_cache(self, st):
        # default no cache
        return None





    def recognize_id(self, st, recognizer_id):
        return self.id2recognizer(recognizer_id)(st)
    def def_id2recognizer(self, def_id):
        # def_id -> recognizer val
        f = self.def_id2result_translater(def_id)
        def def_id_recognizer(st):
            #rint(def_id)
            assert self.RS_check_st_type(st)
            it = self.iter_alt_id_recognizers(def_id)
            r = None
            alt_errs = []
            handler = alt_errs.append
            for alt_id_recognizer in it:
                r = self.catchAltErr(
                    #bug: lambda: alt_id_recognizer(st), alt_id_recognizer)
                    lambda: alt_id_recognizer(st), handler)
                if r:
                    break
            else:
                ex = self.mkExpectedAltErr(st, def_id)
                raise self.merge_AltErr_from_AltErrs(ex, alt_errs)
            alt_result, ts = r
            def_result = f(alt_result)
            assert self.RS_check_st_type(ts)
            return def_result, ts
        return def_id_recognizer


    def iter_alt_id_recognizers(self, def_id):
        return map(self.alt_id2recognizer, self.def_id2alt_ids(def_id))
    def alt_id2recognizer(self, alt_id):
        may_unbox_or_prime, unsingleton, items3s =\
                            self.alt_id2alt_info(alt_id)
        items1_recognizer, items2_recognizer, items3_recognizer =\
                                    map(self.items2recognizer, items3s)
        if not may_unbox_or_prime:
            box = lambda r: (alt_id, r)
        elif may_unbox_or_prime == '&':
            def_id = self.alt_id2def_id(alt_id)
            box = lambda r: (def_id, r)
        elif may_unbox_or_prime == '*':
            box = lambda r: r
        else:
            raise ValueError
        def alt_id_recognizer(st):
            assert self.RS_check_st_type(st)
            def alt_err_handler(e):
                raise self.merge_DeadErr_from_AltErr(
                    self.mkExpectedDeadErr(st, alt_id), e)
            def dead_err_handler(e):
                raise self.merge_AltErr_from_DeadErr(
                    self.mkExpectedAltErr(st, alt_id), e)
            ts = st
            ls1, ts = self.catchDeadErr(lambda:items1_recognizer(ts)
                                    , dead_err_handler)
            assert self.RS_check_st_type(ts)
            ls2, ts = items2_recognizer(ts)
            assert self.RS_check_st_type(ts)
            ls3, ts = self.catchAltErr(lambda:items3_recognizer(ts)
                                    , alt_err_handler)
            r = ls1 + ls2 + ls3
            if unsingleton:
                [r] = r
            # bug: return (alt_id, r) # miss ",ts"
            r = box(r)
            return r, ts
        return alt_id_recognizer
    def alt_id2def_id(self, alt_id):
        return alt_id2def_id(alt_id) # alt_id.split('-')[0]
    def items2recognizer(self, items):
        item_recognizers = tuple(map(self.item2recognizer, items))
        def items_recognizer(st):
            ls = []
            assert self.RS_check_st_type(st)
            for item_recognizer in item_recognizers:
                r = item_recognizer(st)
                L = len(r)
                if L == 1:
                    # skip
                    [st] = r
                elif L == 0:
                    # predicator
                    pass
                else:
                    a, st = r
                    ls.append(a)
                assert self.RS_check_st_type(st)
            return tuple(ls), st
        return items_recognizer
    def mk_indirect_id_recognizer(self, id):
        return cached(self.__id2indirect_recognizer, id
            , lambda:self.__mk_indirect_id_recognizer_impl(id))
    def __mk_indirect_id_recognizer_impl(self, id):
        _id_recognizer = Lazy(lambda:self.id2recognizer(id))
        def id_recognizer(st):
            if not self.RS_check_st_type(st):
                print('##########')
                print(id)
                print(type(st))
                print(st)
                assert self.RS_check_st_type(ts)
            return _id_recognizer.v(st)
        return id_recognizer
    def mk_indirect_id_predicator(self, id):
        return cached(self.__id2indirect_predicator, id
            , lambda:self.__mk_indirect_id_predicator_impl(id))
    def __mk_indirect_id_predicator_impl(self, id):
        _id_predicator = Lazy(lambda:self.id2predicator(id))
        def id_predicator(st):
            return _id_predicator.v(st)
        return id_predicator
    def item2recognizer(self, item):
        case = item[0] # pass | '!' | '?' | '-' | ''
        '''
        if case == 'pass':
            _, = item
            item_recognizer = self.pass_predicator()
            return item_recognizer
        '''

        if case in '-':
            return self.__wrapped_recognizer_item2recognizer(item)
        elif case in '!?':
            return self.__predicator_item2recognizer(item)
        else:
            raise ValueError

    def __wrapped_recognizer_item2recognizer(self, item):
        may_skip, recognizer_item, may_lookahead = item
        id_recognizer = self.recognizer_item2recognizer(recognizer_item)
        if may_lookahead:
            id_recognizer = self.lookahead_item_recognizer(id_recognizer)
        if may_skip:
            item_recognizer = self.skip_item_recognizer(id_recognizer)
        else:
            item_recognizer = id_recognizer
        return item_recognizer
    def recognizer_item2recognizer(self, recognizer_item):
        id, may_multi_ex = recognizer_item
        id_recognizer = self.mk_indirect_id_recognizer(id)
        #log(id, id_recognizer)

        if not may_multi_ex:
            recognizer_item_recognizer = id_recognizer
            # cached by id2recognizer
        else:
            may_sep_by, may_endID, multi = may_multi_ex
            recognizer_item_recognizer = self.mkPrimeItemRecognizer(
                id, id_recognizer, may_sep_by, may_endID, multi)
            recognizer_item_recognizer =\
                self.cached_recognizer_item_recognizer(
                    recognizer_item, recognizer_item_recognizer)
        return recognizer_item_recognizer
    def __predicator_item2recognizer(self, predicator_item):
        case, id = predicator_item
        id_predicator = self.mk_indirect_id_predicator(id)
        if self.is_predicator_id(id):
            id_predicator = self.cached_predicator_item_predicator(
                id, id_predicator)
        f = self.not_id_predicator if case == '!' \
            else self.ask_id_predicator
        item_recognizer = f(id, id_predicator)
        return item_recognizer
    def cached_recognizer_item_recognizer(self, recognizer_item, id_recognizer):
        # -> item_recognizer
        assert is_recognizer_item(recognizer_item)
        def recognizer_item_recognizer(st):
            r = self.RS_query_st_cache_or_set_computing(st, recognizer_item)
            if r is None:
                def handler(e):
                    self.RS_store_st_cache(st, recognizer_item, e)
                    raise
                v, ts = self.catchBothErr(lambda:id_recognizer(st), handler)
                self.RS_store_st_cache(st, recognizer_item, (v,ts))
                return v, ts
            if is_tuple(r, 2):
                return r
            if isinstance(r, Exception):
                raise r
            if is_tuple(r, 0):
                # why predicator result?
                raise logic-error
            if r is ...:
                raise logic-error-left-recur
            raise logic-error
        return recognizer_item_recognizer
    def is_predicator_id(self, id):
        return self.isUsrPredicatorID(id) or self.isBuiltinPredicatorID(id)
    def cached_predicator_item_predicator(self, predicator_id, id_predicator):
        # -> predicator
        assert self.is_predicator_id(predicator_id)
        def predicator_item_predicator(st):
            r = self.RS_query_st_cache_or_set_computing(st, predicator_id)
            if r is None:
                def handler(e):
                    self.RS_store_st_cache(st, predicator_id, e)
                    raise
                r = self.catchBothErr(lambda:id_predicator(st), handler)
                assert r == ()
                self.RS_store_st_cache(st, predicator_id, r)
                return r
            if is_tuple(r, 0):
                return r
            if isinstance(r, Exception):
                raise r
            if is_tuple(r, 2):
                # why recognizer_item result?
                raise logic-error
            if r is ...:
                raise logic-error-left-recur
            raise logic-error
        return predicator_item_predicator
    def id2predicator(self, id):
        return cached(self.__id2predicator, id
            , lambda:self.__id2predicator_impl(id))
    def __id2predicator_impl(self, id):
        # id - predicator_id | recognizer_id
        if self.isUsrPredicatorID(id):
            return self.usr_predicator_id2predicator(id)
        if self.isBuiltinPredicatorID(id):
            return self.builtin_predicator_id2predicator(id)
        recognizer = self.id2recognizer(id)
        return self.recognizer2predicator(recognizer)
    def recognizer2predicator(self, recognizer):
        def predicator(st):
            recognizer(st)
            return ()
        return predicator
    def __id2recognizer_item(self, id):
        # id
        may_multi_ex = ()
        return id, may_multi_ex
    def id2recognizer(self, id):
        assert id != '@noise1@'
        return cached(self.__id2recognizer, id
            , lambda:
                self.cached_recognizer_item_recognizer(
                    self.__id2recognizer_item(id)
                    , self.__id2recognizer_impl(id)
                    )
            )
    def __id2recognizer_impl(self, id):
        # id - recognizer_id
        if self.isDefID(id):
            return self.def_id2recognizer(id)
        if self.isUsrTokenSetID(id):
            return self.usr_token_set_id2recognizer(id)
        if self.isUsrNullableRecognizerID(id):
            return self.usr_nullable_recognizer_id2recognizer(id)
        if self.isUsrNonNullRecognizerID(id):
            return self.usr_nonnull_recognizer_id2recognizer(id)
        if self.isBuiltinTokenSetID(id):
            return self.builtin_token_set_id2recognizer(id)
        if self.isBuiltinNullableRecognizerID(id):
            return self.builtin_nullable_recognizer_id2recognizer(id)
        if self.isBuiltinNonNullRecognizerID(id):
            return self.builtin_nonnull_recognizer_id2recognizer(id)
        # error
        print(id)
        if self.isUsrPredicatorID(id):
            raise logic-error
            # return self.usr_predicator_id2recognizer(id)
        if self.isBuiltinPredicatorID(id):
            raise logic-error
        print(id in self._RecognizeSystem__def_id2alt_id2alt_info.keys())
        print(self._RecognizeSystem__def_id2alt_id2alt_info.keys())
        raise logic-error
    def isBuiltinTokenSetID(self, id):
        return id in ('@any@', '@dead@')
    def isBuiltinPredicatorID(self, id):
        return id in ('@pass@',)
    def isBuiltinNullableRecognizerID(self, id):
        return id in ('@noise@',)
    def isBuiltinNonNullRecognizerID(self, id):
        return False
    def builtin_token_set_id2recognizer(self, builtin_id):
        if builtin_id == '@any@':
            return self.any_token_recognizer
        if builtin_id == '@dead@':
            return self.dead_token_recognizer
        raise logic-error
    def builtin_predicator_id2predicator(self, builtin_id):
        if builtin_id == '@pass@':
            return self.pass_predicator
        raise logic-error
    def builtin_nullable_recognizer_id2recognizer(self, builtin_id):
        if builtin_id == '@noise@':
            return self.noise_token_recognizer
        raise logic-error
    def builtin_nonnull_recognizer_id2recognizer(self, builtin_id):
        raise logic-error
    def token2bool2recognizer(self, token_set_name, token2bool):
        def token_recognizer(st):
            (_, ch), ts = self.any_token_recognizer(st)
            if not token2bool(ch):
                raise self.mkExpectedAltErr(st, token_set_name)
            return (token_set_name, ch), ts
        return token_recognizer
    def _zero_list_recognizer(self, st):
        return [], st
    def pass_predicator(self, st):
        id = '@pass@'
        return ()
    def dead_token_recognizer(self, st):
        id = '@dead@'
        raise self.mkExpectedAltErr(st, id)
    def any_token_recognizer(self, st):
        id = '@any@'
        r = self.RS_uncons(st)
        if r is None:
            raise self.mkExpectedAltErr(st, id)
        t, ts = r
        return (id, t), ts
        #################
        id = '@any@'
        def any_token_recognizer(st):
            r = self.RS_uncons(st)
            if r is None:
                raise self.mkExpectedAltErr(st, id)
            t, ts = r
            return (id, t), ts
        return any_token_recognizer
    @property
    def noise_token_recognizer(self):
        return self.mkManyRecognizer('@noise1@'
            , self.noise1_token_recognizer, 0, None)
    def try_id_recognizer(self, id, id_recognizer):
        # DeadErr -> AltErr
        def try_id_recognizer(st):
            def handler(e):
                raise self.merge_AltErr_from_DeadErr(
                                self.mkExpectedAltErr(st, id), e)
            return self.catchDeadErr(lambda:id_recognizer(st), handler)
        return try_id_recognizer
    @property
    def noise1_token_recognizer(self):
        f0 = self.id2recognizer
        f1 = lambda id: self.id_recognizer2avoid_empty(id, None, f0(id))
        f2 = lambda id: self.try_id_recognizer(id, f1(id))
        return self.mkChoiceRecognizer('@noise1@'
            , [(id, f2(id))
                for id in self.iter_noise_nonnull_recognizer_ids()
              ]
            )
    def lookahead_item_recognizer(self, id_recognizer):
        def lookahead_item_recognizer(st):
            v, _ = id_recognizer(st)
            return v, st
        return lookahead_item_recognizer
    def skip_item_recognizer(self, id_recognizer):
        def skip_item_recognizer(st):
            _, ts = id_recognizer(st)
            return (ts,)
        return skip_item_recognizer
    def ask_id_predicator(self, id, id_predicator_or_recognizer):
        def ask_id_predicator(st):
            def handler(e):
                raise self.merge_AltErr_from_BothErr(
                    self.mkExpectedAltErr(st, id), e)
            self.catchBothErr(lambda:id_predicator_or_recognizer(st), handler)
            return ()
        return ask_id_predicator
    def not_id_predicator(self, id, id_predicator_or_recognizer):
        def not_id_predicator(st):
            def else_(r):
                raise self.mkUnexpectedAltErr(st, id)
            return self.catchBothErr(
                lambda:id_predicator_or_recognizer(st), lambda e:(), else_)
        return not_id_predicator
    def multi2str(self, min, max):
        m, M = min, max
        #multi_str = '{{{},{}}}'.format(m, '' if M is None else M)
        if M is None:
            if m < 2:
                multi_str = '*+'[m]
            else:
                multi_str = '{{{},}}'.format(m)
        elif (m,M) == (0,1):
            multi_str = '?'
        else:
            multi_str = '{{{},{}}}'.format(m, M)
        return multi_str


    def mkPrimeItemRecognizer(
        self, id, id_recognizer, may_sep_by, may_endID, multi):
        # may_sep_by = () | ('/'|'//', sepID)
        # may_endID = '' | endID
        # multi = (min, max) = (uint, uint|None)
        m, M = multi
        multi_str = self.multi2str(m, M)
        name = '{}{}'.format(id, multi_str)
        mk = self.mk_indirect_id_recognizer
        if may_sep_by:
            sep, (auto1, sepID, auto2) = may_sep_by
            selectors = [auto1, sepID, auto2]
            assert sepID
            noiseID = '@noise@'
            recognizer_ids = [noiseID, sepID, noiseID]
            recognizer_ids = compress(recognizer_ids, selectors)
            id_recognizers = list_map(mk, recognizer_ids)
            seq_recognizer = self.mkSeqRecognizer(id_recognizers)
                    #zip(recognizer_ids, id_recognizers))
            sep_recognizer = seq_recognizer
            if sep == '/':
                mkSepBy = self.mkSepByRecognizer
                mkSepByEndBy = self.mkSepByEndByRecognizer
            elif sep == '//':
                mkSepBy = self.mkSepByRecognizer2
                mkSepByEndBy = self.mkSepByEndByRecognizer2
            else:
                raise logic-error
        if not may_endID:
            if not may_sep_by:
                return self.mkManyRecognizer(id, id_recognizer, m, M)
            return mkSepBy(id, id_recognizer, sepID, sep_recognizer, m, M)
        else:
            endID = may_endID
            end_recognizer = mk(endID)
            if not may_sep_by:
                return self.mkEndByRecognizer(
                    id, id_recognizer, endID, end_recognizer, m, M)
            return mkSepByEndBy(
                id, id_recognizer, sepID, sep_recognizer, endID, end_recognizer
                , m, M)
    def mkEndByRecognizer(
        self, id, id_recognizer, endID, end_recognizer, m, M):
        # x$e{m,M} = (!e x){m,M} -e
        not_end_predicator = self.not_id_predicator(endID, end_recognizer)
        def nongreedy_id_recognizer(st):
            not_end_predicator(st)
            return id_recognizer(st)
        many = self.mkManyRecognizer(id, nongreedy_id_recognizer, m, M)
        def endBy_recognizer(st):
            vs, st = many(st)
            _, st = end_recognizer(st)
            return vs, st
        return endBy_recognizer
    def mkSepByEndByRecognizer(self
        , id, id_recognizer, sepID, sep_recognizer, endID, end_recognizer
        , m, M):
        # x/s$e{m,M} = (!e x -s){m,M} -e = (x -s)$e{m,M}
        #not_end_predicator = self.not_id_predicator(endID, end_recognizer)
        def id_sep_recognizer(st):
            #not_end_predicator(st)
            v, st = id_recognizer(st)
            _, st = sep_recognizer(st)
            return v, st
        return self.mkEndByRecognizer(
            id, id_sep_recognizer, endID, end_recognizer, m, M)
        many_id_sep = self.mkManyRecognizer(id, id_sep_recognizer, m, M)
        def sepByEndBy_recognizer(st):
            vs, st = many_id_sep(st)
            _, st = end_recognizer(st)
            return vs, st
        return sepByEndBy_recognizer
    def mkSepByRecognizer2(
        self, id, id_recognizer, sepID, sep_recognizer, m, M):
        # x//s{m,M} = x/s{m,M} !s
        sepBy_recognizer = self.mkSepByRecognizer(
                    id, id_recognizer, sepID, sep_recognizer, m, M)
        not_sep_recognizer = self.not_id_predicator(sepID, sep_recognizer)
        def sepBy_recognizer2(st):
            v, ts = sepBy_recognizer(st)
            not_sep_predicator(ts)
            return v, ts
        return sepBy_recognizer2
    def mkSepByEndByRecognizer2(self
        , id, id_recognizer, sepID, sep_recognizer, endID, end_recognizer
        , m, M):
        # x//s$e{m,M} = x/s$e{m,M} !s
        sepByEndBy_recognizer = self.mkSepByEndByRecognizer(
            id, id_recognizer, sepID, sep_recognizer, endID, end_recognizer
            , m, M)
        not_sep_recognizer = self.not_id_predicator(sepID, sep_recognizer)
        def sepByEndBy_recognizer2(st):
            v, ts = sepByEndBy_recognizer(st)
            not_sep_predicator(ts)
            return v, ts
        return sepByEndBy_recognizer2

    def mkManyRecognizer(self, id, id_recognizer, m, M):
        '''\
if M is None, then id_recognizer should not be nullable
x{m,M} = x{m} x{0,M-m}
'''

        assert m >= 0
        assert M is None or m <= M
        id_recognizer = self.id_recognizer2avoid_empty(id, M, id_recognizer)
        catched_id_recognizer = self.catched_id_recognizer(id_recognizer)

        if M is None:
            def iterM():
                while True:
                    yield
        else:
            M_m = M - m
            def iterM():
                return range(M_m)

        def many_recognizer(st):
            ls = []
            for _ in range(m):
                a, st = id_recognizer(st)
                ls.append(a)
            for _ in iterM():
                r = catched_id_recognizer(st)
                L = len(r)
                if L == 1:break
                a, st = r
                ls.append(a)
            return ls, st
        return many_recognizer

    def mkSepByRecognizer(
        self, id, id_recognizer, sepID, sep_recognizer, m, M):
        '''\
x/s{0,0} = _zero_list_recognizer
x/s{0,M} = x/s{1,M} | pass
x/s{m,M} = x (-s x){m-1,M-1}
'''
        if m == 0:
            if M is not None and M == 0:
                return self._zero_list_recognizer
            recognizer1 = self.mkSepByRecognizer(
                id, id_recognizer, sepID, sep_recognizer, 1, M)
            def sepBy_recognizer(st):
                def handler(e):
                    return [], st
                return self.catchAltErr(lambda:recognizer1(st), handler)
        else:
            def sep_id_recognizer(st):
                _, st = sep_recognizer(st)
                return id_recognizer(st)
            m = m-1
            M = None if M is None else M-1
            many_sep_id = self.mkManyRecognizer(id, sep_id_recognizer, m, M)
            def sepBy_recognizer(st):
                a, st = id_recognizer(st)
                ls, st = many_sep_id(st)
                ls.insert(0, a)
                return ls, st
        return sepBy_recognizer



    def id_recognizer2avoid_empty(self, id, M, id_recognizer):
        # when M is None, id_recognizer should raise ValueError if consume no tokens
        if M is not None:
            return id_recognizer
        def recognizer(st):
            a, ts = id_recognizer(st)
            if self.RS_have_same_position(st, ts):
                print(st)
                print(ts)
                pos1 = st.tell()
                pos2 = ts.tell()
                print(pos1, pos2)
                raise ValueError('nullable id -> id* : {!r}'.format(id))
            return a, ts
            pos1 = st.tell()
            pos2 = ts.tell()
            if pos1 == pos2:
                print(st, pos1)
                array, pos = st.get_args()
                tokens, begin, end = array.get_args()
                #rint(tokens[:pos])
                #rint(tokens[pos:])
                raise ValueError('{!r}: pos1 == pos2'.format(id))
            return a, ts
        return recognizer


    def catched_id_recognizer(self, id_recognizer):
        # (st->(a, st)) -> (st->(e,)|(a,st))
        h = lambda e: (e,)
        def catched_recognizer(st):
            return self.catchAltErr(lambda:id_recognizer(st), h)
        return catched_recognizer

    def mkChoiceRecognizer(self, name, id_recognizer_pairs):
        pairs = list_map(tuple, id_recognizer_pairs)
        def choice_recognizer(st):
            alt_errs = []
            def handler(e):
                alt_err = self.mkExpectedAltErr(st, '{}-{}'.format(name, id))
                alt_err = self.merge_AltErr_from_AltErr(alt_err, e)
                alt_errs.append(alt_err)
                return None
            for id, id_recognizer in pairs:
                r = self.catchAltErr(lambda:id_recognizer(st), handler)
                if r is not None:
                    return r
            id_err = self.mkExpectedAltErr(st, name)
            id_err = self.merge_AltErr_from_AltErrs(id_err, alt_errs)
            raise id_err
        return choice_recognizer
    def mkSeqRecognizer(self, id_recognizers):
        id_recognizers = tuple(id_recognizers)
        def seq_recognizer(st):
            ls = []
            for id_recognizer in id_recognizers:
                a, st = id_recognizer(st)
                ls.append(a)
            return tuple(ls), st
        return seq_recognizer
end_of(RecognizeSystemBase)

