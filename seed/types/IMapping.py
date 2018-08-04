


'''
1) mutable, view, immutable
2) invariable


M a = ... | () | (a,)
    -- ... - not changes
    -- ()  - nothing/to delete
    -- (a,) - an "a" object
'''

__all__ = ''' '''.split()
#from itertools import chain
from abc import ABCMeta, abstractmethod



key2default = lambda key: raise KeyError
key2key_to_key2item = lambda key2key: lambda key: (key2key(key), None)
key2value_to_key2item = lambda key2value: lambda key: (None, key2value(key))
class IMapping(metaclass=ABCMeta):
    # view
    @classmethod
    @abstractmethod
    def saved_old_keys(cls):pass
    @abstractmethod
    def __len__(self):pass
    @abstractmethod
    def __contains__(self, key):pass
    @abstractmethod
    def __iter__(self):pass
    @abstractmethod
    # new_key -> (old_key, value) where old_key == new_key
    def get_item(self, key, *, key2default=key2default):pass

    def keys(self):return iter(self)
    def values(self):
        return map(self.get_value, self.keys())
    def items(self):
        return map(self.get_item, self.keys())
    def get_key(self, key, *, key2default=key2default):
        return self.get_item(key, key2default=key2key_to_key2item(key2default))[0]
    def get_value(self, key, key2default=key2default):
        return self.get_item(key, key2default=key2value_to_key2item(key2default))[1]
    def __getitem__(self, key): return self.get_value(key)

'''
    def try_alter(self, old_keyM, new_keyM, old_keyM_new_keyM_old_valueM_to_new_valueM):
        view = mapping_view(self)
        if old_keyM is ...:
            if new_keyM is ...:
                for old_key in self:
                    self.try_alter((old_key,), ..., mapping_old_keyM_new_keyM_old_valueM_to_new_valueM)
            elif new_keyM == ():
                self.clear()
            else:
                [new_key] = new_keyM
                if new_key in self:
                    old_key, old_value = self.get_item(new_key)
                    #old_keyM = (old_key,)
                    old_valueM = (old_value,)
                    new_valueM = old_keyM_new_keyM_old_valueM_to_new_valueM(view, old_keyM, new_keyM, old_valueM)
                    if new_valueM is ...:
                        self.reset_key(new_keyM)
                    elif new_valueM == ():
                        self.del_item(new_key)
                    else:
                        [new_value] = new_valueM
                        self.reset_item(new_key, new_value)
                else:
                    old_valueM = ()
                    new_valueM = old_keyM_new_keyM_old_valueM_to_new_valueM(view, old_keyM, new_keyM, old_valueM)
                    if new_valueM is ...:
                        pass
                    elif new_valueM == ():
                        pass
                    else:
                        [new_value] = new_valueM
                        self.new_item(new_key, new_value)
        elif old_keyM == ():
            if new_keyM is ...:
                pass
            elif new_keyM == ():
                pass
            else:
                [new_key] = new_keyM
                if new_key in self:
                    raise KeyError('existed')
                old_valueM = ()
                new_valueM = old_keyM_new_keyM_old_valueM_to_new_valueM(view, old_keyM, new_keyM, old_valueM)
                if new_valueM is ...:
                    pass
                elif new_valueM == ():
                    pass
                else:
                    [new_value] = new_valueM
                    self.new_item(new_key, new_value)
        else:
            [old_key] = old_keyM
            old_valueM = (self[old_key],) if old_key in self else ()
            new_valueM = old_keyM_new_keyM_old_valueM_to_new_valueM(view, old_keyM, new_keyM, old_valueM)
            if new_valueM == () or new_keyM == ():
                self.discard_item(old_key)
            elif new_valueM is ...:
                if old_valueM == () or new_keyM is ...:pass
                else:
                    [new_key] = new_keyM
                    if old_key == new_keyM:
                        self.reset_key(new_key)
                    elif new_key not in self:
                        self.alter_key(old_key, new_key)
                    else:
                        self.move_key(old_key, new_key)
            else:
                [new_value] = new_valueM
                if new_keyM is ...:
                    if old_key in self:
                        self.reset_value(old_key, new_value)
                    else:
                        self.new_item(old_key, new_value)
                else:
                    [new_key] = new_keyM
                    if new_key == old_key:
                        if old_key in self:
                            self.reset_item(new_key, new_value)
                        else:
                            self.new_item(new_key, new_value)
                    else:
                        raise KeyError('old_key, new_key, new_value: old_key!=new_key: unknown op')
'''


