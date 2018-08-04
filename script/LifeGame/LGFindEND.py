

from sand_basic import fixed__package__
fixed__package__(__name__)
import sand
from sand import default_fix_paths

from .life_game import life_game_step, little_boys, is_man, is_man_center, \
     set2sorted_tuple, xys2xy0_size, select_small_area_by_scan_area, \
     minmax, xys2bmp_file

output_folder = './findEND/'
default_fix_paths('output', globals(), 'output_folder')

def boundary_man_detect(xys):
    area_size = 10, 10
    xy0_size = xys2xy0_size(xys)
    if not xy0_size:
        return False
    x0, y0, w, h = xy0_size
    xy0 = x0, y0
    xt, yt = x0+w, y0+h

    xmin = x0
    xmax = xt-1
    ymin = y0
    ymax = yt-1

    # xmin edge normal vector
    xminND = (-1, 0)
    xmaxND = (1, 0)
    yminND = (0, -1)
    ymaxND = (0, 1)
    class _EdgeData:
        def __init__(self, normal_vector, this_n):
            self.xys = []
            self.normal = normal_vector
            self.this_n = this_n # x or y
            self.man_centers = []
    edges = {
        'xmin':_EdgeData(xminND, xmin),\
        'xmax':_EdgeData(xmaxND, xmax),\
        'ymin':_EdgeData(yminND, ymin),\
        'ymax':_EdgeData(ymaxND, ymax),}
    for x, y in xys:
        if x == xmin:
            edge = 'xmin'
        elif x == xmax:
            edge = 'xmax'
        elif y == ymin:
            edge = 'ymin'
        elif y == ymax:
            edge = 'ymax'
        else:
            continue

        edges[edge].xys.append((x,y))

    edge_data = edges['xmin']
    ls = edge_data.xys
    keyfs = [(lambda xy:xy[0]), (lambda xy:xy[-1])]
    makexy = lambda this_n, other_n: (this_n, other_n) if other else (other_n, this_n)
    other_directions = [-1, 1]

    for edge_data in edges.values():
        other = bool(edge_data.normal[0])
        this = not other
        
        xys_on_this_edge = edge_data.xys
        if not xys_on_this_edge:
            continue
        
        this__other_ns = this__other_min, this__other_max = \
                         minmax(xys_on_this_edge, keyfs[other])
        this_direction = edge_data.normal[this]
        center_this_n = edge_data.this_n - edge_data.normal[this]
        for this__other_n, other_direction in zip(this__other_ns, other_directions):
            other_n = this__other_n[other]
            maybe_man_centers = [
                makexy(center_this_n, other_n),
                makexy(center_this_n, other_n + other_direction),
                ]
            direction = makexy(this_direction, other_direction)

            for maybe_man_center in maybe_man_centers:
                edge_data.man_centers.append((maybe_man_center, direction))
            
    for edge_data in edges.values():
        _man_centers, edge_data.man_centers = edge_data.man_centers, []
        for maybe_man_center, direction in _man_centers:
            r = is_man_center(xys, maybe_man_center)
            if r == direction:
                edge_data.man_centers.append((maybe_man_center, direction))

    w, h = area_size
    men = set()
    for edge_data in edges.values():
        assert len(edge_data.man_centers) <= 2
        #normal = edge_data.normal 
        for man_center, direction in edge_data.man_centers:
            x, y = man_center
            dx, dy = direction

            # move to boundary
            x += dx
            y += dy

            # move to area topleft
            x -= (1+dx)//2*(w-1)
            y -= (1+dy)//2*(h-1)

            xy = x,y
            area = select_small_area_by_scan_area(xy, area_size, xys)
            if is_man(area):
                men |= area
    return men
    

'''
    w, h = area_size
    d = {'xmin':[(1, 0), (w//2, 0)],\
         'xmax':[(-1, 0), (1-w//2, 0)],\
         'ymin':[(0, 1), (0, h//2)],\
         'ymax':[(0, -1), (0, 1-h//2)],}

    area_corners = []
    for x, y in xys:
        if x == xmin:
            key = 'xmin'
        elif x == xmax:
            key = 'xmax'
        elif y == ymin:
            key = 'ymin'
        elif y == ymax:
            key = 'ymax'
        else:
            continue
        




        
        dxy_for_center, dxy_for_area = d[key]
        dx, dy = dxy_for_center
        if is_man_center(xys, (x+dx,y+dy)):
            dx, dy = dxy_for_area
            area_corners.append((x+dx-w//2,y+dy-h//2))
    for xy in area_corners:
        area = select_small_area_by_scan_area(xy, area_size, xys)
        if is_man(area):
            return True

    return False'''
    
