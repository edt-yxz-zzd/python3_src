
# differ g(*xs) and g(xs...):
#   len(*xs) known at runtime, but sizeof(xs...) known at compiletime

let xs... = ', '.join(xs)
let xs**... = ', '.join('{0}={0}'.format(x) for x in xs)
LS n name = [name + str(i) for i in range(n)]
    LS 2 'x' = ['x0', 'x1']
    
math function
    g(xs..., *, frees...) # no *args, no **kwargs, no defaults
        # but high order functor will have **kwargs?????????? NOOOOOO
        def nargs(g) = sizeof(g.xs...)
        def free_names(g) = g.frees
        def g.subs(frees1={}, **frees2) = g **free1 **free2

    partial call:
    if nargs(g) = 0:
        g = g()  # no side effect
        \:expr = expr
        1 = 1()
        nargs(1) = 0
    else:
        g x = \LS(nargs(g)-1, 'x')...: g(x, LS(nargs(g)-1, 'x')...)
        
    g *x0s = g if not x0s else g x0s[0] *x0s[1:]
    g *() = g
    
    g v=x = g.subs(v=x) = \LS(nargs(g), 'x')...: g(LS(nargs(g), 'x')..., *, v=x)
    g v=x v=y = g v=x
    
    let f = (\xs..., *, frees...: expr)
        if v in frees:
            f.subs(v=x) = \xs..., *, (frees-{'v'})...: f xs..., v=x, (frees-{'v'})**...
        else:
            f.subs(v=x) = f
    
    
    

iter_functor
    f(iterable)
    sum
    II


function without free variable
    g(xs...)
    
    sin(z)
    C(n,k)
    
    sin = \z: sin(z)
    choose = \n,k: C(n,k)

function withonly free variable = expression
    g(*, frees...)
    S(*, n,k) = sum C(i,k) {i=0..n-1} = sum(C(i,k) for i in range(n)) = C(n,k+1)

    E(*, n) = (1+1/n)**n
    e = lim E {n->inf} = lim E(n=n) {n->inf}
    
    \*,n0: lim expr {n->n0} = lim expr.subs(n=n) {n->n0}
    

functor #
    f(x, *, frees...)
    f z is an expression
    
    
    ff(n, *, k) = fall(n,k) = II n-i {~i=0->k}
    
    dff a functor:
        dff f = \@0,*, f.frees...: f(@0+1, f.frees**...) - f(@0, f.frees**...)
        
        dff ff k=d = d * ff k=(d-1)
        dff ff k=k = k * ff k=(k-1)
    
    otherwise dff about a freevarible
    if 'n' not in f.frees...:
        dff@n sum f(n) {~n} = dff@n sum f(i) {~i=0->n} 
            = \*,n, f.frees...: f(n, f.frees**...)
    else:
        dff@n sum f(n, n=n) {~n} = dff@n sum f(i, n=n) {~i=0->n}
            = sum f(i, n=n+1) {~i=0->n+1} - sum f(i, n=n) {~i=0->n}
            = f(n,n=n+1) + sum dff@n f(i) n=n {~i=0->n+1}


functor to expression
    T1 name f = \LS(nargs(f)-1, '@')..., *, (f.frees+{name})...: \
                f(([name]+LS(nargs(f)-1, '@'))..., f.frees...)
expression to functor
    Tv name g = \LS(nargs(g)+1, '@')..., *, (g.frees-{name})...: \
                g(LS(nargs(g)+1, '@')[1:]..., ({name:@0}+g.frees)...)
    
    f(x,*,z) = x+z
        DD f = \x,*,z: z
        DD@x (\*,x,z: x+z) = \*,x,z: z
        Tv 'x' (\*,x,z: x+z) = \@0: (\*,x,z: x+z) x=@0 = \x,*,z: x+z
        
        DD@x expr = \*, (expr.frees+{x})...: DD (Tv 'x' expr) x
            = T1 'x' (DD (Tv 'x' expr))
    DD@x = T1 'x' . DD . Tv 'x'
        
    
    DD sin = DD@z (\*,z:sin z)





















function
    g(xs..., *, frees...)  # xs, frees are sets of names
        def len_noname(g) = len(g.xs)
        def free_names(g) = set(g.frees)
        def domain_nonames(g) = [domain(x) for x in g.xs]
        def domain_names(g) = {name:domain(name) for name in g.frees}
    
    partial call:
    # x0s is a list of arg
    # f0s is a dict in form {name : arg}
    let E g x0s = (exclude g len(x0s)) = g.xs[len(x0s):]
    let E g f0s = (exclude g f0s.keys()) = list(set(g.frees) - f0s.keys())
    
    g *x0s = \(E g x0s)..., *, g.frees...: g(*(x0s+E g x0s), g.frees**...)
    g **f0s = \g.xs..., *, (E g f0s)...: g(*g.xs, (E g f0s)**..., **f0s)
    g *x0s **f0s = ((g *x0s) **f0s) = ((g **f0s) *x0s)
    g *x0s *x1s = g *(x0s+x1s)
    g **f0s **f1s = g **(f0s+f1s)
    
    g *() = \g.xs...,*,g.frees...: g(*g.xs, g.frees**...) = g
    ['z' not in g.frees]: g z=sth = g **{'z':sth} = g **{} = g
    ==>> g k=a k=b = g k=a
    
    def g.subs(f0s) = g **f0s


f z = 1 <==> [any z]: f z = 1 <==> f = \z: 1


functor and function with/without free variable
    g(x) = \y: f(x,y)    # this is a functor: g x y = f(x,y)
    g(x,y) = x+y         # this is a function without free variable
    g() = g = \*, x=a, y=b: a+b # this is a function with free variable
    
polynomial about x:
    [free y]: \x: (x+y)
    \x: \*,y=y:(x+y)
polynomial about z:
    [free x,y]: \z: (x+y)
    \z: \*,x=x,y=y:(x+y)
    
def to_polynomial_about(g, *xs):
    # g = \*, x=x, y=y: x+y; xs=['x', 'z']
    kws = get_kwarg_names(g) # {'x', 'y'}
    new_kws = ', '.join('{}={}'.format(x,x) for x in xs) # 'x=x, z=z'
    '\*,{args}:'
