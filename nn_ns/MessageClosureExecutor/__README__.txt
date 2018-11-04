Message Closure Executor
    used by:
        nn_ns.LALR.calc_CFG_inits.calc_CFG_inits__all_hashable__using_MessageClosureExecutor

datatype:
    Message
    Interface ~ [Message]
        an Interface point to a collection of Message
    Action ~ (Interface,)*n
        an Action will perform over all (Message,)*n which register to (Interface,)*n

Message/Interface/Action has a Constructor
    #message interface action constructor
    constructor - hashable


.interface2constructor :: Interface -> InterfaceConstructor
.message2constructor :: Message -> MessageConstructor
.action2constructor :: Action -> ActionConstructor

# Action = (ActionConstructor, ActionArgs, (Interface,)*n)
# XMessage = Action|Message
.all_actions :: {Action}
.action_constraint :: {ActionConstructor: (InterfaceConstructor,)*n}
.action2args :: Action -> ActionArgs
.action2interfaces :: Action -> (Interface,)*n
.action_constructor2function :: {ActionConstructor: Action -> (Message,)*n -> Iter XMessage}
.interface2actions :: {Interface: [Action]}
    iff interface in action.interfaces

.distinguish_action_and_message :: XMessage -> ((False, Action)|(True, Message))
.action_message_queue :: Queue<XMessage>
.all_messages :: {Message}
.interface2messages :: {Interface: [Message]} # defaultdict
.interface_constraint
    :: {InterfaceConstructor: MessageConstructor}
        constructor:
            InterfaceConstructor many0-to-1 MessageConstructor
.check_interface_message :: Interface -> Message -> None|raise
    user provided
.message_constructor2function :: {MessageConstructor: Message->Iter Interface}
    constraint:
        cmsg = .message2constructor(msg)
        for intf in .message_constructor2function[cmsg]:
            cintf = .interface2constructor(intf)
            assert .interface_constraint[cintf] == cmsg
        .check_interface_message(intf, msg)
.put(msg)
    cmsg = .message2constructor(msg)
    for intf in .message_constructor2function[cmsg]:
        .interface2messages[intf].append(msg)
        msg will be stored at data[intf]
        but since interface has parameters
            , a particular msg will not be store to all interfaces.
.execute_until_closure
