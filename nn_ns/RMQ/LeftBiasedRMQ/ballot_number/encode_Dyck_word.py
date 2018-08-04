

'''
NOTE:
    time (O(Q^2) if table not cached else O(Q)) * ballot_number(Q,Q).'+'
    = time (O(Q^2) if table not cached else O(Q)) * Catalan_number(Q).'+'
    = time O(Q^3) if table not cached else O(Q^2)
    very slow!!!

    but if cached and ballot_number is only a MACHINE_WORD
        then O(Q)!!!
    [ballot_number is a MACHINE_WORD]
        Catalan_number(s) = 4^s /(sqrt(pi)*s^(3/2)) * (1+ O(1/s))
        ==>> ballot_number(q,q) = 4^q * O(1) <= 2*WORD_BITS
        ==>> q <= WORD_BITS/2
            # e.g. q <= 32
    NOTE:
        this encode algorithm used in RMQ to calc normal_block_type
        and assume ballot_number.'+' to be O(1)
        so, complete_normal_block_size <= 32
        it seems complete_normal_block_size is very small




see: ballot_number.py
    # maybe unbalanced
    encode Dyck_word with fixed (num_opens,num_closes)
        by encoding = keyPQ or keyQP
'''



__all__ = '''
    encode_Dyck_word_with_fixed_num_closes_opens
    DyckWordEncoder__with_fixed_num_closes_opens


    encoding2PosMoveEncoder
    IPosMoveEncoder
        PosMoveEncoder__keyQP
            aPosMoveEncoder__keyQP
        PosMoveEncoder__keyPQ
            aPosMoveEncoder__keyPQ

    '''.split()

from collections import namedtuple
from abc import ABC, abstractmethod
from .ballot_number import ballot_number__by_table as _ballot_number

def make_offset0_Dyck_word_for_keyPQ(P,Q):
    # (P,Q) == (num_closes, num_opens)
    # output: rex'1{Q}0{P}'
    if not (0<=P<=Q): raise ValueError
    return [1]*Q + [0]*P
def make_offset0_Dyck_word_for_keyQP(P,Q):
    # (P,Q) == (num_closes, num_opens)
    # output: rex'(10){P}1{Q-P}'
    if not (0<=P<=Q): raise ValueError
    return [1,0]*P + [1]*(Q-P)

