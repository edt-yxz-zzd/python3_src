
__all__ = '''
    MessageClosureExecutor_TypeError
    MessageClosureExecutor_EmptyError
    MessageClosureExecutor_ABC
    '''.split()

#message interface action constructor
from seed.helper.__SpecialMethodGetter__ import SpecialMethodGetter
from ._debug_ import print_err, print_ferr
from .abc import ABC, abstractmethod, final
from types import MappingProxyType
import itertools

def _open_read(mapping, key):
    return mapping.get(key, '')
def _open_write(mapping, key):
    try:
        return mapping[key]
    except KeyError:
        return mapping.setdefault(key, [])

class MessageClosureExecutor_TypeError(Exception):pass
class MessageClosureExecutor_EmptyError(Exception):pass
class MessageClosureExecutor_ABC(ABC):
    '''message/interface/action/constructor should be hashable
xmessage = action | message
auto_action(interface)


'''


    def __init__(self):
        self.__init()

    @property
    @final
    def auto_action_constructor2maker(self):
        #:: {ActionConstructor: Interface -> Action}
        # immutable
        return MappingProxyType(SpecialMethodGetter(self).__get_auto_action_constructor2maker__())
    @property
    @final
    def interface_constructor2auto_action_constructors(self):
        #:: {InterfaceConstructor:{ActionConstructor}}
        # immutable
        return MappingProxyType(SpecialMethodGetter(self).__get_interface_constructor2auto_action_constructors__())
    @property
    @final
    def interface_constraint(self):
        #:: {InterfaceConstructor: MessageConstructor}
        # immutable
        return MappingProxyType(SpecialMethodGetter(self).__get_interface_constraint__())
    @property
    @final
    def action_constraint(self):
        #:: {ActionConstructor: (InterfaceConstructor,)*n}
        # immutable
        return MappingProxyType(SpecialMethodGetter(self).__get_action_constraint__())

    @property
    @final
    def action_constructor2function(self):
        #:: {ActionConstructor: Action -> (Message,)*n -> Iter XMessage}
        #immutable
        return MappingProxyType(SpecialMethodGetter(self).__get_action_constructor2function__())
    @property
    @final
    def message_constructor2function(self):
        #:: {MessageConstructor: Message->Iter Interface}
        # immutable
        return MappingProxyType(SpecialMethodGetter(self).__get_message_constructor2function__())



    '''
    @property
    @final
    def xmessage_queue(self):
        #:: Queue<XMessage>
        # mutable
        return SpecialMethodGetter(self).__get_xmessage_queue__()
    '''

    # Action ~ (ActionConstructor, ActionArgs, (Interface,)*n)
    @property
    @final
    def all_actions(self):
        #:: {Action}
        # mutable
        return SpecialMethodGetter(self).__get_all_actions__()
    @property
    @final
    def all_messages(self):
        #:: {Message}
        # mutable
        return SpecialMethodGetter(self).__get_all_messages__()
    @property
    @final
    def interface2messages(self):
        #:: {Interface: [Message]}
        # mutable dict<list> should not be defaultdict<list>
        return SpecialMethodGetter(self).__get_interface2messages__()
    @property
    @final
    def interface2actions(self):
        #:: {Interface: [Action]} # iff interface in action.interfaces
        # mutable
        return SpecialMethodGetter(self).__get_interface2actions__()


    #initial_xmessages
    @final
    def iter_initial_xmessages(self):
        return iter(SpecialMethodGetter(self).__get_initial_xmessages__())




    @abstractmethod
    def __get_initial_xmessages__(self):
        #:: {XMessage}
        # immutable
        pass
    @abstractmethod
    def __get_interface_constraint__(self):
        #:: {InterfaceConstructor: MessageConstructor}
        # immutable
        pass
    @abstractmethod
    def __get_action_constraint__(self):
        #-> {ActionConstructor: (InterfaceConstructor,)*n}
        # immutable
        pass
    @abstractmethod
    def __get_action_constructor2function__(self):
        #:: {ActionConstructor: Action -> (Message,)*n -> Iter XMessage}
        # immutable
        pass
    @abstractmethod
    def __get_message_constructor2function__(self):
        #:: {MessageConstructor: Message->Iter Interface}
        # immutable
        #constraint:
        #   cmsg = .message2constructor(msg)
        #   for intf in .message_constructor2function[cmsg](msg):
        #       cintf = .interface2constructor(intf)
        #       assert .interface_constraint[cintf] == cmsg
        #   .check_interface_message(intf, msg)
        pass




    @abstractmethod
    def __get_auto_action_constructor2maker__(self):
        #:: {ActionConstructor: Interface -> Action}
        # immutable
        pass
    @abstractmethod
    def __get_interface_constructor2auto_action_constructors__(self):
        #:: {InterfaceConstructor:{ActionConstructor}}
        # immutable
        pass

    def _verify_auto_action_defs(self):
        self._verify_auto_action_defs__static(
            auto_action_constructor2maker
                =self.auto_action_constructor2maker
            ,interface_constructor2auto_action_constructors
                =self.interface_constructor2auto_action_constructors
            ,action_constructor2function
                =self.action_constructor2function
            ,action_constraint
                =self.action_constraint
            )
    @staticmethod
    def _verify_auto_action_defs__static(*
        ,auto_action_constructor2maker
        ,interface_constructor2auto_action_constructors
        ,action_constructor2function
        ,action_constraint
        ):
        return (
        # all be action_constructor
        all(auto_action_constructor in action_constructor2function
        for auto_action_constructor in auto_action_constructor2maker
        ) and
        # all constraint is unit
        all(len(action_constraint[auto_action_constructor]) == 1
        for auto_action_constructor in auto_action_constructor2maker
        ) and
        # auto_action_constructor -[action_constraint]-> interface_constructor
        #   back to auto_action_constructor
        all(auto_action_constructor in interface_constructor2auto_action_constructors.get(interface_constructor, ())
        for auto_action_constructor in auto_action_constructor2maker
        for interface_constructor in action_constraint[auto_action_constructor]
        ) and
        # interface_constructor2auto_action_constructors
        #   back to interface_constructor
        all(list(action_constraint[auto_action_constructor])
            == [interface_constructor]
        for interface_constructor, auto_action_constructors
            in interface_constructor2auto_action_constructors.items()
        for auto_action_constructor in auto_action_constructors
        )
            )




    '''
    @abstractmethod
    def __get_xmessage_queue__(self):
        #:: Queue<XMessage>
        # mutable
        pass
    '''
    @abstractmethod
    def __get_all_messages__(self):
        #:: {Message}
        # mutable
        pass
    @abstractmethod
    def __get_interface2messages__(self):
        #:: {Interface: [Message]} # should not be defaultdict<list>
        # mutable
        pass
    @abstractmethod
    def __get_all_actions__(self):
        #-> {Action} # mutable
        # mutable
        pass
    @abstractmethod
    def __get_interface2actions__(self):
        #:: {Interface: [Action]} # iff interface in action.interfaces
        # mutable
        pass



    @abstractmethod
    def interface2constructor(self, interface):
        #:: Interface -> InterfaceConstructor
        pass
    @abstractmethod
    def message2constructor(self, message):
        #:: Message -> MessageConstructor
        pass
    @abstractmethod
    def action2constructor(self, action):
        #:: Action -> ActionConstructor
        pass
    #def action2args(self, action):
        #:: Action -> ActionArgs
    @abstractmethod
    def action2interfaces(self, action):
        #:: Action -> (Interface,)*n
        pass






    @abstractmethod
    def distinguish_xmessage(self, xmessage):
        #:: XMessage -> ((False, Action)|(True, Message))
        # -> (is_message, (Action|Message))
        pass
    @abstractmethod
    def message2xmessage(self, message):
        #:: Message -> XMessage
        pass
    @abstractmethod
    def action2xmessage(self, action):
        #:: Action -> XMessage
        pass





    @abstractmethod
    def __push_xmessage_into_queue__(self, xmessage):
        # -> None
        pass
    @abstractmethod
    def __pull_xmessage_outfrom_queue__(self):
        # -> XMessage | raise MessageClosureExecutor_EmptyError
        pass
    @abstractmethod
    def __is_xmessage_queue_empty__(self):
        # -> Bool
        pass
    @abstractmethod
    def __clear_xmessage_queue__(self):
        # -> None
        pass
    @final
    def restart(self):
        # -> None
        SpecialMethodGetter(self).__clear_xmessage_queue__()
        self.__init()
    @final
    def __init(self):
        self.put_xmessages(self.iter_initial_xmessages())

    @abstractmethod
    def __check_interface_message__(self, interface, message):
        #:: Interface -> Message -> None|raise MessageClosureExecutor_TypeError
        #user provided
        pass
    @abstractmethod
    def __check_message__(self, message):
        #:: Message -> None|raise MessageClosureExecutor_TypeError
        #user provided
        pass
    @abstractmethod
    def __check_action__(self, action):
        #:: Action -> None|raise MessageClosureExecutor_TypeError
        #user provided
        pass



    @final
    def check_interface_message(self, interface, message):
        cmsg = self.message2constructor(message)
        cintf = self.interface2constructor(interface)
        if self.interface_constraint[cintf] != cmsg:
            raise MessageClosureExecutor_TypeError(
                f'interface mismatch message: interface={interface!r}, message={message!r}')
        SpecialMethodGetter(self).__check_interface_message__(interface, message)



    @final
    def check_action(self, action):
        # action -> None|raise MessageClosureExecutor_TypeError
        action_constructor = self.action2constructor(action)
        interface_constructors = self.action_constraint[action_constructor]
        interfaces = self.action2interfaces(action)
        _interface_constructors = tuple(map(
            self.interface2constructor, interfaces))
        if interface_constructors != _interface_constructors:
            raise MessageClosureExecutor_TypeError(
                f'action.action_constructor.interface_constructors={interface_constructors!r} != {_interface_constructors}=action.interfaces.interface_constructors; interfaces={interfaces!r}')
        SpecialMethodGetter(self).__check_action__(action)

    @final
    def check_message(self, message):
        message_constructor = self.message2constructor(message)
        mfunc = self.message_constructor2function[message_constructor]
        for interface in mfunc(message):
            self.check_interface_message(interface, message)
        SpecialMethodGetter(self).__check_message__(message)

    @final
    def put_xmessages(self, xmessages):
        for _ in map(self.put_xmessage, xmessages):pass
    @final
    def put_xmessage(self, xmessage):
        is_message, action_or_message = self.distinguish_xmessage(xmessage)
        if is_message:
            message = action_or_message
            self.put_message(message)
        else:
            action = action_or_message
            self.put_action(action)
    @final
    def put_action(self, action):
        if action in self.all_actions: return
        self.check_action(action)
        xmessage = self.action2xmessage(action)
        SpecialMethodGetter(self).__push_xmessage_into_queue__(xmessage)
        self.all_actions.add(action)
    @final
    def put_message(self, message):
        #   msg will be stored at data[intf]
        #   but since interface has parameters
        #       , a particular msg will not be store to all interfaces.
        if message in self.all_messages: return
        self.check_message(message)
        xmessage = self.message2xmessage(message)
        SpecialMethodGetter(self).__push_xmessage_into_queue__(xmessage)
        self.all_messages.add(message)


    @final
    def execute_until_closure(self):
        #while not SpecialMethodGetter(self).__is_xmessage_queue_empty__():
        try:
            while True:
                xmessage = SpecialMethodGetter(self).__pull_xmessage_outfrom_queue__()
                is_message, action_or_message = \
                    self.distinguish_xmessage(xmessage)
                if is_message:
                    message = action_or_message
                    self.__execute_message(message)
                else:
                    action = action_or_message
                    self.__execute_action(action)
        except MessageClosureExecutor_EmptyError:
            pass
    @final
    def __execute_message(self, message):
        message_constructor = self.message2constructor(message)
        mfunc = self.message_constructor2function[message_constructor]
        for interface in set(mfunc(message)):
            self.__execute_interface_message(interface, message)

    @final
    def __on_new_interface(self, interface):
        interface_constructor = self.interface2constructor(interface)
        ctors = self.interface_constructor2auto_action_constructors.get(interface_constructor, '')
        for auto_action_constructor in ctors:
            maker = self.auto_action_constructor2maker[auto_action_constructor]
            auto_action = maker(interface)
            self.put_action(auto_action)


    @final
    def __execute_interface_message(self, interface, message):
        print_ferr(lambda:f'store: interface={interface!r}; message={message!r}')
        #assert self.interface_constraint[self.interface2constructor(interface)] == self.message2constructor(message)

        #ls = _open_write(self.interface2messages, interface)
        try:
            ls = self.interface2messages[interface]
        except KeyError:
            ls = self.interface2messages.setdefault(interface, [])
            if not ls:
                # new interface
                self.__on_new_interface(interface)
            else:
                raise logic-error

        begin_idx = len(ls)
        ls.append(message)
        for action in _open_read(self.interface2actions, interface):
            self.__execute_action_from_interface_idx(
                action, interface, begin_idx)
    @final
    def __execute_action(self, action):
        # register to all interfaces
        print_ferr(lambda:f'register: action={action!r}')
        interfaces = self.action2interfaces(action)
        for interface in set(interfaces):
            _open_write(self.interface2actions, interface).append(action)

        if not interfaces:
            messages = ()
            action_constructor = self.action2constructor(action)
            afunc = self.action_constructor2function[action_constructor]
            SpecialMethodGetter(self).__execute_action__function_messages(afunc, action, messages)
        else:
            def f(interface):
                return len(_open_read(self.interface2messages, interface))
            interface = min(interfaces, key=f)
            self.__execute_action_from_interface_idx(action, interface, 0)

    @final
    def __execute_action_from_interface_idx(
        self, action, interface, begin_idx
        ):
        action_constructor = self.action2constructor(action)
        afunc = self.action_constructor2function[action_constructor]
        messages = _open_read(self.interface2messages, interface)
        if len(messages) <= begin_idx: return
        del messages

        interfaces = self.action2interfaces(action)
        idc = [i for i, _interface in enumerate(interfaces)
                if interface == _interface]
        assert idc

        messagess = [_open_read(self.interface2messages, interface)
                    for interface in interfaces]
        lens = tuple(map(len, messagess))
        if any(L == 0 for L in lens): return

        while idc:
            last_idx = idc.pop()
            begins = [0]*len(lens)
            ends = list(lens)

            begins[last_idx] = begin_idx
            for i in idc:
                ends[i] = begin_idx

            iterables = map(itertools.islice, messagess, begins, ends)
            for messages in itertools.product(*iterables):
                # tuple messages not list messages
                # tuple messages are args for action
                # list messages are an interface storage
                SpecialMethodGetter(self).__execute_action__function_messages(afunc, action, messages)

    @final
    def __execute_action__function_messages(self, afunc, action, messages):
        print_ferr(lambda:f'call: action={action!r}; messages={messages!r}')
        for xmessage in afunc(action, *messages):
            self.put_xmessage(xmessage)





