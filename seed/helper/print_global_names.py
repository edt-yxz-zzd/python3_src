

'''
usage:
if __name__ == '__main__':
    for n in list(globals()): print(n)
    del n; print()

if __name__ == '__main__':
    from seed.helper.print_global_names import print_global_names
    print_global_names(globals())
'''

def print_global_names(names, prefix='    , '):
    for n in names:
        if n.startswith('_'): continue
        print(prefix+n)
    print()

