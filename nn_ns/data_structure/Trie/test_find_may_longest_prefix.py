


import unittest
from unittest import TestCase
from .abc import ABC, abstractmethod, override, not_implemented, ABCMeta
from .find_may_longest_prefix import (
    FindMayLongestPrefix__native
    ,FindMayLongestPrefix__string_regex
    ,FindMayLongestPrefix__string_trie
    )

class ITestFindMayLongestPrefix__mixins(ABC): #(TestCase, ABC):
    __slots__ = ()

    @not_implemented
    def get_FindMayLongestPrefix(self):
        # -> cls where cls <: IFindMayLongestPrefix
        raise NotImplementedError
    def _test_prefixes_answer(self, prefixes, s, answer):
        prefixes = list(prefixes)
        cls = self.get_FindMayLongestPrefix()
        finder = cls(prefixes)
        ans = finder.find_may_longest_prefix(s)
        msg = f'{cls.__name__!s}({prefixes!r}).find_may_longest_prefix({s!r}) != {answer!r}'
        self.assertEqual(ans, answer, msg)
    def test_not_found(self):
        self._test_prefixes_answer([], '', None)
        self._test_prefixes_answer(['1', '23', '3'], '2', None)
        self._test_prefixes_answer(['1', '23', '3'], '24', None)
    def test_empty_prefix(self):
        self._test_prefixes_answer(['', '1', '23', '3'], '', '')
        self._test_prefixes_answer(['', '1', '23', '3'], '2', '')
        self._test_prefixes_answer(['', '1', '23', '3'], '24', '')
    def test_nonempty_prefix(self):
        self._test_prefixes_answer(['', '1', '23', '3'], '5', '')
        self._test_prefixes_answer(['', '1', '23', '3'], '1', '1')
        self._test_prefixes_answer(['', '1', '23', '3'], '12', '1')
        self._test_prefixes_answer(['', '1', '23', '3'], '2', '')
        self._test_prefixes_answer(['', '1', '23', '3'], '22', '')
        self._test_prefixes_answer(['', '1', '23', '3'], '23', '23')
        self._test_prefixes_answer(['', '1', '23', '3'], '3', '3')

class Test_FindMayLongestPrefix__native(
    ITestFindMayLongestPrefix__mixins, TestCase):
    __slots__ = ()

    @override
    def get_FindMayLongestPrefix(self):
        return FindMayLongestPrefix__native

class Test_FindMayLongestPrefix__string_regex(
    ITestFindMayLongestPrefix__mixins, TestCase):
    __slots__ = ()

    @override
    def get_FindMayLongestPrefix(self):
        return FindMayLongestPrefix__string_regex
class Test_FindMayLongestPrefix__string_trie(
    ITestFindMayLongestPrefix__mixins, TestCase):
    __slots__ = ()

    @override
    def get_FindMayLongestPrefix(self):
        return FindMayLongestPrefix__string_trie


if __name__ == '__main__':
    unittest.main()

