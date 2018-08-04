
from abc import ABCMeta, abstractmethod
from .PreludeBase import const, from_LinkedList_to_list
from Monad import from_LinkedList_to_listM, Monad
class ParsecM(Monad):
    # <|>
    #def _or_(self, other):
    @abstractmethod
    def __truediv__(self, other):
        'if self success then self elif without consume then other else error from self'
        raise NotImplementedError
    # <?> expected
    @abstractmethod
    def __floordiv__(self, expected_str):
        'if self success then self elif consumed then error from self else set expected msg to error'
        raise NotImplementedError
    @abstractmethod
    def tryP(self):
        'if self success then self else set unconsumed and seek back but signal error'
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def anyToken(cls):
        # m a or fail without consume
        raise NotImplementedError

    @classmethod
    def expected(cls, expected_str):
        return cls.failM("expected: {!r}".format(expected_str))
    @classmethod
    def unexpected(cls, unexpected_str):
        return cls.failM("unexpected: {!r}".format(unexpected_str))

    def many0(self):
        # m a -> m [a]
        # self.many0() != self.tryP().many0()
        # a should fail without consume to let many0 success
        return self.many0LL() >>= from_LinkedList_to_listM
    def many1(self):
        # see many0 ; but len > 0
        return self.many1LL() >>= from_LinkedList_to_listM
    def many0LL(self):
        # m a -> ( m () | m (a,()) | ... m (a, (a, ...())) )
        # see many0 ; but using LinkedList
        return self.many1LL() / self.voidM
    def many1LL(self):
        # see many0LL ; but no ()
        return self * self.many0LL()


class ParsecMixin(ParsecM, MonadError):
    def tell(cls):
        # m Pos
    def seek(cls, pos):
        # pos -> m ()
    def consumed(cls):
        # m bool
    def set_consumed_flag(cls, consumed:bool):
        # bool -> m ()
    def clear_consumed_flag(self):
        # m a -> m a

    @classmethod
    def is_consumed_err(cls, err):
        # err -> bool
    @classmethod
    def err2msg(cls, err):
        # err -> str
    def __truediv__(self, other):
        inside = self.catchM(lambda cls, err:
                cls.throwM(err) if cls.is_consumed_err(err) else other)

        cls = type(self)
        return cls.consumed() ** (lambda cls, c0:
            inside if not c0 else
            cls.set_consumed_flag(False) >> inside >>
            cls.set_consumed_flag(True)
        )

    def __floordiv__(self, expected_str):
        return self.catchM(lambda cls, err:
            cls.throwM(err) if cls.is_consumed_err(err) else
            cls.expected(expected_str)
        )
    def tryP(self):
        pos = self.tell()
        cls = type(self)
        return self.catchM(lambda cls, err:
                cls.seek(pos) >>
                cls.set_consumed_flag(False) >>
                cls.fail(cls.err2msg(err))
                )


