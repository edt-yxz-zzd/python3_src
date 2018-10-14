
class _HasAttr_overwrite:
    def __init__(self, *, overwrite:bool) -> None:
        self.__overwrite = bool(overwrite)
    @property
    def overwrite(self)->bool:
        return self.__overwrite
