


r'''
https://stackoverflow.com/questions/33560364/python-windows-parsing-command-lines-with-shlex

'''

__all__ = ['cmd_parse']
import re

RE_CMD_LEX = r'''"((?:""|\\["\\]|[^"])*)"?()|(\\\\(?=\\*")|\\")|(&&?|\|\|?|\d?>|[<])|([^\s"&|<>]+)|(\s+)|(.)'''
cmd_re = re.compile(RE_CMD_LEX)

def cmd_parse(s):
    args = []
    accu = None   # collects pieces of one arg
    for qs, qss, esc, pipe, word, white, fail in cmd_re.findall(s):
        if word:
            pass   # most frequent
        elif esc:
            word = esc[1]
        elif white or pipe:
            if accu is not None:
                args.append(accu)
            if pipe:
                args.append(pipe)
            accu = None
            continue
        elif fail:
            raise ValueError("invalid or incomplete shell string")
        elif qs:
            word = qs.replace('\\"', '"').replace('\\\\', '\\')
            word = word.replace('""', '"')
        else:
            word = qss   # may be even empty; must be last

        accu = (accu or '') + word

    if accu is not None:
        args.append(accu)

    return args




