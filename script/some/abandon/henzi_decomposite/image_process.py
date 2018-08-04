

import math # atan2(y,x)->[-pi, pi] : (0, -1)->pi but a(-0.,-1)->-pi
# img[y][x] = pix
# top row = img[0]      # y-axis go down
# top-left = img[0][0]  # x-axis go right

def scale(img, scale_xy):
    y_type = type(img)
    new = y_type()
    if len(img) == 0:
        return new
    
    x_type = type(img[0])
    scale_x, scale_y = scale_xy

    ls = []
    for old_row in img:
        row = x_type(pix for pix in old_row for _ in range(scale_x))
        ls.extend(x_type(row) for _ in range(scale_y))

    new = y_type(ls)
    assert len(img) * scale_y == len(new)
    assert len(img[0]) * scale_x == len(new[0])

    return new

def add_border(img, width, color):
    y_type = type(img)
    x_type = type(img[0])

    XL = len(img[0])
    ls = [x_type([color] * (XL+width*2)) for _ in range(width)]
    for row in img:
        tmp = [color] * width
        tmp.extend(row)
        tmp += [color] * width
        ls.append(x_type(tmp))
    ls.extend(x_type([color] * (XL+width*2)) for _ in range(width))
    new = y_type(ls)
    return new


def count_num_block(bytes01):
    n01 = bytes01.count(b'\0\1')
    n10 = bytes10.count(b'\1\0')
    n = max(n01, n10)
    return n

neighbor_idc = [(dx, -1) for dx in range(-1, 2)] + [(1, 0)]
neighbor_idc = neighbor_idc + [(-dx, -dy) for dx, dy in neighbor_idc]
assert len(neighbor_idc) == 8
assert all((dx1==dx2 or dy1==dy2) for (dx1, dy1), (dx2, dy2) in \
           zip(neighbor_idc, neighbor_idc[1:]))

def get_neighbors(img, x, y):
    nbs = bytes(bool(img[y+dy][x+dx]) for dx, dy in neighbor_idc)
    return nbs

def skeleton_border2pix(img_01, k = 3):
    # del if 4 neighbors connected
    # requires: img[:2] img[-2:] img[:][:2] img[:][-2:] is white/0

    def exist_k_neighbors(neighbors, k):
        nbs = neighbors + neighbors[:k-1]
        return -1 != nbs.find(b'\1' * k)

    def is_black(img, x, y):
        return img[y][x]
    def is_intersection(neighbors):
        n = count_num_block(neighbors)
        return n > 1
        
    def del_xy(img, x, y):
        img[y][x] = 0
        return

    for y in range(1, len(img)-1):
        for x in range(1, len(img[0])-1):
            if is_black(img, x, y):
                neighbors = get_neighbors(img, x, y)
                if not is_intersection(neighbors):
                    if exist_x_neighbors(neighbors, k):
                        del_xy(img, x, y)


    return



    
vex2xy, edges = pick_up_graph(img)
