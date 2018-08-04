
from collections.abc import MutableMapping, MutableSet
# does OrderedDict using such implement??
    
        

class OneTimeMap(MutableMapping):
    'NOTE: list is not a good mapping, since +i and L-i refer to same value'
    def __init__(self, key2anything):
        # key2anything is mapping or sequance; is a buffer
        # self.N = len(key2anything)
        self._key2pos_value = key2anything
        self.witnesses = [] # keys

    @property
    def buffer(self):
        # the __init__ arg
        # modify it may broken OneTimeMap
        # recommend to discard OneTimeMap after modify buffer external
        return self._key2pos_value
    def _unpack_pos_value(self, pos_value):
        # pos_value is a pair
        return pos_value
    def _pack_pos_value(self, pos, value):
        return pos, value

    
    def is_valid_witness_pos(self, witness_pos):
        return type(witness_pos) is int and 0 <= witness_pos < len(self.witnesses)

    def is_vaild_pos_value(self, pos_value):
        if type(pos_value) is tuple and len(pos_value) == 2:
            pos, value = self._unpack_pos_value(pos_value)
            return self.is_valid_witness_pos(pos)
        return False
    
    
    def get_witness_pos(self, key):
        # None or int
        pos_value = self._key2pos_value[key]
        if self.is_vaild_pos_value(pos_value):
            witness_pos, value = self._unpack_pos_value(pos_value)
            witness = self.witnesses[witness_pos]
            if key == witness:
                # exists
                return witness_pos
        return None

    def __contains__(self, key):
        return self.get_witness_pos(key) is not None
    def __len__(self):
        return len(self.witnesses)
    def __iter__(self):
        return iter(self.witnesses)
    
    def __setitem__(self, key, value):
        pos = self.get_witness_pos(key)
        if pos is None:
            pos = len(self.witnesses)
            self.witnesses.append(key)
        else:
            self.witnesses[pos] = key # update key ??
        new_pos_value = self._pack_pos_value(pos, value)
        self._key2pos_value[key] = new_pos_value
        
    def __delitem__(self, key):
        pos = self.get_witness_pos(key)
        if pos is None:
            return

        if pos + 1 != len(self.witnesses):
            # not last
            # move last to pos
            last_key = self.witnesses[pos] = self.witnesses[-1]
            last_pos, last_value = self._unpack_pos_value(self._key2pos_value[last_key])
            assert last_pos == len(self.witnesses)-1
            self._key2pos_value[last_key] = self._pack_pos_value(pos, last_value)
            
        self.witnesses.pop()

    def __getitem__(self, key):
        pos = self.get_witness_pos(key)
        if pos is None:
            raise KeyError(key)
        pos, value = self._unpack_pos_value(self._key2pos_value[key])
        return value
    
    def get_key(self, key):
        pos = self.get_witness_pos(e)
        if pos is None:
            raise KeyError(e)
        return self.witnesses[pos]

    

class OneTimeSet(OneTimeMap, MutableSet):
    'value must be key'
    @classmethod
    def _from_iterable(cls, it):
        raise NotImplementedError('since the contructor requires a buffer, no such constructor')

    def is_vaild_pos_value(self, pos_value):
        # pos_value is pos::int
        pos = pos_value # set::pos == map::pos_value
        return self.is_valid_witness_pos(pos)
    def _unpack_pos_value(self, pos_value):
        pos = pos_value # set::pos == map::pos_value
        if not self.is_valid_witness_pos(pos):
            return None, None
        value = self.witnesses[pos]
        return pos, value
    def _pack_pos_value(self, pos, value):
        # discard value
        if value is not self.witnesses[pos]:
            # key is not value!
            raise ValueError('value should be key')
        return pos
    


    def add(self, key):
        self[key] = key
    def discard(self, key):
        if key in self:
            del self[key]
    def remove(self, key):
        del self[key]

    def __setitem__(self, key, value):
        if key is not value:
            raise ValueError('key is not value')
        super().__setitem__(key, value)
        return 


def show_OneTime(d):
    from pprint import pprint
    pprint((type(d), d._key2pos_value, d.witnesses))

def test_OneTimeMap():
    d = OneTimeMap([None]*6)
    d[1] = 4
    d[3] = 2
    show_OneTime(d)
    del d[1]
    show_OneTime(d)
    assert 2 not in d
    assert 2 == d[3]
    print(d[3])

def test_OneTimeSet():
    s = OneTimeSet([None]*6)
    try:
        s[1]
    except KeyError:pass
    else:raise...
    s.add(1)
    s.add(3)
    assert 2 not in s
    assert 1 in s
    assert 3 in s
    del s[3]
    show_OneTime(s)























        
            
