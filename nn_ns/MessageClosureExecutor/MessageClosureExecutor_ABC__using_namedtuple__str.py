

__all__ = '''
    MessageClosureExecutor_ABC__using_namedtuple__str
    '''.split()


from .parse_message_interface_action_definition_str import \
    parse_message_interface_action_definition_str
from .MessageClosureExecutor_ABC__using_namedtuple import \
    MessageClosureExecutor_ABC__using_namedtuple
from .abc import abstractmethod
from inspect import isabstract


class MessageClosureExecutor_ABC__using_namedtuple__str(
    MessageClosureExecutor_ABC__using_namedtuple
    ):
    '''

example:
using_namedtuple_definition_str = """
    ; MMsgNamedTupleDef fieldname0 fieldname1 fieldname2
    ; IIntfNamedTupleDefWithConstraint fieldname0 fieldname1
        <- MMsgNamedTupleDef
    ; AActnNamedTupleDefWithConstraint fieldname0 fieldname1
        <- IIntfNamedTupleDefWithConstraint IIntfNamedTupleDefWithConstraint
    ; AAutoActnDef fieldname0
        <- @IIntfNamedTupleDefWithConstraint
"""

'''

    @abstractmethod
    def message_interface_action_definition_str():
        #require cls.message_interface_action_definition_str
        pass

    # remove abstract:
    _type_name2namedtuple_type_ = None
    _interface_constraint_ = None
    _action_constraint_ = None
    _auto_action_constructor2maker_ = None
    _interface_constructor2auto_action_constructors_ = None

    def __init_subclass__(cls, **kwargs):
        if not isabstract(cls):
            s = cls.message_interface_action_definition_str
            (type_name2namedtuple_type
            ,interface_constraint
            ,action_constraint
            ,auto_action_constructor2maker
            ,interface_constructor2auto_action_constructors
            ) = parse_message_interface_action_definition_str(s)
            cls._type_name2namedtuple_type_ = type_name2namedtuple_type
            cls._interface_constraint_ = interface_constraint
            cls._action_constraint_ = action_constraint
            cls._auto_action_constructor2maker_ \
                = auto_action_constructor2maker
            cls._interface_constructor2auto_action_constructors_ \
                = interface_constructor2auto_action_constructors

        super().__init_subclass__(**kwargs)


