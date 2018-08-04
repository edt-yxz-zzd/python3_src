
from Case import Ignore, IgnoredCaseID
from sand import match_case, do_assign, lh_star_star,\
     LeftHandConstValue, LHID_RHFilter
class XXXX:
    ids = {'minmax', 'regex', 'syms', 'item', 'token', 'null', 'group', 'symbol', '_and', '_or', 'count', '_not', 'name', 'atom', 'symbol_not', 'items', 'repeat', 'any', 'concat', 'refID'}
    id2subcases = {'count': ['repeat', 'minmax'], 'regex': ['concat', '_and', '_or', '_not', 'null', 'token'], 'token': ['symbol', 'symbol_not', 'any'], 'refID': ['regex'], 'atom': ['group', 'refID']}
    id2itemsStr = {'minmax': ' _, _', 'item': ' atom, count', 'null': " ('null',)", 'group': " ('group', name, regex)", '_not': " ('not', regex)", '_and': " ('and', items)", '_or': " ('or', items)", 'symbol': " 'symbol', syms", 'symbol_not': " 'symbol', 'not', syms", 'repeat': ' _,', 'any': " 'any',", 'concat': " ('concat', items)"}
    id2itemsVal = {'minmax': (Ignore(), Ignore()), 'item': (IgnoredCaseID('atom'), IgnoredCaseID('count')), 'null': ('null',), 'group': ('group', IgnoredCaseID('name'), IgnoredCaseID('regex')), '_not': ('not', IgnoredCaseID('regex')), '_and': ('and', IgnoredCaseID('items')), '_or': ('or', IgnoredCaseID('items')), 'symbol': ('symbol', IgnoredCaseID('syms')), 'symbol_not': ('symbol', 'not', IgnoredCaseID('syms')), 'repeat': (Ignore(),), 'any': ('any',), 'concat': ('concat', IgnoredCaseID('items'))}
    id2leftsideID = {'minmax': ('_', '_'), 'item': ('atom_0', 'count_1'), 'null': (LeftHandConstValue('null'),), 'group': (LeftHandConstValue('group'), 'name_2', 'regex_3'), 'symbol': (LeftHandConstValue('symbol'), 'syms_7'), '_and': (LeftHandConstValue('and'), 'items_5'), '_or': (LeftHandConstValue('or'), 'items_6'), '_not': (LeftHandConstValue('not'), 'regex_4'), 'symbol_not': (LeftHandConstValue('symbol'), LeftHandConstValue('not'), 'syms_8'), 'repeat': ('_',), 'any': (LeftHandConstValue('any'),), 'concat': (LeftHandConstValue('concat'), 'items_9')}

    def _preprocess_minmax(self, case, arg, attr):
        return attr
    def _postprocess_minmax(self, case, arg, attr, value):
        return value

    def _preprocess_regex(self, case, arg, attr):
        return attr
    def _postprocess_regex(self, case, arg, attr, value):
        return value

    def _preprocess_syms(self, case, arg, attr):
        return attr
    def _postprocess_syms(self, case, arg, attr, value):
        return value

    def _preprocess_item(self, case, arg, attr):
        return attr
    def _postprocess_item(self, case, arg, attr, value):
        return value

    def _preprocess_token(self, case, arg, attr):
        return attr
    def _postprocess_token(self, case, arg, attr, value):
        return value

    def _preprocess_null(self, case, arg, attr):
        return attr
    def _postprocess_null(self, case, arg, attr, value):
        return value

    def _preprocess_group(self, case, arg, attr):
        return attr
    def _postprocess_group(self, case, arg, attr, value):
        return value

    def _preprocess_symbol(self, case, arg, attr):
        return attr
    def _postprocess_symbol(self, case, arg, attr, value):
        return value

    def _preprocess__and(self, case, arg, attr):
        return attr
    def _postprocess__and(self, case, arg, attr, value):
        return value

    def _preprocess__or(self, case, arg, attr):
        return attr
    def _postprocess__or(self, case, arg, attr, value):
        return value

    def _preprocess_count(self, case, arg, attr):
        return attr
    def _postprocess_count(self, case, arg, attr, value):
        return value

    def _preprocess__not(self, case, arg, attr):
        return attr
    def _postprocess__not(self, case, arg, attr, value):
        return value

    def _preprocess_name(self, case, arg, attr):
        return attr
    def _postprocess_name(self, case, arg, attr, value):
        return value

    def _preprocess_atom(self, case, arg, attr):
        return attr
    def _postprocess_atom(self, case, arg, attr, value):
        return value

    def _preprocess_symbol_not(self, case, arg, attr):
        return attr
    def _postprocess_symbol_not(self, case, arg, attr, value):
        return value

    def _preprocess_items(self, case, arg, attr):
        return attr
    def _postprocess_items(self, case, arg, attr, value):
        return value

    def _preprocess_repeat(self, case, arg, attr):
        return attr
    def _postprocess_repeat(self, case, arg, attr, value):
        return value

    def _preprocess_any(self, case, arg, attr):
        return attr
    def _postprocess_any(self, case, arg, attr, value):
        return value

    def _preprocess_concat(self, case, arg, attr):
        return attr
    def _postprocess_concat(self, case, arg, attr, value):
        return value

    def _preprocess_refID(self, case, arg, attr):
        return attr
    def _postprocess_refID(self, case, arg, attr, value):
        return value

    def preprocess_minmax(self, case, arg, attr):
        return self._preprocess_minmax(case, arg, attr)
    def postprocess_minmax(self, case, arg, attr, value):
        return self._postprocess_minmax(case, arg, attr)

    def preprocess_regex(self, case, arg, attr):
        return self._preprocess_regex(case, arg, attr)
    def postprocess_regex(self, case, arg, attr, value):
        return self._postprocess_regex(case, arg, attr)

    def preprocess_syms(self, case, arg, attr):
        return self._preprocess_syms(case, arg, attr)
    def postprocess_syms(self, case, arg, attr, value):
        return self._postprocess_syms(case, arg, attr)

    def preprocess_item(self, case, arg, attr):
        return self._preprocess_item(case, arg, attr)
    def postprocess_item(self, case, arg, attr, value):
        return self._postprocess_item(case, arg, attr)

    def preprocess_token(self, case, arg, attr):
        return self._preprocess_token(case, arg, attr)
    def postprocess_token(self, case, arg, attr, value):
        return self._postprocess_token(case, arg, attr)

    def preprocess_null(self, case, arg, attr):
        return self._preprocess_null(case, arg, attr)
    def postprocess_null(self, case, arg, attr, value):
        return self._postprocess_null(case, arg, attr)

    def preprocess_group(self, case, arg, attr):
        return self._preprocess_group(case, arg, attr)
    def postprocess_group(self, case, arg, attr, value):
        return self._postprocess_group(case, arg, attr)

    def preprocess_symbol(self, case, arg, attr):
        return self._preprocess_symbol(case, arg, attr)
    def postprocess_symbol(self, case, arg, attr, value):
        return self._postprocess_symbol(case, arg, attr)

    def preprocess__and(self, case, arg, attr):
        return self._preprocess__and(case, arg, attr)
    def postprocess__and(self, case, arg, attr, value):
        return self._postprocess__and(case, arg, attr)

    def preprocess__or(self, case, arg, attr):
        return self._preprocess__or(case, arg, attr)
    def postprocess__or(self, case, arg, attr, value):
        return self._postprocess__or(case, arg, attr)

    def preprocess_count(self, case, arg, attr):
        return self._preprocess_count(case, arg, attr)
    def postprocess_count(self, case, arg, attr, value):
        return self._postprocess_count(case, arg, attr)

    def preprocess__not(self, case, arg, attr):
        return self._preprocess__not(case, arg, attr)
    def postprocess__not(self, case, arg, attr, value):
        return self._postprocess__not(case, arg, attr)

    def preprocess_name(self, case, arg, attr):
        return self._preprocess_name(case, arg, attr)
    def postprocess_name(self, case, arg, attr, value):
        return self._postprocess_name(case, arg, attr)

    def preprocess_atom(self, case, arg, attr):
        return self._preprocess_atom(case, arg, attr)
    def postprocess_atom(self, case, arg, attr, value):
        return self._postprocess_atom(case, arg, attr)

    def preprocess_symbol_not(self, case, arg, attr):
        return self._preprocess_symbol_not(case, arg, attr)
    def postprocess_symbol_not(self, case, arg, attr, value):
        return self._postprocess_symbol_not(case, arg, attr)

    def preprocess_items(self, case, arg, attr):
        return self._preprocess_items(case, arg, attr)
    def postprocess_items(self, case, arg, attr, value):
        return self._postprocess_items(case, arg, attr)

    def preprocess_repeat(self, case, arg, attr):
        return self._preprocess_repeat(case, arg, attr)
    def postprocess_repeat(self, case, arg, attr, value):
        return self._postprocess_repeat(case, arg, attr)

    def preprocess_any(self, case, arg, attr):
        return self._preprocess_any(case, arg, attr)
    def postprocess_any(self, case, arg, attr, value):
        return self._postprocess_any(case, arg, attr)

    def preprocess_concat(self, case, arg, attr):
        return self._preprocess_concat(case, arg, attr)
    def postprocess_concat(self, case, arg, attr, value):
        return self._postprocess_concat(case, arg, attr)

    def preprocess_refID(self, case, arg, attr):
        return self._preprocess_refID(case, arg, attr)
    def postprocess_refID(self, case, arg, attr, value):
        return self._postprocess_refID(case, arg, attr)

    def is_match(self, case, value):
        if case in self.id2itemsVal:
            pattern = self.id2itemsVal[case]
            return pattern == value
        elif case in self.id2subcases:
            return any(self.is_match(sub, value)
                       for sub in id2subcases[case])
        else:
            # leaf match every thing!
            return True


    def process(self, case, arg, attr = None):
        pre = getattr(self, 'preprocess_{case}'.format(case))
        post = getattr(self, 'postprocess_{case}'.format(case))
        attr = pre(case, arg, attr)
        if case in self.id2subcases:
            for sub in self.id2subcases:
                if self.is_match(sub, arg):
                    break
            else:
                raise ValueError('not matched subcase for {}'.format(case))
            value = self.process(case, arg, attr)
        elif case in self.id2itemsVal:
            pattern = self.id2itemsVal[case]
            if not pattern == arg:
                raise ValueError('not match {}'.format(case))
            value = self.assign_and_process(self.id2leftsideID[case], arg, attr)
        else:
            # leaf
            value = None
        return post(case, arg, attr, value)


    def assign_and_process(self, leftsideID, arg, attr):
        #OrderedDict?
        r = match_case([leftsideID], arg)
        if not r:
            raise logic-error
        _, _, id2value = r
        if _ignored_id in id2value:
            id2value.pop(_ignored_id)

        ls = [None] * len(id2value)
        for lhid, value in id2value.items():
            ID, n = split_lhID(lhid)
            if n >= len(ls) or ls[n] is not None:
                raise logic-error
            ls[n] = (ID, value)

        if any(x is None for x in ls):
            raise logic-error

        vs = []
        for case, arg in ls:
            r = self.process(case, arg, attr)
            vs.append(r)
        return vs

    pass
