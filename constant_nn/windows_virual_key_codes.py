import collections

name_list = ('VK_0', 'VK_1', 'VK_2', 'VK_3', 'VK_4', 'VK_5', 'VK_6', 'VK_7', 'VK_8', 'VK_9', 'VK_A', 'VK_ACCEPT', 'VK_ADD', 'VK_APPS', 'VK_ATTN', 'VK_B', 'VK_BACK', 'VK_BROWSER_BACK', 'VK_BROWSER_FAVORITES', 'VK_BROWSER_FORWARD', 'VK_BROWSER_HOME', 'VK_BROWSER_REFRESH', 'VK_BROWSER_SEARCH', 'VK_BROWSER_STOP', 'VK_C', 'VK_CANCEL', 'VK_CAPITAL', 'VK_CLEAR', 'VK_CONTROL', 'VK_CONVERT', 'VK_CRSEL', 'VK_D', 'VK_DECIMAL', 'VK_DELETE', 'VK_DIVIDE', 'VK_DOWN', 'VK_E', 'VK_END', 'VK_EREOF', 'VK_ESCAPE', 'VK_EXECUTE', 'VK_EXSEL', 'VK_F', 'VK_F1', 'VK_F10', 'VK_F11', 'VK_F12', 'VK_F13', 'VK_F14', 'VK_F15', 'VK_F16', 'VK_F17', 'VK_F18', 'VK_F19', 'VK_F2', 'VK_F20', 'VK_F21', 'VK_F22', 'VK_F23', 'VK_F24', 'VK_F3', 'VK_F4', 'VK_F5', 'VK_F6', 'VK_F7', 'VK_F8', 'VK_F9', 'VK_FINAL', 'VK_G', 'VK_H', 'VK_HANGUEL', 'VK_HANGUL', 'VK_HANJA', 'VK_HELP', 'VK_HOME', 'VK_I', 'VK_INSERT', 'VK_J', 'VK_JUNJA', 'VK_K', 'VK_KANA', 'VK_KANJI', 'VK_L', 'VK_LAUNCH_APP1', 'VK_LAUNCH_APP2', 'VK_LAUNCH_MAIL', 'VK_LAUNCH_MEDIA_SELECT', 'VK_LBUTTON', 'VK_LCONTROL', 'VK_LEFT', 'VK_LMENU', 'VK_LSHIFT', 'VK_LWIN', 'VK_M', 'VK_MBUTTON', 'VK_MEDIA_NEXT_TRACK', 'VK_MEDIA_PLAY_PAUSE', 'VK_MEDIA_PREV_TRACK', 'VK_MEDIA_STOP', 'VK_MENU', 'VK_MODECHANGE', 'VK_MULTIPLY', 'VK_N', 'VK_NEXT', 'VK_NONCONVERT', 'VK_NUMLOCK', 'VK_NUMPAD0', 'VK_NUMPAD1', 'VK_NUMPAD2', 'VK_NUMPAD3', 'VK_NUMPAD4', 'VK_NUMPAD5', 'VK_NUMPAD6', 'VK_NUMPAD7', 'VK_NUMPAD8', 'VK_NUMPAD9', 'VK_O', 'VK_OEM_1', 'VK_OEM_102', 'VK_OEM_2', 'VK_OEM_3', 'VK_OEM_4', 'VK_OEM_5', 'VK_OEM_6', 'VK_OEM_7', 'VK_OEM_8', 'VK_OEM_CLEAR', 'VK_OEM_COMMA', 'VK_OEM_MINUS', 'VK_OEM_PERIOD', 'VK_OEM_PLUS', 'VK_P', 'VK_PA1', 'VK_PACKET', 'VK_PAUSE', 'VK_PLAY', 'VK_PRINT', 'VK_PRIOR', 'VK_PROCESSKEY', 'VK_Q', 'VK_R', 'VK_RBUTTON', 'VK_RCONTROL', 'VK_RETURN', 'VK_RIGHT', 'VK_RMENU', 'VK_RSHIFT', 'VK_RWIN', 'VK_S', 'VK_SCROLL', 'VK_SELECT', 'VK_SEPARATOR', 'VK_SHIFT', 'VK_SLEEP', 'VK_SNAPSHOT', 'VK_SPACE', 'VK_SUBTRACT', 'VK_T', 'VK_TAB', 'VK_U', 'VK_UP', 'VK_V', 'VK_VOLUME_DOWN', 'VK_VOLUME_MUTE', 'VK_VOLUME_UP', 'VK_W', 'VK_X', 'VK_XBUTTON1', 'VK_XBUTTON2', 'VK_Y', 'VK_Z', 'VK_ZOOM')
vkname_t = collections.namedtuple('vkname_t', name_list) # frozendict???