class IMapping_ResetValue(IMapping):
    @abstractmethod
    # invariable: keys, other_values, len
    # (old_key, old_value) existed -> (old_key, new_value)
    def reset_value(self, key, new_value):pass
    def reset_fvalue(self, key, old2new_value):
        old = self.get_value(key)
        new = old2new_value(old)
        self.reset_value(new)

class IMapping_ResetKey(IMapping):
    @abstractmethod
    # invariable: old_keys == new_keys, values, len
    # new_key == old_key = old_self.get_key(new_key)
    def reset_key(self, new_key):pass

class IMapping_AlterKey(IMapping_ResetKey):
    @abstractmethod
    # invariable: other_keys, values, len
    # new_key == old_key or new_key not in old_self
    def alter_key(self, old_key, new_key):pass
class IMapping_ResetItem(IMapping_ResetKey, IMapping_ResetValue):
    def reset_item(self, new_key, new_value):
        self.reset_key(new_key)
        self.reset_value(new_key, new_value)
    def reset_fitem(self, new_key, old2new_value):
        self.reset_key(new_key)
        self.reset_fvalue(new_key, old2new_value)
class IMapping_ResetValueOrItem(IMapping_ResetValue):
    @classmethod
    @abstractmethod
    def does_reset_value_instead_of_item(cls):pass
    def reset_value_or_item(self, nkey, new_value):
        if self.does_reset_value_instead_of_item():
            f = self.reset_value
        else:
            f = self.reset_item
        f(nkey, new_value)
    def reset_fvalue_or_fitem(self, nkey, old2new_value):
        if self.does_reset_value_instead_of_item():
            f = self.reset_fvalue
        else:
            f = self.reset_fitem
        f(nkey, new_value)


class IMapping_NewItem(IMapping):
    @abstractmethod
    # inc len
    # new_key not in old_self
    def new_item(self, new_key, new_value):pass
    def get_or_new_fdefault(self, nkey, key2default):
        if nkey not in self:
            self.new_item(nkey, key2default(nkey))
        return self[nkey]
class IMapping_SetItem(IMapping_NewItem, IMapping_ResetValueOrItem)
    # reset_value, reset_item, new_item
    def set_item(self, nkey, new_value):
        f = self.reset_value_or_item if nkey in self else self.new_item
        f(nkey, new_value)
    def set_fitem(self, nkey, key2new_value, old2new_value):
        if nkey in self:
            self.reset_fvalue_or_fitem(nkey, old2new_value)
        else:
            self.new_item(nkey, key2new_value(nkey))
class IMapping_DelItem(IMapping):
    @abstractmethod
    # dec len
    # key in old_self
    def del_item(self, key):pass
    def __delitem__(self, key): self.del_item(key)
    def discard_item(self, key):
        if key in self: self.del_item(key)
    def clear(self):
        for key in self: self.del_item(key)
    def pop_item(self, key, *, key2default=key2default):
        item = self.get_item(key, key2default=key2default)
        self.discard_item(key)
        return item
    def pop_key(self, key, *, key2default=key2default):
        return self.pop_item(key, key2default=key2key_to_key2item(key2default))[0]
    def pop_value(self, key, *, key2default=key2default):
        return self.pop_item(key, key2default=key2value_to_key2item(key2default))[1]
class IMapping_MoveKey(IMapping_DelItem, IMapping_AlterKey):
    def move_key(self, old_key, new_key):
        assert old_key in self
        self.discard_item(new_key)
        self.alter_key(old_key, new_key)




