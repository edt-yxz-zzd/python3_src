import sys
from random import randint
import sdl2
import sdl2.ext
from tkinter.simpledialog  import askstring
from tkinter.messagebox import showerror
import sand
import random
import math
from time import perf_counter


from root.life_game import init, xys2xy0_size, move_xys, life_game_step, \
     xys2bmp_file, bmp_file2xys, mx2xys, xys2mx, bmp2xys, xys2bmp #
from root.c_life_game import life_game_steps # to replace life_game_step in LifeGameOp.step


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
SELECTED_COLOR = RED # living
CURSOR_COLOR = GREEN
DEAD_COLOR = BLACK
LIVED_COLOR = WHITE

size = 800, 600
x_max, y_max = size
temp_folder = 'E:/temp_output/pybmp/life_game/'


class LifeGameRender:
    #title = 'life game'
    _member_name = 'xys, surface, size, scale, xrel, yrel, selected, cursor'.split(', ')
    

    '''
    @staticmethod
    def _calc_inv_setvars():
        tpl = '{name} = self.{name}'
        ls = []
        for name in self._member_name:
            ls.append(tpl.format(name=name))

        _inv_setvars = compile('\n'.join(ls))
        return _inv_setvars

    # let xys = self.xys
    _inv_setvars = _calc_inv_setvars()
    '''
    
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
            sdl2.ext.fill(self.surface, CURSOR_COLOR, area=pixel_area)

    def get_pixel_area(self, x, y):
        x -= self.xrel
        y -= self.yrel

        s = self.scale
        x *= s
        y *= s

        return x, y, s, s
        


                
    '''
    def draw(self):
        sdl2.ext.fill(self.surface, DEAD_COLOR)
        #help(sdl2.ext.fill)

        for x, y in self.xys:
            self.draw_pixel(x, y, LIVED_COLOR)

        for x, y in self.selected:
            self.draw_pixel(x, y, SELECTED_COLOR)

        if self.cursor:
            self.draw_pixel(x, y, CURSOR_COLOR)
    def draw_pixel(self, x, y, color):
        x -= self.xrel
        y -= self.yrel
        
        x *= self.scale
        y *= self.scale
        

        x_max, y_max = self.size
        pixelview = sdl2.ext.PixelView(self.surface)
        for i in range(x, x+self.scale):
            if not 0 <= i < x_max: continue
            for j in range(y, y+self.scale):
                if not 0 <= j < y_max: continue

                pixelview[j][i] = color'''
    
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
def random_xys(width, height, p):
    xys = set()
    for i in range(width):
        for j in range(height):
            if random.random() < p:
                xys.add((i,j))

    return xys

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

    
'''
def absMsLine(x, length):
    'line section is [x, x+len] or [x+len, x], not [x, x+len)'
    if length < 0:
        x = x + length
        length = -length

    return x, length
        
def absMsRect(xy, size): # since width/height maybe negative
    w, h = size
    x, y = xy
    x, w = absMsLine(x, w)
    y, h = absMsLine(y, h)

    size = w,h
    xy = x,y
    return xy, size
'''


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

def lineTo(xy0, xyt):
    pass

class Namespace:pass

MS_ALL_UP = 0
MS_LDOWN = 1
MS_MDOWN = 2
MS_RDOWN = 4
MS_LDOWN_CAPS_ON = 1 << 3
MS_LDOWN_CTRL = 1 << 4


