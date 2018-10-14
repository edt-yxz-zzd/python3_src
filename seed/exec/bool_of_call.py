
__all__ = '''
    bool_of_call
    '''.split()
from subprocess import run, CalledProcessError, CompletedProcess, PIPE, STDOUT

def bool_of_call(args, *, stdin=None, input=None, shell=False, timeout=None, encoding=None, errors=None) -> bool:
    '''-> success?

, stdout=None, stderr=None, check=False
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, timeout=None, check=False, encoding=None, errors=None)

#>>> bool_of_call(['ls', '.', '-1'])
>>> bool_of_call(['cd', '.'])
True
'''
    r = run(args
        , stdout=None, stderr=None, check=False

        , stdin=stdin
        , input=input, encoding=encoding, errors=errors
        , shell=shell, timeout=timeout
        )
    return not r.returncode

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +IGNORE_EXCEPTION_DETAIL


