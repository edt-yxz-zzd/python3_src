
def unbox_complex(z):
    return z.real, z.imag
def std_float(f):
    assert type(f) is float
    if repr(f) == '-0.0':
        f = +0.0
    return f
def std_complex(z):
    assert type(z) is complex
    r, j = unbox_complex(z)
    r = std_float(r)
    j = std_float(j)
    z = complex(r, j)
    return z









