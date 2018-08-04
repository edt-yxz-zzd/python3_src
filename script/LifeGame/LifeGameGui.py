import sand
from sand_basic import fixed__package__
fixed__package__(__name__)
import sand.exec.dialog as dialog


from .MouseState import MouseState
from .LifeGameRender import LifeGameRender, LifeGameOp
from life_game import select_small_area_by_scan_area as select_area

import sys
import traceback
import random
from time import perf_counter
import sdl2
import sdl2.ext
from tkinter.simpledialog import askstring
from tkinter.messagebox import showerror
from sand import default_fix_paths


size = 800, 600
x_max, y_max = size
#temp_folder = 'E:/temp_output/pybmp/life_game/'
default_quick_fname='./quick_life_game.bmp'
default_fix_paths('output', globals(), 'default_quick_fname')
##working_dir = get_output_data_path(__name__)
##default_quick_fname = get_output_data_path(__name__, default_quick_fname)
##assert default_quick_fname.startswith(working_dir)

class EventHandlerBase:
    __doc__ = '''maintain keyboard state and dispatch hotkey

to get keyboard state: self.state.curr_kbd_state

hotkeys:
H show this help info
N generate a new game
CtrlN generate a null game
L quick load from "{picture}";
CtrlL ask to load a picture
S quick save to "{picture}"
CtrlS ask to save
P print the current state
LeftDrag select points
CtrlLeftClick turn more unselected points selected or unselect those selected
I inverse the selected state
Delete kill the selected points
CapslockOnLeftMove&CapslockOnLeftClick - resurrect the passed points
Space step to the next state
MiddleClick step to the next {nsteps}th state
RightDrag drag the whole world
V show the super_view window to select where to goto
G ask where to go to
CtrlF search the first place where there are some living points
F3 search next place
Up&Down&Left&Right move one window size each
Escape disable cursor
CapslockOffLeftClick set the cursor
CtrlG ask to set the cursor
A ask for a dict that will use as args like those in LifeGameGui.__init__
'''
    def __init__(self):
        self.jump = {\
            'CapslockOnShiftUpCtrlUpAltUpH':self.onH, 
            'CapslockOffShiftUpCtrlUpAltUpH':self.onH, 
            'CapslockOnShiftUpCtrlUpAltUpN':self.onN, 
            'CapslockOffShiftUpCtrlUpAltUpN':self.onN, 
            'CapslockOnShiftUpCtrlDownAltUpN':self.onCtrlN, 
            'CapslockOffShiftUpCtrlDownAltUpN':self.onCtrlN, 
            'CapslockOnShiftUpCtrlUpAltUpL':self.onL, 
            'CapslockOffShiftUpCtrlUpAltUpL':self.onL, 
            'CapslockOnShiftUpCtrlDownAltUpL':self.onCtrlL, 
            'CapslockOffShiftUpCtrlDownAltUpL':self.onCtrlL, 
            'CapslockOnShiftUpCtrlUpAltUpS':self.onS, 
            'CapslockOffShiftUpCtrlUpAltUpS':self.onS, 
            'CapslockOnShiftUpCtrlDownAltUpS':self.onCtrlS, 
            'CapslockOffShiftUpCtrlDownAltUpS':self.onCtrlS, 
            'CapslockOnShiftUpCtrlUpAltUpP':self.onP, 
            'CapslockOffShiftUpCtrlUpAltUpP':self.onP, 
            'CapslockOffShiftUpCtrlUpAltUpLeftDrag':self.onCapslockOffLeftDrag, 
            'CapslockOnShiftUpCtrlDownAltUpLeftClick':self.onCtrlLeftClick, 
            'CapslockOffShiftUpCtrlDownAltUpLeftClick':self.onCtrlLeftClick, 
            'CapslockOnShiftUpCtrlUpAltUpI':self.onI, 
            'CapslockOffShiftUpCtrlUpAltUpI':self.onI, 
            'CapslockOnShiftUpCtrlUpAltUpDelete':self.onDelete, 
            'CapslockOffShiftUpCtrlUpAltUpDelete':self.onDelete, 
            'CapslockOnShiftUpCtrlUpAltUpLeftMove':self.onCapslockOnLeftMove_CapslockOnLeftClick, 
            'CapslockOnShiftUpCtrlUpAltUpLeftClick':self.onCapslockOnLeftMove_CapslockOnLeftClick, 
            'CapslockOnShiftUpCtrlUpAltUpSpace':self.onSpace, 
            'CapslockOffShiftUpCtrlUpAltUpSpace':self.onSpace, 
            'CapslockOnShiftUpCtrlUpAltUpMiddleClick':self.onMiddleClick, 
            'CapslockOffShiftUpCtrlUpAltUpMiddleClick':self.onMiddleClick, 
            'CapslockOnShiftUpCtrlUpAltUpRightDrag':self.onRightDrag, 
            'CapslockOffShiftUpCtrlUpAltUpRightDrag':self.onRightDrag, 
            'CapslockOnShiftUpCtrlUpAltUpV':self.onV, 
            'CapslockOffShiftUpCtrlUpAltUpV':self.onV, 
            'CapslockOnShiftUpCtrlUpAltUpG':self.onG, 
            'CapslockOffShiftUpCtrlUpAltUpG':self.onG, 
            'CapslockOnShiftUpCtrlDownAltUpF':self.onCtrlF, 
            'CapslockOffShiftUpCtrlDownAltUpF':self.onCtrlF, 
            'CapslockOnShiftUpCtrlUpAltUpF3':self.onF3, 
            'CapslockOffShiftUpCtrlUpAltUpF3':self.onF3, 
            'CapslockOnShiftUpCtrlUpAltUpUp':self.onUp_Down_Left_Right, 
            'CapslockOffShiftUpCtrlUpAltUpUp':self.onUp_Down_Left_Right, 
            'CapslockOnShiftUpCtrlUpAltUpDown':self.onUp_Down_Left_Right, 
            'CapslockOffShiftUpCtrlUpAltUpDown':self.onUp_Down_Left_Right, 
            'CapslockOnShiftUpCtrlUpAltUpLeft':self.onUp_Down_Left_Right, 
            'CapslockOffShiftUpCtrlUpAltUpLeft':self.onUp_Down_Left_Right, 
            'CapslockOnShiftUpCtrlUpAltUpRight':self.onUp_Down_Left_Right, 
            'CapslockOffShiftUpCtrlUpAltUpRight':self.onUp_Down_Left_Right, 
            'CapslockOnShiftUpCtrlUpAltUpEscape':self.onEscape, 
            'CapslockOffShiftUpCtrlUpAltUpEscape':self.onEscape, 
            'CapslockOffShiftUpCtrlUpAltUpLeftClick':self.onCapslockOffLeftClick, 
            'CapslockOnShiftUpCtrlDownAltUpG':self.onCtrlG, 
            'CapslockOffShiftUpCtrlDownAltUpG':self.onCtrlG,
            'CapslockOnShiftUpCtrlUpAltUpA':self.onA, 
            'CapslockOffShiftUpCtrlUpAltUpA':self.onA,
            'CapslockOnShiftUpCtrlUpAltUpZ':self.onZ, 
            'CapslockOffShiftUpCtrlUpAltUpZ':self.onZ,
            'CapslockOnShiftUpCtrlDownAltUpZ':self.onCtrlZ, 
            'CapslockOffShiftUpCtrlDownAltUpZ':self.onCtrlZ, 
            }
        self.state = MouseState()
        
    def process(self, event):
        concrete_hotkeys = self.state.update_state(event)
        for concrete_hotkey in concrete_hotkeys:
            if concrete_hotkey in self.jump:
                self.jump[concrete_hotkey](event)



