


'''
LeftHandID = LHAtom | LHDict | LHIterable



LHAtom = None | '' | python_id | LHID_RHFilter | LeftHandConstValue

None | ''
    means to discard the value
python_id
    a nonempty str which does not start with '*'
    if an id starting with '*' required, we may add ' ' to all ids.


LHID_RHFilter:
    .get_left_hand_rhfilter()->rh_filter
        rh_filter(rh_value)->value
    .get_left_hand_lhid()->LeftHandID
    we will try to match the results of those two methods above.
    
LeftHandConstValue:
    .get_left_hand_constvalue()->sth
        sth: to match with right hand
        sth: requires '=='
        
-- str, LeftHandFilter, LeftHandConstValue: should be distinguishable
-- otherwise, the l-eft one wins



LHDict:
    is a dict of (key: LeftHandID);
    may contains (lh_star_star: LHStarStarID)
    
LHIterable:
    is a iterable(but not str!) of LeftHandID;
    last element may be a LHStarID
    
-- LHAtom, LHDict, LHSeq: should be distinguishable
-- otherwise, the l-eft one wins




LHStarID is a string = '*' | '*' + python_id
LHStarStarID is a string = '**' | '**' + python_id
lh_star_star # **, only one instance

'''


__all__ = ('match_case', 'do_assign', 'lh_star_star',
           'LeftHandConstValue', 'LHID_RHFilter')
from .. import LogicError

from collections import Mapping, Iterable


class MatchCaseModuleErrorBase(Exception):pass
class MatchCaseError(ValueError, MatchCaseModuleErrorBase):pass
class NotLeftHandIDError(ValueError, MatchCaseModuleErrorBase):pass





def match_case(cases, rh_value)->'None or (index, case, id2value)':
    '''find the first case that match rh_value.
input: cases, rh_value
    case     - a LeftHandID
    rh_value - this and all subvalues should be container but not iterable
               that is they have attr '__iter__' but no '__next__'
output:
    None if none matched
    (index, case, id2value)
        index    - the index of case in cases
        case     - the matched case
        id2value - result of do_assign(case, rh_value)


example:
    >>> SS = lh_star_star
    >>> CV = LeftHandConstValue
    >>> cases = ({'k':'id', SS:'**'}, [CV('case'), 't', '*'])
    >>> match_case(cases, 1)
    >>> match_case(cases, (1, 2))
    >>> (i, case, d) = match_case(cases, ('case', 2))
    >>> i, d
    (1, {'t': 2})
    >>> case is cases[i]
    True
    >>> match_case(cases, {'o':'o'})
    >>> (i, case, d) = match_case(cases, {'o':'o', 'k':'this'})
    >>> i, d
    (0, {'id': 'this'})
    >>> case is cases[i]
    True
    
'''
    for index, case in enumerate(cases):
        try:
            id2value = do_assign(case, rh_value)
            return (index, case, id2value)
        
        except MatchCaseError:
            continue
        
        raise

    return None