def encode_Dyck_word_with_fixed_num_closes_opens(Dyck_word, encoding_or_encoder):
    ''':: Iter Boolable -> (str|IPosMoveEncoder) -> (UInt->UInt->UInt) -> (UInt, (UInt, UInt))


time:
    Q = num_opens >= Dyck_word/2
    let Q = O(len(Dyck_word))
    this ~ time DyckWordEncoder__with_fixed_num_closes_opens.'begin'
         ~ O(Q) * encoder.'edge2weight_ex'

    time O(Q^3) if table not cached else O(Q^2)
    or time (O(Q^2) if table not cached else O(Q)) * ballot_number.'+'

    using ballot_number__by_table:
        # NOTE:
        #   bit_size_of(ballot_number) = O(Q)
        #   ballot_number.'+' ~ time O(Q)
        create_table ~ time O(Q^3)  # table size Q^2 * bit_size O(Q)
        query ~ time O(Q^2)         # Q queries * bit_size O(Q) # uint.'+'
        i.e. if table has been cached, need only O(Q^2)
    if using ballot_number__by_direct_calc:
        ballot_number(p,q)  ~ time O(q^2 * log(q))
        ==>> time O(Q^3 * log(Q))

__this__ Dyck_word encoding_or_encoder
    = (encode_uint, (num_closes, num_opens))

input:
    # see: DyckWordEncoder__with_fixed_num_closes_opens
    Dyck_word :: Iter Boolable
    encoding_or_encoder :: IPosMoveEncoder | 'keyPQ' | 'keyQP'

    #ballot_number :: UInt -> UInt -> UInt
        ballot(p,q)
            | 0 <= p <= q = C(q+p,p)*(q-p+1)/(q+1)
            | otherwise = 0
        # used to verify "offset"
        p - num_closes
        q - num_opens

output:
    encode_uint, num_closes, num_opens :: UInt


example:
    >>> ballot = _ballot_number
    >>> this = encode_Dyck_word_with_fixed_num_closes_opens
    >>> keyPQ = 'keyPQ' # prefer keyPQ
    >>> keyQP = 'keyQP'
    >>> P = 6; Q = 7

    #>>> this(rex'1{Q}0{P}', 'keyPQ') == (0, (P,Q))
    >>> Dyck_word_PQ0 = make_offset0_Dyck_word_for_keyPQ(P,Q)

    #>>> this(rex'(10){P}1{Q-P}', 'keyQP') == (0, (P,Q))
    >>> Dyck_word_QP0 = make_offset0_Dyck_word_for_keyQP(P,Q)

    >>> this(Dyck_word_PQ0, keyPQ) == (0, (P,Q))
    True
    >>> this(Dyck_word_QP0, keyPQ) == (ballot(P,Q)-1, (P,Q))
    True
    >>> this(Dyck_word_QP0, keyQP) == (0, (P,Q))
    True
    >>> this(Dyck_word_PQ0, keyQP) == (ballot(P,Q)-1, (P,Q))
    True



    >>> encoding = 'keyPQ'
    >>> this([], encoding)
    (0, (0, 0))
    >>> this([1], encoding)
    (0, (0, 1))
    >>> this([1,0], encoding)
    (0, (1, 1))
    >>> this([1,1], encoding)
    (0, (0, 2))

    >>> this([1,0,1], encoding)
    (1, (1, 2))
    >>> this([1,1,0], encoding)
    (0, (1, 2))
    >>> this([1,1,1], encoding)
    (0, (0, 3))

    >>> this([1,0,1,0], encoding)
    (1, (2, 2))
    >>> this([1,0,1,1], encoding)
    (2, (1, 3))
    >>> this([1,1,0,0], encoding)
    (0, (2, 2))
    >>> this([1,1,0,1], encoding)
    (1, (1, 3))
    >>> this([1,1,1,0], encoding)
    (0, (1, 3))
    >>> this([1,1,1,1], encoding)
    (0, (0, 4))

    >>> this([1,0,1,0,1], encoding)
    (4, (2, 3))
    >>> this([1,0,1,1,0], encoding)
    (2, (2, 3))
    >>> this([1,0,1,1,1], encoding)
    (3, (1, 4))
    >>> this([1,1,0,0,1], encoding)
    (3, (2, 3))
    >>> this([1,1,0,1,0], encoding)
    (1, (2, 3))
    >>> this([1,1,0,1,1], encoding)
    (2, (1, 4))
    >>> this([1,1,1,0,0], encoding)
    (0, (2, 3))
    >>> this([1,1,1,0,1], encoding)
    (1, (1, 4))
    >>> this([1,1,1,1,0], encoding)
    (0, (1, 4))
    >>> this([1,1,1,1,1], encoding)
    (0, (0, 5))




    >>> encoding = 'keyQP'
    >>> this([], encoding)
    (0, (0, 0))
    >>> this([1], encoding)
    (0, (0, 1))
    >>> this([1,0], encoding)
    (0, (1, 1))
    >>> this([1,1], encoding)
    (0, (0, 2))

    >>> this([1,0,1], encoding)
    (0, (1, 2))
    >>> this([1,1,0], encoding)
    (1, (1, 2))
    >>> this([1,1,1], encoding)
    (0, (0, 3))

    >>> this([1,0,1,0], encoding)
    (0, (2, 2))
    >>> this([1,0,1,1], encoding)
    (0, (1, 3))
    >>> this([1,1,0,0], encoding)
    (1, (2, 2))
    >>> this([1,1,0,1], encoding)
    (1, (1, 3))
    >>> this([1,1,1,0], encoding)
    (2, (1, 3))
    >>> this([1,1,1,1], encoding)
    (0, (0, 4))

    >>> this([1,0,1,0,1], encoding)
    (0, (2, 3))
    >>> this([1,0,1,1,0], encoding)
    (2, (2, 3))
    >>> this([1,0,1,1,1], encoding)
    (0, (1, 4))
    >>> this([1,1,0,0,1], encoding)
    (1, (2, 3))
    >>> this([1,1,0,1,0], encoding)
    (3, (2, 3))
    >>> this([1,1,0,1,1], encoding)
    (1, (1, 4))
    >>> this([1,1,1,0,0], encoding)
    (4, (2, 3))
    >>> this([1,1,1,0,1], encoding)
    (2, (1, 4))
    >>> this([1,1,1,1,0], encoding)
    (3, (1, 4))
    >>> this([1,1,1,1,1], encoding)
    (0, (0, 5))


'''
    self = DyckWordEncoder__with_fixed_num_closes_opens.begin(
            encoding_or_encoder, Dyck_word)
    return self.offset, (self.fst, self.snd)