id2names = ((), ('VK_LBUTTON',), ('VK_RBUTTON',), ('VK_CANCEL',), ('VK_MBUTTON',), ('VK_XBUTTON1',), ('VK_XBUTTON2',), (), ('VK_BACK',), ('VK_TAB',), (), (), ('VK_CLEAR',), ('VK_RETURN',), (), (), ('VK_SHIFT',), ('VK_CONTROL',), ('VK_MENU',), ('VK_PAUSE',), ('VK_CAPITAL',), ('VK_HANGUEL', 'VK_HANGUL', 'VK_KANA'), (), ('VK_JUNJA',), ('VK_FINAL',), ('VK_HANJA', 'VK_KANJI'), (), ('VK_ESCAPE',), ('VK_CONVERT',), ('VK_NONCONVERT',), ('VK_ACCEPT',), ('VK_MODECHANGE',), ('VK_SPACE',), ('VK_PRIOR',), ('VK_NEXT',), ('VK_END',), ('VK_HOME',), ('VK_LEFT',), ('VK_UP',), ('VK_RIGHT',), ('VK_DOWN',), ('VK_SELECT',), ('VK_PRINT',), ('VK_EXECUTE',), ('VK_SNAPSHOT',), ('VK_INSERT',), ('VK_DELETE',), ('VK_HELP',), ('VK_0',), ('VK_1',), ('VK_2',), ('VK_3',), ('VK_4',), ('VK_5',), ('VK_6',), ('VK_7',), ('VK_8',), ('VK_9',), (), (), (), (), (), (), (), ('VK_A',), ('VK_B',), ('VK_C',), ('VK_D',), ('VK_E',), ('VK_F',), ('VK_G',), ('VK_H',), ('VK_I',), ('VK_J',), ('VK_K',), ('VK_L',), ('VK_M',), ('VK_N',), ('VK_O',), ('VK_P',), ('VK_Q',), ('VK_R',), ('VK_S',), ('VK_T',), ('VK_U',), ('VK_V',), ('VK_W',), ('VK_X',), ('VK_Y',), ('VK_Z',), ('VK_LWIN',), ('VK_RWIN',), ('VK_APPS',), (), ('VK_SLEEP',), ('VK_NUMPAD0',), ('VK_NUMPAD1',), ('VK_NUMPAD2',), ('VK_NUMPAD3',), ('VK_NUMPAD4',), ('VK_NUMPAD5',), ('VK_NUMPAD6',), ('VK_NUMPAD7',), ('VK_NUMPAD8',), ('VK_NUMPAD9',), ('VK_MULTIPLY',), ('VK_ADD',), ('VK_SEPARATOR',), ('VK_SUBTRACT',), ('VK_DECIMAL',), ('VK_DIVIDE',), ('VK_F1',), ('VK_F2',), ('VK_F3',), ('VK_F4',), ('VK_F5',), ('VK_F6',), ('VK_F7',), ('VK_F8',), ('VK_F9',), ('VK_F10',), ('VK_F11',), ('VK_F12',), ('VK_F13',), ('VK_F14',), ('VK_F15',), ('VK_F16',), ('VK_F17',), ('VK_F18',), ('VK_F19',), ('VK_F20',), ('VK_F21',), ('VK_F22',), ('VK_F23',), ('VK_F24',), (), (), (), (), (), (), (), (), ('VK_NUMLOCK',), ('VK_SCROLL',), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ('VK_LSHIFT',), ('VK_RSHIFT',), ('VK_LCONTROL',), ('VK_RCONTROL',), ('VK_LMENU',), ('VK_RMENU',), ('VK_BROWSER_BACK',), ('VK_BROWSER_FORWARD',), ('VK_BROWSER_REFRESH',), ('VK_BROWSER_STOP',), ('VK_BROWSER_SEARCH',), ('VK_BROWSER_FAVORITES',), ('VK_BROWSER_HOME',), ('VK_VOLUME_MUTE',), ('VK_VOLUME_DOWN',), ('VK_VOLUME_UP',), ('VK_MEDIA_NEXT_TRACK',), ('VK_MEDIA_PREV_TRACK',), ('VK_MEDIA_STOP',), ('VK_MEDIA_PLAY_PAUSE',), ('VK_LAUNCH_MAIL',), ('VK_LAUNCH_MEDIA_SELECT',), ('VK_LAUNCH_APP1',), ('VK_LAUNCH_APP2',), (), (), ('VK_OEM_1',), ('VK_OEM_PLUS',), ('VK_OEM_COMMA',), ('VK_OEM_MINUS',), ('VK_OEM_PERIOD',), ('VK_OEM_2',), ('VK_OEM_3',), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ('VK_OEM_4',), ('VK_OEM_5',), ('VK_OEM_6',), ('VK_OEM_7',), ('VK_OEM_8',), (), (), ('VK_OEM_102',), (), (), ('VK_PROCESSKEY',), (), ('VK_PACKET',), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ('VK_ATTN',), ('VK_CRSEL',), ('VK_EXSEL',), ('VK_EREOF',), ('VK_PLAY',), ('VK_ZOOM',), (), ('VK_PA1',), ('VK_OEM_CLEAR',), ())
name2description = vkname_t(VK_0='0 key', VK_1='1 key', VK_2='2 key', VK_3='3 key', VK_4='4 key', VK_5='5 key', VK_6='6 key', VK_7='7 key', VK_8='8 key', VK_9='9 key', VK_A='A key', VK_ACCEPT='IME accept', VK_ADD='Add key', VK_APPS='Applications key (Natural keyboard)', VK_ATTN='Attn key', VK_B='B key', VK_BACK='BACKSPACE key', VK_BROWSER_BACK='Browser Back key', VK_BROWSER_FAVORITES='Browser Favorites key', VK_BROWSER_FORWARD='Browser Forward key', VK_BROWSER_HOME='Browser Start and Home key', VK_BROWSER_REFRESH='Browser Refresh key', VK_BROWSER_SEARCH='Browser Search key', VK_BROWSER_STOP='Browser Stop key', VK_C='C key', VK_CANCEL='Control-break processing', VK_CAPITAL='CAPS LOCK key', VK_CLEAR='CLEAR key', VK_CONTROL='CTRL key', VK_CONVERT='IME convert', VK_CRSEL='CrSel key', VK_D='D key', VK_DECIMAL='Decimal key', VK_DELETE='DEL key', VK_DIVIDE='Divide key', VK_DOWN='DOWN ARROW key', VK_E='E key', VK_END='END key', VK_EREOF='Erase EOF key', VK_ESCAPE='ESC key', VK_EXECUTE='EXECUTE key', VK_EXSEL='ExSel key', VK_F='F key', VK_F1='F1 key', VK_F10='F10 key', VK_F11='F11 key', VK_F12='F12 key', VK_F13='F13 key', VK_F14='F14 key', VK_F15='F15 key', VK_F16='F16 key', VK_F17='F17 key', VK_F18='F18 key', VK_F19='F19 key', VK_F2='F2 key', VK_F20='F20 key', VK_F21='F21 key', VK_F22='F22 key', VK_F23='F23 key', VK_F24='F24 key', VK_F3='F3 key', VK_F4='F4 key', VK_F5='F5 key', VK_F6='F6 key', VK_F7='F7 key', VK_F8='F8 key', VK_F9='F9 key', VK_FINAL='IME final mode', VK_G='G key', VK_H='H key', VK_HANGUEL='IME Hanguel mode (maintained for compatibility; use VK_HANGUL)', VK_HANGUL='IME Hangul mode', VK_HANJA='IME Hanja mode', VK_HELP='HELP key', VK_HOME='HOME key', VK_I='I key', VK_INSERT='INS key', VK_J='J key', VK_JUNJA='IME Junja mode', VK_K='K key', VK_KANA='IME Kana mode', VK_KANJI='IME Kanji mode', VK_L='L key', VK_LAUNCH_APP1='Start Application 1 key', VK_LAUNCH_APP2='Start Application 2 key', VK_LAUNCH_MAIL='Start Mail key', VK_LAUNCH_MEDIA_SELECT='Select Media key', VK_LBUTTON='Left mouse button', VK_LCONTROL='Left CONTROL key', VK_LEFT='LEFT ARROW key', VK_LMENU='Left MENU key', VK_LSHIFT='Left SHIFT key', VK_LWIN='Left Windows key (Natural keyboard)', VK_M='M key', VK_MBUTTON='Middle mouse button (three-button mouse)', VK_MEDIA_NEXT_TRACK='Next Track key', VK_MEDIA_PLAY_PAUSE='Play/Pause Media key', VK_MEDIA_PREV_TRACK='Previous Track key', VK_MEDIA_STOP='Stop Media key', VK_MENU='ALT key', VK_MODECHANGE='IME mode change request', VK_MULTIPLY='Multiply key', VK_N='N key', VK_NEXT='PAGE DOWN key', VK_NONCONVERT='IME nonconvert', VK_NUMLOCK='NUM LOCK key', VK_NUMPAD0='Numeric keypad 0 key', VK_NUMPAD1='Numeric keypad 1 key', VK_NUMPAD2='Numeric keypad 2 key', VK_NUMPAD3='Numeric keypad 3 key', VK_NUMPAD4='Numeric keypad 4 key', VK_NUMPAD5='Numeric keypad 5 key', VK_NUMPAD6='Numeric keypad 6 key', VK_NUMPAD7='Numeric keypad 7 key', VK_NUMPAD8='Numeric keypad 8 key', VK_NUMPAD9='Numeric keypad 9 key', VK_O='O key', VK_OEM_1="Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the ';:' key", VK_OEM_102='Either the angle bracket key or the backslash key on the RT 102-key keyboard', VK_OEM_2="Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the '/?' key", VK_OEM_3="Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the '`~' key", VK_OEM_4="Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the '[{' key", VK_OEM_5="Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the '\\|' key", VK_OEM_6="Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the ']}' key", VK_OEM_7="Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the 'single-quote/double-quote' key", VK_OEM_8='Used for miscellaneous characters; it can vary by keyboard.', VK_OEM_CLEAR='Clear key', VK_OEM_COMMA="For any country/region, the ',' key", VK_OEM_MINUS="For any country/region, the '-' key", VK_OEM_PERIOD="For any country/region, the '.' key", VK_OEM_PLUS="For any country/region, the '+' key", VK_P='P key', VK_PA1='PA1 key', VK_PACKET='Used to pass Unicode characters as if they were keystrokes. The VK_PACKET key is the low word of a 32-bit Virtual Key value used for non-keyboard input methods. For more information, see Remark in KEYBDINPUT, SendInput, WM_KEYDOWN, and WM_KEYUP', VK_PAUSE='PAUSE key', VK_PLAY='Play key', VK_PRINT='PRINT key', VK_PRIOR='PAGE UP key', VK_PROCESSKEY='IME PROCESS key', VK_Q='Q key', VK_R='R key', VK_RBUTTON='Right mouse button', VK_RCONTROL='Right CONTROL key', VK_RETURN='ENTER key', VK_RIGHT='RIGHT ARROW key', VK_RMENU='Right MENU key', VK_RSHIFT='Right SHIFT key', VK_RWIN='Right Windows key (Natural keyboard)', VK_S='S key', VK_SCROLL='SCROLL LOCK key', VK_SELECT='SELECT key', VK_SEPARATOR='Separator key', VK_SHIFT='SHIFT key', VK_SLEEP='Computer Sleep key', VK_SNAPSHOT='PRINT SCREEN key', VK_SPACE='SPACEBAR', VK_SUBTRACT='Subtract key', VK_T='T key', VK_TAB='TAB key', VK_U='U key', VK_UP='UP ARROW key', VK_V='V key', VK_VOLUME_DOWN='Volume Down key', VK_VOLUME_MUTE='Volume Mute key', VK_VOLUME_UP='Volume Up key', VK_W='W key', VK_X='X key', VK_XBUTTON1='X1 mouse button', VK_XBUTTON2='X2 mouse button', VK_Y='Y key', VK_Z='Z ke', VK_ZOOM='Zoom key')
name2id = vkname_t(VK_0=48, VK_1=49, VK_2=50, VK_3=51, VK_4=52, VK_5=53, VK_6=54, VK_7=55, VK_8=56, VK_9=57, VK_A=65, VK_ACCEPT=30, VK_ADD=107, VK_APPS=93, VK_ATTN=246, VK_B=66, VK_BACK=8, VK_BROWSER_BACK=166, VK_BROWSER_FAVORITES=171, VK_BROWSER_FORWARD=167, VK_BROWSER_HOME=172, VK_BROWSER_REFRESH=168, VK_BROWSER_SEARCH=170, VK_BROWSER_STOP=169, VK_C=67, VK_CANCEL=3, VK_CAPITAL=20, VK_CLEAR=12, VK_CONTROL=17, VK_CONVERT=28, VK_CRSEL=247, VK_D=68, VK_DECIMAL=110, VK_DELETE=46, VK_DIVIDE=111, VK_DOWN=40, VK_E=69, VK_END=35, VK_EREOF=249, VK_ESCAPE=27, VK_EXECUTE=43, VK_EXSEL=248, VK_F=70, VK_F1=112, VK_F10=121, VK_F11=122, VK_F12=123, VK_F13=124, VK_F14=125, VK_F15=126, VK_F16=127, VK_F17=128, VK_F18=129, VK_F19=130, VK_F2=113, VK_F20=131, VK_F21=132, VK_F22=133, VK_F23=134, VK_F24=135, VK_F3=114, VK_F4=115, VK_F5=116, VK_F6=117, VK_F7=118, VK_F8=119, VK_F9=120, VK_FINAL=24, VK_G=71, VK_H=72, VK_HANGUEL=21, VK_HANGUL=21, VK_HANJA=25, VK_HELP=47, VK_HOME=36, VK_I=73, VK_INSERT=45, VK_J=74, VK_JUNJA=23, VK_K=75, VK_KANA=21, VK_KANJI=25, VK_L=76, VK_LAUNCH_APP1=182, VK_LAUNCH_APP2=183, VK_LAUNCH_MAIL=180, VK_LAUNCH_MEDIA_SELECT=181, VK_LBUTTON=1, VK_LCONTROL=162, VK_LEFT=37, VK_LMENU=164, VK_LSHIFT=160, VK_LWIN=91, VK_M=77, VK_MBUTTON=4, VK_MEDIA_NEXT_TRACK=176, VK_MEDIA_PLAY_PAUSE=179, VK_MEDIA_PREV_TRACK=177, VK_MEDIA_STOP=178, VK_MENU=18, VK_MODECHANGE=31, VK_MULTIPLY=106, VK_N=78, VK_NEXT=34, VK_NONCONVERT=29, VK_NUMLOCK=144, VK_NUMPAD0=96, VK_NUMPAD1=97, VK_NUMPAD2=98, VK_NUMPAD3=99, VK_NUMPAD4=100, VK_NUMPAD5=101, VK_NUMPAD6=102, VK_NUMPAD7=103, VK_NUMPAD8=104, VK_NUMPAD9=105, VK_O=79, VK_OEM_1=186, VK_OEM_102=226, VK_OEM_2=191, VK_OEM_3=192, VK_OEM_4=219, VK_OEM_5=220, VK_OEM_6=221, VK_OEM_7=222, VK_OEM_8=223, VK_OEM_CLEAR=254, VK_OEM_COMMA=188, VK_OEM_MINUS=189, VK_OEM_PERIOD=190, VK_OEM_PLUS=187, VK_P=80, VK_PA1=253, VK_PACKET=231, VK_PAUSE=19, VK_PLAY=250, VK_PRINT=42, VK_PRIOR=33, VK_PROCESSKEY=229, VK_Q=81, VK_R=82, VK_RBUTTON=2, VK_RCONTROL=163, VK_RETURN=13, VK_RIGHT=39, VK_RMENU=165, VK_RSHIFT=161, VK_RWIN=92, VK_S=83, VK_SCROLL=145, VK_SELECT=41, VK_SEPARATOR=108, VK_SHIFT=16, VK_SLEEP=95, VK_SNAPSHOT=44, VK_SPACE=32, VK_SUBTRACT=109, VK_T=84, VK_TAB=9, VK_U=85, VK_UP=38, VK_V=86, VK_VOLUME_DOWN=174, VK_VOLUME_MUTE=173, VK_VOLUME_UP=175, VK_W=87, VK_X=88, VK_XBUTTON1=5, VK_XBUTTON2=6, VK_Y=89, VK_Z=90, VK_ZOOM=251)

