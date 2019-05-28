
'''
input() print prompt to stdout instead of stderr!
using raw_input__echo/raw_input__not_echo to print prompt to stderr.
'''

__all__ = '''
    raw_input__echo
    raw_input__not_echo
    '''.split()

import getpass, sys

def __flush(maybe_stdout):
    if maybe_stdout is None:
        stdout = sys.stdout
    else:
        stdout = maybe_stdout
    stdout.flush()

def raw_input__not_echo(prompt='', stdout=None):
    __flush(stdout)
    if prompt is None:
        prompt = ''
    return getpass.getpass(prompt)
def raw_input__echo(prompt='', stdout=None):
    __flush(stdout)
    if prompt is None:
        prompt = ''
    if prompt:
        sys.stderr.write(str(prompt))
    return input()