#########################
class IPosMoveEncoder(ABC):
    '''encoder for eval weight of pos_move edge

see: ballot_number.py :: weight_of<(x0,y0), key>
    encode good_path
    encode Dyck_word
    encode canonical_Cartesian_tree
'''
    @abstractmethod
    def edge2weight_ex(self, begin_pt_of_pos_move, is_pos_qmove):
        '''edge2weight_ex :: Point -> bool -> (UInt, Point)

Point = (UInt,UInt)
edge2weight_ex begin_pt_of_pos_move is_pos_qmove -> (weight, end_pt_of_pos_move)

see: edge2weight
'''
        fst, snd = begin_pt_of_pos_move
        weight = self.edge2weight(begin_pt_of_pos_move, is_pos_qmove)
        if is_pos_qmove:
            snd += 1
        else:
            fst += 1
        end_pt_of_pos_move = (fst, snd)
        return weight, end_pt_of_pos_move
    def edge2weight(self, begin_pt_of_pos_move, is_pos_qmove):
        '''edge2weight :: Point -> bool -> UInt

Point = (UInt,UInt)
edge2weight begin_pt_of_pos_move is_pos_qmove -> weight



def edge2weight
    see: ballot_number.py :: weight_of<(x0,y0), key>
        weight_of<(x0,y0), key> :: (Point, Point) -> UInt
        # weight_of<path_begin, key> (begin_pt_of_neg_move, end_pt_of_neg_move) = weight
        #   where exist neg_move, s.t. begin_pt_of_neg_move+neg_move == end_pt_of_neg_move

    -- self is the "key"/encoding
    -- (x0,y0) == (0,0)
    -- define edge2weight
    edge2weight begin_pt_of_pos_move is_pos_qmove
        = ballot_number.weight_of<(0,0),self> (end_pt_of_pos_move, begin_pt_of_neg_move)
        where end_pt_of_pos_move -- see below



input:
    begin_pt_of_pos_move :: (UInt, UInt)
        begin_pt_of_pos_move.fst >= 0
        begin_pt_of_pos_move.snd >= 0

    is_pos_qmove :: bool
        the conceptual input edge is a qmove or pmove?

    # ballot_number :: UInt -> UInt -> UInt
        ballot(p,q)
            | 0 <= p <= q = C(q+p,p)*(q-p+1)/(q+1)
            | otherwise = 0



output:
    weight :: UInt
        # see: ballot_number.py :: weight_of



-- compare begin_pt_of_pos_move/begin_pt_of_neg_move
begin_pt_of_pos_move :: (UInt, UInt)
    is diff with begin_pt_of_neg_move
    begin_pt_of_neg_move > end_pt_of_neg_move
    begin_pt_of_pos_move < end_pt_of_pos_move

    end_pt_of_neg_move.fst = begin_pt_of_neg_move.fst - not is_neg_qmove
    end_pt_of_neg_move.snd = begin_pt_of_neg_move.snd - is_neg_qmove

    end_pt_of_pos_move.fst = begin_pt_of_pos_move.fst + not is_pos_qmove
    end_pt_of_pos_move.snd = begin_pt_of_pos_move.snd + is_pos_qmove

'''
        weight, end_pt_of_pos_move = self.edge2weight_ex(
                        begin_pt_of_pos_move, is_pos_qmove)
        return weight

    @property
    def ballot_number(self):
        '''ballot_number :: UInt -> UInt -> UInt

ballot(p,q)
    | 0 <= p <= q = C(q+p,p)*(q-p+1)/(q+1)
    | otherwise = 0
'''
        return _ballot_number


class PosMoveEncoder__keyQP(IPosMoveEncoder):
    def edge2weight_ex(self, begin_pt_of_pos_move, is_pos_qmove):
        p, q = begin_pt_of_pos_move
        if is_pos_qmove:
            # qmove
            # since qmove before pmove, offset is 0
            return 0, (p,q+1)

        # pmove
        end_pt_of_pos_move = P,Q = p+1,q
        return self.ballot_number(P,Q-1), end_pt_of_pos_move
        return self.ballot_number(p+1,q-1), end_pt_of_pos_move
aPosMoveEncoder__keyQP = PosMoveEncoder__keyQP()

class PosMoveEncoder__keyPQ(IPosMoveEncoder):
    def edge2weight_ex(self, begin_pt_of_pos_move, is_pos_qmove):
        p, q = begin_pt_of_pos_move
        if not is_pos_qmove:
            # pmove
            # since pmove before qmove, offset is 0
            return 0, (p+1,q)

        # qmove
        end_pt_of_pos_move = P,Q = p,q+1
        return self.ballot_number(P-1,Q), end_pt_of_pos_move
        return self.ballot_number(p-1,q+1), end_pt_of_pos_move
aPosMoveEncoder__keyPQ = PosMoveEncoder__keyPQ()


_encoding2PosMoveEncoder = \
    {'keyPQ':aPosMoveEncoder__keyPQ, 'keyQP':aPosMoveEncoder__keyQP}
def encoding2PosMoveEncoder(encoding):
    # -> IPosMoveEncoder
    d = _encoding2PosMoveEncoder
    return d[encoding]














#####################

