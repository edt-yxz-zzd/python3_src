

def accumulate_product_mod(N):
    ls = [1]
    for i in range(1, N):
        ls.append((ls[-1] * i) % N)
    return ls


def show(N):
    for n in range(1, N+1):
        print(n, accumulate_product_mod(n))

show(100)






















