

assert (0 - 1) >> 2 == 0 - 1 >> 2 != 0 - (1 >> 2)

# so, A -tag --opt >>f -tag2 ==>> (A -tag --opt) >>(f -tag2)


eg = '''
# import fresh objects
from my_constructors.nonterminal import A, B, C 
from my_constructors.terminal import a, b, c
from my_constructors.attribute import child1, child2
from my_constructors.filter import f, g, h
from my_constructors.local_tag import tag1, tag2
from my_constructors.global_tag import opt1, opt2



# A -> B C
A[child1:B, child2:C] # init
A[B, C] # cannot init twice
A[B -tag1 --opt1 >>f -tag2 >>g --opt2]

# A -> B | C
A(B, C)
A(B | C)

# A -> B | ''
A(B, ())
A(B | ())

A*[1,3] ==>> A{1,3} == A[1..3] == A A A | A A | A
A*[1,()] ==>> A{1,} == A+
A*3 ==>> A*[3,3]
A.x ==>> A+
A.o ==>> A*
A.z ==>> A?


A[()] # null
A(()) # null
A() # dead






'''
