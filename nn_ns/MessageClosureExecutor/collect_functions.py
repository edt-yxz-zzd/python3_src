
r'''
helper to build
    action_constructor2function
    message_constructor2function
usage:
    action_constructor2function = \
        collect_functions(self, 'ac_{}', action_constructors)
    message_constructor2function = \
        collect_functions(self, 'mc_{}', message_constructors)
'''


def collect_functions(obj, fmt, names):
    return {name: getattr(obj, fmt.format(name)) for name in set(names)}


