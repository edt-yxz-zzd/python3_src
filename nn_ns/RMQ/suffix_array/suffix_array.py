

'''

SA = suffix array

SA<array> :: [ArrayBeginIdx]
SA<array> = sorted(range(L), key=lambda i: array[i:])
  where
    L = len(array)
    nonempty_suffices = [array[i] for i in range(len(array))]

    assert len(nonempty_suffices) == L
    ArrayBeginIdx = UInt[0..L-1] # may have no instances
    assert len(SA<array>) == L

    see:
        # both def are the same
        [Range_Minimum_Query_2007]A_New_Succinct_Representation_of_RMQ_Information_and_Improvements_in_the_Enhanced_Suffix_Array.pdf
            :: SA

        [String_Suffix_Tree_2003]Simple_Linear_Work_Suffix_Array_Construction.pdf
            :: SA


'''


class String2SuffixArray:
    def string2suffix_array(self, alphabet_size, string):
        ''':: (sz<-UInt) -> [UInt[0..sz-1]] -> [ArrayBeginIdx]

input:
    alphabet_size :: UInt
    string :: [Char]
        an array
        Char = UInt[0..alphabet_size-1]

let L = len(string)
output:
    suffix_array :: [ArrayBeginIdx]
        ArrayBeginIdx = UInt[0..L-1]
        len(suffix_array) == L
        is_sorted(suffix_array, key = lambda i: string[i:])
        sorted(suffix_array) == range(L)

see:
    seed.types.View.SeqTransformView
        e.g. for s :: str, SeqTransformView(ord, s) gives a [UInt]
'''
        if not all(0 <= ch < alphabet_size for ch in string): raise ValueError
        L = len(string)

        # [all char are different]
        #   ==>> no suffices has common prefix
        #   then we simply bucket_sort them and done
        #
        # sort string_idx by char_ord
        sorted_string_idc = bucket_sort(
                    alphabet_size, range(L), key=string.__getitem__)
                    #alphabet_size, range(L-1, -1, -1), key=string.__getitem__)

        if all(string[i] != string[j] for i, j in zip_me2(sorted_string_idc)):
            # now [all char are different]
            suffix_array = sorted_string_idc
            return suffix_array

        if L < ???:
            ...
            return
        if alphabet_size == L:
            # 

zip_me2
if __name__ == "__main__":
    import doctest
    doctest.testmod()