def do_assign(lh_id, rh_value):
    '''make pattern match and assign value to ID


do sth like:
a, b, *c = v
{1:c, **:g} = v
a, b, (_, [t]), {2:y, 'w':x} = u

see also : this module.__doc__ for definition of LeftHandID
example:
    # ignore or assign to id
    >>> do_assign('', 23)
    {}
    >>> do_assign(None, 23)
    {}
    >>> do_assign('i', 23) == {'i': 23}
    True


    # match iterable
    >>> do_assign(['i'], [23]) == {'i': 23}
    True
    >>> do_assign(('i', 'j'), '23') == {'i': '2', 'j': '3'}
    True
    >>> do_assign(('i', 'i'), '23') == {'i': '3'}
    True

    # match *
    >>> do_assign(('i', 'j', '*'), '23rtert') == {'i': '2', 'j': '3'}
    True
    >>> r = do_assign(('i', 'j', '*c'), '23rtert')
    >>> r == {'i': '2', 'j': '3', 'c': list('rtert')}
    True


    # match dict
    >>> r = do_assign({1:'c', 2:'d'}, {1:'abc', 2:'def'})
    >>> r == {'c': 'abc', 'd': 'def'}
    True

    # match **
    >>> r = do_assign({1:'c', lh_star_star:'**g'}, {1:'abc', 2:'def', 3:4})
    >>> r == {'c': 'abc', 'g': {2: 'def', 3: 4}}
    True


    # match more
    >>> SS = lh_star_star
    >>> r = do_assign(['a', [{8:['b'], SS:'**c'}, '*d'], '*e'], \
                      ['a', [{8:['b']          }      ]      ])
    >>> r == {'a':'a', 'b':'b', 'c':{}, 'd':[], 'e':[]}
    True


    # match LeftHandConstValue
    >>> CV = LeftHandConstValue
    >>> do_assign(CV(23), 23)
    {}
    >>> do_assign([CV(23), 'a'], [23, 'a']) == {'a':'a'}
    True
    
    # match LHID_RHFilter
    >>> LRF = LHID_RHFilter
    >>> lrf = LRF(['min', '*others'], sorted)
    >>> do_assign(lrf, set(range(4))) == {'min':0, 'others':[1,2,3]}
    True




    
    # exception
    >>> do_assign(['a', 'b', '*'], [1])
    Traceback (most recent call last):
        ...
    MatchCaseError: len(LHIterable) > len(rh_value) : 2* > 1
    >>> do_assign(['a', 'b'], [1])
    Traceback (most recent call last):
        ...
    MatchCaseError: len(LHIterable) != len(rh_value) : 2 != 1
    >>> do_assign(['a'], [1, 2])
    Traceback (most recent call last):
        ...
    MatchCaseError: len(LHIterable) != len(rh_value) : 1 != 2
    
    
    >>> do_assign({1:'a', 2:'b', SS:'**c'}, {1:1})
    Traceback (most recent call last):
        ...
    MatchCaseError: not LHDict.keys() <= rh_value.keys() : {2}
    >>> do_assign({1:'a', 2:'b', SS:'c'}, {1:1})
    Traceback (most recent call last):
        ...
    NotLeftHandIDError: not LHStarStarID <- LHDict[lh_star_star]
    >>> do_assign({1:'a', 2:'b'}, {1:1})
    Traceback (most recent call last):
        ...
    MatchCaseError: LHDict.keys() != rh_value.keys() : {2}|samekeys != set()|samekeys
    >>> do_assign({1:'a'}, {2:2})
    Traceback (most recent call last):
        ...
    MatchCaseError: LHDict.keys() != rh_value.keys() : {1}|samekeys != {2}|samekeys

    
    >>> do_assign(CV(3), 2)
    Traceback (most recent call last):
        ...
    MatchCaseError: LeftHandConstValue != rh_value
    >>> do_assign(3, 2)
    Traceback (most recent call last):
        ...
    NotLeftHandIDError: not LeftHandID
'''
    space = {}
    match_and_assign(space, lh_id, rh_value)
    return space
















##########################################
            

class OneValue:
    __slots__ = ('_OneValue__value',)
    def __init__(self, value):
        self.__value = value
        return
    def __get_value(self):
        return self.__value
    
    pass

class LeftHandConstValue(OneValue):
    __slots__ = ()
    def __repr__(self):
        return 'LeftHandConstValue({!r})'.format(self._OneValue__get_value())
    def __init__(self, value):
        value == value # test
        super().__init__(value)
        return
    def get_left_hand_constvalue(self):
        return self._OneValue__get_value()
    
    pass




class LHID_RHFilter(OneValue):
    __slots__ = ()
    def __repr__(self):
        return 'LHID_RHFilter{!r}'.format(self._OneValue__get_value())
    def __init__(self, lh_id, rh_filter):
        '''lh_id is a LeftHandID
rh_filter(rh_value) -> value'''
        value = lh_id, rh_filter
        super().__init__(value)
        return
    def get_left_hand_lhid(self) -> 'LeftHandID':
        return self._OneValue__get_value()[0]
    def get_left_hand_rhfilter(self) -> 'rh_filter':
        return self._OneValue__get_value()[1]
    
    pass




