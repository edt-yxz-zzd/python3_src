
from ast import literal_eval as e

int('-1')
# int('--1') # error
e('--1')

# e('set()') # error

e('[]')
# e('[0][0]') # error
# e('[].__class__') # error
# e('[x for x in []]') # error


