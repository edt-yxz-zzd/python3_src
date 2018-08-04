
'''
what if seq[:] and seq[1:] when seq is tuple?
tuple[:] is no-op
tuple[1:] do copy

'''


L = 10000000
seq = (1,)*L
input("seq = (1,)*{L}; now see the memory usage")
seq2 = seq[:]
input("seq2 = seq[:]; now see the memory usage")
seq3 = seq[1:]
input("seq3 = seq[1:]; now see the memory usage")

'''
    L = 10000000
    seq = ...
        python.exe 83_928K
    seq2 = ...
        python.exe 83_928K
    seq3 = ...
        python.exe 162_168K
'''

