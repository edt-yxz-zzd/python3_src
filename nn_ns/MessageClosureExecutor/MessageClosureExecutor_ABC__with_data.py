
__all__ = '''
    MessageClosureExecutor_ABC__with_data
    '''.split()

from .MessageClosureExecutor_ABC import (
    MessageClosureExecutor_ABC
    ,MessageClosureExecutor_EmptyError
    )

from collections import defaultdict

class MessageClosureExecutor_ABC__with_data(MessageClosureExecutor_ABC):
    def __init__(self, *
        ,interface_constraint
        ,action_constraint
        ,action_constructor2function
        ,message_constructor2function
        ,initial_xmessages
        ,auto_action_constructor2maker
        ,interface_constructor2auto_action_constructors

        ,xmessage_queue=None
        ,all_messages=None
        ,interface2messages=None
        ,all_actions=None
        ,interface2actions=None
        ):
        if initial_xmessages is None:
            initial_xmessages = ()
        if xmessage_queue is None:
            xmessage_queue = []
        if all_messages is None:
            all_messages = set()
        if interface2messages is None:
            interface2messages = {}# defaultdict(list)
        if all_actions is None:
            all_actions = set()
        if interface2actions is None:
            interface2actions = {}#defaultdict(list)
        assert not isinstance(interface2messages, defaultdict)
        assert not isinstance(interface2actions, defaultdict)

        self.__interface_constraint = interface_constraint
        self.__action_constraint = action_constraint
        self.__action_constructor2function = action_constructor2function
        self.__message_constructor2function = message_constructor2function

        self.__initial_xmessages = initial_xmessages
        self.__xmessage_queue = xmessage_queue
        self.__all_messages = all_messages
        self.__interface2messages = interface2messages
        self.__all_actions = all_actions
        self.__interface2actions = interface2actions
        self.__auto_action_constructor2maker \
            = auto_action_constructor2maker
        self.__interface_constructor2auto_action_constructors \
            = interface_constructor2auto_action_constructors
        super().__init__()

    def __get_auto_action_constructor2maker__(self):
        #:: {ActionConstructor: Interface -> Action}
        # immutable
        return self.__auto_action_constructor2maker
    def __get_interface_constructor2auto_action_constructors__(self):
        #:: {InterfaceConstructor:{ActionConstructor}}
        # immutable
        return self.__interface_constructor2auto_action_constructors
    def __get_interface_constraint__(self):
        #:: {InterfaceConstructor: MessageConstructor}
        # immutable
        return self.__interface_constraint
    def __get_action_constraint__(self):
        #-> {ActionConstructor: (InterfaceConstructor,)*n}
        # immutable
        return self.__action_constraint
    def __get_action_constructor2function__(self):
        #:: {ActionConstructor: Action -> (Message,)*n -> Iter XMessage}
        # immutable
        return self.__action_constructor2function
    def __get_message_constructor2function__(self):
        #:: {MessageConstructor: Message->Iter Interface}
        # immutable
        #constraint:
        #   cmsg = .message2constructor(msg)
        #   for intf in .message_constructor2function[cmsg](msg):
        #       cintf = .interface2constructor(intf)
        #       assert .interface_constraint[cintf] == cmsg
        #   .check_interface_message(intf, msg)
        return self.__message_constructor2function
    def __get_initial_xmessages__(self):
        #:: {XMessage}
        # immutable
        return self.__initial_xmessages





    '''
    def __get_xmessage_queue__(self):
        #:: Queue<XMessage>
        # mutable
        return self.__xmessage_queue
    '''
    def __get_all_messages__(self):
        #:: {Message}
        # mutable
        return self.__all_messages
    def __get_interface2messages__(self):
        #:: {Interface: [Message]} # defaultdict
        # mutable
        return self.__interface2messages
    def __get_all_actions__(self):
        #-> {Action} # mutable
        # mutable
        return self.__all_actions
    def __get_interface2actions__(self):
        #:: {Interface: [Action]} # iff interface in action.interfaces
        # mutable
        return self.__interface2actions











    def __push_xmessage_into_queue__(self, xmessage):
        # -> None
        self.__xmessage_queue.append(xmessage)
    def __pull_xmessage_outfrom_queue__(self):
        # -> XMessage | raise MessageClosureExecutor_EmptyError
        try:
            return self.__xmessage_queue.pop()
        except IndexError:
            raise MessageClosureExecutor_EmptyError
    def __is_xmessage_queue_empty__(self):
        # -> Bool
        return not self.__xmessage_queue
    def __clear_xmessage_queue__(self):
        # -> None
        self.__xmessage_queue.clear()

