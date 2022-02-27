
r'''
e ../../python3_src/script/try_python/try_num_max_recur.py
py -m script.try_python.try_num_max_recur
    #Exception: max: 993

#'''

def try_num_max_recur(N, /):
    def f(n, /):
        if n > 0:
            try:
                f(n-1)
            except RecursionError:
                raise Exception(f'max: {(N-n)}')
        f(0)
    f(N)

try_num_max_recur(20000)
    #Exception: max: 993
