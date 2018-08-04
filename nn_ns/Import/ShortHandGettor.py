

'''
local short hand:
    from ._get_ import xxx

___get___.py
    lazy import local shorthand:
        from ._get_ import xxx
        first search "xxx" in ".___get___",
            notfount then search "xxx" in "..___get___",
            and so on.
    ___get___.py can forward the query:
        __default_fallback__ = [pkg/mod...]
        __forward_to__ = {name:pkg/mod}
        __declare__ = {pkg/mod:names}
    set upperbounded:
        from ._get_...upperbounded import xxx
        from ._get_...mid...upperbounded import xxx
    set grandson as upperbounded:
        from ._get_.son.grand import xxx


theShortHandGettor :: MetaPathFinder
when theShortHandGettor invoke?
    given qname
    remove all _get_
    search its preifx
    if preifx registered, then invoke; else pass it

'''

from importlib.abc import MetaPathFinder

'''
def is_qname_to_be_handle_ex(qname):
    _get_ = '_get_'
    names = qname.split('.')
    org_qname = '.'.join(name for name in names if name != _get_)
    if len(org_qname) == len(qname):
        # _get_ not in qname
        return False
    prefix = get_shortest_prefix_registered(org_qname)
    if not prefix:
        #if not has_prefix_registered(org_qname):
        return False
    # handle registered package
    return prefix, org_qname, names
'''

qname_re = re.compile(r'^((?!\W_get_\W).)*\._get_$')
class TheShortHandGettor(MetaPathFinder):
    # from .afaf._get_ import xxx
    # _get_ is at last
    # regex for qname = r'^((?!\W_get_\W).)*\._get_$'
    def find_spec(qname, maybe_parent_pkg_paths, reload_target_module=None):
        # -> (None | module_spec)
        if reload_target_module is None: raise NotImplementedError
        ___get___ = '___get___'
        _get_ = '_get_'
        dot_get_ = '._get_'
        if not qname.endswith(dot_get_): return
        m = qname_re.match(qname)
        if not m: return

        L = len(qname)
        qname[:-len(dot_get_)]


