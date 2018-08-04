
__all__ = '''
    echo
    fst
    snd
    last

    ifNone
    echo_ifNone
    '''.split()

from operator import attrgetter, itemgetter, methodcaller, __not__
from functools import partial
from .Caller import Caller, Partial
from .ChainFuncs import ChainFuncs, apply

echo = lambda x:x
fst = lambda seq: seq[0]
snd = lambda seq: seq[1]
last = lambda seq: seq[-1]


def ifNone(default, obj):
    return default if obj is None else obj
def echo_ifNone(obj):
    return ifNone(echo, obj)

def echo(x): return x
def fst(seq): return seq[0]
def snd(seq): return seq[1]
def last(seq): return seq[-1]

