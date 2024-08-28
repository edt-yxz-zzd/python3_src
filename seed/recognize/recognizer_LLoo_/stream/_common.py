#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/stream/_common.py

seed.recognize.recognizer_LLoo_.stream._common
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.stream._common -x


TODO:
scene
    mk...
any_token
eof
constant_tkeys
    constant_tkey
any_tokens_end_by_constant_tkeys
    constant_tkeys ?=> [constant_tkeys[0] not in constant_tkeys[1:]]
raw_string:
    dependent_pair(end_by(constant_tkey(sep), any_token),\tag->any_tokens_end_by_constant_tkeys(sep++tag))
one_of:
    vivi choice but only for tkeys
[[
######################
:browse Text.Parsec.Combinator
===
ghci> :browse Text.Parsec.Combinator
anyToken :: (Stream s m t, Show t) => ParsecT s u m t
between ::
  Stream s m t =>
  ParsecT s u m open
  -> ParsecT s u m close -> ParsecT s u m a -> ParsecT s u m a
chainl ::
  Stream s m t =>
  ParsecT s u m a
  -> ParsecT s u m (a -> a -> a) -> a -> ParsecT s u m a
chainl1 ::
  Stream s m t =>
  ParsecT s u m a -> ParsecT s u m (a -> a -> a) -> ParsecT s u m a
chainr ::
  Stream s m t =>
  ParsecT s u m a
  -> ParsecT s u m (a -> a -> a) -> a -> ParsecT s u m a
chainr1 ::
  Stream s m t =>
  ParsecT s u m a -> ParsecT s u m (a -> a -> a) -> ParsecT s u m a
choice :: Stream s m t => [ParsecT s u m a] -> ParsecT s u m a
count ::
  Stream s m t => Int -> ParsecT s u m a -> ParsecT s u m [a]
endBy ::
  Stream s m t =>
  ParsecT s u m a -> ParsecT s u m sep -> ParsecT s u m [a]
endBy1 ::
  Stream s m t =>
  ParsecT s u m a -> ParsecT s u m sep -> ParsecT s u m [a]
eof :: (Stream s m t, Show t) => ParsecT s u m ()
many1 :: Stream s m t => ParsecT s u m a -> ParsecT s u m [a]
manyTill ::
  Stream s m t =>
  ParsecT s u m a -> ParsecT s u m end -> ParsecT s u m [a]
notFollowedBy ::
  (Stream s m t, Show a) => ParsecT s u m a -> ParsecT s u m ()
option :: Stream s m t => a -> ParsecT s u m a -> ParsecT s u m a
optionMaybe ::
  Stream s m t => ParsecT s u m a -> ParsecT s u m (Maybe a)
optional :: Stream s m t => ParsecT s u m a -> ParsecT s u m ()
parserTrace :: (Show t, Stream s m t) => String -> ParsecT s u m ()
parserTraced ::
  (Stream s m t, Show t) =>
  String -> ParsecT s u m b -> ParsecT s u m b
sepBy ::
  Stream s m t =>
  ParsecT s u m a -> ParsecT s u m sep -> ParsecT s u m [a]
sepBy1 ::
  Stream s m t =>
  ParsecT s u m a -> ParsecT s u m sep -> ParsecT s u m [a]
sepEndBy ::
  Stream s m t =>
  ParsecT s u m a -> ParsecT s u m sep -> ParsecT s u m [a]
sepEndBy1 ::
  Stream s m t =>
  ParsecT s u m a -> ParsecT s u m sep -> ParsecT s u m [a]
skipMany1 :: Stream s m t => ParsecT s u m a -> ParsecT s u m ()
lookAhead :: Stream s m t => ParsecT s u m a -> ParsecT s u m a
]]
######################
view ../../python3_src/haskell_src/try_Parsec.hs
:browse Control.Arrow
:info Control.Arrow.Arrow
sepEndBy a sep ~= (sepBy a sep &&& optional sep) >>= fst
######################

######################
view /sdcard/0my_files/unzip/hs_doc/hs9_2_5/libraries/parsec-3.1.15.0/Text-Parsec-Combinator.html
parserTrace:print_err(pos)@beginning
parserTraced:print_err(pos)@beginning +@err
######################


#]]]'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...

from seed.types.ForkableForwardInputStream import IForkableForwardInputStream, ForkableForwardInputStream__using_LazyListIter
from seed.types.ForkableForwardInputStream import mk_forkable_char_stream5txt, mk_forkable_char_stream5ipath, mk_forkable_char_stream5ifile, iter_char_tokens5ifile



from seed.types.IToken import IBaseToken, IToken, BaseToken, Token__char
from seed.types.IToken import IBasePositionInfo, IPositionInfo4Gap, IPositionInfo4Span
from seed.types.IToken import LinenoColumn, PositionInfo4Gap__file, PositionInfo4Gap__text_file, PositionInfo4Gap__higher_level, PositionInfo4Span, PositionInfo4Span__text_file
from seed.types.IToken import Token__char, PositionInfo4Span__text_file, PositionInfo4Gap__text_file, LinenoColumn

___end_mark_of_excluded_global_names__0___ = ...



__all__
from seed.recognize.recognizer_LLoo_.stream._common import (IToken
,IForkableForwardInputStream, ForkableForwardInputStream__using_LazyListIter
,mk_forkable_char_stream5txt, mk_forkable_char_stream5ipath, mk_forkable_char_stream5ifile, iter_char_tokens5ifile


,IBaseToken, IToken, BaseToken, Token__char
,IBasePositionInfo, IPositionInfo4Gap, IPositionInfo4Span
,LinenoColumn, PositionInfo4Gap__file, PositionInfo4Gap__text_file, PositionInfo4Gap__higher_level, PositionInfo4Span, PositionInfo4Span__text_file
,Token__char, PositionInfo4Span__text_file, PositionInfo4Gap__text_file, LinenoColumn
)
from seed.recognize.recognizer_LLoo_.stream._common import *
