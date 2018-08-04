

'''
OneTimeXXX = OneTimeSet or OneTimeMap

use uninitialize buffer as a mapping (and not clean-up at the end)
that buffer can be used over and over again.
so, the total execute time will be O(n).
but at any time, at most 1 mapping object are allowed to own the buffer.


general purpose set/dict will be O(n log n) or n * avg(hash-find)

'''

__all__ = 'OneTimeSet OneTimeMap'.split()


class OneTimeSet:
    @staticmethod
    def _id(key):
        return key
    
    def __init__(self, buffer_element2int, iterable=(), *, key=None):
        self.buffer = buffer_element2int
        self.__set_elements([])
        
        self.update(iterable)
        self.key = key if key is not None else self._id
    def __test_key(self, key):
        if isinstance(self.buffer, list):
            if not 0 <= key < len(self.buffer):
                raise KeyError('out of range')


    def __set_elements(self, elements):
        self.certificate = self.elements = elements
    def __buffer_get(self, element):
        k = self.key(element)
        self.__test_key(k)
        return self.buffer[k]
    def __buffer_set(self, element, idx):
        k = self.key(element)
        self.__test_key(k)
        self.buffer[k] = idx
        
    def update(self, iterable):
        for e in iterable:
            self.add(e)
    def add(self, element):
        if element not in self:
            new_idx = len(self.certificate)
            self.__buffer_set(element, new_idx)
            self.certificate.append(element)
        else:
            idx = self.get_first_added_order(element)
            self.elements[idx] = element
    def visit(self, element):
        idx = self.get_first_added_order(element)
        return self.elements[idx]
    
    def __contains__(self, element):
        idx = self.__buffer_get(element)
        
        result= type(idx) == int and \
               0 <= idx < len(self.certificate) and \
               self.key(self.certificate[idx]) == self.key(element)
        #print(result, element)
        # why ? I wrong naming as '__contain__'
        # and 'in self' just return False not Exception!!!
        return result

    def is_last(self, element):
        idx = self.get_first_added_order(element)
        return idx == len(self)-1
    def get_first_added_order(self, element):
        if element not in self:
            raise KeyError('no such element')
        return self.__buffer_get(element)
    
    def __iter__(self):
        return iter(self.elements)
    def __len__(self):
        return len(self.elements)
    def buffer_size(self):
        return len(self.buffer)
    
    def pop(self):
        if not self:
            raise IndexError('pop from empty set')
        return self.elements.pop()
    def pop_all(self):
        es = self.elements
        self.__set_elements([])
        return es
    def clear(self):
        self.pop_all()
    
        

class OneTimeMap:
    def __init__(self, buffer_key2int, iterable=(), *, key=None):
        key = OneTimeSet._id if key is None else key
        self.__key = lambda pair: key(pair[0])
        iterable = ((key, value) for key, value in iterable)
        self.onetimeset = OneTimeSet(
            buffer_key2int, iterable, key=self.__key)
    def update(self, iterable):
        self.onetimeset.update(iterable)
    
    def __contains__(self, key):
        r = (key, None) in self.onetimeset
        #print(r)
        return r
    def get_first_added_order(self, key):
        return self.onetimeset.get_first_added_order((key, None))

    
    def __iter__(self):
        for key, value in self.onetimeset:
            yield key
    def keys(self):
        return iter(self)
    def values(self):
        for key, value in self.onetimeset:
            yield value
    def items(self):
        return iter(self.onetimeset)
            
    def __len__(self):
        return len(self.onetimeset)
    def buffer_size(self):
        return self.onetimeset.buffer_size()
    
    def popitem(self):
        if not self:
            raise IndexError('pop from empty map')
        return self.onetimeset.pop()
    
    def popitem_all(self):
        return self.onetimeset.pop_all()
    def clear(self):
        self.onetimeset.clear()
        
    def setdefault(self, key, default = None):
        element = (key, default)
        if key in self:
            _, value = self.onetimeset.visit(element)
            return value
        self.onetimeset.add(element)
        return default

    def get(self, key, default = None):
        element = (key, default)
        if key in self:
            _, value = self.onetimeset.visit(element)
            return value
        return default

    def __getitem__(self, key):
        element = (key, None)
        _, value = self.onetimeset.visit(element)
        return value
    def __setitem__(self, key, value):
        element = (key, value)
        self.onetimeset.add(element)
        return
    
    def __delitem__(self, key):
        element = (key, None)
        if self.is_last(element):
            self.popitem()
        raise NotImplementedError('del nonlast item')
        return 
        














