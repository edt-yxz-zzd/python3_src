

'''
to work with builtin/immutable types, we provide XXX_OpsABC interface
to ease imodify_operation, we have XXX_WrappedOpsABC
to ease XXX_WrappedOps creation, we require XXX_OpsABC.wrapped
'''


class OpsABC:
    '''

though we can use a wrap class to handle other class,
but if the target is immutable, code will be "me = me.replace(xxx=xxx...)"
that was too terrible

let the object keep immutable in I/O form (e.g. in container like set)
    and we wrap it while it be a local variable.
but use which wrapper??
there are many possible wrapped classes, and so many wrapperes.
we should offer a wrapper at the same time!!

to implement a same function, different underly classes may require
different basic actions, generic version may be too inefficient or impossible.
yet we can override them...only if they present as methods of wrapper base class!!
1) we could not have foreseen such requirements when we start
2) the number of methods will grow more and more,
    and the base class become a package itself.
    do we want to subclass a package??


this Ops class is INDEED a package itself.
first we create an ops obj
and then insert more and more free function into it as its method

'''
    def wrapped(self):
        
