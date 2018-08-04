from .decoder import *
from .encoder import *

def uint_case2Encoder_Decoder(uint_case):
    words = uint_case.split('_')
    words = (w.capitalize() for w in words)
    prefix = ''.join(words)
    type_names = [prefix+postfix for postfix in ['Encoder', 'Decoder']]
    
    return tuple(globals()[type_name] for type_name in type_names)
    

uint_case2Encoder = {case:uint_case2Encoder_Decoder(case)[0] for case in cases_TSLH}
uint_case2Decoder = {case:uint_case2Encoder_Decoder(case)[1] for case in cases_TSLH}


uint_case2encode_to_file = {case: Encoder().encode_to_file
                            for case, Encoder in uint_case2Encoder.items()}
uint_case2decode_from_file = {case: Decoder().decode_from_file
                              for case, Decoder in uint_case2Decoder.items()}


















