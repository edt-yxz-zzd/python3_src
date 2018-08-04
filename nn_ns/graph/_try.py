dedge2face = [None]*6

for i, face in enumerate(dedge2face):
    dedge2face[i] = 2
for face in dedge2face:
    dedge2face[2] = 2
a = sorted((2,1,3,4,0))
b = a[::-1]

c = list(range(5))
c = c[2:-1:-1]

_ = b[-1:]
