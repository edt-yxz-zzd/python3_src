

__all__ = 'BiLink'.split()


def is_pair(t):
    return type(t) is tuple and len(t) == 2
class BiLink:
    def __init__(self, key2prev_succ):
        # may have 0 or many links
        key2prev_succ = dict(key2prev_succ)
        self.key2prev_succ = key2prev_succ
        assert all(map(is_pair, key2prev_succ.values()))
        for key, (prev, succ) in key2prev_succ.items():
            if prev not in key2prev_succ:
                raise ValueError('{key} <<-- {prev} not in {keys}'.format(
                    key=key, prev=prev, keys=set(key2prev_succ)))
            if succ not in key2prev_succ:
                raise ValueError('{key} -->> {succ} not in {keys}'.format(
                    key=key, succ=succ, keys=set(key2prev_succ)))
            if self.succ(prev) != key:
                raise ValueError('{key} <<-- {prev} -/->> {key}: {d}'.format(
                    key=key, prev=prev, d=key2prev_succ))
            if self.prev(succ) != key:
                raise ValueError('{key} -->> {succ} <<-/- {key}: {d}'.format(
                    key=key, succ=succ, d=key2prev_succ))
    def succ(self, key):
        return self[key][1]
    def prev(self, key):
        return self[key][0]
    def __len__(self):
        return len(self.key2prev_succ)
    def __getitem__(self, key):
        return self.key2prev_succ[key]
    def __delitem__(self, key):
        d = self.key2prev_succ
        prev, succ = d.pop(key)
        if prev == succ:
            if prev != key:
                assert (key, key) == self[prev]
                self.key2prev_succ[prev] = (prev, prev)
        else:
            assert prev != key != succ
            d[prev] = self.prev(prev), succ
            d[succ] = prev, self.succ(succ)
    def __contains__(self, key):
        return key in self.key2prev_succ
    def insert_new_link(self, key):
        if key in self:
            raise KeyError('try insert but already existed')
        self.key2prev_succ[key] = key, key
    def insert_after(self, key, succ):
        if succ in self:
            raise KeyError('try insert but already existed')
        d = self.key2prev_succ
        prev, succ_succ = d[key]
        if succ_succ != key:
            assert prev != key
            d[key] = prev, succ
            d[succ] = key, succ_succ
            d[succ_succ] = succ, self.succ(succ_succ)
        else:
            assert prev == key
            d[key] = succ, succ
            d[succ] = key, key

    @classmethod
    def keys2single_link(cls, iterable):
        d = cls({})
        it = iter(iterable)
        for key in it:
            break
        else:
            return d

        d.insert_new_link(key)
        for succ in it:
            d.insert_after(key, succ)
            key = succ
        return d




