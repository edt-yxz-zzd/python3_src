

import cmd, sys, shlex
import argparse
import subprocess
# import readline
from nn_ns.cmd_call import decoded_cmd_call




def build_argparser_for_do_set():
    parser = argparse.ArgumentParser(
        #add_help = True,
        prog = 'set',
        description = 'set the two flags for shlex.split',
        epilog = 'print the two current flags if no input')

##    parser.add_argument('-h', '--help',
##                        action='store_true', default = False,
##                        help='show this help message')
    
    comments_group = parser.add_mutually_exclusive_group()
    comments_group.add_argument('-c', '--set_comments_flag',
                                action='store_true', dest = 'comments',
                                help='set comments = True')
    comments_group.add_argument('-C', '--clear_comments_flag',
                                action='store_false', dest = 'comments',
                                help='set comments = False')

    posix_group = parser.add_mutually_exclusive_group()
    posix_group.add_argument('-p', '--set_posix_flag',
                             action='store_true', dest = 'posix',
                             help='set posix = True')
    posix_group.add_argument('-P', '--clear_posix_flag',
                             action='store_false', dest = 'posix',
                             help='set posix = False')

    parser.set_defaults(comments=None, posix=None)
    # no: parser.get_help('set_comments_flag')
    return parser



class ArgsShowShell(cmd.Cmd):
    # __slots__ = ('comments', 'posix') ??????? why? the super class open the dict?
    
    intro = 'Welcome to the args-show shell.\n'\
            'Type help or ? to list commands.\n'\
            'Type shell or ! to execute shell command.\n'
    
    prompt = 'args-show > '
    
    __do_set_parser = build_argparser_for_do_set()


    
    
    def __init__(self, comments=False, posix=True,
                 completekey='tab', stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)
        self.comments = comments
        self.posix = posix
        
##        try:
##            self.fail = 0
##        except AttributeError as success:
##            pass
##        else:
##            raise logic-error; should.never.come.here;
            



    def do_help(self, args):
        if args:
            print('help on {!r}'.format(args))
        if args == '?':
            args = 'help'
        elif args == '!':
            args = 'shell'
            
        return super().do_help(args)

    do_help.__doc__ = cmd.Cmd.do_help.__doc__


    
    @staticmethod
    def str_set_flag(flag_name, flag_status):
        op = 'clear set'.split()[flag_status]
        return '{} {} flag'.format(op, flag_name)
    
    def do_set(self, args):
        'set two flag: "comments" and "posix"'
        args = args.split()
        try:
            args = self.__do_set_parser.parse_args(args)
        except SystemExit as wrong_args:
            # --help or wrong-args
            return
            self.__do_set_parser.print_usage()
            print(type(wrong_args), wrong_args)
            return

        
        if args.comments is not None:
            b = self.comments = args.comments
            print(self.str_set_flag('comments', b))
        if args.posix is not None:
            b = self.posix = args.posix
            print(self.str_set_flag('posix', b))

        if args.comments is None and args.posix is None:
            print('comments = {}; posix = {};'
                  .format(self.comments, self.posix))
        return
    do_set.__doc__ = __do_set_parser.format_help()

    
    
    def do_cmd(self, args):
        'show how the shell split args by calling "py -m args ARGS"'
        cmd = 'py -m args {}'.format(args)
        self.subcall(cmd)

##    def decode_output(self, output):
##        
##        encoding = sys.getfilesystemencoding()
##        output = output.decode(encoding)
##        return output

    def subcall(self, cmd):
        try:
            outs, errs, returncode, is_timeout = decoded_cmd_call(cmd)
        except Exception as e:
            print('Exception:', e, file=sys.stderr)
            return None
        except BaseException as e:
            print('BaseException:', e, file=sys.stderr)
            return None
##        
##        outs = self.decode_output(outs)
##        errs = self.decode_output(errs)
        
        if returncode:
            print('returncode: {}'.format(returncode), file = sys.stderr)
            print('stderr output: ', errs, file = sys.stderr)
        
        print(outs)
        return returncode
    
    def do_shell(self, args):
        '''execute shell call; use "!" as alias.

example: "! cmd /k @dir"
'''
        cmd = args
        self.subcall(cmd)
        
            
    def do_show(self, args):
        'echo args'
        print(args)
        
    def do_shlex(self, args):
        'show how the shell split args by calling shlex.split(args)'
        r = shlex.split(args, comments = self.comments, posix = self.posix)
        print(r)

    def do_quote(self, args):
        'to quote args by shlex.quote(args)'
        r = shlex.quote(args)
        print(r)

        
    def do_bye(self, arg):
        'exit'
        return True


    def precmd(self, line):
        return line
    def postcmd(self, stop, line):
        print()
        return stop

##    def postloop(self):
##        try:
##            self.do_set_parser.exit(0) # 'ArgumentParser.exit'
##        except SystemExit as e:
##            # print('hi, SystemExit', e, file = sys.stderr)
##            raise


def main(args=None):
    parser = argparse.ArgumentParser(
        #add_help = True,
        description = 'To figure out what args the command-line tools will get.',
        epilog = '"?" for help; "bye" to quit.')

    parser.parse_args(args)
    ArgsShowShell().cmdloop()
    parser.exit(0)
    
    
if __name__ == '__main__':
    main()
    




