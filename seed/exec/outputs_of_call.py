
__all__ = '''
    outputs_of_call
    outputs_of_call_ex
    '''.split()

from subprocess import run, CalledProcessError, CompletedProcess, PIPE, STDOUT

def outputs_of_call(args, *, stdin=None, input=None, shell=False, timeout=None, encoding=None, errors=None) -> {bytes, str}:
    '''-> (stdout,stderr)::(bytes,bytes)|(str,str)

>>> outputs_of_call(['echo', '.', '-1']) #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
(b'. -1...', b'')
'''
    (returncode, outputs) = outputs_of_call_ex(
                    args
                    , stdin=stdin
                    , input=input, encoding=encoding, errors=errors
                    , shell=shell, timeout=timeout
                    )
    stdout, stderr = outputs
    return stdout, stderr
def outputs_of_call_ex(args, *, stdin=None, input=None, shell=False, timeout=None, encoding=None, errors=None) -> (int, {bytes, str}):
    '''-> (returncode::int, outputs::(bytes,bytes)|(str,str))

, stdout=PIPE, stderr=PIPE, check=False
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, timeout=None, check=False, encoding=None, errors=None)

#>>> outputs_of_call_ex(['ls', '.', '-1']) #doctest: +ELLIPSIS
>>> outputs_of_call_ex(['echo', '.', '-1']) #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
(0, (b'. -1...', b''))
'''
    r = run(args
        , stdout=PIPE, stderr=PIPE, check=False

        , stdin=stdin
        , input=input, encoding=encoding, errors=errors
        , shell=shell, timeout=timeout
        )
    return (r.returncode, (r.stdout, r.stderr))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +IGNORE_EXCEPTION_DETAIL


