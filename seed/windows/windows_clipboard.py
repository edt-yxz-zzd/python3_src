
__all__ = '''
    maybe_get_Windows_clipboard
    clear_Windows_clipboard
    set_Windows_clipboard
    maybe_set_Windows_clipboard
    '''.split()

import ctypes
from ctypes import sizeof, create_unicode_buffer, c_wchar_p

CF_UNICODETEXT = 13
GMEM_MOVEABLE=0x0002
windows_wchar_encoding = 'utf_16_le'

OpenClipboard = ctypes.cdll.user32.OpenClipboard
CloseClipboard = ctypes.cdll.user32.CloseClipboard
GetClipboardData = ctypes.cdll.user32.GetClipboardData
EmptyClipboard = ctypes.cdll.user32.EmptyClipboard
SetClipboardData = ctypes.cdll.user32.SetClipboardData

GlobalLock = ctypes.cdll.kernel32.GlobalLock
GlobalUnlock = ctypes.cdll.kernel32.GlobalUnlock
GlobalAlloc = ctypes.cdll.kernel32.GlobalAlloc
GlobalFree = ctypes.cdll.kernel32.GlobalFree


#should not use:
#   strncpy = ctypes.cdll.msvcrt.strncpy
#not found:
#   wmemcpy = ctypes.cdll.msvcrt.wmemcpy
memcpy = ctypes.cdll.msvcrt.memcpy

del ctypes

def verify_text(s):
    return type(s) is str and '\0' not in s
def check_text(s):
    if type(s) is not str: raise TypeError
    if '\0' in s: raise ValueError
    return

def maybe_get_Windows_clipboard():
    # -> (None|str)
    if not OpenClipboard(0): raise Exception
    try:
        hMem = GetClipboardData(CF_UNICODETEXT)
        if not hMem: return None
        try:
            pointer = GlobalLock(hMem)
            if not pointer: raise Exception
            try:
                buffer_ptr = c_wchar_p(pointer)     # copy...??
                if not buffer_ptr: raise Exception
                text = buffer_ptr.value             # copy...??
            finally:
                GlobalUnlock(hMem)
        finally:
            # bug:GlobalFree(hMem)
            pass
    finally:
        CloseClipboard()
    #text = wdata.decode('utf_16_le')
    check_text(text)
    return text

def maybe_set_Windows_clipboard(maybe_text):
    if maybe_text is None:
        clear_Windows_clipboard()
    else:
        text = maybe_text
        set_Windows_clipboard(text)
    return
def clear_Windows_clipboard():
    if not OpenClipboard(0): raise Exception
    try:
        if not EmptyClipboard(): raise Exception
    finally:
        CloseClipboard()
def set_Windows_clipboard(text):
    check_text(text)
    #text += '\U00101F1F' # used to let "len(wdata) > len(text)+1"
    #
    #bug: one python.char ==>> one or two c.wchar
    #   wdata = create_unicode_buffer(text, len(text)+1)
    #   assert wdata[len(text)] == '\0'
    #
    wdata = create_unicode_buffer(text+'\0')
    assert wdata[-1] == '\0'
    assert len(wdata) >= len(text)+1
    num_bytes = sizeof(wdata)
    #bug?: assert num_bytes == 2*len(wdata)
    #   windows.wchar == 2*byte??
    #print(f'wdata.value={wdata.value!r}')

    if not OpenClipboard(0): raise Exception
    try:
        if not EmptyClipboard(): raise Exception

        hMem = GlobalAlloc(GMEM_MOVEABLE, num_bytes)
        if not hMem: raise Exception
        try:
            buffer_ptr = c_wchar_p(GlobalLock(hMem))
            if not buffer_ptr: raise Exception
            try:
                # bug: strncpy at most n, will trunc if '\0'
                #   strncpy(buffer_ptr, wdata, num_bytes)
                # no wmemcpy??
                #   wmemcpy(buffer_ptr, wdata, len(wdata))
                memcpy(buffer_ptr, wdata, num_bytes)
                    # memcpy returns buffer_ptr
                    #   must success
            finally:
                GlobalUnlock(hMem)
            #print(f'buffer_ptr.value={buffer_ptr.value!r}')
        except:# BaseException:
            GlobalFree(hMem)
            raise
        if not SetClipboardData(CF_UNICODETEXT, hMem): raise Exception
    finally:
        CloseClipboard()



#############################
def main():
    import sys
    def print_sep():
        print()
        print('='*70)
        print()
    def read_and_show():
        may_text = maybe_get_Windows_clipboard()
        print(f'\tread clipboard: maybe_text={may_text!r}')
        print_sep()

    # maybe_get_Windows_clipboard
    print('maybe_get_Windows_clipboard:')
    read_and_show()

    # clear_Windows_clipboard
    print('clear_Windows_clipboard:')
    clear_Windows_clipboard()
    read_and_show()

    # set_Windows_clipboard
    print('set_Windows_clipboard:')
    #
    #set_Windows_clipboard(str(sys.argv)+'-\n1\n\r2\r3\r\n4\0abc')
    #   \0 will be truncated
    text = str(sys.argv)+'-\n1\n\r2\r3\r\n4\U00101F1F一了'
    print(f'\tset_Windows_clipboard({text!r})')
    set_Windows_clipboard(text)
    read_and_show()

if __name__ == "__main__":
    main()

