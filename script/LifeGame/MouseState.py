
import sdl2
import sdl2.ext

from sand import *
from nn_ns.parse.hc_parser import key_ls

def key2scancode(key):
    return getattr(sdl2, 'SDL_SCANCODE_' + key.upper())

_scancode2key = {key2scancode(key):key for key in key_ls}
def scancode2key(c):
    return _scancode2key[c]



def kbd_state2str(state):
        onoff = ['Off', 'On']
        updown = ['Up', 'Down']

        ls = (
            'Capslock', onoff[not not get_flag(state, sdl2.KMOD_CAPS)],
            'Shift', updown[not not get_flag(state, sdl2.KMOD_SHIFT)],
            'Ctrl', updown[not not get_flag(state, sdl2.KMOD_CTRL)],
            'Alt', updown[not not get_flag(state, sdl2.KMOD_ALT)],
            )

        return ''.join(ls)
def event2hkfullname(state, event):
    head = kbd_state2str(state)
class KeybdState:
    def __init__(self, state=0):
        self.state = state
        

    def copy(self):
        return KeybdState(self.state)
    def isCapslockOn(self):
        return self.state & sdl2.KMOD_CAPS
    def downShift(self):
        return self.state & sdl2.KMOD_SHIFT
    def downCtrl(self):
        return self.state & sdl2.KMOD_CTRL
    def downAlt(self):
        return self.state & sdl2.KMOD_ALT

    
    def update_state(self, event):
        if event.type == sdl2.SDL_KEYDOWN:
            self.onKeyDown(event)
            action = 'Down'
            k = event.key.keysym
            scancode = k.scancode
            if scancode in _scancode2key:
                key = scancode2key(scancode)
                hkfullnames = [self.state2str() + key]
                return hkfullnames
        elif event.type == sdl2.SDL_KEYUP:
            self.onKeyUp(event)
            action = 'Up'
        return []

        
        
            

    def onKeyUp(self, event):
        self.state = event.key.keysym.mod
            
    def onKeyDown(self, event):
        k = event.key.keysym
        scancode = k.scancode

        self.state = event.key.keysym.mod

        if scancode == sdl2.SDL_SCANCODE_CAPSLOCK:
            if not event.key.repeat:
                self.state = flip_flag(self.state, sdl2.KMOD_CAPS)
        elif scancode in {sdl2.SDL_SCANCODE_LSHIFT, sdl2.SDL_SCANCODE_RSHIFT}:
            self.state = set_flag(self.state, sdl2.KMOD_SHIFT)
        elif scancode in {sdl2.SDL_SCANCODE_LCTRL, sdl2.SDL_SCANCODE_RCTRL}:
            self.state = set_flag(self.state, sdl2.KMOD_CTRL)
        elif scancode in {sdl2.SDL_SCANCODE_LALT, sdl2.SDL_SCANCODE_RALT}:
            self.state = set_flag(self.state, sdl2.KMOD_ALT)
    def state2str(self):
        return kbd_state2str(self.state)

    def __repr__(self):
        return '<{class_name}({state!r})>'\
               .format(class_name='KeybdState', state=self.state2str())


class MouseState:
    MS_UP = 0
    LDOWN = 'Left'
    MDOWN = 'Middle'
    RDOWN = 'Right'
    def __init__(self):
        self.hkfullnames = []
        
        # the data below are reflashed when ms down!!!
        # but used when ms up
        self.prev_kbd_state = KeybdState()
        self.curr_kbd_state = KeybdState()
        self.prev_ms_action = self.MS_UP
        self.prev_xy = None
    
    def update_state(self, event):
        self.hkfullnames = self.curr_kbd_state.update_state(event)
        
        if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
            self.onMouseDown(event)
        elif event.type == sdl2.SDL_MOUSEBUTTONUP:
            self.onMouseUp(event)
        elif event.type == sdl2.SDL_MOUSEMOTION:
            self.onMouseMotion(event)
        else:
            pass
        return self.hkfullnames
    
    def onMouseMotion(self, event):
        m = event.motion

        head = self.curr_kbd_state.state2str()
        action = 'Move'
        
        button = m.state
        if button == sdl2.SDL_BUTTON_LEFT:
            button = self.LDOWN
        elif button == sdl2.SDL_BUTTON_RIGHT:
            button = self.RDOWN
                
        elif button == sdl2.SDL_BUTTON_MIDDLE:
            button = self.MDOWN
        else:
            self.hkfullnames = []
            return

        self.hkfullnames = [head + button + action]

    def onMouseUp(self, event):
        b = event.button
        xy = b.x, b.y

        head = self.curr_kbd_state.state2str()
        actions = [(head, 'Up')]
        
        if b.button == sdl2.SDL_BUTTON_LEFT:
            button = self.LDOWN #left drag or click
        elif b.button == sdl2.SDL_BUTTON_RIGHT:
            button = self.RDOWN
                
        elif b.button == sdl2.SDL_BUTTON_MIDDLE:
            button = self.MDOWN

        if self.prev_ms_action == button:
            self.prev_ms_action = self.MS_UP
            head = self.prev_kbd_state.state2str()
            if self.prev_xy != xy:
                actions.append([head, 'Drag'])
            elif b.clicks:
                actions.append([head, 'Click'])
            

        self.hkfullnames = []
        for head, action in actions:
            self.hkfullnames.append(head + button + action)

    def onMouseDown(self, event):
        b = event.button
        self.prev_kbd_state = self.curr_kbd_state.copy()
        self.prev_xy = (b.x, b.y)
        
        head = self.curr_kbd_state.state2str()
        action = 'Down'
        self.prev_ms_action = self.MS_UP
        if b.button == sdl2.SDL_BUTTON_LEFT:
            self.prev_ms_action = self.LDOWN
        elif b.button == sdl2.SDL_BUTTON_RIGHT:
            self.prev_ms_action = self.RDOWN
        elif b.button == sdl2.SDL_BUTTON_MIDDLE:
            self.prev_ms_action = self.MDOWN

        if self.prev_ms_action != self.MS_UP:
            button = self.prev_ms_action
            hkfullname = head + button + action
            self.hkfullnames = [hkfullname]
        else:
            self.hkfullnames = []
            
            
    def get_hkfullnames(self):
        return self.hkfullnames




