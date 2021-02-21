
import logging

assert logging.getLogger() is logging.getLogger('')
assert logging.getLogger() is not logging.getLogger('root')

logging.disable()
logging.disable(logging.NOTSET)


