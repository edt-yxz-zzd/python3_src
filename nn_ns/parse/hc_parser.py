
import itertools
import re
import io
#import sdl2

__all__ = ['parse_HC_file', 'generate_sourcecode']


__doc__ = '''parse HC file

hotkey comment file (HC file) look like this:
#    --------------   HC file example start --------------
H                  show this help info
Escape             comment that tells what happens when Esc press
#                  the whole line is a comment 
CtrlLeftClick      comment
H&F3&ShiftCtrlK    comment about these 3 hotkey that has same function

CapslockOnLeftMove comment about mouse movement at caps key toggled on

#    --------------   HC file example end   --------------

HC file's line format:
#    --------------   HC file line format start --------------
line ::= [spaces] hk ('|' hk)* spaces comment [spaces] | [spaces] '#' comment
hk ::= hk_state hk_action // <hk> stands for macro hotkey

hk_state ::= [caps][shift][ctrl][alt]
caps ::= '' | 'CapslockOn' | 'CapslockOff'  // '' represents capslock state ignored
ctrl ::= '' | 'Ctrl' | '[Ctrl]' // '' repersents ctrl up; '[Ctrl]' represents ctrl state ignored
shift ::= '' | 'Shift' | '[Shift]'
alt ::= '' | 'Alt' | '[Alt]'

hk_action ::= kb | ms

kb ::= key kb_action
key ::= digit | capital_letter | 'F1'-'F12'
       | 'Space' | 'Escape' | 'Delete'
       | 'Up' | 'Down' | 'Left' | 'Right'
kb_action ::= '' // stands for 'Down'. yeah, no 'Up'

ms ::= button ms_action
button ::= 'Left' | 'Right' | 'Middle'
ms_action ::= 'Up' | 'Down' | 'Move' | 'Drag' | 'Click'
#    --------------   HC file line format end   --------------



parse HC file and then generate file like this:
#    --------------   generated code example start --------------
from root.MouseState import MouseState

class EventHandlerBase:
    __doc__ = 'maintain keyboard state and dispatch hotkey\n'\
              '\n'\
              'to get keyboard state: self.state.curr_kbd_state\n'\
              '\n'\
              'H                  show this help info' '\n'\
              ...

    def __init__(self):
        self.jump = {\
            'CapslockOnShiftUpCtrlUpAltUpH':self.onH, 
            'CapslockOffShiftUpCtrlUpAltUpH':self.onH,
            ...
            ...
            }
        self.state = MouseState()
    def process(self, event):
        hkfullnames = self.state.update_state(event)
        for hkfullname in hkfullnames:
            if hkfullname in self.jump:
                self.jump[hkfullname](event)
    
    
    def onH(self, event):
        'show this help info'
        print('press ' + 'H')
        print('# ' + 'show this help info')
    
#    --------------   generated code example end   --------------

and then the user can fill the on<HotKey> function and write some like this:

class Window(EventHandlerBase):
    def __init__(self):
        EventHandlerBase.__init__(self)
    def run(self):
        while True:
            e = system.get_event()
            self.process(e)
        
'''



class HCParseException(Exception):pass
def parse_HC_line(line):
    line = line.strip()
    if not line or line[0] == '#':
        return None

    ls = line.split(None, 1)
    while len(ls) < 2:
        ls.append('')
    macro_hotkeys_str, tail = ls
    
    macro_hotkeys, macro_hotkey_infos = parse_macro_hotkeys_str(macro_hotkeys_str)
    comment = tail.strip()
    return macro_hotkeys, macro_hotkey_infos, comment
    
def parse_macro_hotkeys_str(macro_hotkeys_str):
    macro_hotkeys = macro_hotkeys_str.split('&')
    return macro_hotkeys, [parse_hk(hk_str) for hk_str in macro_hotkeys]

def parse_hk(hk_str):
    t, hk_state_str, hk_action = parse_hk_action_from_hk_end(hk_str)

    hk_state = parse_hk_state(hk_state_str)
    return t, hk_state, hk_action


