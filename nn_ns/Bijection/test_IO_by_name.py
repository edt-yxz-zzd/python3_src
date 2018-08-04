
__all__ = 'test_IO_by_name test_IO test_I test_O'.split()
from .test_data import examples
from .InverseBijection import inverse_bijection

def test_IO_by_name(input_name, output_name, bijection):
    print('test_IO_by_name:', input_name, '->', output_name)
    print('\tInputType:', bijection.get_InputType().get_TypeSpec())
    print('\tOutputType:', bijection.get_OutputType().get_TypeSpec())
    inputs = examples[input_name]
    outputs = examples[output_name]
    test_IO(inputs, outputs, bijection)
def test_IO(inputs, outputs, bijection):
    test_I(inputs, bijection)
    test_O(outputs, bijection)

def backward(bijection, o):
    i = bijection.typechecked_backward(o)
    return i
def ubackward(bijection, o):
    i = bijection.untypechecked_backward(o)
    return i
def forward(bijection, i):
    o = bijection.typechecked_forward(i)
    return o
def uforward(bijection, i):
    o = bijection.untypechecked_forward(i)
    return o

def backward_forward(bijection, i):
    return forward_backward(inverse_bijection(bijection), i)
def forward_backward(bijection, o):
    eqO = bijection.get_OutputType().untypechecked_equal
    try:
        i = backward(bijection, o)
    except:
        try:
            i_ = ubackward(bijection, o)
        except:
            print(o)
        else:
            print(i_, o)
        raise

    try:
        o_ = forward(bijection, i)
    except:
        try:
            o_ = uforward(bijection, i)
        except:
            print(i, o)
        else:
            print(i, o, o_)
        raise

    try:
        assert eqO(o, o_)
    except:
        print(i, o, o_)
        raise
    return o_
def test_I(inputs, bijection):
    eqI = bijection.get_InputType().untypechecked_equal
    for i in inputs:
        backward_forward(bijection, i)
        continue
        o = bijection.typechecked_forward(i)
        i_ = bijection.typechecked_backward(o)
        print(i, o)
        assert eqI(i, i_)
def test_O(outputs, bijection):
    eqO = bijection.get_OutputType().untypechecked_equal
    for o in outputs:
        forward_backward(bijection, o)
        continue
        i = bijection.typechecked_backward(o)
        o_ = bijection.typechecked_forward(i)
        print(i, o)
        assert eqO(o, o_)

#est_IO_by_name('PInt1s', '(UInt, PInt)', pint1s_2_uint_pint)


