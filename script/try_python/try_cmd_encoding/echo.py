
'''
fail for arbitrary input

it seems better to be:
sys.stdin = sys.stdin.detach() # to binary mode


'''

import sys

for line in sys.stdin:
    print(line)

