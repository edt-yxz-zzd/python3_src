
why?
    "*.bat" is ugly # powershell "*.ps"???
target:
    to call python and shell command more easily
encoding:
    utf8
syntax:
    python_stmt[replace python_expr by expr]
    python_expr
    expr = python_expr | command
    command = atom_command
            | binary_op_command
    atom_command = simple_command
                    | open command close
    binary_op_command<command_binary_op> = atom_command (command_binary_op atom_command)+
    command_binary_op = command_and | command_or | command_chain
    simple_command = exe_op command_name command_argument*
    command_name = command_string
    command_argument = command_positional_argument | command_option_argument
    command_positional_argument = command_string
    command_option_argument = command_option_flag (eq command_option_payload)?
    command_option_flag = flag
    command_option_payload = command_string
    command_string = string | open (command | python_expr) close
    @@token_set@@:
        @@ignore@@ = regex"\s+"
        string = f?r?"..." | f?r?'...' # python string
        flag = regex"-[^:=\s]*"
        eq = '='
        open = '('
        close = ')'
        exe_op = '!'
        command_and = '&&'
        command_or = '||'
        command_chain = '>>>'
        #?? iostream redirect ??

################
bool(command) == (not ExitCode)
bytes(command) == bytes(stdout)
str(command, encoding) == str(stdout, encoding)
################
input parameters:
    input: parameter_name1 name2 ...
    parameter_name1 = -switch_name1 | -switch_name2             # optional
    parameter_name2 = -keyword1= | -keyword2=                   # required
    parameter_name3 = [-keyword3= | -keyword4=] defalut_str     # optional
    parameter_name4     # positional, required
    [parameter_name5]   # positional, optional
    parameter_names*    # positional
    parameter_names+    # positional
    parameter_names?    # positional
    parameter_names{...}    # positional

