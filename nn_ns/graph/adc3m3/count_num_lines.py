

import argparse
import traceback

def main(args=None):
    parser = argparse.ArgumentParser(description='count number of lines')
    parser.add_argument('file', type=argparse.FileType('r'),
                        help='source')
    parser.add_argument('line_no', type=int, nargs='*',
                        default = [],
                        help='show the line')
    parser.add_argument('-H', '--hold', action='store_true',
                        default = False,
                        help='remain to execute command')

    args = parser.parse_args()
    d = dict.fromkeys(args.line_no)
    line2pos = []
    locals_dict = {}
    globals_dict = {}
    def show(i):
        'show ith line of file'
        
        fin.seek(line2pos[i])
        s = fin.readline()
        print(s)

    locals_dict['show'] = show



    ##################################################
    with args.file as fin:
        i = -1
        line2pos.append(fin.tell())
        while fin:
        #for i, line in enumerate(fin):
            # OSError: telling position disabled by next() call
            # strange!!!!
            line = fin.readline()
            if not line: break
            assert line[-1] == '\n'
            i += 1 # line_no
            assert i == len(line2pos)-1
            
            line2pos.append(fin.tell()) # next line begin
            
            if i in d:
                d[i] = line
                print('{}:{}'.format(i, line))
        else:
            print('bool(fin) ==', bool(fin))
            
        total_lines = i+1
        assert total_lines == len(line2pos)-1
        print('total_lines:', total_lines)


        ##########################################################
        # shell...
        locals_dict['total'] = total_lines
        print('\n'*2)
        print('>'*75)
        print('locals:', sorted(locals_dict))
        print('You can use "show(line_no)" to show that line.')
        #print('quit() or exit() to exit')
        print(quit)
        print(exit)
        print('\n'*2)

        
        while args.hold:
            try:
                stat = input('>>> ')
            except KeyboardInterrupt:
                print()
                raise
            
            if not stat.strip(): continue

            
            try:
                r = eval(stat, globals_dict, locals_dict)
                if r is not None:
                    print(repr(r))
            except Exception as e:
                #print(file=sys.stderr)
                traceback.print_exc()

    parser.exit(0)
    return 0


if __name__ == '__main__':
    main()













                












