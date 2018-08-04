
class SliceTuple:
    def __getitem__(self, key):
        return key


s = SliceTuple()
sin = '''
s[:,:]
s[2,4]
s[:2,:]
s[:2,4:]
s[:2,4:3,:]
s[:2,4]
s[2,4]
s[2,]
s[2]
s[:(2,4)]'''
'''
s[1:2:3:4]
    s[1:2:3:4]
           ^
SyntaxError: invalid syntax
s[]
    s[]
      ^
SyntaxError: unexpected EOF while parsing
'''
import io
fin = io.StringIO(sin)
for line in fin:
    line = line.strip()
    if line:
        print(line, ' '*(12-len(line)), eval(line))


'''
s[:,:]        (slice(None, None, None), slice(None, None, None))
s[2,4]        (2, 4)
s[:2,:]       (slice(None, 2, None), slice(None, None, None))
s[:2,4:]      (slice(None, 2, None), slice(4, None, None))
s[:2,4:3,:]   (slice(None, 2, None), slice(4, 3, None), slice(None, None, None))
s[:2,4]       (slice(None, 2, None), 4)
s[2,4]        (2, 4)
s[2,]         (2,)
s[2]          2
s[:(2,4)]     slice(None, (2, 4), None)
'''





        
