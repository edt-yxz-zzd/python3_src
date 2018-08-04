

r'''
example:
=======================
curl --continue-at - --retry 990 -L -O https://github.com/arvidn/libtorrent/releases/download/libtorrent-1_0_11/libtorrent-rasterbar-1.0.11.tar.gz
** Resuming transfer from byte position 520765
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   610    0   610    0     0    131      0 --:--:--  0:00:04 --:--:--   137
  1 2739k    1 33244    0     0    106      0  7:21:02  0:05:12  7:15:50     0
curl: (56) Send failure: Connection was reset
=======================

I have to call it manually!


retry [failure exit code...] --cmd <cmd>
if exit code in the given list, then retry


py bugs:
    subprocess
        call(['xx.exe', 'http://xxx.com/get.php?md5=xxx&key=xxxx'])
        ==>> call(['xx.exe', 'http://xxx.com/get.php?md5=xxx'])
            +call(['key=xxxx'])

    should escape "&" ==>> "^&"
'''


import subprocess
import time


def wrapped_call(cmd_args, exts = ('', '.exe', '.bat', '.cmd')):
    cmd_args = list(cmd_args)
    prog = cmd_args[0]
    for ext in exts:
        cmd_args[0] = prog + ext
        try:
            return subprocess.call(cmd_args)
        except FileNotFoundError:
            continue
    cmd_args[0] = prog
    return subprocess.call(cmd_args)
    raise


def main(args=None):
    import argparse, sys
    if args is None:
        args = sys.argv
    print(args)

    cmd_option = '--cmd'
    usage = 'usage: retry [FailureExitCode...] --cmd <cmd>'
    if cmd_option not in args[1:]:
        raise Exception(usage)

    i = args.index('--cmd', 1)
    retry_exit_codes = frozenset(map(int, args[1:i]))
    cmd = args[i+1:]
    print('FailureExitCodes: {}'.format(retry_exit_codes))
    print('CMD: {}'.format(cmd))

    exit_code = retry(retry_exit_codes, cmd)
    print('exit_code = {}'.format(exit_code))
    argparse.ArgumentParser.exit(exit_code)

def retry(retry_exit_codes, cmd):
    while True:
        # exit_code = subprocess.call(cmd)
        exit_code = wrapped_call(cmd)
        if exit_code not in retry_exit_codes: break
        time.sleep(5)
    return exit_code

if __name__ == '__main__':
    main()



