

__all__ = '''
    get_MessageClosureExecutor_properties
    show_MessageClosureExecutor
    '''.split()


from pprint import pprint

# MessageClosureExecutor
all_properties = '''
    interface_constraint
    action_constraint
    action_constructor2function
    message_constructor2function
    all_actions
    all_messages
    interface2messages
    interface2actions
    auto_action_constructor2maker
    interface_constructor2auto_action_constructors
    '''.split()


def get_all_properties(obj):
    return dict(iter_get_all_properties(obj))
def iter_get_all_properties(obj):
    cls = type(obj)
    for attr in dir(cls):
        value = getattr(cls, attr)
        if isinstance(value, property):
            yield attr, getattr(obj, attr)

def get_MessageClosureExecutor_properties(e:'MessageClosureExecutor'):
    d = get_all_properties(e)
    try:
        assert set(all_properties) <= set(d)
    except:
        print(list(d))
        raise
    return d
def show_MessageClosureExecutor(e:'MessageClosureExecutor'):
    d = get_MessageClosureExecutor_properties(e)
    pprint(d)

