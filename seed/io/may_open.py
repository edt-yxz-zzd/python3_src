

__all__ = '''
    may_open_stdin
    may_open_stdout

    may_open
    '''.split()

from seed.tiny import with_if
import sys

def may_open(fdefault, may_file, mode, *, encoding, **kwargs):
    # should be used with "with"
    return with_if(may_file is not None
        , lambda:open(may_file, mode, encoding=encoding, **kwargs)
        , fdefault
        )
def may_open_stdin(may_file, mode, *, encoding, **kwargs):
    # should be used with "with"
    return may_open(
        (lambda:sys.stdin.buffer) if 'b' in mode else (lambda:sys.stdin)
        , may_file, mode, encoding=encoding, **kwargs)
def may_open_stdout(may_file, mode, *, encoding, **kwargs):
    # should be used with "with"
    return may_open(
        (lambda:sys.stdout.buffer) if 'b' in mode else (lambda:sys.stdout)
        , may_file, mode, encoding=encoding, **kwargs)