def parse_hk_action_from_hk_end(hk):
    r = find_ms_at_end(hk)
    if r:
        head, ms = r
        t = 'ms'
    else:
        r = find_kb_at_end(hk)
        if not r: raise HCParseException('HC file format error: '+hk)
        head, kb = r
        t = 'kb'

    hk_state_str = head
    hk_action = r[-1]
    return t, hk_state_str, hk_action

capslock = ['CapslockOn', 'CapslockOff', '']
shift = ['Shift', '[Shift]', '']
ctrl = ['Ctrl', '[Ctrl]', '']
alt = ['Alt', '[Alt]', '']

press = ['Down', 'Any', 'Up']
toggle = ['On', 'Off', 'Any']

tkeys = [(capslock, 'Capslock')]
pkeys = [(shift, 'Shift'),
         (ctrl, 'Ctrl'),
         (alt, 'Alt')]

tp_startstrs_name_ls__allstates = [(tkeys, toggle), (pkeys, press)]
def parse_hk_state(hk_state_str):
    ls = []
    head = hk_state_str
    for startstrs_name_ls, allstates in tp_startstrs_name_ls__allstates:
        for start_strings, name in startstrs_name_ls:
            for start_str, state in zip(start_strings, allstates):
                if head.startswith(start_str):
                    head = head[len(start_str):]
                    ls.append((name, state))
                    break

    if len(head): raise HCParseException('HC file format error: ' + head)
    return ls

'''
digit | capital_letter | 'F1'-'F12'
       | 'Space' | 'Escape' | 'Up' | 'Down' | 'Left' | 'Right'''

digits = [str(i) for i in range(10)]
capital_letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]
Fdds = ['F{n}'.format(n=n+1) for n in range(12)]
other_keys = 'Space Escape Up Down Left Right Delete'.split()

key_ls = sorted(itertools.chain(digits, capital_letters, Fdds, other_keys))
kb_action_ls = ['']

button_ls = sorted('Left Right Middle'.split())
ms_action_ls = sorted('Up Down Move Drag Click'.split())

def find_longest_word_at_end(sorted_ls, line):
    #print('find_longest_word_at_end', sorted_ls, line)

    r = None
    for word in reversed(sorted_ls):
        if line.endswith(word):
            head = line[: len(line)-len(word)]
            r = head, word
            break
            
    #print('\t', r)
    return r

def find_2words_at_end(first_ls, second_ls, line):
    #print('find_2words_at_end', line)
    r = find_longest_word_at_end(second_ls, line)
    if not r: return None
    head, second = r
    
    r = find_longest_word_at_end(first_ls, head)
    if not r: return None
    head, first = r

    fs = (first, second)
    return head, fs

def find_ms_at_end(hk):
    return find_2words_at_end(button_ls, ms_action_ls, hk)

def find_kb_at_end(hk):
    return find_2words_at_end(key_ls, kb_action_ls, hk)

def methodname_from_macro_hotkeys(macro_hotkeys):
    return 'on' + '_'.join(macro_hotkeys)

def yields_concrete_hotkeys_from_macro_hotkey_infos(macro_hotkey_infos):
    return [name for hk_info in macro_hotkey_infos \
            for name in yields_concrete_hotkeys_from_hk_info(hk_info)]

def yields_concrete_hotkeys_from_hk_info(hk_info):
    t, hk_state, hk_action = hk_info

    ls = ['']
    i = -1
    for startstrs_name_ls, allstates in tp_startstrs_name_ls__allstates:
        for start_strings, name in startstrs_name_ls:
            i += 1
            kname, state = hk_state[i]
            assert kname == name

            if state == 'Any':
                concrete_states = [s for s in allstates if s != 'Any']
            else:
                concrete_states = [state]

            ls = [head + name + concrete_state for head in ls \
                  for concrete_state in concrete_states]
                    
    hk_action_str = ''.join(hk_action)
    ls = [concrete_state + hk_action_str for concrete_state in ls]
    return ls

