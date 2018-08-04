
def power(T, power, I = None):
    assert isinstance(power, int)
    assert power >= 0
    if I == None:
        assert power > 0

    return calc_power(I, [T], power)


def calc_power(I, T_2pow_ls, power:int):
    assert len(T_2pow_ls)
    assert power >= 0
    s = bin(power)[-1:1:-1]

    while len(T_2pow_ls) < len(s):
        T = T_2pow_ls[-1]
        T_2pow_ls.append(T*T)
    assert len(T_2pow_ls) >= len(s)

    '''
    T = I
    for t, c in zip(T_2pow_ls, s):
        if c == '1':
            T = T*t'''
    
    i = s.find('1')
    if i == -1:
        return I
    
    T = T_2pow_ls[i]
    for t, c in zip(T_2pow_ls[i+1:], s[i+1:]):
        if c == '1':
            T = T*t 
    
    return T
