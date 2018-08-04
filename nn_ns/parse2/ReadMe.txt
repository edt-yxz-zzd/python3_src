
tokenize + parse

distinguish advantage_regex and basic_regex
    basic_regex is used to determine exist and length
    advantage_regex is used to determine token case and another info
questions:
    what if the file is huge?
    read a block? what is the size?
    what if we want to skip a huge block?

    scan from right to left? how to reverse regex?


class ChainableIterator:
    __next__
        return next(self.it)
    append_left(iterable):
        self.it = chain(iterable, self.it)

tokenize :: Iter Char -> (Iter Token, UInt, Iter Char)
    input:
        make_token :: TokenCase -> Seq Char -> Token
        skip :: Iter Char -> (Iter Token, UInt, Iter Char) # reason see below
        skip_at_begin :: Iter Char -> (Iter Token, UInt, Iter Char)
        is_end_token :: Token -> bool
        skip_at_end :: Iter Char -> (Iter Token, UInt, Iter Char)
    output:
        tokenize <=[def_by]<= next_may_token

    internal:
        next_may_token :: Iter Char -> (Maybe (Token, UInt), Iter Char)
        next_tokens :: Iter Char -> ([Token], UInt, Iter Char)
            # [] - end
            # [end_token, skipped_tokens_at_end...] - end
            #       end_token may or may not skipped token
            # [nonskipped_token, skipped_tokens...] - not end
        next_may_token <=[def_by]=< [advantage_search, make_token]

        # result (Seq Char) cannot be empty
        advantage_search :: Iter Char -> (Maybe (TokenCase, Seq Char), Iter Char)

    * recognize system over iterator
        advantage_search <=[def_by]=< advantage_searchRS
        advantage_searchRS :: RS -> Iter Char -> (Maybe (TokenCase, Seq Char), Iter Char)
    * regex
        * advantage regex over seq
            advantage_search <=[def_by]=< advantage_searchAR
            type Seq T = ([T], Range)
            advantage_searchAR :: ARegex -> Seq Char -> Maybe ((TokenCase, Seq Char), Seq Char)

            python.re
            fine but require memoryview!
            what if the file is huge?
            read a block? what is the size?
        * basic regex over iterator
            need not so many features
            used only to determine the block size

            advantage_search <=[def_by]=< advantage_searchBR
            advantage_searchBR :: BRegex -> Iter Char -> (Seq Char, Seq Char)

            what if we want to skip a huge block?
                we should not save so many useless [Char]
                let us introduce a "skip"


parse