def askxy(title, prompt):
    result = dialog.ask(tuple, prompt, title = title, check=\
                      lambda x: len(x) == 2 and type(x[0]) == type(x[1]) == int)
    return result



class LifeGameGui(EventHandlerBase):
    __doc__ = EventHandlerBase.__doc__
    
    def process(self, event):
        concrete_hotkeys = self.state.update_state(event)
        for concrete_hotkey in concrete_hotkeys:
            if concrete_hotkey in self.jump:
                f = self.jump[concrete_hotkey]
                print(concrete_hotkey, f.__doc__)
                self.jump[concrete_hotkey](event)
    
    def __init__(self, size, scale, generator, nsteps, quick_fname):
        EventHandlerBase.__init__(self)
        
        sdl2.ext.init()
        window = sdl2.ext.Window("life game", size=size)
        window.show()
        surface = window.get_surface()

        xys = set()
        self.render = LifeGameRender(xys, surface, size, scale)
        self.op = LifeGameOp(self.render, generator)
        self.nsteps = nsteps
        self.quick_fname = quick_fname
        
        self.window = window
        #help(window)
        #help(surface)


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
z - zoom in
ctrl+z - zoom out
'''

    def help_str(self):
        return self.help_str_tpl.format(\
            picture=self.quick_fname, nsteps=self.nsteps)

    def run(self):
        print(self.help_str())
        running = True
        self.op.generate()
        
        while running:
            events = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break
                try:
                    self.process(event)
                except:
                    traceback.print_exc()

            self.window.refresh()
        sdl2.ext.quit()
        return 0

    
            
    def reset(self, size=None, scale=None, nsteps=None, quick_fname=None):
        d = {}
        if size:
            self.window.size = size
            d['size'] = size
        if nsteps:
            self.nsteps = nsteps
        if quick_fname:
            self.quick_fname = quick_fname
        if scale:
            d['scale'] = scale

        self.render.update(**d)
            
    def onH(self, event):
        'show this help info'
        print(self.help_str())

    def onN(self, event):
        'generate a new game'
        self.op.generate()

    def onCtrlN(self, event):
        'generate a null game'
        self.op.null_new()

    def onL(self, event):
        'quick load from "{picture}";'
        self.op.load_from_sc_bmp_file(self.quick_fname, self.render.cursor)


    def onCtrlL(self, event):
        'ask to load a picture'
        fn = dialog.askopenfilename(title='load bmp')
        if fn:
            self.op.load_from_sc_bmp_file(fn, self.render.cursor) 

    def onS(self, event):
        'quick save to "{picture}"'
        selected = None
        self.op.save_as_sc_bmp_file(self.quick_fname, selected)

    def onCtrlS(self, event):
        'ask to save'
        selected = None
        fn = dialog.asksaveasfilename(title='save as bmp')
        if fn:
            self.op.save_as_sc_bmp_file(fn, selected) 

    def onP(self, event):
        'print the current state'
        print(self.op.xys0)
        print(self.op.save_as_xys())

    def onCapslockOffLeftDrag(self, event):
        'select points'
        b = event.button
        msxy = (b.x, b.y)
        x, y = self.render.mousexy2xy(msxy)
        px, py = self.render.mousexy2xy(self.state.prev_xy)
        
        x0, xt = sorted((x, px))
        y0, yt = sorted((y, py))
        xt += 1
        yt += 1

        xys = select_area((x0,y0), (xt-x0,yt-y0), self.render.lives())
        '''
        xys = set()
        for x in range(x0, xt):
            for y in range(y0, yt):
                xy = (x,y)
                if xy in self.render.lives():
                    xys.add(xy)'''

        self.op.select(xys)

    def onCtrlLeftClick(self, event):
        'turn more unselected points selected or unselect those selected'
        b = event.button
        msxy = (b.x, b.y)
        xy = self.render.mousexy2xy(msxy)
        if xy in self.render.selected_lives():
            self.op.unselect({xy})
        else:
            self.op.inc_select({xy})

    def onI(self, event):
        'inverse the selected state'
        self.op.inv_select(self.render.selected_lives())

    def onDelete(self, event):
        'kill the selected points'
        self.op.delxys(self.render.selected_lives())

    def onCapslockOnLeftMove_CapslockOnLeftClick(self, event):
        'resurrect the passed points'
        

        if event.type == sdl2.SDL_MOUSEBUTTONUP:
            b = event.button
            msxy = (b.x, b.y)
            xy = self.render.mousexy2xy(msxy)
            self.op.addxy(xy)
        elif event.type == sdl2.SDL_MOUSEMOTION:
            m = event.motion
            msxy = (m.x, m.y)
            xyt = self.render.mousexy2xy(msxy)
            msxy = (m.x-m.xrel, m.y-m.yrel)
            xy0 = self.render.mousexy2xy(msxy)
            self.op.addline(xy0, xyt)

    def onSpace(self, event):
        'step to the next state'
        self.op.step(1)

    def onMiddleClick(self, event):
        'step to the next {nsteps}th state'
        tmp = self.window.title
        self.window.title += '  *****calc...*****'
        print('steps {}... ...'.format(self.nsteps))
        
        start = perf_counter()
        self.op.step(self.nsteps)
        print('{} steps! spended {} seconds.\n'.format(self.nsteps, perf_counter() - start))
        
        self.window.title = tmp

    def onRightDrag(self, event):
        'drag the whole world'

        b = event.button
        msxy = (b.x, b.y)
        xt, yt = self.render.mousexy2xy(msxy)
        x0, y0 = self.render.mousexy2xy(self.state.prev_xy)
        
        dx = xt - x0
        dy = yt - y0
        self.op.move_window_rel((-dx, -dy))
        
    def onV(self, event):
        'show the super_view window to select where to goto'
        print('press ' + 'V')
        print('# ' + 'show the super_view window to select where to goto')
        showerror('Nonimpliment', 'on process')
        

    def onG(self, event):
        'ask where to go to'
        xy = askxy("move window", "input xy like (3, 4):")
        if xy:
            self.op.move_window_abs(xy)

    def onCtrlF(self, event):
        'search the first place where there are some living points'
        self.op.search_begin()

    def onF3(self, event):
        'search next place'
        self.op.search_next()

    def onUp_Down_Left_Right(self, event):
        'move one window size each'
        self.op.move_window_arrow(event.key.keysym.scancode, 1)

    def onEscape(self, event):
        'disable cursor'
        self.op.disable_cursor()

    def onCapslockOffLeftClick(self, event):
        'set the cursor'
        b = event.button
        msxy = (b.x, b.y)
        xy = self.render.mousexy2xy(msxy)
        self.op.move_cursor_abs(xy)

    def onCtrlG(self, event):
        'ask to set the cursor'
        xy = askxy("move cursor", "input xy like (3, 4):")
        if xy:
            self.op.move_cursor_abs(xy)

    def onA(self, event):
        print('onA')
        args = dialog.ask(dict, "input like: \n"
                 "dict(scale=2, nsteps=50, quick_fname='c:/qk.bmp')\n")
        print('onA', args)
        if args:
            self.reset(**args)
    def onZ(self, event):
        'zoom in around cursor if exists'

        where = self.render.cursor
        if where == None:
            self.op.zoom(1)
        else:
            self.op.zoom_around(1, where)
            
    def onCtrlZ(self, event):
        'zoom out around cursor if exists'

        where = self.render.cursor
        if where == None:
            self.op.zoom(-1)
        else:
            self.op.zoom_around(-1, where)

            
def random_xys(width, height, p):
    xys = set()
    for i in range(width):
        for j in range(height):
            if random.random() < p:
                xys.add((i,j))

    return xys

class LifeGameGui_Random(LifeGameGui):
    def __init__(self, size, scale, random_args, nsteps, quick_fname):
        LifeGameGui.__init__(self, size, scale,
                             self.generator(random_args),
                             nsteps, quick_fname)
    def generator(self, random_args):# width, height, p
        (width, height, p) = random_args
        while True:
            yield random_xys(width, height, p)
            
def main(nsteps=100, random_args=(300, 300, 0.1), scale=3, \
         size=size, quick_fname=default_quick_fname):
    lg = LifeGameGui_Random(size=size, scale=scale, \
                     random_args=random_args, \
                     nsteps=nsteps, \
                     quick_fname=quick_fname)
    sys.exit(lg.run())

if __name__ == "__main__":
    main()


