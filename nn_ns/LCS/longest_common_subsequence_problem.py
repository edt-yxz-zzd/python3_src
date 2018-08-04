
r'''

https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
A Survey of Longest Common Subsequence Algorithms (2000)(L. Bergroth)

row by row
-   {}  A   G   C   A   T
{}  0   0   0   0   0   0
G   0   0   1   1   1   1
A   0   1   1   1   2   2
C   0   1   1   2   2   2

-   {}  A   G   C   A   T
{}  0   0   0   0   0   0
G   0   0  \1  <1  <1  <1
A   0  \1  <1^ <1^ \2  <2
C   0   1^ <1^ \2  <2^ <2^


horizontal_string = 'AGCAT'
vertical_string = 'GAC'
lcs in {'GA', 'GC', 'AC'}
'''

class LCS_RowByRow:
    def __init__(self, horizontal_string):
        if horizontal_string is None:
            raise ValueError('horizontal_string is None')
        # self.horizontal_string = horizontal_string
        self.reset(horizontal_string)
    def reset(self, horizontal_string=None):
        if horizontal_string is not None:
            self.horizontal_string = horizontal_string
        return
    def feed(self, vertical_string):
        for vc in vertical_string:
            self.feed1(vc)
    def feed1(self, new_vertical_char):
        return
    def calc_longest_common_subsequence_length(self):
        raise NotImplementedError

# direction for LCS_RowByRow__impl.__ndirections
LEFT = -1
UP = -2
UP_LEFT = -3
# ndirections = ()
#             | [(direction, ndirections)]
class LCS_RowByRow__impl(LCS_RowByRow):
    @property
    def _count_data_pairs(self):
        return self.__count_data_pairs
    def _set_count_data_pairs(self, count_data_pairs):
        self.__count_data_pairs = count_data_pairs
    def calc_longest_common_subsequence_length(self):
        return self.get_last_count_data()[0]
    def get_last_count_data(self):
        if not self._count_data_pairs:
            return (0, ())
        return self._count_data_pairs[-1]
    def reset(self, horizontal_string=None):
        super().reset(horizontal_string=horizontal_string)
        self.__count_data_pairs =\
            [(0, ())] * len(self.horizontal_string)
    def feed1(self, vc):
        L = len(self.horizontal_string)
        # count[i][j] : len(lcs(horizontal_string[:j], vertical_string[:i]))
        # count[-1][j] == 0 == count[i][-1]
        # count[i][j] = max ( count[i][j-1]
        #                   , count[i-1][j]
        #                   , count[i-1][j-1]+1
        #                       if vertical_string[i] == horizontal_string[j])

        L = len(self.horizontal_string)
        j = 0
        # cd : count, data
        cd_n1_n1 = (0, ())              # count[i-1][j-1]   # \upleft
        cd_i_n1 = (0, ())               # count[i][j-1]     # <left
        for j in range(L):
            # __counts[:j] === count[i][:j]
            # __counts[j:] === count[i-1][j:]
            cd_n1_j = self.__count_data_pairs[j]
                                        # count[i-1][j]     # ^up
            hc = self.horizontal_string[j]
            cd_i_j = self.make_cd_i_j_from_Up_Left_UpLeft(
                    vc, hc, cd_n1_j, cd_i_n1, cd_n1_n1)

            # update
            # j -> j-1=n1
            cd_n1_n1 = cd_n1_j
            cd_i_n1 = cd_i_j
            self.__count_data_pairs[j] = cd_i_j

    def make_cd_i_j_from_Up_Left_UpLeft(self, vc, hc, cd_n1_j, cd_i_n1, cd_n1_n1):
        raise NotImplementedError
    def build_longest_common_subsequence1(self):
        raise NotImplementedError

def iter_llist(llist):
    # llist a = () | (a, llist a)
    # @return : [a]
    while llist:
        head, llist = llist
        yield head
