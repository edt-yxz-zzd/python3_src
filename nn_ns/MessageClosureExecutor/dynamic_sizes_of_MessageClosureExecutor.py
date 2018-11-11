
__all__ = '''
    dynamic_sizes_of_MessageClosureExecutor
    '''.split()


'''
all_actions
all_messages
interface2messages
interface2actions
'''
def dynamic_sizes_of_MessageClosureExecutor(e):
    return {
        'all_actions': len(e.all_actions)
        ,'all_messages': len(e.all_messages)
        ,'interface2messages':
            (len(e.interface2messages), sum(map(len, e.interface2messages.values())))
        ,'interface2actions':
            (len(e.interface2actions), sum(map(len, e.interface2actions.values())))
        }

