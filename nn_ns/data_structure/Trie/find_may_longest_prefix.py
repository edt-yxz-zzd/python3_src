
__all__ = '''
    IFindMayLongestPrefix
    FindMayLongestPrefix__native
    FindMayLongestPrefix__string_regex
    FindMayLongestPrefix__string_trie
    '''.split()

from .abc import ABC, abstractmethod, override, not_implemented, ABCMeta
from .Trie import CharTrie
import re


class IFindMayLongestPrefix(ABC):
    __slots__ = ()

    @not_implemented
    def find_may_longest_prefix(self, s):
        # Seq a -> None | Seq a
        raise NotImplementedError

class FindMayLongestPrefix__native(IFindMayLongestPrefix):
    '''O(find) = O(sum(map(len, prefixes)))'''

    def __init__(self, prefixes):
        self.prefixes = tuple(sorted(prefixes, key=len, reverse=True))
    @override
    def find_may_longest_prefix(self, s):
        for prefix in self.prefixes:
            if s.startswith(prefix):
                return prefix
        return None

class FindMayLongestPrefix__string_regex(IFindMayLongestPrefix):
    '''O(find) = O(max(map(len, prefixes)))

assume:
    1) re -> DFA // instead of NFA
    2) Seq a === String
'''

    def __init__(self, prefixes):
        self.prefixes = tuple(sorted(prefixes, key=len, reverse=True))
        prefixes = self.prefixes
        # bug: when not prefixes
        pattern = '|'.join(map(re.escape, prefixes)) \
                if prefixes else '(?!1)1'
        self.or_prefixes_regex = re.compile(pattern)

    @override
    def find_may_longest_prefix(self, s):
        m = self.or_prefixes_regex.match(s)
        return m.group() if m else None


class FindMayLongestPrefix__string_trie(IFindMayLongestPrefix):
    '''O(find) = O(max(map(len, prefixes)))'''

    def __init__(self, prefixes):
        self.prefixes_trie = CharTrie((p,p) for p in prefixes)

    @override
    def find_may_longest_prefix(self, s):
        may_size_value_pair = self.prefixes_trie\
            .query_maybe_longest_prefix_item(s)
        if may_size_value_pair is None:
            return None
        size, prefix = may_size_value_pair
        assert size == len(prefix)
        assert s[:size] == prefix
        return prefix




