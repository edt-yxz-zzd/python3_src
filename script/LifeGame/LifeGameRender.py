
import math
import sdl2
import sdl2.ext


from .life_game import init, xys2xy0_size, move_xys, life_game_step, \
     xys2bmp_file, bmp_file2xys, mx2xys, xys2mx, bmp2xys, xys2bmp #
from .c_life_game import life_game_steps # to replace life_game_step in LifeGameOp.step
#from .life_game import life_game_steps

'''
render class - hold the args, render when updated
gui class - switch event
    help -
op class - functions:
    new - random+arg load+path 
    save - save+path print_xys save+selected
    select - 
    modify - del add load+loction
    iter - nsteps (update print)
    move window - drag super_view+select_section goto search arrow_move
    move cursor - click goto arrow_move
    #help - 
    
super_view class
'''
BLACK = sdl2.ext.Color(0, 0, 0)
WHITE = sdl2.ext.Color(255, 255, 255)
RED = sdl2.ext.Color(255, 0, 0)
GREEN = sdl2.ext.Color(0, 255, 0)
YELLOW = sdl2.ext.Color(255, 255, 0)
LIGHT_GREEN = sdl2.ext.Color(128, 255, 128)

SELECTED_COLOR = RED # living
CURSOR_COLOR = GREEN
SELECTED_CURSOR_COLOR = YELLOW
LIVED_CURSOR_COLOR = LIGHT_GREEN

DEAD_COLOR = BLACK
LIVED_COLOR = WHITE


class LifeGameRender:
    #title = 'life game'
    _member_name = 'xys, surface, size, scale, xrel, yrel, selected, cursor'.split(', ')
    
    def __init__(self, xys, surface, size, scale, \
                 xrel=0, yrel=0, selected=None, cursor=None):
        if selected == None:
            selected = set()
            
        # let self.xys = xys
        for name in self._member_name:
            setattr(self, name, locals()[name])

        self.update()

    def update(self, **member):
        for name in member:
            #assert hasattr(self, name)
            setattr(self, name, member[name])

        if self.lives() == None:
            raise
        if {'xys', 'selected'} & member.keys():
            self.fix_selected()
            
        if {'xrel', 'yrel'} & member.keys():
            print('where = ', self.where())
        if 'xys' in member:
            #(x0, y0), (w,h) =
            xy0_size = xys2xy0_size(self.lives())
            if not xy0_size:
                #print(xy0_size)
                xy0_size = (0, 0, 0, 0)
            print('x0 = {}, y0 = {}, width = {}, height = {}'\
                  .format(*xy0_size))
            print('total = {}'.format(len(self.lives())))
        self.draw()
        
    def fix_selected(self):
        self.selected &= self.lives()
        
    def draw(self):
        sdl2.ext.fill(self.surface, DEAD_COLOR)
        #help(sdl2.ext.fill)

        pixel_area_ls = [self.get_pixel_area(x, y) for x, y in self.xys]
        sdl2.ext.fill(self.surface, LIVED_COLOR, area=pixel_area_ls)

        pixel_area_ls = [self.get_pixel_area(x, y) for x, y in self.selected]
        sdl2.ext.fill(self.surface, SELECTED_COLOR, area=pixel_area_ls)

        if self.cursor:
            x, y = self.cursor
            pixel_area = self.get_pixel_area(x, y)
            color = CURSOR_COLOR
            if self.cursor in self.lives():
                color = LIVED_CURSOR_COLOR
                if self.cursor in self.selected_lives():
                    color = SELECTED_CURSOR_COLOR
            sdl2.ext.fill(self.surface, color, area=pixel_area)

    def get_pixel_area(self, x, y):
        x -= self.xrel
        y -= self.yrel

        s = self.scale
        x *= s
        y *= s

        return x, y, s, s
        


    
    def isLiving(self, xy):
        return xy in self.xys

    def lives(self):
        return self.xys


    def selected_lives(self):
        return self.selected

    def where(self):
        return self.xrel, self.yrel
    

    def inv_scale(self, msxy):
        mx, my = msxy
        s = self.scale
        xy = math.floor(mx/s), math.floor(my/s)
        return xy
    def mousexy2xy(self, msxy):
        x, y = self.inv_scale(msxy)
        x += self.xrel
        y += self.yrel
        return x,y


