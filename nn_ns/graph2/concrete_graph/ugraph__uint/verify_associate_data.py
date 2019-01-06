__all__ = '''
    verify_associate_data
    verify_associate_data_ex
    '''.split()

from seed.verify.common_verify import (
    is_UInt, is_Sequence
    )
from .is_uint_sequence import is_uint_sequence

def verify_associate_data_ex(*
    ,expected_input_size
    ,maybe_input2output
    ,maybe_num_outputs
    ):

    if (maybe_num_outputs is None) is not (maybe_input2output is None): raise TypeError
    if maybe_input2output is None:
        if not is_UInt(expected_input_size): raise TypeError
        return True

    return verify_associate_data(
        expected_input_size = expected_input_size
        ,input2output = maybe_input2output
        ,num_outputs = maybe_num_outputs
        )

def verify_associate_data(*
    ,expected_input_size
    ,input2output
    ,num_outputs
    ):
    if not is_UInt(expected_input_size): raise TypeError
    if not is_UInt(num_outputs): raise TypeError
    if not is_uint_sequence(input2output): raise TypeError
    if len(input2output) != expected_input_size: raise ValueError
    if not num_outputs <= expected_input_size: raise ValueError
    if not max(input2output, default=-1) < num_outputs: raise ValueError
    return True

'''bug:

def verify_associate_data_ex(*
    ,expected_input_size
    ,maybe_input2output
    ,maybe_num_outputs
    ):
    input2output, num_outputs = make_std_associate_data(
        maybe_input2output=maybe_input2output
        maybe_num_outputs=maybe_num_outputs
        )
    return verify_associate_data(
        expected_input_size = expected_input_size
        ,input2output = input2output
        ,num_outputs = num_outputs
        )
def make_std_associate_data(*
    ,maybe_input2output
    ,maybe_num_outputs
    ):
    if maybe_input2output is None:
        input2output = ()
    else:
        input2output = maybe_input2output
    if maybe_num_outputs is None:
        num_outputs = 0
    else:
        num_outputs = maybe_num_outputs
    return input2output, num_outputs
'''