def iter_nllist1(nllist):
    # nllist a = () | [(a, nllist a)] -- is forest
    # @return : [a] # iter one tree
    while nllist:
        head, nllist = nllist[0]
        yield head
class LCS_RowByRow__common_elements(LCS_RowByRow__impl):
    def build_longest_common_subsequence1(self):
        ls = list(iter_llist(self.get_last_count_data()[-1]))
        ls.reverse()
        assert len(ls) == self.get_last_count_data()[0]
        return ls
    def make_cd_i_j_from_Up_Left_UpLeft(self, vc, hc, cd_n1_j, cd_i_n1, cd_n1_n1):
        cs = [ cd_n1_j #(cd_n1_j[0], (UP, cd_n1_j[1]))
             , cd_i_n1 #(cd_i_n1[0], (LEFT, cd_i_n1[1]))
             ]
        if vc == hc:
            cs.append((cd_n1_n1[0]+1, (hc, cd_n1_n1[1])))
        cd_i_j = max(cs)
        return cd_i_j

class LCS_RowByRow__ndirections(LCS_RowByRow__impl):
    def get_ndirections(self):
        return self.get_last_count_data()[-1]
    def iter_reversed_LCS_directions1(self):
        return iter_nllist1(self.get_ndirections())
    def build_longest_common_subsequence1(self):
        L = len(self.horizontal_string)
        i = L - 1
        ls = []
        for direction in self.iter_reversed_LCS_directions1():
            assert i >= 0
            if direction == LEFT:
                pass
            elif direction == UP_LEFT:
                ls.append(self.horizontal_string[i])
            elif direction == UP:
                pass
            else:
                raise logic-error
            if direction != UP:
                i -= 1
        ls.reverse()

        assert len(ls) == self.get_last_count_data()[0]
        return ls
    def make_cd_i_j_from_Up_Left_UpLeft(self, vc, hc, cd_n1_j, cd_i_n1, cd_n1_n1):
        cs = [ (cd_n1_j[0], (UP, cd_n1_j[1]))
             , (cd_i_n1[0], (LEFT, cd_i_n1[1]))]
        if vc == hc:
            cs.append((cd_n1_n1[0]+1, (UP_LEFT, cd_n1_n1[1])))
        max_count, _ = max(cs)
        cd_i_j = ( max_count
                 , tuple(pair for count, pair in cs if count == max_count)
                 )
        return cd_i_j
class LCS_RowByRow__directions(LCS_RowByRow__ndirections):
    def get_directions(self):
        return self.get_last_count_data()[-1]
    def iter_reversed_LCS_directions1(self):
        return iter_llist(self.get_directions())
    def make_cd_i_j_from_Up_Left_UpLeft(self, vc, hc, cd_n1_j, cd_i_n1, cd_n1_n1):
        cs = [ (cd_n1_j[0], (UP, cd_n1_j[1]))
             , (cd_i_n1[0], (LEFT, cd_i_n1[1]))]
        # if vc == hc:
        if vc == hc:
            cs.append((cd_n1_n1[0]+1, (UP_LEFT, cd_n1_n1[1])))
        cd_i_j = max(cs)
        if cd_i_j[0] == cd_n1_j[0]:
            cd_i_j = cd_n1_j # remove UP
        return cd_i_j


def test_LCS_RowByRow__impl():
    horizontal_string = 'AGCAT'
    vertical_string = 'GAC'
    lcs_set = {'GA', 'GC', 'AC'}
    for cls in  [ LCS_RowByRow__ndirections
                , LCS_RowByRow__directions
                , LCS_RowByRow__common_elements
                ]:
        lcs_obj = cls(horizontal_string)
        lcs_obj.feed(vertical_string)
        assert 2 == lcs_obj.calc_longest_common_subsequence_length()
        lcs = lcs_obj.build_longest_common_subsequence1()
        assert ''.join(lcs) in lcs_set
test_LCS_RowByRow__impl()


