
__all__ = '''
    is_uint_injection
    is_uint_surjection
    is_uint_bijection

    has_uint_mapping_no_self_reflect
    is_uint_bijection_without_self_reflect

    is_partial_uint_injection
    is_partial_uint_surjection
    is_partial_uint_bijection
    '''.split()

def is_uint_injection(forward_mapping, backward_mapping):
    # precodition:
    #   forward_mapping :: [UInt]
    #   backward_mapping:: [Maybe UInt]
    #
    # fface2arbitrary_hedge -> hedge2fake_clockwise_fface
    L = len(backward_mapping)
    return (all(0 <= u < L for u in forward_mapping)
        and all(backward_mapping[o] == i for i, o in enumerate(forward_mapping))
        )
def is_uint_surjection(forward_mapping, backward_mapping):
    # precodition: forward_mapping, backward_mapping:: [UInt]
    #
    # hedge2fake_clockwise_fface -> fface2arbitrary_hedge
    L = len(backward_mapping)
    return (is_uint_injection(backward_mapping, forward_mapping)
        and all(0 <= u < L for u in forward_mapping)
        )
def is_uint_bijection(forward_mapping, backward_mapping):
    # precodition: forward_mapping, backward_mapping:: [UInt]
    #
    # hedge2another_hedge <-> hedge2another_hedge
    return (is_uint_injection(forward_mapping, backward_mapping)
        and is_uint_injection(backward_mapping, forward_mapping)
        )


def has_uint_mapping_no_self_reflect(forward_mapping):
    # precodition: forward_mapping :: [UInt]
    #
    return not any(i == j for i, j in enumerate(forward_mapping))

def is_uint_bijection_without_self_reflect(forward_mapping, backward_mapping):
    # precodition: forward_mapping, backward_mapping:: [UInt]
    #
    return is_uint_bijection(forward_mapping, backward_mapping) and has_uint_mapping_no_self_reflect(forward_mapping)

def is_partial_uint_injection(forward_mapping, backward_mapping):
    # precodition:
    #   forward_mapping :: [Maybe UInt]
    #   backward_mapping :: [Maybe UInt]
    L = len(backward_mapping)
    return all(0 <= mo < L and backward_mapping[mo] == i
            for i, mo in enumerate(forward_mapping) if mo is not None
            )
def is_partial_uint_surjection(forward_mapping, backward_mapping):
    # precodition:
    #   forward_mapping :: [Maybe UInt]
    #   backward_mapping :: [UInt]
    LI = len(forward_mapping)
    LO = len(backward_mapping)
    return (LI >= LO
        and all(0 <= mo < LO for mo in forward_mapping if mo is not None)
        and all(0 <= i < LI and forward_mapping[i] == o
                for o, i in enumerate(backward_mapping)
                )
        )
def is_partial_uint_bijection(forward_mapping, backward_mapping):
    # precodition:
    #   forward_mapping :: [Maybe UInt]
    #   backward_mapping :: [UInt]
    return (is_partial_uint_surjection(forward_mapping, backward_mapping)
        and is_partial_uint_injection(forward_mapping, backward_mapping)
        )