class EventHandlerBase:
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
            'CapslockOnShiftUpCtrlUpAltUpLeftDrag':self.onLeftDrag, 
            'CapslockOffShiftUpCtrlUpAltUpLeftDrag':self.onLeftDrag, 
            'CapslockOnShiftUpCtrlDownAltUpLeftClick':self.onCtrlLeftClick, 
            'CapslockOffShiftUpCtrlDownAltUpLeftClick':self.onCtrlLeftClick, 
            'CapslockOnShiftUpCtrlUpAltUpI':self.onI, 
            'CapslockOffShiftUpCtrlUpAltUpI':self.onI, 
            'CapslockOnShiftUpCtrlUpAltUpDelete':self.onDelete, 
            'CapslockOffShiftUpCtrlUpAltUpDelete':self.onDelete, 
            'CapslockOnShiftUpCtrlUpAltUpLeftDrag':self.onCapslockOnLeftDrag_CapslockOnLeftClick, 
            'CapslockOnShiftUpCtrlUpAltUpLeftClick':self.onCapslockOnLeftDrag_CapslockOnLeftClick, 
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
            'CapslockOffShiftUpCtrlDownAltUpG':self.onCtrlG
            }
        self.state = MouseState()
    def process(self, event):
        concrete_hotkeys = self.state.update_state(event)
        for concrete_hotkey in concrete_hotkeys:
            if concrete_hotkey in self.jump:
                self.jump[concrete_hotkey](event)
    
    
    def onH(self, event):
        'show this help info'
        print('press ' + 'H')
        print('# ' + 'show this help info')

    def onN(self, event):
        'generate a new game'
        print('press ' + 'N')
        print('# ' + 'generate a new game')

    def onCtrlN(self, event):
        'generate a null game'
        print('press ' + 'CtrlN')
        print('# ' + 'generate a null game')

    def onL(self, event):
        'quick load from "{picture}";'
        print('press ' + 'L')
        print('# ' + 'quick load from "{picture}";')

    def onCtrlL(self, event):
        'ask to load a picture'
        print('press ' + 'CtrlL')
        print('# ' + 'ask to load a picture')

    def onS(self, event):
        'quick save to "{picture}"'
        print('press ' + 'S')
        print('# ' + 'quick save to "{picture}"')

    def onCtrlS(self, event):
        'ask to save'
        print('press ' + 'CtrlS')
        print('# ' + 'ask to save')

    def onP(self, event):
        'print the current state'
        print('press ' + 'P')
        print('# ' + 'print the current state')

    def onLeftDrag(self, event):
        'select points'
        print('press ' + 'LeftDrag')
        print('# ' + 'select points')

    def onCtrlLeftClick(self, event):
        'turn more unselected points selected or unselect those selected'
        print('press ' + 'CtrlLeftClick')
        print('# ' + 'turn more unselected points selected or unselect those selected')

    def onI(self, event):
        'inverse the selected state'
        print('press ' + 'I')
        print('# ' + 'inverse the selected state')

    def onDelete(self, event):
        'kill the selected points'
        print('press ' + 'Delete')
        print('# ' + 'kill the selected points')

    def onCapslockOnLeftDrag_CapslockOnLeftClick(self, event):
        '- resurrect the passed points'
        print('press ' + 'CapslockOnLeftDrag | CapslockOnLeftClick')
        print('# ' + '- resurrect the passed points')

    def onSpace(self, event):
        'step to the next state'
        print('press ' + 'Space')
        print('# ' + 'step to the next state')

    def onMiddleClick(self, event):
        'step to the next {nsteps}th state'
        print('press ' + 'MiddleClick')
        print('# ' + 'step to the next {nsteps}th state')

    def onRightDrag(self, event):
        'drag the whole world'
        print('press ' + 'RightDrag')
        print('# ' + 'drag the whole world')

    def onV(self, event):
        'show the super_view window to select where to goto'
        print('press ' + 'V')
        print('# ' + 'show the super_view window to select where to goto')

    def onG(self, event):
        'ask where to go to'
        print('press ' + 'G')
        print('# ' + 'ask where to go to')

    def onCtrlF(self, event):
        'search the first place where there are some living points'
        print('press ' + 'CtrlF')
        print('# ' + 'search the first place where there are some living points')

    def onF3(self, event):
        'search next place'
        print('press ' + 'F3')
        print('# ' + 'search next place')

    def onUp_Down_Left_Right(self, event):
        'move one window size each'
        print('press ' + 'Up | Down | Left | Right')
        print('# ' + 'move one window size each')

    def onEscape(self, event):
        'disable cursor'
        print('press ' + 'Escape')
        print('# ' + 'disable cursor')

    def onCapslockOffLeftClick(self, event):
        'set the cursor'
        print('press ' + 'CapslockOffLeftClick')
        print('# ' + 'set the cursor')

    def onCtrlG(self, event):
        'ask to set the cursor'
        print('press ' + 'CtrlG')
        print('# ' + 'ask to set the cursor')
