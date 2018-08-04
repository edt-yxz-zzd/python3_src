
'''
parse_known_args is not a prefix parse method
    it ignore unknown option and continue!!
'''



import argparse



parser = argparse.ArgumentParser(description='try parse_known_args')
parser.add_argument('1', type=str,
                    help='read after unknown?')
parser.add_argument('-k', type=str,
                    help='known')

try:
    parser.parse_known_args('-k s -unknown 1'.split())
except SystemExit as e:
    'error: argument -k: expected one argument'
    assert str(e) == 2 # exit code??

r = parser.parse_known_args('1 -unknown -k s'.split())
assert str(r) == "(Namespace(1='1', k='s'), ['-unknown'])"


    


