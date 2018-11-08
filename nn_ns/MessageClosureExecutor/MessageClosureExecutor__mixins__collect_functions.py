
__all__ = '''
    MessageClosureExecutor__mixins__collect_functions
    '''.split()

from .MessageClosureExecutor_ABC__with_data import \
    MessageClosureExecutor_ABC__with_data
from .collect_functions import collect_functions
from .abc import abstractmethod

class MessageClosureExecutor__mixins__collect_functions(
    MessageClosureExecutor_ABC__with_data
    ):
    '''
assume:
    message_constructor/action_constructor is string
        and can be used to generate method name
    message_function/action_function is method
'''
    def __init__(self, *
        ,all_message_constructors
        ,interface_constraint
        ,action_constraint
        ,initial_xmessages
        ,auto_action_constructor2maker
        ,interface_constructor2auto_action_constructors

        ,xmessage_queue=None
        ,all_messages=None
        ,interface2messages=None
        ,all_actions=None
        ,interface2actions=None
        ):
        af_fmt = self.get_action_function_name_foramt()
        mf_fmt = self.get_message_function_name_foramt()

        action_constructor2function = collect_functions(
            self, af_fmt, action_constraint)
        message_constructor2function = collect_functions(
            self, mf_fmt, all_message_constructors)

        super().__init__(
            interface_constraint=interface_constraint
            ,action_constraint=action_constraint
            ,action_constructor2function=action_constructor2function
            ,message_constructor2function=message_constructor2function
            ,initial_xmessages=initial_xmessages
            ,auto_action_constructor2maker
                =auto_action_constructor2maker
            ,interface_constructor2auto_action_constructors
                =interface_constructor2auto_action_constructors

            ,xmessage_queue=xmessage_queue
            ,all_messages=all_messages
            ,interface2messages=interface2messages
            ,all_actions=all_actions
            ,interface2actions=interface2actions
            )


    #@abstractmethod
    def get_action_function_name_foramt(self):
        return '{}'
        return 'af_{}'
    #@abstractmethod
    def get_message_function_name_foramt(self):
        return '{}'
        return 'mf_{}'

