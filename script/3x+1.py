


'''
f : odd -> odd
f odd = 3*odd // 2^n
odd2uint, uint2odd
g : uint -> uint
g = odd2uint . f . uint2odd

i -> j
j = ((3*(2*i+1)+1)//2^n -1)//2
    = ((6*i+4)//2^n -1)//2
    = ((3*i+2)//2^n -1)//2

let 2*j+1 == (3*i+2)//2^n
    3*i+2 == (2*j+1)*2^n
    i = ((2*j+1)*2^n - 2)//3
    3 | (2*j+1)*2^n - 2
    case 2^n of
        3*u -> 3|-2 fail
        3*u+1 -> 3|(2j+1)-2 = 3|2j-1 ==>> j=(3v'+1)//2=3v+2
            2^n mod 3 = (-1)^n mod 3 = (n mod 2)+1
            2^n -1 mod 3 = n mod 2
            2^n == 3*u+1 => 3|2^n-1 => n=2*s
          1)i = ((6v+5)*4^s - 2)//3; j=3v+2
            j = ((3v+2)*3+2 - 2)//3 = ((9v+8) -2)//3
        3*u+2 -> 3|(2j+1)*2-2 = 3|4j ==>> j=3v
            3|2^n-2 => n=2*s+1
          2)i = ((6v+1)*2*4^s - 2)//3; j=3v
            j = ((3v)*3+2 - 2)//3 = ((9v+2) -2)//3
    let (9u+8|9u+2)==(6v+5|12v+2)*4^s==(4k+r123)*(9t+r1_8)
        == (36kt + 4*r1_8*k + 9*r123*t + r123*r1_8)
    let 9u+8=(6v+5)*4^s=(6v+5)(3k+1)=18vk+15k+6*v+5
        9u+3=18vk+15k+6*v
        3u+1=6vk+5k+2*v
        mod 3: 1==5k+2v==2v-k; k==2v-1==2v+2
        mod 3: 1==5k+2v==2k-v; v==2k-1==2k+2
        let v = 3t+(2k+2) = 3t+2(3k+3)//3 = 3t+2(4^s+2)//3
        3u+1=6(3t+2k+2)k+5k+2*(3t+2k+2) = 18tk+12kk+12k+5k+6t+4k+4
            = 18tk+12kk+21k+6t+4
        u = 6tk+2kk+7k+2t+1 = 2t(3k+1) + (2k+1)(k+3) - 2
            = 2t(3k+1) + (3k+1-k)(k+3) - 2
            = 2t(3k+1) + (3k+1)(k+3) -k(k+3) - 2
            = 2t(3k+1) + (3k+1)(3k+1+8)//3 -(3k+1-1)(3k+1+8)//9 - 2
            = 2t*4^s + 4^s(4^s+8)//3 - (4^s-1)(4^s+8)//9 - 2



----
let i == 2*k+1
    = ((6*k+5)//2^n -1)//2
    = ((6*k+5) -1)//2
    = (6*k+4)//2
    = (3*k+2)
    = (3*i+1)//2
    = 3*(i-1)//2+2
#let i == (2*k+1)*2^m ; m >= 0

-----
'''

def is_even(uint):
    return not is_odd(uint)
def is_odd(uint):
    return uint & 1
def odd2odd(odd):
    i = 3*odd+1
    while is_even(i):
        i >>= 1
    return i

def uint2odd(u):
    return 2*u+1
def odd2uint(odd):
    return (odd-1)//2
def uint2uint(u):
    return odd2uint(odd2odd(uint2odd(u)))

for i in range(100):
    j = uint2uint(i)
    if i < j: print(i, j)




