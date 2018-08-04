

import re
meta_chars = '()%!^"<>&|'
meta_char_rex = re.compile(r'([{}])'.format(meta_chars))
def escape_arguments_for_cmd_exe(args):
    return ' '.join(map(escape_argument_for_cmd_exe, args))
def escape_argument_for_cmd_exe(old_arg):
    new_arg = '"{}"'.format(old_arg.replace('"', r'\"'))
    return _escape_argument_for_cmd_exe(new_arg)
def _escape_argument_for_cmd_exe(arg):
    def f(m):
        c = m.group(1)
        return '^'+c
    arg = meta_char_rex.sub(f, arg)
    return arg
    return ''.join('^'+c if c in meta_chars else c for c in meta_chars)

r'''
# http://stackoverflow.com/questions/29213106/how-to-securely-escape-command-line-arguments-for-the-cmd-exe-shell-on-windows
import re

def escape_argument(arg):
    # Escape the argument for the cmd.exe shell.
    # See http://blogs.msdn.com/b/twistylittlepassagesallalike/archive/2011/04/23/everyone-quotes-arguments-the-wrong-way.aspx
    #
    # First we escape the quote chars to produce a argument suitable for
    # CommandLineToArgvW. We don't need to do this for simple arguments.

    if not arg or re.search(r'(["\s])', arg):
        arg = '"' + arg.replace('"', r'\"') + '"'

    return escape_for_cmd_exe(arg)

def escape_for_cmd_exe(arg):
    # Escape an argument string to be suitable to be passed to
    # cmd.exe on Windows
    #
    # This method takes an argument that is expected to already be properly
    # escaped for the receiving program to be properly parsed. This argument
    # will be further escaped to pass the interpolation performed by cmd.exe
    # unchanged.
    #
    # Any meta-characters will be escaped, removing the ability to e.g. use
    # redirects or variables.
    #
    # @param arg [String] a single command line argument to escape for cmd.exe
    # @return [String] an escaped string suitable to be passed as a program
    #   argument to cmd.exe

    meta_chars = '()%!^"<>&|'
    meta_re = re.compile('(' + '|'.join(re.escape(char) for char in list(meta_chars)) + ')')
    meta_map = { char: "^%s" % char for char in meta_chars }

    def escape_meta_chars(m):
        char = m.group(1)
        return meta_map[char]

    return meta_re.sub(escape_meta_chars, arg)
'''










