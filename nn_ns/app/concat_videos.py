

r'''
ffmpeg -f concat -safe 0 -i mylist.txt -c copy 20516451.flv
where "mylist.txt":
# not file "20516451-1-15.flv"
file '20516451-1-15.flv'
file '20516451-2-15.flv'
file '20516451-3-15.flv'
file '20516451-4-15.flv'


BUT:
    does ffmpeg using utf8 to decode mylist.txt?
    does ffmpeg escape "'" by r"\'"?
    below "concat_videos" using assumption both "YES"


#####################################
https://ffmpeg.org/ffmpeg-utils.html#Quoting-and-escaping
2.1 Quoting and escaping
    FFmpeg adopts the following quoting and escaping mechanism, unless explicitly specified. The following rules are applied:

        "'" and "\" are special characters (respectively used for quoting and escaping). In addition to them, there might be other special characters depending on the specific syntax where the escaping and quoting are employed.
        A special character is escaped by prefixing it with a "\".
        All characters enclosed between "''" are included literally in the parsed string. The quote character "'" itself cannot be quoted, so you may need to close the quote and escape it.
        Leading and trailing whitespaces, unless escaped or quoted, are removed from the parsed string. 

    Note that you may need to add a second level of escaping when using the command line or a script, which depends on the syntax of the adopted shell language.

    The function av_get_token defined in libavutil/avstring.h can be used to parse a token quoted or escaped according to the rules defined above.

    The tool tools/ffescape in the FFmpeg source tree can be used to automatically quote or escape a string in a script.
    2.1.1 Examples

        Escape the string Crime d'Amour containing the ' special character:

        Crime d\'Amour

        The string above contains a quote, so the ' needs to be escaped when quoting it:

        'Crime d'\''Amour'

        Include leading or trailing whitespaces using quoting:

        '  this string starts and ends with whitespaces  '

        Escaping and quoting can be mixed together:

        ' The string '\'string\'' is a string '

        To include a literal "\" you can use either escaping or quoting:

        'c:\foo' can be written as c:\\foo
'''

from seed.exec.cmd_call import decoded_cmd_call
import os.path
import sys
#from tempfile import NamedTemporaryFile
from io import StringIO

class Global:
    list_fname_encoding = 'utf8'
    @classmethod
    def quote_and_escape_path(cls, path):
        # "'" -> r"'\''" # end quote "'" + escaped r"\'" + begin quote "'"
        # "\\" -> r"'\\'" # end quote "'" + escaped r"\\" + begin quote "'"
        # ^ -> "'" # begin quote "'"
        # $ -> "'" # end quote "'"
        path = path.replace("'", r"'\''")
        path = path.replace("\\", r"'\\'")
        return f"'{path!s}'"

def concat_videos(ofname, ifnames):
    # '-' is stdin, should avoid it by: abspath
    list_fname_encoding = Global.list_fname_encoding
    quote_and_escape_path = Global.quote_and_escape_path

    ifnames = tuple(ifnames)
    if len(ifnames) < 2: raise TypeError
    if os.path.exists(ofname): raise FileExistsError(ofname)
    if not all(map(os.path.exists, ifnames)):
        raise FileNotFoundError([n for n in ifnames
                                if not os.path.exists(n)])

    ifnames = tuple(map(os.path.abspath, ifnames))
    ofname = os.path.abspath(ofname)


    r'''
    with NamedTemporaryFile(mode='wt', encoding=list_fname_encoding) as list_fout:
        list_fname = list_fout.name
        input = None
        for ifname in ifnames:
            print("file '{}'".format(ifname.replace("'", r"\'")), file=list_fout)
        cmd = 'ffmpeg -f concat -safe 0 -i'.split() + [list_fname] + '-c copy'.split() + [ofname]
        outs, errs, returncode, is_timeout =\
            decoded_cmd_call(cmd, input=input, timeout=None, encoding=None)
            # D:\TEMP_O~1\SYSTEM~1\tmptyha2lak: Permission denied
            # NamedTemporaryFile can not be openned by ffmpeg??
    '''
    list_fout = StringIO()
    list_fname = '-' # stand for "stdin"
    if True:
        for ifname in ifnames:
            print("file {}".format(quote_and_escape_path(ifname)), file=list_fout)
        cmd = 'ffmpeg -f concat -safe 0 -i'.split() + [list_fname] + '-c copy'.split() + [ofname]
        #print(' '.join(cmd))
        input = list_fout.getvalue()
        #print(input)
        input = input.encode(list_fname_encoding) # must be 'bytes' not 'str'

        outs, errs, returncode, is_timeout =\
            decoded_cmd_call(cmd, input=input, timeout=None, encoding=None)
    print(errs, file=sys.stderr)
    print(outs, file=sys.stdout)
    return returncode

def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser(description='concat videos using FFmpeg')
    parser.add_argument('fnames', type=str, nargs='+' # '>=2'
                        , help='input file paths')
    parser.add_argument('-o', '--output', type=str, required=True
                        , help='output file path')


    args = parser.parse_args()
    ofname = args.output
    ifnames = args.fnames

    concat_videos(ofname, ifnames)




if __name__ == "__main__":
    main()


