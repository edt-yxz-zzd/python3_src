WORDSIZE = 64 # bit
intsize = 4   # Byte

m = lambda: (WORDSIZE-1+n)//WORDSIZE
# if s=1, nedges = n*(n-1)/2:
packed_form_size = lambda: n*m()*WORDSIZE//8      # Byte
sparse_form_size = lambda: intsize*(n*n + 3*n)//2
ss = lambda:(packed_form_size(), sparse_form_size())

tpl = lambda s:'{:10,} B = {:7.5} KB = {:7.5} MB'.format(s, s/1024, s/2**20)

for n in range(100000, 140000, 10000):
    pks, sps = ss()
    
    print('n = {:5}, pack={}, sparse={}'.format(n, tpl(pks), tpl(sps)))

