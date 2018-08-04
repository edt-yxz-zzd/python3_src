
import random
from nn_ns.fileformat.single_color_bmp import single_color_bmp_write, single_color_bmp_read
#from sand import where, makedirs

'''
coordinate_set_of_black_points
or xys is a set of (x,y)

mx is a list of bytes of byte in {0x0, 0x1}
'''
'''
def life_game_step(coordinate_set_of_black_points):
    xys = coordinate_set_of_black_points
    xy2count = {}

    for x, y in xys:
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if (i,j) == (x,y): continue
                if (i,j) not in xy2count:
                    xy2count[(i,j)] = 0
                xy2count[(i,j)] += 1

    new_xys = set()
    for xy, count in xy2count.items():
        if count == 3:
            new_xys.add(xy)
        elif count == 2 and xy in xys:
            new_xys.add(xy)

    return new_xys'''

'''
xy-> wv
w = x+y
v = -x+y

x=(w-v)//2
y=(w+v)//2

'''

def xy2wv(xy):
    x,y = xy
    w = x + y
    v = -x + y
    return w,v
def wv2xy(wv):
    w,v = wv
    assert (w+v)%2 == 0
    x = (w-v)//2
    y = (w+v)//2
    return xy
def xys2wvs(xys):
    return type(xys)(xy2wv(xy) for xy in xys)
def wvs2xys(wvs):
    return type(wvs)(wv2xy(wv) for wv in wvs)

dxy_ls = [(-1,0), (1,0), (0,1), (0,-1)]
dxy_ls = [(x,y) for x in range(-1, 2) for y in range(-1, 2) if (x,y) != (0,0)]
dwv_ls = xys2wvs(dxy_ls)

assert len(dxy_ls) == 8

def life_game_step(xys, dxy_ls=dxy_ls):
    xy2count = {}

    for x, y in xys:
        for dx, dy in dxy_ls:
            xy = (x + dx,y + dy)
            if xy not in xy2count:
                xy2count[xy] = 0
            xy2count[xy] += 1

    new_xys = set()
    for xy, count in xy2count.items():
        if count == 3:
            new_xys.add(xy)
        elif count == 2 and xy in xys:
            new_xys.add(xy)

    return new_xys


def life_game_steps(xys, nsteps, dxy_ls=dxy_ls):
    xys = xys.copy()
    for _ in range(nsteps):
        xys = life_game_step(xys, dxy_ls)
    return xys






def id_f(x): return x

def minmax(ls, key = id_f):
    n = min(ls, key=key)
    x = max(ls, key=key)
    return n, x

def xys2xy0_size(xys):
    if not xys:
        return ()

    xs = [x for x,y in xys]
    ys = [y for x,y in xys]
    x0, x1 = minmax(xs)
    y0, y1 = minmax(ys)

    width = x1+1 - x0
    height = y1+1 - y0
    return (x0, y0, width, height)


def move_xys(xys, where):
    x0, y0 = where
    return type(xys)((x+x0, y+y0) for x, y in xys)

def normalize_xys(xys):
    xy0_size = xys2xy0_size(xys)
    if not xy0_size:
        assert not xys
        return type(xys)()

    x0, y0, width, height = xy0_size
    xys = move_xys(xys, (-x0, -y0))
    return xys


def select_big_area_by_scan_xys(xy0, size, xys):
    x0, y0 = xy0
    w, h = size
    xt, yt = x0+w, y0+h

    r = set()
    for x,y in xys:
        if x0 <= x < xt and y0 <= y < yt:
            r.add((x,y))
    return r
        
def select_small_area_by_scan_area(xy0, size, xys):
    x0, y0 = xy0
    w, h = size
    xt, yt = x0 + w, y0 + h
    
    r = set()
    for x in range(x0, xt):
        for y in range(y0, yt):
            xy = (x,y)
            if xy in xys:
                r.add(xy)

    return r

def rotate_xys_half_pie(xys):
    return type(xys)((-y, x) for x,y in xys)

def flip_xys_by_x_axis(xys):
    return type(xys)((x, -y) for x,y in xys)

def set2sorted_tuple(s):
    ls = list(s)
    ls.sort()
    return tuple(ls)

little_boy = {(0, 1), (1, 0), (0, 0), (0, 2), (2, 1)}
direction = (-1,-1)
little_boys = {}
for i in range(8):
    little_boy = normalize_xys(little_boy)
    little_boys[set2sorted_tuple(little_boy)] = direction
    little_boy = life_game_step(little_boy)

