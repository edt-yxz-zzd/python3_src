
__all__ = '''
    ICanonLabelUGraph
    '''.split()

from .abc import ABC, abstractmethod, final
from ..UGraphBasic import UGraphBasic
from ..UGraphLabelling import UGraphLabelling

class ICanonLabelUGraph(ABC):
    __slots__ = ()

    @abstractmethod
    def __canon_label_ugraph__(self, ugraph):
        raise NotImplementedError
    def verify_input_ugraph(self, ugraph):
        return True
    @final
    def canon_label_ugraph(self, ugraph):
        assert isinstance(ugraph, UGraphBasic)
        assert self.verify_input_ugraph(ugraph)
        canon_labelling = type(self).__canon_label_ugraph__(ugraph)
        assert isinstance(canon_labelling, UGraphLabelling)
        return canon_labelling