def corner_man_detect(xys):
    #return False
    area_size = 10, 10
    xy0_size = xys2xy0_size(xys)
    if not xy0_size:
        return False

    x0, y0, w, h = xy0_size
    xy0 = x0, y0
    xt, yt = x0+w, y0+h

    dxy_ls = [(x,y) for x in range(2) for y in range(2)]
    xy_ls = []
    aw, ah = area_size

    men = set()
    for dx, dy in dxy_ls:
        x = x0 + w*dx
        y = y0 + h*dx
        if not is_man_center(xys, (x+1-3*dx, y+1-3*dy)):
            continue

        x -= aw*dx
        y -= ah*dy
        area = select_small_area_by_scan_area((x,y), area_size, xys)
        if is_man(area):
            men |= area

    return men
'''
    w, h = area_size
    xyR = xt-w, y0
    xyU = x0, yt-h
    xyUR = xt-w, yt-h

    men = set()
    for xy in [xy0, xyR, xyU, xyUR]:
        area = select_small_area_by_scan_area(xy, area_size, xys)
        if is_man(area):
            men += area

    return men'''
    
    
#'''
def _life_game_find_END_step(xys, xys_man, step,
                             corner_man_detected_steps,
                             boundary_man_detected_steps):
    xys = life_game_step(xys)
    xys_man = life_game_step(xys_man)
    return _life_game_find_END_splitmen(xys, xys_man, step,
                                        corner_man_detected_steps,
                                        boundary_man_detected_steps)

def _life_game_find_END_splitmen(xys, xys_man, step,
                                 corner_man_detected_steps,
                                 boundary_man_detected_steps):
    xys_r = xys - xys_man

    loop = True
    while loop:
        loop = False
        if step % corner_man_detected_steps == 0:
            men = corner_man_detect(xys_r)
            if men:
                xys_man |= men
                xys_r -= men
                loop = True
                
        if step % boundary_man_detected_steps == 0:
            men = boundary_man_detect(xys_r)
            if men:
                xys_man |= men
                xys_r -= men
                loop = True
    return xys, xys_man, xys_r

