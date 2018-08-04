

from ._UintCodec__TSLH.UintCodec__TSLH import *
from ._UintCodec__TSLH.UintCodec__TSLH import __doc__


##from .UintCodec__ver1 import UintScodeCodec
##
##class _ModifiedUintScodeCodec(UintScodeCodec):
##    
##    def _calc_min_code_size(self, bit_length_of_uint):
##        # +1 for sign # now we move the sign into prefix mask
##        return super()._calc_min_code_size(bit_length_of_uint+1)
##    
##    def _calc_num_bytes(self, num_1s, num_0s):
##        assert num_1s >= 1 # in fact >= 2
##        num_bytes = super()._calc_num_bytes(num_1s, num_0s)
##        num_bytes -= 1
##        assert num_bytes >= 1
##        return num_bytes
##
##_aModifiedUintScodeCodec = _ModifiedUintScodeCodec()




    
        
        

    