assert len(little_boys) == 4


for _fxy in [rotate_xys_half_pie, flip_xys_by_x_axis]:
    for little_boy, direction in list(little_boys.items()):
        little_boy = set(little_boy)
        little_boy = normalize_xys(_fxy(little_boy))
        direction, = _fxy([direction])
        little_boys[set2sorted_tuple(little_boy)] = direction
        


assert len(little_boys) == 4*4

wv_boys = {normalize_xys(xys2wvs(xy_boy)): xy2wv(xy_direction) \
           for xy_boy, xy_direction in little_boys.items()}

'''
def boundary_man_detect(wvs):'''
    

def is_man(xys):
    len_man = 5
    if len(xys) == len_man:
        xys = set2sorted_tuple(normalize_xys(xys))
        if xys in little_boys:
            return little_boys[xys]
    return False

def is_man_center(xys, xy):
    x, y = xy
    x -= 1
    y -= 1

    man_area_size = 3,3
    len_man = 5
    area = select_small_area_by_scan_area((x,y), man_area_size, xys)
    return is_man(area)



def init(n, p):
    xys = set()
    for i in range(n):
        for j in range(n):
            if random.random() < p:
                xys.add((i,j))

    return xys



def xys2mx(xys):
    xy0_size = xys2xy0_size(xys)
    if not xy0_size:
        return ''

    x0, y0, width, height = xy0_size
    xys = move_xys(xys, (-x0, -y0))


    mx = [[0 for y in range(height)] for x in range(width)]
    for x, y in xys:
        mx[x][y] = 1

    for i in range(len(mx)):
        mx[i] = bytes(mx[i])
    return mx


def mx2xys(mx):
    xys = set()
    for x in range(len(mx)):
        row = mx[x]
        for y in range(len(row)):
            if row[y]:
                xys.add((x,y))
    return xys


            



draw = xys2mx
def draw2txt(xys):
    mx = draw(xys)
    txt = []
    for row in mx:
        line = ['o' if b else ' ' for b in row]
        line.append('\n')
        txt.append(''.join(line))
    txt = ''.join(txt)

    return txt
'''
def bmp2mx(bmp):
    return single_color_bmp_read(bmp)
def mx2bmp(mx):
    return single_color_bmp_write(mx, len(mx), len(mx[0]) if len(mx) else 0)
'''

def xys2bmp(xys):
    mx = xys2mx(xys)
    bmp = single_color_bmp_write(mx, len(mx), len(mx[0]) if len(mx) else 0)

    return bmp

def bmp2xys(bmp):
    mx = single_color_bmp_read(bmp)
    xys = mx2xys(mx)
    return xys




output_folder = 'e:/temp_output/'
output_folder = r'E:\my_data\program_source\python3_src\root\temp/'

def output_txt(main_result, fname = output_folder+'life_game.txt'):
    
    eq, xys0, xys = main_result
    txt0 = draw2txt(xys0)
    txt = draw2txt(xys)

    with open(fname, 'w') as fout:
        fout.write('end state\n' if eq else 'not end\n')
        fout.write(txt0)
        fout.write('------------------\n')
        fout.write(txt)
        
def xys2bmp_file(xys, fname = output_folder+'life_game.bmp'):
    bmp = xys2bmp(xys)

    with open(fname, 'wb') as fout:
        fout.write(bmp)
        
def bmp_file2xys(fname = output_folder+'life_game.bmp'):
    with open(fname, 'rb') as fin:
        bmp = fin.read()
    xys = bmp2xys(bmp)
    return xys

def test_bmp():
    xys = bmp_file2xys(output_folder+'lg.bmp')
    bmp = xys2bmp(xys)
    xys2 = bmp2xys(bmp)
    assert xys == xys2


def _output_little_boys():
    for little_boy, i in zip(little_boys, range(16)):
        fn = './little_boy{}.bmp'.format(i)
        xys2bmp_file(set(little_boy), fn)




def main(n = 30, p = 0.1, nsteps = 1000):
    xys0 = init(n, p)
    r = life_game_steps(xys0, nsteps)

    return xys0, r


t = lambda n = 30, p = 0.1, nsteps = 1000:xys2bmp_file(main(n, p, nsteps)[-1])

    
if __name__ == '__main__':
    #output_bmp(main())
    #t()
    main()
    

    
    