def parse_HC_file(file):
    ls = []
    lineNo = 0
    for line in file:
        lineNo += 1
        try:
            r = parse_HC_line(line)
        except HCParseException as e:
            raise HCParseException('LineNumber {} {}'.format(lineNo, e.args[0]))
        
        if r:
            macro_hotkeys, macro_hotkey_infos, comment = r
            methodname = methodname_from_macro_hotkeys(macro_hotkeys)
            concrete_hotkeys = yields_concrete_hotkeys_from_macro_hotkey_infos(macro_hotkey_infos)
            ls.append((macro_hotkeys, macro_hotkey_infos, comment, \
                       methodname, concrete_hotkeys))
    return ls

def generate_sourcecode(parse_HC_file_result):
    ls = []
    for macro_hotkeys, macro_hotkey_infos, comment, \
        methodname, concrete_hotkeys in parse_HC_file_result:
        for concrete_hotkey in concrete_hotkeys:
            s = '{concrete_hotkey!r}:self.{methodname}'.format(\
                concrete_hotkey=concrete_hotkey, methodname=methodname)
            ls.append(s)

    head = '\n            '
    concrete_hotkey2onFunc = '{\\' + head + (', '+head).join(ls) + head + '}'

    ls = []
    for macro_hotkeys, macro_hotkey_infos, comment, \
        methodname, concrete_hotkeys in parse_HC_file_result:
        f = '''
    def {methodname}(self, event):
        '{comment}'
        print('press ' + {macro_hotkeys!r})
        print('# ' + {comment!r})'''\
        .format(macro_hotkeys=' | '.join(macro_hotkeys), \
                comment=comment, methodname=methodname)
        ls.append(f)

    onFuncs = '\n'.join(ls)
    
    src = '''
from root.MouseState import MouseState

class EventHandlerBase:
    __doc__ = 'maintain keyboard state and dispatch hotkey\n\n'\
              'to get keyboard state: self.state.curr_kbd_state'
              
    def __init__(self):
        self.jump = {concrete_hotkey2onFunc}
        self.state = MouseState()


    def process(self, event):
        concrete_hotkeys = self.state.update_state(event)
        for concrete_hotkey in concrete_hotkeys:
            if concrete_hotkey in self.jump:
                self.jump[concrete_hotkey](event)
    
    {onFuncs}
#'''.format(concrete_hotkey2onFunc=concrete_hotkey2onFunc,
            onFuncs=onFuncs)

    return src

_test_file = '''

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
CapslockOnLeftMove&CapslockOnLeftClick resurrect the passed points
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
Z zoom in around cursor if exists
CtrlZ zoom out around cursor if exists
#cccc
'''

_test_file = io.StringIO(_test_file)

def test_parse_HC_line():
    for line in _test_file:
        print(line, parse_HC_line(line))

def test_yields_all_hknames_from_hks():
    for line in _test_file:
        r = parse_HC_line(line)
        if r:
            hknames, hks, comment = r
            print(line, yields_concrete_hotkeys_from_macro_hotkey_infos(hks))


def test_generate_sourcecode():
    print(generate_sourcecode(parse_HC_file(_test_file)))



#if __name__ == '__main__':
    #test_parseLine()
    #test_yields_all_hknames_from_hks()
    #test_generate_sourcecode()


def main(args = None):
    import argparse, sys

    parser = argparse.ArgumentParser(description='compile HC file')
    parser.add_argument('source', type=argparse.FileType('r'), \
                        nargs='?', default=sys.stdin,
                        help='HC file name')

    parser.add_argument('destination', type=argparse.FileType('w'), \
                        nargs='?', default=sys.stdout,
                        help='file name for output')

    if args == None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(args)

    
    fout = args.destination
    with args.source as fin:
        if fout is sys.stdout:
            py = generate_sourcecode(parse_HC_file(fin))
            fout.write(py)
        else:
            with fout:
                py = generate_sourcecode(parse_HC_file(fin))
                fout.write(py)
        

    


if __name__ == "__main__":
    main()

    
'''see temp/test_sdl2_event.py
class KeybdState:
    def __init__(self):
        self.state = 0
            
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
        elif event.type == sdl2.SDL_KEYUP:
            self.onKeyUp(event)

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
    
'''

