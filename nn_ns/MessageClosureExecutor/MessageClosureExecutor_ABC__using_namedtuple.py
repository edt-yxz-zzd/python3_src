

__all__ = '''
    MessageClosureExecutor_ABC__using_namedtuple
    '''.split()

from seed.types.DictKeyAsObjAttr import DictKeyAsObjAttr
from .parse_message_interface_action_definition_str import \
    check_parse2_result
from .MessageClosureExecutor_ABC import MessageClosureExecutor_TypeError
from .MessageClosureExecutor__mixins__collect_functions import \
    MessageClosureExecutor__mixins__collect_functions
from .MessageClosureExecutor__mixins__remove_checks import \
    MessageClosureExecutor__mixins__remove_checks

#from .MessageClosureExecutor_ABC__with_data import \
#    MessageClosureExecutor_ABC__with_data
#from .make_namedtuples import make_namedtuples
from .abc import abstractmethod
from inspect import isabstract

def namedtuple2type_name(named_tuple_obj):
    return type(named_tuple_obj).__name__

class MessageClosureExecutor_ABC__using_namedtuple(
    #MessageClosureExecutor_ABC__with_data
    MessageClosureExecutor__mixins__collect_functions
    ,MessageClosureExecutor__mixins__remove_checks
    ):
    '''
assume
    namedtuple's type_name is Constructor
    type_name of Message/Interface/Action beginswith 'M'/'I'/'A'
    xmessage is (action|message) # without boxing
    Action args... interface_objects...
        len(interface_objects...) == len(action_constraint[action_constructor])
        see: action2interfaces
'''
    '''
    @classmethod
    @abstractmethod
    def get_namedtuples_in_str(cls):
        # format: see make_namedtuples
        # return namedtuples_in_str
        pass
    '''
    @abstractmethod
    def _type_name2namedtuple_type_():
        #require cls.type_name2namedtuple_type
        # type_name/Constructor to namedtuple_type
        # return type_name2namedtuple_type
        pass
    @abstractmethod
    def _interface_constraint_():
        #require cls.interface_constraint
        #return interface_constraint
        pass
    @abstractmethod
    def _action_constraint_():
        #require cls.action_constraint
        #return action_constraint
        pass
    @abstractmethod
    def _auto_action_constructor2maker_():
        #require cls.auto_action_constructor2maker
        #return auto_action_constructor2maker
        pass
    @abstractmethod
    def _interface_constructor2auto_action_constructors_():
        #require cls.interface_constructor2auto_action_constructors
        #return interface_constructor2auto_action_constructors
        pass

    @classmethod
    def check_type_name2namedtuple_type(cls, type_name2namedtuple_type):
        for type_name, tp in type_name2namedtuple_type.items():
            if type_name != tp.__name__:
                raise ValueError(f'{type_name!r} != {tp.__name__!r}')
        for type_name in type_name2namedtuple_type:
            if type_name[:1] not in ('M', 'I', 'A'):
                raise ValueError(f'{type_name!r} not startswith M/I/A')

    @classmethod
    def check_interface_constraint(cls, interface_constraint):
        for intf_name, msg_name in interface_constraint.items():
            if intf_name[0] != 'I':
                raise ValueError(f'{intf_name!r} not startswith "I"')
            if msg_name[0] != 'M':
                raise ValueError(f'{msg_name!r} not startswith "M"')

    @classmethod
    def check_action_constraint(cls, action_constraint):
        for actn_name, intf_names in action_constraint.items():
            if actn_name[0] != 'A':
                raise ValueError(f'{actn_name!r} not startswith "A"')
            if type(intf_names) is not tuple:
                raise ValueError('{actn_name!r}: type({intf_names!r}) is not tuple')
            for intf_name in intf_names:
                if intf_name[0] != 'I':
                    raise ValueError(f'{intf_name!r} not startswith "I"')


    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if isabstract(cls): return

        #initial_xmessages = frozenset(cls.static_iter_initial_xmessages())
        action_constraint = cls._action_constraint_
        interface_constraint = cls._interface_constraint_
        #namedtuples_in_str = cls.get_namedtuples_in_str()
        #type_name2namedtuple_type = make_namedtuples(namedtuples_in_str)
        type_name2namedtuple_type = cls._type_name2namedtuple_type_

        auto_action_constructor2maker = cls._auto_action_constructor2maker_
        interface_constructor2auto_action_constructors = cls._interface_constructor2auto_action_constructors_

        check_parse2_result(
            type_name2namedtuple_type
            ,interface_constraint
            ,action_constraint
            ,auto_action_constructor2maker
            ,interface_constructor2auto_action_constructors
            )

        cls.check_type_name2namedtuple_type(type_name2namedtuple_type)
        cls.check_action_constraint(action_constraint)
        cls.check_interface_constraint(interface_constraint)
        # TODO: see: check at last of parse_using_namedtuple_definition_str
        '''
        action_constructor2function??
        cls._verify_auto_action_defs__static(
            auto_action_constructor2maker
                =auto_action_constructor2maker
            ,interface_constructor2auto_action_constructors
                =interface_constructor2auto_action_constructors
            ,action_constructor2function
                =action_constructor2function
            ,action_constraint
                =action_constraint
            )
        '''

        all_message_constructors = {type_name
            for type_name in type_name2namedtuple_type
            if type_name.startswith('M')
            }

        cls.all_message_constructors = all_message_constructors
        #cls.action_constraint = action_constraint
        #cls.interface_constraint = interface_constraint
        #cls.type_name2namedtuple_type = type_name2namedtuple_type

        # cls.mk.Mxxx
        # cls.mk.Ixxx
        # cls.mk.Axxx
        #for type_name, namedtuple_type in type_name2namedtuple_type.items():
        #   setattr(cls, f'mk{type_name}', namedtuple_type)
        cls.mk = DictKeyAsObjAttr(type_name2namedtuple_type)
    def __init__(self, *, initial_xmessages):
        #bug: cls = __class__
        cls = type(self)
        super().__init__(
            initial_xmessages = initial_xmessages

            ,all_message_constructors = cls.all_message_constructors
            ,interface_constraint = cls._interface_constraint_
            ,action_constraint = cls._action_constraint_
            ,auto_action_constructor2maker
                =cls._auto_action_constructor2maker_
            ,interface_constructor2auto_action_constructors
                =cls._interface_constructor2auto_action_constructors_
            )

    '''
    def __getattr__(self, attr):
        # self.Mxxx is message function
        # self.Axxx is action function
        # self.mkMxxx/self.mkIxxx/self.mkAxxx is constructor
        if attr.startswith('mk'):
            name = attr[2:]
            may_f = self.type_name2namedtuple_type.get(name, None)
            if may_f is not None:
                return may_f
        return super().__getattr__()
    '''

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
        #return tuple(action)
        L = len(action)
        sz = len(self.action_constraint[self.action2constructor(action)])
        assert sz <= L
        #print(__name__)
        #print(action)
        #print(tuple(action)[L-sz:])
        return tuple(action)[L-sz:]






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



