{-
e ../../python3_src/haskell_src/try_Parsec.hs

[[
ghci>
:browse Text.Parsec.Combinator
:browse Text.Parsec.Char
import Text.Parsec
:info char
char :: Stream s m Char => Char -> ParsecT s u m Char
        -- Defined in ‘Text.Parsec.Char’

ghci> :info runPT
runPT ::
  Stream s m t =>
  ParsecT s u m a -> u -> SourceName -> s -> m (Either ParseError a)
        -- Defined in ‘Text.Parsec.Prim’
ghci> :info runP
runP ::
  Stream s Data.Functor.Identity.Identity t =>
  Parsec s u a -> u -> SourceName -> s -> Either ParseError a
        -- Defined in ‘Text.Parsec.Prim’

-- runP === runPT{m:=Identity}

runP (sepEndBy (char 'a') (char ',')) 999 "666" "aaa,aa,a,bb"
dlopen failed: cannot locate symbol "stg_bh_upd_frame_info" referenced by "/data/data/com.termux/files/usr/lib/ghc-9.2.5/text-1.2.5.0/libHStext-1.2.5.0-ghc9.2.5.so"...
    ???
find /data/data/com.termux/files/usr/lib/ghc-9.2.5/  -name 'libHStext-*'
    /data/data/com.termux/files/usr/lib/ghc-9.2.5/text-1.2.5.0/libHStext-1.2.5.0-ghc9.2.5.so
    /data/data/com.termux/files/usr/lib/ghc-9.2.5/text-1.2.5.0/libHStext-1.2.5.0.a
find /data/data/com.termux/files/usr/lib/ghc-9.2.5/  -name '*stg_bh_upd_frame_info*'
    <none>
grep -F stg_bh_upd_frame_info -r /data/data/com.termux/files/usr/lib/ghc-9.2.5/
    ...many...
e ../../python3_src/haskell_src/try_Parsec.hs
ghc ../../python3_src/haskell_src/try_Parsec.hs --run
    <interactive>: <command line>: dlopen failed: cannot locate symbol "stg_bh_upd_frame_info" referenced by "/data/data/com.termux/files/usr/lib/ghc-9.2.5/text-1.2.5.0/libHStext-1.2.5.0-ghc9.2.5.so"...

ghc ../../python3_src/haskell_src/try_Parsec.hs -o  ~/tmp/tmp1/try_Parsec
~/tmp/tmp1/try_Parsec

ls  ../../python3_src/haskell_src/
ls  ../../python3_src/haskell_src/try_Parsec.{hi,o}
  ../../python3_src/haskell_src/try_Parsec.hi
  ../../python3_src/haskell_src/try_Parsec.o
rm ../../python3_src/haskell_src/try_Parsec.{hi,o}
rm ../../python3_src/haskell_src/try_Parsec
ls  ../../python3_src/haskell_src/

]]


-}


import Text.Parsec
p = do
  a <- (sepEndBy (char 'a') (char ','))
  b <- optionMaybe (char 'b')
  return (a, b)

g = runP p 999 "666"
f s = (s, g s)
main = print $ map f ["", "a", "ab", "a,", "a,b", "a,a", "a,ab", "a,a,", "a,a,b"]
  -- [("",Right ("",Nothing)),("a",Right ("a",Nothing)),("ab",Right ("a",Just 'b')),("a,",Right ("a",Nothing)),("a,b",Right ("a",Just 'b')),("a,a",Right ("aa",Nothing)),("a,ab",Right ("aa",Just 'b')),("a,a,",Right ("aa",Nothing)),("a,a,b",Right ("aa",Just 'b'))]
  {-
:browse Control.Arrow
:info Control.Arrow.Arrow
sepEndBy a sep ~= (sepBy a sep &&& optional sep) >>= fst
  -}