class __LeftHandStarStar:
    __slots__ = ()
    __instance = None
    
    @classmethod
    def get_instance(cls):
        it = cls.__instance
        if it != None:
            return it
        else:
            it = cls()
            cls.__instance = it
        
    def __init__(self):
        if self.__instance != None:
            raise LogicError('instance exists')
        pass
    def __hash__(self):
        return hash('**')
    def __eq__(self, other):
        return self is other
    def __ne__(self, other):
        return not self == other
    pass


def LeftHandStarStar():
    it = __LeftHandStarStar.get_instance()
    return it

lh_star_star = LeftHandStarStar()


##
##class LeftHandAtom(OneValue):
##    __slots__ = ()
##    def __init__(self, name):
##        if not isinstance(name, str):
##            raise ValueError('not str')
##        super().__init__(name)
##        return
##    def get_left_hand_atomid(self):
##        return self._OneValue__get_value()
##    
##    pass
##class LeftHandStarAtom(LeftHandAtom):
##    def is_left_hand_staratom(self):
##        return True
##    pass






#############################
def is_mapping(d):
    return isinstance(d, Mapping)
def is_iterable(x):
    return isinstance(x, Iterable)

def _is_pythonid(lh_id):
    return len(lh_id) and not lh_id.startswith('*')

def is_prefix_pythonid(lh_id, prefix):
    return isinstance(lh_id, str) and lh_id.startswith(prefix)\
           and _is_pythonid(lh_id[len(prefix):])

def is_prefix_optional_pythonid(lh_id, prefix):
    return (isinstance(lh_id, str) and lh_id == prefix) or \
           is_prefix_pythonid(lh_id, prefix)

def is_pythonid(lh_id):
    return is_prefix_pythonid(lh_id, '')

def is_LHStarStarID(lh_id):
    return is_prefix_optional_pythonid(lh_id, '**')
def is_LHStarID(lh_id):
    return is_prefix_optional_pythonid(lh_id, '*')

def is_LHAtom(lh_id):
    return lh_id is None or \
           lh_id == '' or \
           is_pythonid(lh_id) or \
           is_LHID_RHFilter(lh_id) or \
           is_LeftHandConstValue(lh_id)

def is_LeftHandConstValue(lh_id):
    return hasattr(lh_id, 'get_left_hand_constvalue')

def is_LHID_RHFilter(lh_id):
    return all(hasattr(lh_id, f)
               for f in ['get_left_hand_lhid',
                         'get_left_hand_rhfilter'])
    
def is_LHDict(lh_id):
    return is_mapping(lh_id)
def is_LHIterable(lh_id):
    return is_iterable(lh_id)



#############################

def match_and_assign_LHAtom(space, lh_id, rh_value):
    if lh_id is None or lh_id == '':
        pass
    elif is_pythonid(lh_id):
        pythonid = lh_id
        match_and_assign_pythonid(space, pythonid, rh_value)
        pass
    
    elif is_LHID_RHFilter(lh_id):
        lhid_rhfilter = lh_id
        lh_id = lhid_rhfilter.get_left_hand_lhid()
        if lh_id is lhid_rhfilter:
            raise NotLeftHandIDError('lhid_rhfilter.get_left_hand_lhid() -> self')
        
        rh_value = lhid_rhfilter.get_left_hand_rhfilter()(rh_value)
        match_and_assign(space, lh_id, rh_value)
        pass
    
    elif is_LeftHandConstValue(lh_id):
        if not lh_id.get_left_hand_constvalue() == rh_value:
            raise MatchCaseError(
                'LeftHandConstValue != rh_value')
        pass
    else:
        raise NotLeftHandIDError('not LHAtom')
    return






def build_LHDict(lh_dict):
    d = lh_dict.copy()
    if lh_star_star in d:
        starstarid = d[lh_star_star]
        if not is_LHStarStarID(starstarid):
            raise NotLeftHandIDError(
                'not LHStarStarID <- LHDict[lh_star_star]')
    return d