#assert tuple(sorted(name2id.__dict__.keys())) == name_list
globals().update(name2id.__dict__)






'''
n = (2**8)
id2names = list(set() for _ in range(n))
name2id = {}
name2description = {}
name_list = ()



def _assign(name, idx, description):
    #print(idx)
    #assert id2name[idx] == None
    #assert id2description[idx] == None
    assert name2id.get(name) == None == name2description.get(name)
    id2names[idx].add(name)
    name2description[name] = description
    name2id[name] = idx


def _split_file(fname, nline):
    ls = []
    with open(fname) as fin:
        for line in fin:
            ls.append(line[:-1])

    lines_ls = []
    for i in range(0, len(ls), nline):
        lines_ls.append(ls[i:i+nline])

    return lines_ls

def _body3():
    lines_ls = _split_file('body3.txt', 3)

    
    for t in lines_ls:
        t[1] = int(t[1], 0)
        name, idx, description = t
        _assign(name, idx, description)

def _body2():
    lines_ls = _split_file('body2.txt', 2)

    
    for t in lines_ls:
        t[0] = int(t[0], 0)
        name = 'VK_' + t[1][0]
        idx, description = t
        _assign(name, idx, description)

def _eval():
    _body3()
    _body2()
    
    global id2names, name2description, name2id, name_list
    name_list = tuple(sorted(name2id.keys()))

    
    vkname_t = collections.namedtuple('vkname_t', name_list) # frozendict???
    
    id2names = tuple(tuple(sorted(s)) for s in id2names)
    name2description = vkname_t(**name2description)
    name2id = vkname_t(**name2id)
    
def _show():
    print('name_list =', name_list)
    print('id2names =', id2names)
    print('name2description =', name2description)
    print('name2id =', name2id)

def _init():
    _eval()
    _show()

_init()
'''

