
from ..error import Error as _ErrorBase
class Error(_ErrorBase):pass


class NotPrimeError(ValueError, Error):pass