def match_and_assign_LHDict(space, lh_id, rh_value):
    d = build_LHDict(lh_id)
    if not is_mapping(rh_value):
        raise MatchCaseError('LHDict while rh_value not mapping')
    
    if lh_star_star in d:
        starstarid = d.pop(lh_star_star)
        dkeys = d.keys() - rh_value.keys()
        if dkeys:
            raise MatchCaseError(
                'not LHDict.keys() <= rh_value.keys() : {}'
                .format(dkeys))

        dkeys = rh_value.keys() - d.keys()
        value = {k: rh_value[k] for k in dkeys}
        match_and_assign_LHStarStarID(space, starstarid, value)
        
        rh_value = {k: rh_value[k] for k in d}
        
    if d.keys() != rh_value.keys():
        # may not support '<'
##        dlr = sorted(d.keys() - rh_value.keys())
##        drl = sorted(rh_value.keys() - d.keys())
        dlr = d.keys() - rh_value.keys()
        drl = rh_value.keys() - d.keys()
        raise MatchCaseError(
            'LHDict.keys() != rh_value.keys() : {}|samekeys != {}|samekeys'
            .format(dlr, drl))

    for key, sub_lh_id in d.items():
        value = rh_value[key]
        match_and_assign(space, sub_lh_id, value)

    return






def build_LHList(lh_iterable):
    ls = list(lh_iterable)
    if any(is_LHStarID(lh) for lh in ls[:-1]):
        raise NotLeftHandIDError('LHStarID not at last')
    return ls

def match_and_assign_LHIterable(space, lh_id, rh_value):
    ls = build_LHList(lh_id)
    if not is_iterable(rh_value):
        raise MatchCaseError('LHIterable while rh_value not iterable')
    
    rh_value = list(rh_value)
    if ls and is_LHStarID(ls[-1]):
        if not len(ls) - 1 <= len(rh_value):
            raise MatchCaseError(
                'len(LHIterable) > len(rh_value) : {}* > {}'
                .format(len(ls) - 1, len(rh_value)))

        starid = ls[-1]
        match_and_assign_LHStarID(space, starid, rh_value[len(ls)-1:])
        
        rh_value = rh_value[:len(ls)-1]
        ls = ls[:-1]
        
    if len(ls) != len(rh_value):
        raise MatchCaseError(
            'len(LHIterable) != len(rh_value) : {} != {}'
            .format(len(ls), len(rh_value)))
        

    for sub_lh_id, value in zip(ls, rh_value):
        match_and_assign(space, sub_lh_id, value)







#############################


_match_and_assign_ls = tuple((g['is_'+case], g['match_and_assign_'+case])
                             for g in [globals()]
                             for case in 'LHAtom LHDict LHIterable'.split())
def match_and_assign(space, lh_id, rh_value):
    for is_, match in _match_and_assign_ls:
        if is_(lh_id):
            match(space, lh_id, rh_value)
            break
    else:
        raise NotLeftHandIDError('not LeftHandID')
    
    return





#############################

def ignore_or_match_and_assign_pythonid(space, pythonid, rh_value):
    if pythonid == '':
        pass
    else:
        match_and_assign_pythonid(space, pythonid, rh_value)
    return

    
def match_and_assign_pythonid(space, pythonid, rh_value):
    if not is_pythonid(pythonid):
        raise NotLeftHandIDError('not python_id')
    space[pythonid] = rh_value
    return

def match_and_assign_LHStarStarID(space, starstarid, rh_value):
    if not is_LHStarStarID(starstarid):
        raise NotLeftHandIDError('not LHStarStarID')

    if not starstarid.startswith('**'):
        raise LogicError('unknown format')
    
    pythonid = starstarid[2:]
    ignore_or_match_and_assign_pythonid(space, pythonid, rh_value)
    return


def match_and_assign_LHStarID(space, starid, rh_value):
    if not is_LHStarID(starid):
        raise NotLeftHandIDError('not LHStarID')

    if not starid.startswith('*'):
        raise LogicError('unknown format')
    
    pythonid = starid[1:]
    ignore_or_match_and_assign_pythonid(space, pythonid, rh_value)
    return



if __name__ == "__main__":
    import doctest
    doctest.testmod()



