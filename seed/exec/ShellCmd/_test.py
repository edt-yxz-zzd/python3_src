
from .GNU_Cmd import GNU_Cmd
from .CallSetting import CallSetting
from .CallTheShellCmd import CallTheShellCmd
from subprocess import CalledProcessError, CompletedProcess, PIPE, STDOUT, DEVNULL

__doc__ = r'''
>>> default_caller = CallSetting()
>>> default_caller
CallSetting()
>>> quiet_caller = CallSetting(stdout=DEVNULL, stderr=DEVNULL)
>>> quiet_caller == default_caller.ireplace(stdout=DEVNULL, stderr=DEVNULL)
True

>>> ls1 = GNU_Cmd(True, 'ls', ['.'], {}, _1=True)
>>> ls1
GNU_Cmd(True, 'ls', ['.'], {'-1': True})

>>> quiet_caller.call_shell_cmd(ls1)
CompletedProcess(args=['ls', '-1', '--', '.'], returncode=0)

>>> quiet_checker = quiet_caller.ireplace(check=True)
>>> quiet_checker == CallSetting(stdout=DEVNULL, stderr=DEVNULL, check = True)
True
>>> quiet_checker.call_shell_cmd(ls1)
CompletedProcess(args=['ls', '-1', '--', '.'], returncode=0)


>>> lsX1 = GNU_Cmd(False, 'ls', ['non exist driver:/'], {}, _1=True)
>>> quiet_caller.call_shell_cmd(lsX1)
CompletedProcess(args=['ls', '-1', '--', 'non exist driver:/'], returncode=1)
>>> quiet_checker.call_shell_cmd(lsX1)
Traceback (most recent call last):
    ...
subprocess.CalledProcessError: Command '['ls', '-1', '--', 'non exist driver:/']' returned non-zero exit status 1.


#>>> e = catch_subprocess_CalledProcessError(lambda:quiet_checker.call_shell_cmd(lsX1))
>>> e = catch_subprocess_CalledProcessError(CallTheShellCmd(lsX1, quiet_checker))
>>> repr(e)
"CalledProcessError(1, ['ls', '-1', '--', 'non exist driver:/'])"

#>>> dir(e)
>>> e.args  # args of the Exception.__init__ instead of command args
(1, ['ls', '-1', '--', 'non exist driver:/'])
>>> e.cmd   # here is the command args
['ls', '-1', '--', 'non exist driver:/']
>>> e.returncode
1

# donot capture output! since input: stdout=stderr=None
>>> e.output
>>> e.stdout
>>> e.stderr



# PIPE means to capture the output
>>> captured_checker = CallSetting(check=True, stdout=PIPE, stderr=PIPE)
>>> e = catch_subprocess_CalledProcessError(lambda:captured_checker.call_shell_cmd(lsX1))
>>> repr(e)
"CalledProcessError(1, ['ls', '-1', '--', 'non exist driver:/'])"
>>> e.output
b''
>>> e.stdout
b''
>>> e.stderr #doctest: +ELLIPSIS
b'ls:...non exist driver:/...: No such file or directory...'



#########################
>>> lsX1.overwrite
False
>>> ls = CallTheShellCmd(lsX1, quiet_caller)
>>> ls()
CompletedProcess(args=['ls', '-1', '--', 'non exist driver:/'], returncode=1)
>>> ls(_1=False)
Traceback (most recent call last):
    ...
ValueError: duplicated flags: {'-1'}

#turn-on overwrite
>>> lsX1_on = lsX1.iextend(True, (), {})
>>> lsX1_on.overwrite
True
>>> ls = CallTheShellCmd(lsX1_on, quiet_caller)
>>> ls()
CompletedProcess(args=['ls', '-1', '--', 'non exist driver:/'], returncode=1)
>>> ls(_1=False, _A=True)
CompletedProcess(args=['ls', '-A', '--', 'non exist driver:/'], returncode=1)

'''




def catch_subprocess_CalledProcessError(lazy)->CalledProcessError:
    try:
        lazy()
    except CalledProcessError as e:
        return e
    raise Exception



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +IGNORE_EXCEPTION_DETAIL



