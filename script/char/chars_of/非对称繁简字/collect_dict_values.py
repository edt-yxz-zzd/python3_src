


class CollectDictValues:
    def collects(self, pairs):
        raise NotImplementedError
class CollectDictValues__1by1(CollectDictValues):
    def collect(self, key, values):
        raise NotImplementedError
    def collects(self, pairs):
        for key, values in pairs:
            self.collect(key, values)

class CollectDictValues__New_or_IAdd(CollectDictValues__1by1):
    def exists_key(self, key):
        raise NotImplementedError
    def on_new_values(self, key, values):
        raise NotImplementedError
    def on_iadd_values(self, key, values):
        raise NotImplementedError
    def collect(self, key, values):
        if not self.exists_key(key):
            f = self.on_new_values
        else:
            f = self.on_iadd_values
        f(key, values)

class CollectDictValues__TransformValues(CollectDictValues__New_or_IAdd):
    # exists_key, _on_new_values_, _on_iadd_values_
    def _on_new_values_(self, key, values):
        raise NotImplementedError
    def _on_iadd_values_(self, key, values):
        raise NotImplementedError
    def transform_new_values(self, values):
        return values # list(values)
    def transform_iadd_values(self, values):
        return values # iter(values)
    def on_new_values(self, key, values):
        values = self.transform_new_values(values)
        self._on_new_values_(key, values)
    def on_iadd_values(self, key, values):
        values = self.transform_iadd_values(values)
        self._on_iadd_values_(key, values)
class CollectDictValues__Mapping(CollectDictValues__TransformValues):
    # get_dict
    def get_dict(self):
        raise NotImplementedError
    def _iadd_values_(self, old_values, new_values):
        # return values
        old_values += new_values
        return old_values

    def exists_key(self, key):
        return key in self.get_dict()
    def _on_new_values_(self, key, values):
        self.get_dict()[key] = values
    def _on_iadd_values_(self, key, values):
        d = self.get_dict()
        d[key] = self._iadd_values_(d[key], values)

class CollectDictValues__MappingToSet(CollectDictValues__Mapping):
    # get_dict
    def transform_new_values(self, values):
        return set(values)
    def _iadd_values_(self, old_values, new_values):
        old_values.update(new_values)
        return old_values


class CollectDict_SetValues(CollectDictValues__MappingToSet):
    def __init__(self, d):
        self.__dict = d
    def get_dict(self):
        return self.__dict

def collect_dict_values(pairs):
    # [(k, [v])] -> Map k (Set v)
    c = CollectDict_SetValues({})
    c.collects(pairs)
    return c.get_dict()


r = collect_dict_values([(1,'1'), (2, '1'), (1,'1231'), (1,'32')])
assert r == {1:set('123'), 2:set('1')}








