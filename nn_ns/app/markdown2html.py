
'''
markdown to html
*.md -> *.html
'''


from pathlib import Path
import subprocess
import os.path
import glob

def main(args=None):
    import argparse

    parser = argparse.ArgumentParser(
        description='markdown to html: *.md -> *.html'
        , epilog='''
using pandoc:
    pandoc -f markdown -t html -s -o XXX.html    XXX.md
'''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('input_glob_pattern', type=str
                        , help='input glob pattern')

    args = parser.parse_args(args)
    input_glob_pattern = args.input_glob_pattern
    args = 'pandoc -f markdown -t html -s -o'.split()
    for path in glob.iglob(input_glob_pattern):
        ext = path[-3:].lower()
        if ext != '.md':
            raise Exception(f'not *.md: {path!r}')
        opath = path[:-3] + '.html'
        if os.path.exists(opath):
            raise FileExistsError(f'*.html exists: {opath!r}')
        args.append(opath)
        args.append(path)
        subprocess.run(args)
        args.pop()
        args.pop()



if __name__ == "__main__":
    main()


