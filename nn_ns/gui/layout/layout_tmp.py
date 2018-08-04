'''
from functools import reduce
from itertools import accumulate, product, islice

import operator

from root.math.math_func import vadd, rproduct, vsub
'''

from .LayoutGrid_old import *
from sand import Walk
from root.math.math_func import vadd














def testLayout(constructor, args_outsize_ls):
    data = args_outsize_ls
    ls = []
    for args, outSize in data:
        layout = constructor(*args)
        assert layout.getOutsize() == outSize
        ls.append(layout)
        
    return ls

class __Data:
    dataLayoutGrid = [
        ([(3, 2), [LayoutBox(minSize=(i,i)) for i in range(3)]], (3, 3)),
        ([(2, 3), [LayoutBox(minSize=(i,i)) for i in range(3)]], (3, 2)),
        ([(0,0), []], (0, 0)),
        ]

    dataLayoutHBox = [
        ([[LayoutBox(minSize=(i,i)) for i in range(10)]], (45, 9)),
        ([[]], (0, 0)),
        ]

    dataLayoutVBox = [
        ([[LayoutBox(minSize=(i,i)) for i in range(10)]], (9, 45)),
        ([[]], (0, 0)),
        ]

    dataLayout工 = [
        ([[LayoutBox(minSize=(i,i)) for i in range(5)]], (6, 7)),
        ]

    dataLayout井 = [
        ([[LayoutBox(minSize=(i,i)) for i in range(9)]], (21, 15)),
        ]

    dataLayoutUnion = [
        ([[LayoutBox(minSize=(i,i)) for i in range(7)]], (6, 6)),
        ]


def test():
    dataLayoutClassNames = (key for key in dir(__Data) if key.startswith('dataLayout'))
        

    layouts = []
    for dataLayoutClassName in dataLayoutClassNames:
        className = dataLayoutClassName[4:]
        layoutClass = eval(className)
        
        data = getattr(__Data, dataLayoutClassName)
        r = testLayout(layoutClass, data)
        layouts.extend(r)

    v = LayoutVBox(layouts)
    return v


class DrawLayoutPath2Children:
    def __init__(self):pass
    def __call__(self, path):
        layout, childOffset = node = path[-1]
        if isinstance(layout, LayoutChildren):
            for child, (childOffset, _) in \
                zip(layout.getChildren(), \
                    layout.getChildrenOffsetOutsizes()):
                yield child, childOffset
                
        return None
    
        
def drawLayout(layout, background = ' '):
    L = len(background)
    c, r = outSize = layout.getOutsize()
    txt = [[0]*c for i in range(r)]

    def draw(txt, location, size):
        x0, y0 = location
        w, h = size
        for x in range(x0, x0+w):
            for y in range(y0, y0+h):
                try:
                    txt[y][x] += 1
                except:
                    print('r, c', r, c)
                    print('location, size', location, size)
                    print('x, y', x, y)
                    raise
                
    def to_txt(txt):
        ls = []
        for row in txt:
            for i in range(len(row)):
                if not row[i]:
                    row[i] = background
                else:
                    tpl = '{:*^' + str(L) +'}'
                    fg = tpl.format(row[i])
                    assert len(fg) == L # row[i] to big will cause error
                    row[i] = ''.join((b if f == '*' else f) for f, b in zip(fg, background))
            ls.append(''.join(row))
        
        return '\n'.join(ls)
    
                    

    root = layout, (0,0)
    location_stack = [(0,0)]
    for action, path, node in Walk(root, DrawLayoutPath2Children()):
        if action == Walk.ENTER:
            assert len(location_stack) == len(path)
            child, childOffset = node
            offset = child.getOffset()
            parent_location = location_stack[-1]
            location = vadd(parent_location, childOffset, offset)
            location_stack.append(location)
            size = child.getSize()
            
            draw(txt, location, size)
        elif action == Walk.EXIT:
            location_stack.pop()
            assert len(location_stack) == len(path)
            
    txt = to_txt(txt)
    return txt



            
        
        


if __name__ == '__main__':
    v = test()
    drawLayout(v)



        



