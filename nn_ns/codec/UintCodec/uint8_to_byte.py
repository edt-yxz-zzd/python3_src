
def uint8_to_byte(uint8):
    return bytes([uint8])

def byte_to_uint8(byte):
    assert type(byte) is bytes
    assert len(byte) == 1
    u, = byte

    assert 0 <= u < 0x100
    return u