def life_game_find_END(xys, max_num_steps, \
                       corner_man_detected_steps = 10, \
                       boundary_man_detected_steps = 100):
    eq = False
    xys0 = xys
    xys_man = set()
    xys_mid = xys
    xys_mid_man = set()
    xys_mid_r = xys_mid
    step = 0
    men_occur = None
    for step in range(1, max_num_steps+1):
        xys, xys_man, xys_r = _life_game_find_END_step(
            xys, xys_man, step,
            corner_man_detected_steps, boundary_man_detected_steps)
                
        if not men_occur and xys_man:
            men_occur = step
            
        if step % 2 == 0:
            xys_mid, xys_mid_man, xys_mid_r = _life_game_find_END_step(
                xys_mid, xys_mid_man, step//2,
                corner_man_detected_steps, boundary_man_detected_steps)

        if xys_r == xys_mid_r:
            eq = True
            break

    assert xys_man <= xys
    assert xys_mid_man <= xys_mid
    
    if not eq:
        T = None
        return (xys0, men_occur, step, xys, xys_man, T)

    if men_occur:
        if men_occur % boundary_man_detected_steps == 0:
            begin_man_test = men_occur - boundary_man_detected_steps
        else:
            begin_man_test = men_occur - corner_man_detected_steps

    end_rs = set()
    for T in range((step+1)//2):
        end_rs.add(set2sorted_tuple(xys_r))
        xys_r = life_game_step(xys_r)
        if xys_r == xys_mid_r:
            T += 1
            assert len(end_rs) == T
            break
    else:
        print(T, step)
        raise Exception('logic error')


    xys = xys0
    xys_man = set()
    for i in range(T):
        xys, xys_man, xys_r = _life_game_find_END_step(
            xys, xys_man, i,
            corner_man_detected_steps, boundary_man_detected_steps)

    xys_end = xys0
    xys_end_man = set()
    #xys_end, xys_end_man, xys_end_r = _life_game_find_END_splitmen(xys_end, xys_end_man, 0,1,1)
    end_nsteps = 0
    men_occur_first = None
    if not men_occur:
        for end_nsteps in range(0, step+1):
            if set2sorted_tuple(xys_end) in end_rs:
                break
            xys_end = life_game_step(xys_end)
            #
        else:
            raise Exception('logic error')
    else:
        for end_nsteps in range(1, begin_man_test+1):
            xys_end = life_game_step(xys_end)

        assert end_nsteps == begin_man_test
        assert not bool(_life_game_find_END_splitmen(
            xys_end, xys_end_man, end_nsteps, 1, 1)[1])
        for end_nsteps in range(begin_man_test+1, \
                                begin_man_test+1+boundary_man_detected_steps):
            xys_end, xys_end_man, xys_end_r = _life_game_find_END_step(
                xys_end, xys_end_man, end_nsteps, 1, 1)
            
            if xys_end_man:
                men_occur_first = end_nsteps
                break
        else:
            raise Exception('logic error')

        xys_end_man = set()
        for end_nsteps in range(end_nsteps, step+1):
            if set2sorted_tuple(xys_end_r) in end_rs:
                break
            xys_end, _, xys_end_r = _life_game_find_END_step(
                xys_end, xys_end_man, end_nsteps, 1, 1)
        xys_end_man = xys_end - xys_end_r
    '''
    for end_nsteps in range(1, step+1):
        if men_occur:
            if end_nsteps >= begin_man_test:
                corner_man_detected_steps = boundary_man_detected_steps = 1
                
        xys, xys_man, xys_r = _life_game_find_END_step(
            xys, xys_man, end_nsteps + T,
            corner_man_detected_steps, boundary_man_detected_steps)
        
        xys_end, xys_end_man, xys_end_r = _life_game_find_END_step(
            xys_end, xys_end_man, end_nsteps,
            corner_man_detected_steps, boundary_man_detected_steps)
        
        if not men_occur_first and xys_man:
            men_occur_first = end_nsteps
            
        if xys_end_r == xys_r:
            break

    assert xys_man <= xys
    assert xys_r <= xys
    assert xys == xys_r | xys_man
    assert xys_end_man <= xys_end
    assert xys_end_r <= xys_end
    assert xys_end == xys_end_r | xys_end_man'''
    
    return (xys0, men_occur_first, end_nsteps, xys_end, xys_end_man, T)

#'''



def find_line_END(start = 3, end = 20, path = output_folder, max_steps = 10000, man_detected_steps = 300):
    for xys in iter(set((i, 0) for i in range(s)) for s in range(start, end)):
        r = life_game_find_END(xys, max_steps)
        xys0, men_occur, step, xys_end, xys_end_man, T = r
        fn = path + '/n{originalsize}_menoccur{menoccur}_step{step}to_'\
             'n{endsize}_r{remaindersize}_men{nummen}_T{T}.bmp'\
             .format(originalsize = len(xys0), menoccur = men_occur, step = step, \
                     endsize = len(xys_end), remaindersize = len(xys_end)-len(xys_end_man),\
                     nummen = len(xys_end_man)//5, T = T)
        xys2bmp_file(xys_end, fn)



def main(args = None):
    import argparse, sys

    parser = argparse.ArgumentParser(description='find the end of life games which begin with one line')
    parser.add_argument('first', type=int, \
                        #nargs='?', default=3,
                        help='the number of living points on line of the first game')

    parser.add_argument('last', type=int, \
                        nargs='?', default=None,
                        help='the number of living points on line of the last game')

    parser.add_argument('--path', type=str, \
                        nargs='?', default=output_folder,
                        help='path to save the END states')

    parser.add_argument('--max', type=int, \
                        nargs='?', default=10000,
                        help='max steps for each game')

    if args == None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(args)

    if args.last == None:
        args.last = args.first

    if args.first < 1:
        return 0
        
    sand.makedirs(args.path)
    find_line_END(args.first, args.last+1, args.path, args.max)

    return 0


if __name__ == '__main__':
    main()
