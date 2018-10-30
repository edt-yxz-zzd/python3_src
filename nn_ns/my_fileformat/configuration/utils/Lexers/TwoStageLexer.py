
__all__ = '''
    TwoStageLexer
    '''.split()
from .MultiStageLexer import MultiStageLexer
#from .MultiStageLexer import TwoStageLexer

class TwoStageLexer(MultiStageLexer):
    def __init__(__self, input_symbols2raw_tokens, raw_tokens2terminals):
        super().__init__([input_symbols2raw_tokens, raw_tokens2terminals])