def has_xy_in_rect(xys, rect):
    (x0, y0), (width, height) = rect

    for x,y in xys:
        if x0 <= x < x0+width and \
           y0 <= y < y0+height:
            return True
    return False
class Rect:
    def __init__(self, xy, size):
        w, h = size
        assert w >= 0
        assert h >= 0

        self.x, self.y = xy
        self.width, self.height = size
    def size(self):
        return self.width, self.height

    def xy0(self):
        return self.x, self.y

    def xyt(self):
        return self.x + self.width, self.y + self.height



def pt_pair2line_args(xy0, xyt):
    'return a, b, c # ax+by=c'
    assert xy0 != xyt
    '''
(x0, y0), (xt, yt), (x, y) on the same line:
(xt-x0, yt-y0) -> (x-x0, y-y0)

(x, y) .* (y, -x) == 0
(xt-x0, yt-y0) * (a,b) == 0 ==>
a = yt-y0
b = x0-xt
c = a*x0 + b*y0
'''
    x0, y0 = xy0
    xt, yt = xyt
    a = yt-y0
    b = x0-xt
    c = a*x0 + b*y0
    return a, b, c



def cross_pt_of_2lines(line1, line2):
    '''
a*x + b*y = c
s*x + t*y = w
x = (ct-wb)/(at-sb)
y = (cs-wa)/(bs-ta) = (wa-cs)/(at-sb)
'''

    a,b,c = line1
    s,t,w = line2
    d = a*t-s*b
    xd = (c*t-w*b)
    yd = (w*a-c*s)
    assert a*xd + b*yd == c*d
    assert s*xd + t*yd == w*d
    

    assert d
    d *= 1.0
    x = xd/d
    y = yd/d
    return x, y

