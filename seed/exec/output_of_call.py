
__all__ = '''
    output_of_call
    output_of_call_ex
    '''.split()

from subprocess import run, CalledProcessError, CompletedProcess, PIPE, STDOUT

def output_of_call(args, *, stdin=None, input=None, shell=False, timeout=None, encoding=None, errors=None) -> {bytes, str}:
    '''-> bytes|str

>>> output_of_call(['echo', '.', '-1']) #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
b'. -1...'
'''
    (returncode, output) = output_of_call_ex(
                    args
                    , stdin=stdin
                    , input=input, encoding=encoding, errors=errors
                    , shell=shell, timeout=timeout
                    )
    return output
def output_of_call_ex(args, *, stdin=None, input=None, shell=False, timeout=None, encoding=None, errors=None) -> (int, {bytes, str}):
    '''-> (returncode::int, output::bytes|str)

, stdout=PIPE, stderr=STDOUT, check=False
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, timeout=None, check=False, encoding=None, errors=None)

#>>> output_of_call_ex(['ls', '.', '-1']) #doctest: +ELLIPSIS
>>> output_of_call_ex(['echo', '.', '-1']) #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
(0, b'. -1...')
'''
    r = run(args
        , stdout=PIPE, stderr=STDOUT, check=False

        , stdin=stdin
        , input=input, encoding=encoding, errors=errors
        , shell=shell, timeout=timeout
        )
    return (r.returncode, r.stdout)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +IGNORE_EXCEPTION_DETAIL


