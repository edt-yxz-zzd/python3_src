'''
Definition of GRAPH6 and SPARSE6.

  All numbers in this description are in decimal unless obviously in
  binary.  GRAPH6 and SPARSE6 are text formats, and a file containing
  them is a text file.

  Apart from the header, there is one object per line.  Apart from the
  header and the end-of-line characters, all bytes have a value in the
  range 63-126 (which are all printable ASCII characters).

  BIT VECTORS:

  A bit vector x of length k can be represented as follows.  
      Example:  1000101100011100

  (1) Pad on the right with 0 to make the length a multiple of 6.
      Example:  100010110001110000

  (2) Split into groups of 6 bits each.
      Example:  100010 110001 110000

  (3) Add 63 to each group, considering them as bigendian binary numbers.
      Example:  97 112 111

  These values are then stored one per byte.  
  So, the number of bytes required is ceiling(k/6).

  Let R(x) denote this representation of x as a string of bytes.
      
  SMALL NONNEGATIVE INTEGERS:
 
  Let n be an integer in the range 0-262143 (262143 = 2^18-1).

  If 0 <= n <= 62, define N(n) to be the single byte n+63.
  If n >= 63, define N(n) to be the four bytes 126 R(x), where
    x is the bigendian 18-bit binary form of n.

  Examples:  N(30) = 93
             N(12345) = N(000011 000000 111001) = 126 69 63 120


  GRAPH6 format:

  Suppose G has n vertices.  Write the upper triangle of the adjacency
  matrix of G as a bit vector x of length n(n-1)/2, using the ordering
  (0,1),(0,2),(1,2),(0,3),(1,3),(2,3),...,(n-1,n).

  Then the graph is represented as  N(n) R(x).

    Example: Suppose n=5 and G has edges 0-2, 0-4, 1-3 and 3-4.

       x = 0 10 010 1001
    
       Then N(n) = 68 and R(x) = R(010010 100100) = 81 99.
       So, the graph is  68 81 99.

  Note that GRAPH6 format cannot represent loops or parallel edges.

  SPARSE6 format:

  The encoded graph consists of:
     (1) The character ':'.   (This is present to distinguish
                                  the code from GRAPH6 format.)
     (2) The number of vertices.
     (3) A list of edges.
     (4) end-of-line

  Loops and multiple edges are supported, but not directed edges.

  Number of vertices n:  Represented as N(n) like in GRAPH6 format.

  List of edges:

    Let k be the number of bits needed to represent n-1 in binary.
    The remaining bytes encode a sequence R(z) where
      z = b[0] x[0] b[1] x[1] b[2] x[2] ... b[m] x[m] ...

    Each b[i] occupies 1 bit, and each x[i] occupies k bits.
    Padding at the end is chosen so that the decoding algorithm below
    does not imply any spurious edges.

    The vertices of the graph are 0..n-1.
    The edges encoded by this sequence are determined thus:

       v = 0
       for i from 0 to m do
          if b[i] = 1 then v = v+1 endif;
          if x[i] > v then v = x[i] else output {x[i],v} endif
       endfor

    Example:    :Fa@x^
    ':' indicates sparse6 format.
    Subtract 63 from the other bytes and write them in binary, six bits each.
         000111 100010 000001 111001 011111
    The first byte is not 63, so it is n.  n=7
    n-1 needs 3 bits (k=3).  Write the other bits in groups of 1 and k:
      1 000  1 000  0 001  1 110   0 101  1 111
    This is the b/x sequence  1,0 1,0 0,1 1,6 0,5 1,7.
    The 1,7 at the end is just padding.
    The remaining pairs give the edges 0-1 1-2 5-6.

'''

# networkx.parse_graph6




def char2int(c):
    n = ord(c) - 63
    assert 0 <= n < 64
    return n

def int2char(i):
    assert 0 <= i < 64
    i += 63
    return chr(i)
    
def str2int(s, L = 3):
    assert len(s) == L
    n = 0
    for c in s:
        i = char2int(c)
        n *= 64
        n += i
    return n

def int2str(i, L = 3):
    bs = bin(i)[2:]
    r = L*6 - bs
    assert r >= 0
    if r:
        bs = '0'*r + bs

    return bin2str(bs)
    

def read_n(s):
    assert len(s) > 0
    n = char2int(s[0])
    if n != 63:
        assert 0 <= n < 63
        return (n, 1)
    
    assert len(s) > 3
    s = s[1:4]
    return (str2int(s), 4)
        
def write_n(n):
    assert n >= 0
    if n < 63:
        return int2char(n)
    assert n < 2**18
    return chr(126) + int2str(n)

def str2bin(s, nv):
    nbit = nv*(nv-1)//2
    L = (nbit+5)//6 # == len(s)
    n = str2int(s, L)
    bs = bin(n)[2:]
    bs = '0'*(6*L - len(bs)) + bs[:len(bs) - (6*L - nbit)]
    assert len(bs) == nbit
    return bs


def bin2str(bs):
    r = len(bs) % 6
    if r:
        bs += '0'*(6-r)

    s = []
    for i in range(0, len(bs), 6):
        n = int(bs[i: i+6], 2)
        s.append(int2char(n))

    return ''.join(s)
    


def bin2up3(bs, nv):
    nbit = nv*(nv-1)//2
    assert len(bs) == nbit
    i = 0
    edge = []
    for col in range(nv):
        for row in range(col):
            if bs[i] == '1':
                edge.append((row, col))
            i += 1
    return edge



def up32bin(edge, nv):
    nbit = nv*(nv-1)//2
    bs = ['0']*nbit
    for row, col in edge:
        assert 0 <= row < col < nv
        pre = col*(col-1)//2
        idx = pre + row
        assert bs[idx] == '0'
        bs[idx] = '1'
    return ''.join(bs)


def line2up3(line):
    assert line[-1] == '\n'
    nv, k = read_n(line)
    bs = str2bin(line[k:-1], nv)
    return (bin2up3(bs, nv), nv)

def up32line(edge, nv):
    return write_n(nv) + bin2str(up32bin(edge, nv)) + '\n'
    


    
    
