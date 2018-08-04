
def do_work(expr):
    r = safe_eval(expr)
    print(repr(r))
if __name__ == '__main__':
    import sys
    from seed.helper.safe_eval import safe_eval
    args = sys.argv[1:]
    if args:
        expr = ' '.join(args)
        do_work(expr)
    else:
        for line in sys.stdin:
            line = line.strip()
            if not line: continue
            expr = line
            do_work(expr)