#

class wb:
    def __init__(self, size=(800,600)):
        sdl2.ext.init()
        window = sdl2.ext.Window("test", size=size)
        window.show()
        surface = window.get_surface()
        self.window = window

        self.s = MouseState()
        self.p = EventHandlerBase()

    
    def run(self):
        running = True
        while running:
            events = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break
                self.p.process(event)
                continue
                self.s.update_state(event)
                if self.s.get_hkfullnames():print(self.s.get_hkfullnames())
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break
                elif event.type in self.jump:
                    self.jump[event.type](self, event)
                    '''
                elif event.type == sdl2.SDL_MOUSEBUTTONDOWN:
                    self.onMouseDown(event)
                elif event.type == sdl2.SDL_MOUSEBUTTONUP:
                    self.onMouseUp(event)
                elif event.type == sdl2.SDL_MOUSEMOTION:
                    self.onMouseMotion(event)
                    

                elif event.type == sdl2.SDL_KEYDOWN:
                    self.onKeyDown(event)
                elif event.type == sdl2.SDL_KEYUP:
                    self.onKeyUp(event)'''

                #break


            self.window.refresh()
        sdl2.ext.quit()
        return 0

    def onMouseMotion(self, event):
        m = event.motion
        #print(dir(m))
        #'state', 'timestamp', 'type', 'which', 'windowID', 'x', 'xrel', 'y', 'yrel'
        #print_attr(m)
    def onMouseUp(self, event):pass

    def onMouseDown(self, event):
        b = event.button
        '''
        if b.button == sdl2.SDL_BUTTON_LEFT:
        elif b.button == sdl2.SDL_BUTTON_RIGHT:
        elif b.button == sdl2.SDL_BUTTON_MIDDLE:'''

    def onKeyUp(self, event):
        k = event.key.keysym

    def onKeyDown(self, event):
        k = event.key
        '''
        self.ns.bCtrl = ctrl = sdl2.KMOD_CTRL & k.keysym.mod
        if sdl2.SDL_SCANCODE_CAPSLOCK == k.keysym.scancode:'''

        #print(dir(k))
        #'keysym', 'padding2', 'padding3', 'repeat', 'state', 'timestamp', 'type', 'windowID'
        #print('repeat', k.repeat) bool //is a repeating key
        '''
        k = k.keysym
        for n in dir(k):
            if not n.startswith('_'):
                print(n, getattr(k, n))

        #print('chr(sym)', chr(k.sym))
        print('')'''

        #print(self.s.state2str())
    jump = {sdl2.SDL_MOUSEBUTTONDOWN:onMouseDown,
            sdl2.SDL_MOUSEBUTTONUP:onMouseUp,
            sdl2.SDL_MOUSEMOTION:onMouseMotion,
            sdl2.SDL_KEYDOWN:onKeyDown,
            sdl2.SDL_KEYUP:onKeyUp
            }
        

class w(wb):
    def onMouseDown(self, event):
        b = event.button
        k = event.key
        #print(dir(event))
        #print(k.keysym.mod)
        
        #print(dir(b))
        #'button', 'clicks', 'padding1', 'state', 'timestamp',
        #'type', 'which', 'windowID', 'x', 'y'

        #print(b.state)???

        #print(b.clicks) good

        

if __name__ == '__main__':
    w().run()
    
