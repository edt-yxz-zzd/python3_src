
__all__ = '''
    echo_key
    '''.split()

class EchoKey:
    def __getitem__(sf, k, /):
        return k
EchoKey
echo_key = EchoKey()
assert echo_key[0] == 0
assert echo_key[[]] == []

from seed.tiny_.echo_key import echo_key
