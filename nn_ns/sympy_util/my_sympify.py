
from sympy import expand, nsimplify, powsimp, trigsimp, sympify, simplify
def my_sympify(y):
    ans = y
    ans = expand(ans)
    #ans = nsimplify(ans)
    ans = powsimp(ans)
    ans = trigsimp(ans)
    ans = sympify(ans)
    ans = simplify(ans)
    return ans
    
