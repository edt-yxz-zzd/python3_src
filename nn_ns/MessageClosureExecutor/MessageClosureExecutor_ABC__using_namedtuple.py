
from .MessageClosureExecutor_ABC import (
    MessageClosureExecutor_ABC
    ,MessageClosureExecutor_TypeError
    )
from .MessageClosureExecutor_ABC__with_data import \
    MessageClosureExecutor_ABC__with_data
from .make_namedtuples import make_namedtuples
from .abc import abstractmethod

def namedtuple2type_name(named_tuple_obj):
    return type(named_tuple_obj).__name__

class MessageClosureExecutor_ABC__using_namedtuple(
    MessageClosureExecutor_ABC__with_data
    ):
    '''
assume
    namedtuple's type_name is Constructor
    type_name of Message/Interface/Action beginswith 'M'/'I'/'A'
    xmessage is (action|message) # without boxing
'''
    @classmethod
    @abstractmethod
    def get_namedtuples_in_str(cls):
        # format: see make_namedtuples
        # return namedtuples_in_str
        pass
    @classmethod
    @abstractmethod
    def get_interface_constraint(cls):
        #return interface_constraint
        pass
    @classmethod
    @abstractmethod
    def get_action_constraint(cls):
        #return action_constraint
        pass

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        #initial_xmessages = frozenset(cls.static_iter_initial_xmessages())
        action_constraint = cls.get_action_constraint()
        interface_constraint = cls.get_interface_constraint()
        namedtuples_in_str = cls.get_namedtuples_in_str()
        type_name2type = make_namedtuples(namedtuples_in_str)

        all_message_constructors = {type_name
            for type_name in type_name2type if type_name.startswith('M')}

        cls.all_message_constructors = all_message_constructors
        cls.action_constraint = action_constraint
        cls.interface_constraint = interface_constraint
        cls.name2constructor = type_name2type

    def __init__(self, *, initial_xmessages):
        #bug: cls = __class__
        cls = type(self)
        super().__init__(
            initial_xmessages = initial_xmessages

            ,all_message_constructors = cls.all_message_constructors
            ,interface_constraint = cls.interface_constraint
            ,action_constraint = cls.action_constraint
            )

    def interface2constructor(self, interface):
        #:: Interface -> InterfaceConstructor
        return namedtuple2type_name(interface)
    def message2constructor(self, message):
        #:: Message -> MessageConstructor
        return namedtuple2type_name(message)
    def action2constructor(self, action):
        #:: Action -> ActionConstructor
        return namedtuple2type_name(action)
    #def action2args(self, action):
        #:: Action -> ActionArgs
    def action2interfaces(self, action):
        #:: Action -> (Interface,)*n
        return tuple(action)






    def distinguish_xmessage(self, xmessage):
        #:: XMessage -> ((False, Action)|(True, Message))
        # -> (is_message, (Action|Message))
        type_name = namedtuple2type_name(xmessage)
        head = type_name[0]
        if head == 'M':
            message = xmessage
            return (True, message)
        elif head == 'A':
            action = xmessage
            return (False, action)
        else:
            raise MessageClosureExecutor_TypeError(f'not xmessage: {type_name!r}; {xmessage!r}')

    def message2xmessage(self, message):
        #:: Message -> XMessage
        return message
    def action2xmessage(self, action):
        #:: Action -> XMessage
        return action