'''
http://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx

Virtual-Key Codes
The following table shows the symbolic constant names, hexadecimal values, and mouse or keyboard equivalents for the virtual-key codes used by the system. The codes are listed in numeric order.
Constant/value	Description

---3
VK_LBUTTON
0x01
Left mouse button
VK_RBUTTON
0x02
Right mouse button
VK_CANCEL
0x03
Control-break processing
VK_MBUTTON
0x04
Middle mouse button (three-button mouse)
VK_XBUTTON1
0x05
X1 mouse button
VK_XBUTTON2
0x06
X2 mouse button
VK_BACK
0x08
BACKSPACE key
VK_TAB
0x09
TAB key
VK_CLEAR
0x0C
CLEAR key
VK_RETURN
0x0D
ENTER key
VK_SHIFT
0x10
SHIFT key
VK_CONTROL
0x11
CTRL key
VK_MENU
0x12
ALT key
VK_PAUSE
0x13
PAUSE key
VK_CAPITAL
0x14
CAPS LOCK key
VK_KANA
0x15
IME Kana mode
VK_HANGUEL
0x15
IME Hanguel mode (maintained for compatibility; use VK_HANGUL)
VK_HANGUL
0x15
IME Hangul mode
VK_JUNJA
0x17
IME Junja mode
VK_FINAL
0x18
IME final mode
VK_HANJA
0x19
IME Hanja mode
VK_KANJI
0x19
IME Kanji mode
VK_ESCAPE
0x1B
ESC key
VK_CONVERT
0x1C
IME convert
VK_NONCONVERT
0x1D
IME nonconvert
VK_ACCEPT
0x1E
IME accept
VK_MODECHANGE
0x1F
IME mode change request
VK_SPACE
0x20
SPACEBAR
VK_PRIOR
0x21
PAGE UP key
VK_NEXT
0x22
PAGE DOWN key
VK_END
0x23
END key
VK_HOME
0x24
HOME key
VK_LEFT
0x25
LEFT ARROW key
VK_UP
0x26
UP ARROW key
VK_RIGHT
0x27
RIGHT ARROW key
VK_DOWN
0x28
DOWN ARROW key
VK_SELECT
0x29
SELECT key
VK_PRINT
0x2A
PRINT key
VK_EXECUTE
0x2B
EXECUTE key
VK_SNAPSHOT
0x2C
PRINT SCREEN key
VK_INSERT
0x2D
INS key
VK_DELETE
0x2E
DEL key
VK_HELP
0x2F
HELP key
VK_LWIN
0x5B
Left Windows key (Natural keyboard)
VK_RWIN
0x5C
Right Windows key (Natural keyboard)
VK_APPS
0x5D
Applications key (Natural keyboard)
VK_SLEEP
0x5F
Computer Sleep key
VK_NUMPAD0
0x60
Numeric keypad 0 key
VK_NUMPAD1
0x61
Numeric keypad 1 key
VK_NUMPAD2
0x62
Numeric keypad 2 key
VK_NUMPAD3
0x63
Numeric keypad 3 key
VK_NUMPAD4
0x64
Numeric keypad 4 key
VK_NUMPAD5
0x65
Numeric keypad 5 key
VK_NUMPAD6
0x66
Numeric keypad 6 key
VK_NUMPAD7
0x67
Numeric keypad 7 key
VK_NUMPAD8
0x68
Numeric keypad 8 key
VK_NUMPAD9
0x69
Numeric keypad 9 key
VK_MULTIPLY
0x6A
Multiply key
VK_ADD
0x6B
Add key
VK_SEPARATOR
0x6C
Separator key
VK_SUBTRACT
0x6D
Subtract key
VK_DECIMAL
0x6E
Decimal key
VK_DIVIDE
0x6F
Divide key
VK_F1
0x70
F1 key
VK_F2
0x71
F2 key
VK_F3
0x72
F3 key
VK_F4
0x73
F4 key
VK_F5
0x74
F5 key
VK_F6
0x75
F6 key
VK_F7
0x76
F7 key
VK_F8
0x77
F8 key
VK_F9
0x78
F9 key
VK_F10
0x79
F10 key
VK_F11
0x7A
F11 key
VK_F12
0x7B
F12 key
VK_F13
0x7C
F13 key
VK_F14
0x7D
F14 key
VK_F15
0x7E
F15 key
VK_F16
0x7F
F16 key
VK_F17
0x80
F17 key
VK_F18
0x81
F18 key
VK_F19
0x82
F19 key
VK_F20
0x83
F20 key
VK_F21
0x84
F21 key
VK_F22
0x85
F22 key
VK_F23
0x86
F23 key
VK_F24
0x87
F24 key
VK_NUMLOCK
0x90
NUM LOCK key
VK_SCROLL
0x91
SCROLL LOCK key
VK_LSHIFT
0xA0
Left SHIFT key
VK_RSHIFT
0xA1
Right SHIFT key
VK_LCONTROL
0xA2
Left CONTROL key
VK_RCONTROL
0xA3
Right CONTROL key
VK_LMENU
0xA4
Left MENU key
VK_RMENU
0xA5
Right MENU key
VK_BROWSER_BACK
0xA6
Browser Back key
VK_BROWSER_FORWARD
0xA7
Browser Forward key
VK_BROWSER_REFRESH
0xA8
Browser Refresh key
VK_BROWSER_STOP
0xA9
Browser Stop key
VK_BROWSER_SEARCH
0xAA
Browser Search key
VK_BROWSER_FAVORITES
0xAB
Browser Favorites key
VK_BROWSER_HOME
0xAC
Browser Start and Home key
VK_VOLUME_MUTE
0xAD
Volume Mute key
VK_VOLUME_DOWN
0xAE
Volume Down key
VK_VOLUME_UP
0xAF
Volume Up key
VK_MEDIA_NEXT_TRACK
0xB0
Next Track key
VK_MEDIA_PREV_TRACK
0xB1
Previous Track key
VK_MEDIA_STOP
0xB2
Stop Media key
VK_MEDIA_PLAY_PAUSE
0xB3
Play/Pause Media key
VK_LAUNCH_MAIL
0xB4
Start Mail key
VK_LAUNCH_MEDIA_SELECT
0xB5
Select Media key
VK_LAUNCH_APP1
0xB6
Start Application 1 key
VK_LAUNCH_APP2
0xB7
Start Application 2 key
VK_OEM_1
0xBA
Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the ';:' key
VK_OEM_PLUS
0xBB
For any country/region, the '+' key
VK_OEM_COMMA
0xBC
For any country/region, the ',' key
VK_OEM_MINUS
0xBD
For any country/region, the '-' key
VK_OEM_PERIOD
0xBE
For any country/region, the '.' key
VK_OEM_2
0xBF
Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the '/?' key
VK_OEM_3
0xC0
Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the '`~' key
VK_OEM_4
0xDB
Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the '[{' key
VK_OEM_5
0xDC
Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the '\|' key
VK_OEM_6
0xDD
Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the ']}' key
VK_OEM_7
0xDE
Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the 'single-quote/double-quote' key
VK_OEM_8
0xDF
Used for miscellaneous characters; it can vary by keyboard.
VK_OEM_102
0xE2
Either the angle bracket key or the backslash key on the RT 102-key keyboard
VK_PROCESSKEY
0xE5
IME PROCESS key
VK_PACKET
0xE7
Used to pass Unicode characters as if they were keystrokes. The VK_PACKET key is the low word of a 32-bit Virtual Key value used for non-keyboard input methods. For more information, see Remark in KEYBDINPUT, SendInput, WM_KEYDOWN, and WM_KEYUP
VK_ATTN
0xF6
Attn key
VK_CRSEL
0xF7
CrSel key
VK_EXSEL
0xF8
ExSel key
VK_EREOF
0xF9
Erase EOF key
VK_PLAY
0xFA
Play key
VK_ZOOM
0xFB
Zoom key
VK_PA1
0xFD
PA1 key
VK_OEM_CLEAR
0xFE
Clear key


----2
0x30
0 key
0x31
1 key
0x32
2 key
0x33
3 key
0x34
4 key
0x35
5 key
0x36
6 key
0x37
7 key
0x38
8 key
0x39
9 key
0x41
A key
0x42
B key
0x43
C key
0x44
D key
0x45
E key
0x46
F key
0x47
G key
0x48
H key
0x49
I key
0x4A
J key
0x4B
K key
0x4C
L key
0x4D
M key
0x4E
N key
0x4F
O key
0x50
P key
0x51
Q key
0x52
R key
0x53
S key
0x54
T key
0x55
U key
0x56
V key
0x57
W key
0x58
X key
0x59
Y key
0x5A
Z key


-----others
-
0x07
Undefined
-
0x0A-0B
Reserved
-
0x0E-0F
Undefined
-
0x16
Undefined
-
0x1A
Undefined
-
0x3A-40
Undefined
-
0x5E
Reserved
-
0x88-8F
Unassigned
0x92-96
OEM specific
-
0x97-9F
Unassigned
-
0xB8-B9
Reserved
-
0xC1-D7
Reserved
-
0xD8-DA
Unassigned
-
0xE0
Reserved
0xE1
OEM specific
0xE3-E4
OEM specific
0xE6
OEM specific
-
0xE8
Unassigned
0xE9-F5
OEM specific
VK_NONAME
0xFC
Reserved
'''