DyckWordEncoder__with_fixed_num_closes_opens_Base =\
    namedtuple('DyckWordEncoder__with_fixed_num_closes_opens_Base'
        , '''
        fst
        snd
        offset
        encoder
        '''.split())
class DyckWordEncoder__with_fixed_num_closes_opens(
        DyckWordEncoder__with_fixed_num_closes_opens_Base):
    '''Dyck_word :: [Boolable] # maybe unbalanced

immutable
time
    self.'ifeed' ~ time O(1)* encoder.'edge2weight_ex'
    self.'begin' ~ self.'ifeeds' ~ time O(len(input)) * encoder.'edge2weight_ex'

if bool(char): char is a open
else:          char is a close
    why?
        # open > close
        # 1      0
            Dyck_word0 = [1,0]
            Dyck_word1 = [1,0,1,0]
            Dyck_word2 = [1,1,0,0]
            sorted are [Dyck_word0, Dyck_word1, Dyck_word2]

        # open < close
        # 0      1
            Dyck_word0 = [0,1]
            Dyck_word1 = [0,1,0,1]
            Dyck_word2 = [0,0,1,1]
            sorted are [Dyck_word2, Dyck_word0, Dyck_word1]
            bad idea!!!

encoding = keyPQ | keyQP
see: ballot_number.py
    open <==> PosQMove
see: IPosMoveEncoder
'''
    __slots__ = ()
    @classmethod
    def begin(cls, encoding_or_encoder, Dyck_word):
        self = cls((0,0), 0, encoding_or_encoder)
        return self.ifeeds(Dyck_word)

    def __new__(cls, begin_pt_of_next_pos_move, offset, encoding_or_encoder:[IPosMoveEncoder,str]):
        '''

input:
    begin_pt_of_next_pos_move :: (UInt, UInt)
        # see: IPosMoveEncoder.begin_pt_of_pos_move
        == end_pt_of_prev_pos_move
        let (fst, snd) = begin_pt_of_next_pos_move
        fst - num_closes
        snd - num_opens
    offset :: UInt
        = encode_good_path<begin_pt_of_next_pos_move, (0,0), encoding>
            some_a_good_path<begin_pt_of_next_pos_move, (0,0)>
        offset = 0 if begin_pt_of_next_pos_move==(0,0)
        0 <= offset <= ballot_number(fst, snd)
    encoding :: IPosMoveEncoder | 'keyPQ' | 'keyQP'

    # ballot_number :: UInt -> UInt -> UInt
        ballot(p,q)
            | 0 <= p <= q = C(q+p,p)*(q-p+1)/(q+1)
            | otherwise = 0
        # used to verify "offset"
        p - num_closes
        q - num_opens
'''
        fst, snd = begin_pt_of_next_pos_move
        if not (0 <= fst <= snd): raise ValueError
        if not (0 <= offset <= _ballot_number(fst, snd)): raise ValueError
        if type(encoding_or_encoder) is str:
            encoder = encoding2PosMoveEncoder(encoding_or_encoder)
        elif not isinstance(encoding_or_encoder, IPosMoveEncoder): raise TypeError
        else:
            encoder = encoding_or_encoder


        self = super(__class__, cls).__new__(cls, fst, snd, offset, encoder)
        return self

        self.fst = fst
        self.snd = snd
        self.offset = offset
        self.encoder = encoder
        #self.ballot_number = ballot_number


    def ifeeds(self, boolable_chars):
        'ifeeds :: Iter Boolable -> __class__'
        for ch in boolable_chars:
            self = self.ifeed(ch)
        return self

    def ifeed(self, boolable_char):
        ''' ifeed :: Boolable -> __class__

input:
    boolable_char :: Boolable
        assume Dyck_word[:i] have been fed
        now feed(Dyck_word[i])
        i.e. boolable_char is Dyck_word[i]

    # ballot_number :: UInt -> UInt -> UInt
        ballot(p,q)
            | 0 <= p <= q = C(q+p,p)*(q-p+1)/(q+1)
            | otherwise = 0
        # used to make __class__
'''

        # true_char is open is PosQMove
        is_pos_qmove = is_open = bool(boolable_char)
        weight, end_pt_of_pos_move = self.encoder.edge2weight_ex(
                        (self.fst, self.snd), is_pos_qmove)
        offset = self.offset+weight
        return __class__(end_pt_of_pos_move, offset, self.encoder)

    @property
    def ballot_number(self):
        '''ballot_number :: UInt -> UInt -> UInt

ballot(p,q)
    | 0 <= p <= q = C(q+p,p)*(q-p+1)/(q+1)
    | otherwise = 0
'''
        return _ballot_number





if __name__ == "__main__":
    import doctest
    doctest.testmod()






