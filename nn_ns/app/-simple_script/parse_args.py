

'''
def xxx_cmd(input_path:'the input path'
        , *input_paths:'*: input paths'
        , iencoding:'-ie --input_encoding: input encoding'
            # without value - required
            #   cannot "=None" see below "verbose=None" for "switch"
        , output_path:'-o --output: the output path; default to stdout' = ''
            # '' - the default value
        , oencoding:'-oe --output_encoding: outnput encoding' = (None, 'gbk, 'utf8')
            # tuple - choices; the first element is the default choice
            # None - required
            # if the first element is not None: optional
        , verbose:'-v --verbose: show details' = False
            # False - optional
            # if None - required
        ):
def xxx_cmd(parameter1, parameter2, *, required_parameter3:'flag3_1 flag3_2', optional_parameter4:'flag4'='xxxx', parameter5:'switch5'=False):
    args = parse_args(xxx_cmd, locals())
    ...

positional_argument = parameter ':' help_str ('=' default_str)?
star_argument = '*' parameter ':' range_and_help_str
keywordonly_argument = parameter ':' flags_and_help_str ('=' True | False | None | default_str | ((None,)|())+tuple<str>{.len>=2})
    # None (the one not in tuple) for bool; without '=' for str
help_str = string
range_and_help_str = regex"\s*{range}\s*:\s*{help_str}\s*"
flags_and_help_str = regex"\s*{flag}(\s+{flag})*\s*:\s*{help_str}\s*"
range = regex'\s*([+?*]|{{\s*{UInt}\s*,\s*{UInt}\s*}})\s*'
flag = regex'-[^\s=]'
UInt=regex'0|[1-9][0-9]*'
'''