def line_to(xy0, xyt):
    if xy0 == xyt:
        return [xy0]
    x0, y0 = xy0
    xt, yt = xyt

    usingY = abs(xt-x0) < abs(yt-y0)
    if usingY:
        x0, y0 = y0, x0
        xt, yt = yt, xt

    if x0 > xt:
        x0, y0, xt, yt = xt, yt, x0, y0

    Txy0 = x0, y0
    Txyt = xt, yt
    a,b,c = pt_pair2line_args(Txy0, Txyt)
    assert b

    ls = [(x, (c - a*x)//b) for x in range(x0, xt+1)]
    if usingY:
        ls = [(x,y) for y,x in ls]
    if ls[0] != xy0:
        ls.reverse()

    if ls[0] != xy0 or ls[-1] !=  xyt:
        print(xy0, xyt, ls)
    assert ls[0] == xy0
    assert ls[-1] ==  xyt
    return ls





class LifeGameOp:
    def __init__(self, render, generator):
        self.xys0 = None
        self.render = render # LifeGameRender
        #self.load_random_args = load_random_args # width, height, p
        self.generator = iter(generator) # next(generator) yields a xys

    def null_new(self):
        self.load_from_xys(set())
        
    def generate(self):
        for xys in self.generator:
            self.load_from_xys(xys)
            return
        print('nothing can be generated!!!')

    def load_from_xys(self, xys, cursor=None):
        self.xys0 = xys.copy()
        if cursor == None: # drop old state
            self.render.update(xys=xys, xrel=0, yrel=0, selected=set(), cursor=None)
        else:
            self.add_xys_to(xys, cursor)
            
    def load_from_mx(self, mx, cursor=None):
        xys = mx2xys(mx)
        self.load_from_xys(xys, cursor)
    def load_from_sc_bmp(self, bmp, cursor=None):
        xys = bmp2xys(bmp)
        self.load_from_xys(xys, cursor)
    def load_from_sc_bmp_file(self, fname, cursor=None):
        xys = bmp_file2xys(fname)
        self.load_from_xys(xys, cursor)


    def what_selected_to_save(self):
        selected = self.render.selected_lives()
        if not selected:
            selected = self.render.lives()

        return selected
    
    def save_as_xys(self, selected=None):
        if selected == None:
            selected = self.what_selected_to_save()
        else:
            selected = selected & self.render.lives()

        return selected
    
    def save_as_mx(self, selected=None):
        xys = self.save_as_xys(selected)
        return xys2mx(xys)
    def save_as_sc_bmp(self, selected=None):
        xys = self.save_as_xys(selected)
        return xys2bmp(xys)
    def save_as_sc_bmp_file(self, fname, selected=None):
        xys = self.save_as_xys(selected)
        xys2bmp_file(xys, fname)

    def select(self, xys):
        self.render.update(selected=xys)
    def inc_select(self, xys):
        self.select(self.render.selected_lives() | xys)
    def inv_select(self, xys):
        self.select(self.render.lives() - xys)
    def unselect(self, xys):
        self.select(self.render.selected_lives() - xys)

    def delxy(self, xy):
        self.delxys({xy})
    def delxys(self, xys):
        self.render.update(xys=self.render.lives() - xys)
    def addline(self, xy0, xyt):
        xys = set(line_to(xy0, xyt))
        self.addxys(xys)
    def addxy(self, xy):
        self.addxys({xy})
    def addxys(self, xys):
        self.render.update(xys=self.render.lives() | xys)
    def add_xys_to(self, xys, where):
        xys = move_xys(xys, where)
        self.addxys(xys)
    def add_mx_to(self, mx, where):
        xys = mx2xys(mx)
        self.add_xys_to(xys, where)
    def add_bmp_to(self, bmp, where):
        xys = bmp2xys(bmp)
        self.add_xys_to(xys, where)
    def add_bmpfile_to(self, fname, where):
        xys = bmp_file2xys(fname)
        self.add_xys_to(xys, where)

        

    def step(self, nsteps):
        xys = self.render.lives()

        xys = life_game_steps(xys, nsteps)
        #for _ in range(nsteps): xys = life_game_step(xys)

        self.render.update(xys=xys)
        


    def move_window_rel(self, dxy):
        dx, dy = dxy
        xrel, yrel = self.render.where()
        xrel += dx
        yrel += dy
        where = (xrel, yrel)
        self.move_window_abs(where)
        
    def move_window_abs(self, where):
        xrel, yrel = where
        self.render.update(xrel=xrel, yrel=yrel)
    def move_window_by_superview(self):
        raise NotImplementedError('move_window_by_superview')
    def move_window_arrow(self, arrow, times):
        m = {sdl2.SDL_SCANCODE_UP:(0, -1), sdl2.SDL_SCANCODE_DOWN:(0, 1),
             sdl2.SDL_SCANCODE_LEFT:(-1, 0), sdl2.SDL_SCANCODE_RIGHT:(1, 0)}
        dx, dy = m[arrow]
        w, h = self.render.inv_scale(self.render.size)
        dx *= w*times
        dy *= h*times
        dxy = (dx, dy)
        self.move_window_rel(dxy)
        


        
    def search_begin(self):
        xys = self.render.lives()
        x0, y0, width, height = xys2xy0_size(xys)
        xy0 = x0,y0
        self.move_window_abs(xy0)
        w, h = self.render.inv_scale(self.render.size)

        if has_xy_in_rect(xys, (xy0, (w,h))):
            return
        self.search_next()
        
    def search_next(self):
        xys = self.render.lives()
        if not xys:
            self.move_window_abs((0, 0))
            return
        
        x0, y0, width, height = xys2xy0_size(xys)
        w, h = self.render.inv_scale(self.render.size)

        xc = math.ceil(width/w)
        yc = math.ceil(height/h)

        xrel, yrel = self.render.where()
        i = (xrel - x0) // w
        j = (yrel - y0) // h

        if i < 0:
            i, j = 0, -1
        if j < 0:
            j = -1
        for i in range(i, xc):
            for j in range(j+1, yc):
                xy = (x0+w*i, y0+h*j)
                if has_xy_in_rect(xys, (xy, (w,h))):
                    self.move_window_abs(xy)
                    return
            j = -1

        self.search_begin()
        
                
    

    def move_cursor_abs(self, where):
        self.render.update(cursor=where)
    #def move_cursor_arrow(self, arrow, times):pass
    def disable_cursor(self):
        self.render.update(cursor=None)

    def zoom(self, dscale, where=None):
        scale = dscale + self.render.scale
        if scale < 1:
            scale = 1

        if where != None:
            self.move_window_abs(where)
        self.render.update(scale=scale)

    def zoom_around(self, dscale, where):
        self.zoom(dscale)
        w, h = self.render.inv_scale(self.render.size)
        x, y = where
        x -= w//2
        y -= h//2
        where = x, y
        self.move_window_abs(where)
        
    def help_info(self):pass
    

    
class LifeGameSuperView:pass

