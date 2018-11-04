
__all__ = '''
    MessageClosureExecutor__mixins__remove_checks
    '''.split()

from .MessageClosureExecutor_ABC import MessageClosureExecutor_ABC

class MessageClosureExecutor__mixins__remove_checks(
    MessageClosureExecutor_ABC
    ):
    def __check_interface_message__(self, interface, message):
        #:: Interface -> Message -> None|raise MessageClosureExecutor_TypeError
        #user provided
        pass
    def __check_message__(self, message):
        #:: Message -> None|raise MessageClosureExecutor_TypeError
        #user provided
        pass
    def __check_action__(self, action):
        #:: Action -> None|raise MessageClosureExecutor_TypeError
        #user provided
        pass