class LifeGameGui:
    def isCapsOn(self):
        return self.ns.bCaps
    def downCtrl(self):
        return self.ns.bCtrl
    def __init__(self, size, scale, random_args, nsteps, quick_fname):
        sdl2.ext.init()
        window = sdl2.ext.Window("life game", size=size)
        window.show()
        surface = window.get_surface()

        xys = set()
        self.render = LifeGameRender(xys, surface, size, scale)
        self.op = LifeGameOp(self.render, self.generator(random_args))
        self.nsteps = nsteps
        self.quick_fname = quick_fname

        self.ns = Namespace()
        self.ns.ms_down = MS_ALL_UP
        self.ns.bCaps = False
        self.ns.bCtrl = False
        
        self.window = window
        #print(help(window))

    help_str_tpl = '''
h - show this help info

new
yield a new state
n - generate a new game
ctrl+n - generate a null game

load
load at the cursor
if no cursor, then drop the old state
l - quick load from "{picture}";
ctrl+l - ask to load a picture

save
save selected points
if no points selected, then save the all
s - quick save to "{picture}"
ctrl+s - ask to save
p - print the current state

select
select some living points
leftmouse drag - select points
ctrl + leftmouse click - turn more unselected points selected or unselect those selected
i - inverse the selected state


modify
delete - kill the selected points
caps on + leftmouse drag?/click - resurrect the passed points


step
space - step to the next state
middlemouse click - step to the next {nsteps}th state

move window
rightmouse drag - drag the whole world
v - show the super_view window to select where to goto
g - ask where to go to
ctrl+f - search the first place where there are some living points
F3 - search next place
arrow(up, down, left, right) - move one window size each

move cursor
ESC - disable cursor
caps off + leftmouse click - set the cursor
ctrl+g - ask to set the cursor
##arrow_move

modify args
a - ask for a dict that will use as args like those in LifeGameGui.__init__
    key can be one of 'scale, random_args, nsteps, quick_fname'
'''

    def help_str(self):
        return self.help_str_tpl.format(\
            picture=self.quick_fname, nsteps=self.nsteps)
    def run(self):
        print(self.help_str())
        running = True
        self.ns.down = False
        self.op.generate()
        
        while running:
            events = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break
                elif event.type == sdl2.SDL_MOUSEBUTTONDOWN:
                    self.onMouseDown(event)
                elif event.type == sdl2.SDL_MOUSEBUTTONUP:
                    self.onMouseUp(event)
                elif event.type == sdl2.SDL_MOUSEMOTION:
                    self.onMouseMotion(event)
                    

                elif event.type == sdl2.SDL_KEYDOWN:
                    self.onKeyDown(event)
                elif event.type == sdl2.SDL_KEYUP:
                    self.onKeyUp(event)

                #break


            self.window.refresh()
        sdl2.ext.quit()
        return 0
    
    def generator(self, random_args):# width, height, p
        (width, height, p) = random_args
        while True:
            yield random_xys(width, height, p)
    
    
    
    def onMouseMotion(self, event):
        m = event.motion
        msxy = m.x, m.y
        msxyrel = m.xrel, m.yrel

        #print(m.x, m.y, m.xrel, m.yrel)
        if self.ns.ms_down == MS_LDOWN_CAPS_ON:
            return
            msxy, msxyrel = absMsRect(msxy, msxyrel)
            r = Rect(msxy, msxyrel)
            xy0 = self.render.mousexy2xy(r.xy0())
            xt, yt = self.render.mousexy2xy(r.xyt())
            xyt = xt+1, yt+1
            
            xys = lineTo(xy0, xyt)
            self.op.addxys(xys)
            
            
            
    def onMouseUp(self, event):
        b = event.button
        msxy = (b.x, b.y)
        x, y = xy = self.render.mousexy2xy(msxy)
        #print(dir(b))
        #print(b.button, b.which, b.windowID, b.state)
        if b.button == sdl2.SDL_BUTTON_LEFT:
            if self.ns.ms_down == MS_LDOWN: #left drag
                x0, xt = sorted((x, self.ns.x))
                y0, yt = sorted((y, self.ns.y))
                xt += 1
                yt += 1
                

                xys = set()
                for x in range(x0, xt):
                    for y in range(y0, yt):
                        xy = (x,y)
                        if xy in self.render.lives():
                            xys.add(xy)

                self.op.select(xys)
                        
                
        elif b.button == sdl2.SDL_BUTTON_RIGHT:
            if self.ns.ms_down == MS_RDOWN: #right drag
                x0, y0 = self.ns.x, self.ns.y
                xt, yt = xy
                
                dx = xt - x0
                dy = yt - y0
                self.op.move_window_rel((-dx, -dy))
                
        elif b.button == sdl2.SDL_BUTTON_MIDDLE:
            pass

        self.ns.ms_down = MS_ALL_UP

    def onMouseDown(self, event):
        b = event.button
        msxy = (b.x, b.y)
        xy = self.render.mousexy2xy(msxy)
        self.ns.x, self.ns.y = xy
        
        if b.button == sdl2.SDL_BUTTON_LEFT:
            self.ns.ms_down = MS_LDOWN
            if self.isCapsOn():
                self.ns.ms_down = MS_LDOWN_CAPS_ON
                self.op.addxy(xy)
            elif self.downCtrl():
                self.ns.ms_down = MS_LDOWN_CTRL
                if xy in self.render.selected_lives():
                    self.op.unselect({xy})
                else:
                    self.op.inc_select({xy})
            else:
                self.op.move_cursor_abs(xy)
                
                    
            
            #self.op.move_window_rel((-nd_xrel, -nd_yrel)) 
                
        elif b.button == sdl2.SDL_BUTTON_RIGHT:
            self.ns.ms_down = MS_RDOWN
            
        elif b.button == sdl2.SDL_BUTTON_MIDDLE:
            self.ns.ms_down = MS_MDOWN
            
            tmp = self.window.title
            self.window.title += '  *****calc...*****'
            print('steps {}... ...'.format(self.nsteps))
            
            start = perf_counter()
            self.op.step(self.nsteps)
            print('{} steps! spended {} seconds.\n'.format(self.nsteps, perf_counter() - start))
            
            self.window.title = tmp
        else:
            return

        '''
        print('xrel = {}, yrel = {}'.format(\
            self.render.xrel/self.render.scale, \
            self.render.yrel/self.render.scale))
        print('x0 = {}, y0 = {}, width = {}, height = {}'.format(\
            *xys2xy0_size(self.render.xys)))
        print('total = {}'.format(len(self.render.xys)))
        


        ''
        print(m.x, m.y, m.xrel, m.yrel)
        d = dir(sdl2)
        for n in d:
            if n.startswith('SDL_MOUSE'):
                print(n)
        '''
        
        
    def onKeyUp(self, event):
        k = event.key
        self.ns.bCtrl = ctrl = sdl2.KMOD_CTRL & k.keysym.mod
        #self.ns.bCaps = caps = sdl2.KMOD_CAPS & k.keysym.mod
        #print('up caps', caps)
        #print('up ctrl', ctrl)
        if sdl2.SDL_SCANCODE_CAPSLOCK == k.keysym.scancode:
            pass
            #self.ns.bCaps = False
            #print('up caps', self.ns.bCaps)
        elif k.keysym.scancode in {sdl2.SDL_SCANCODE_LCTRL, sdl2.SDL_SCANCODE_RCTRL}:
            self.ns.bCtrl = False
            #print('up ctrl', self.ns.bCtrl)
    def onKeyDown(self, event):
        k = event.key
        '''
        print('-------k-------')
        #print(dir(k))
        print('type', k.type)
        print('windowID', k.windowID)
        print('timestamp', k.timestamp)
        print('repeat', k.repeat)
        print('padding2', k.padding2)
        print('padding3', k.padding3)
        print('state', k.state)
        #print('keysym', k.keysym)
        print('-------keysym-------')
        #print(dir(k.keysym))
        print('sym', k.keysym.sym)
        print('mod', k.keysym.mod)
        print('unicode', k.keysym.unicode, chr(k.keysym.unicode))
        print('scancode', k.keysym.scancode)
        #print(sdl2.SDL_GetKeyboardState(k.keysym))'''

        self.ns.bCtrl = ctrl = sdl2.KMOD_CTRL & k.keysym.mod
        self.ns.bCaps = caps = sdl2.KMOD_CAPS & k.keysym.mod
        #print('down caps', caps)
        #print('down ctrl', ctrl)
        if sdl2.SDL_SCANCODE_CAPSLOCK == k.keysym.scancode:
            self.ns.bCaps = not self.ns.bCaps
            #print('down caps', self.ns.bCaps)
        elif k.keysym.scancode in {sdl2.SDL_SCANCODE_LCTRL, sdl2.SDL_SCANCODE_RCTRL}:
            self.ns.bCtrl = True
            #print('down ctrl', self.ns.bCtrl)
        elif sdl2.SDL_SCANCODE_H == k.keysym.scancode:
            print(self.help_str())
        elif sdl2.SDL_SCANCODE_N == k.keysym.scancode:
            if ctrl:
                self.op.null_new() # ctrl+n
            else:
                self.op.generate() # n
        elif sdl2.SDL_SCANCODE_L == k.keysym.scancode:
            if ctrl:  # ctrl+l
                fn = sand.askopenfilename(title='load bmp')
                if fn:
                    self.op.load_from_sc_bmp_file(fn, self.render.cursor) 
            else:
                self.op.load_from_sc_bmp_file(self.quick_fname, self.render.cursor) # l
            
        elif sdl2.SDL_SCANCODE_S == k.keysym.scancode:
            selected = None
            if ctrl:  # ctrl+s
                fn = sand.asksaveasfilename(title='save as bmp')
                if fn:
                    self.op.save_as_sc_bmp_file(fn, selected) 
            else:
                self.op.save_as_sc_bmp_file(self.quick_fname, selected) # s
        elif sdl2.SDL_SCANCODE_P == k.keysym.scancode:
            print(self.op.save_as_xys())
            
        elif sdl2.SDL_SCANCODE_I == k.keysym.scancode:
            self.op.inv_select(self.render.selected_lives())
            
        elif sdl2.SDL_SCANCODE_DELETE == k.keysym.scancode:
            self.op.delxys(self.render.selected)
            
        elif sdl2.SDL_SCANCODE_SPACE == k.keysym.scancode:
            self.op.step(1)
        elif sdl2.SDL_SCANCODE_V == k.keysym.scancode:
            showerror('Nonimpliment', 'on process')
        elif sdl2.SDL_SCANCODE_G == k.keysym.scancode:
            if ctrl:  # ctrl+g
                #xy = eval(askstring("move cursor", "input xy like (3, 4):"))
                xy = askxy("move cursor", "input xy like (3, 4):")
                if xy: self.op.move_cursor_abs(xy)
            else:
                #xy = eval(askstring("move window", "input xy like (3, 4):"))
                xy = askxy("move window", "input xy like (3, 4):")
                if xy: self.op.move_window_abs(xy)
        elif sdl2.SDL_SCANCODE_F == k.keysym.scancode:
            if ctrl:  # ctrl+f
                self.op.search_begin()
        elif sdl2.SDL_SCANCODE_F3 == k.keysym.scancode:
            self.op.search_next()
        elif k.keysym.scancode in {sdl2.SDL_SCANCODE_UP, sdl2.SDL_SCANCODE_DOWN, \
                                   sdl2.SDL_SCANCODE_LEFT, sdl2.SDL_SCANCODE_RIGHT}:
            self.op.move_window_arrow(k.keysym.scancode, 1)
        elif sdl2.SDL_SCANCODE_ESCAPE == k.keysym.scancode:
            self.op.disable_cursor()
        elif sdl2.SDL_SCANCODE_A == k.keysym.scancode:
            args = sand.ask(dict, "input like: \n"
                 "dict(scale=2, random_args=(400,500,0.1), nsteps=50, quick_fname='c:/')\n")
            if args:
                self.reset(**args)
    def reset(self, scale=None, random_args=None, nsteps=None, quick_fname=None):
        if nsteps:
            self.nsteps = nsteps
        if quick_fname:
            self.quick_fname = quick_fname
        if random_args:
            self.op.generator = self.generator(random_args)
        if scale:
            self.render.update(scale=scale)
        else:
            self.render.update()



def askxy(title, prompt):
    result = sand.ask(tuple, prompt, title = title, check=\
                      lambda x: len(x) == 2 and type(x[0]) == type(x[1]) == int)
    return result

class LifeGameOp:
    def __init__(self, render, generator):
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
    def help_info(self):pass
    

    
class LifeGameSuperView:pass

def main(nsteps=100, random_args=(300, 300, 0.1), scale=1, \
         size=size, quick_fname=temp_folder+'qk_life_game.bmp'):
    lg = LifeGameGui(size=size, scale=scale, \
                     random_args=random_args, \
                     nsteps=nsteps, \
                     quick_fname=quick_fname)
    sys.exit(lg.run())
    
if __name__ == "__main__":
    main()


