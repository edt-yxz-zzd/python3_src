


from PIL import Image, ImageTk

import collections, itertools, ast
import tkinter as tk
import tkinter.font as tkfont
#import tkinter.constants as cs
import tkinter.messagebox as tk_msgbox
import tkinter.simpledialog as tk_ask
import tkinter.filedialog as tk_fdlg
from tkinter.scrolledtext import ScrolledText as tk_ScrolledText

import os, os.path
import sys
from traceback import print_exc
import shlex # quote was using \' which doesnot work on Windows!!
import subprocess



r'''
images should be hold by myself, otherwise it would be deleted and show nothing.

when I update the showing object, I completely deleted them, and rebind.
so the 'drag' operation just failed.

should keep in mind: history/configure; filesystem changing.


pack/hold-img-myself/
bind/focus_set/wm_protocol/
config/keys/cget/
winfo_screenwidth/winfo_toplevel/wm_geometry/winfo_y/winfo_height
Canvas:
    canvasy/find_closest/coords/["scrollregion"]
    yview_moveto/yview_scroll/yview/bbox/find_all/coords



slow where too many images under a folder: fixed by 'dynamic load when idle'
using up memory if too many images and enlarge them: fixed by 'load when show'


'''
xbase_path2 = r'E:\multimedia\picture\beauty\wallpaper'
xbase_path = r'E:\multimedia\picture\something'
#base_path = r'E:\multimedia\picture\funny'




##print(shlex.split(r' " \" \""', False, False))
##print(shlex.split(r' " \" \""', False, True))
##raise
##
##print(shlex.split(shlex.quote('a b'), False, False))
##raise
def shell_quote(s):
    r = '"{!s}"'.format(s.replace('"', r'\"'))
    return r

##base_path = os.path.abspath(base_path)
##paths = [base_path]

#Frame Label LabelFrame PanedWindow

def ls_all(path):
    assert os.path.isdir(path)
    
    fnames = os.listdir(path)
    files = []
    dirs = []
    for fname in fnames:
        fpath = os.path.abspath(os.path.join(path, fname))
        if os.path.isdir(fpath):
            dirs.append(fpath)
        else:
            files.append(fpath)
    dirs.sort()
    files.sort()
    return dirs, files


def get_entries(paths, is_close):
    fnames = []
    depths = []
    _get_entries(fnames, depths, paths, depth=0, is_close=is_close)
    assert len(fnames) == len(depths)
    return fnames, depths

def _get_entries(output_fnames, output_depths, paths, depth, is_close):
    assert 0 <= depth < len(paths)
    assert len(output_fnames) == len(output_depths)
    
    dirs, files = ls_all(paths[depth])
    if depth + 1 == len(paths):
        output_fnames.extend(dirs)
        if not is_close:
            output_fnames.extend(files) # only last layer, show its files
        output_depths += [depth] * (len(output_fnames) - len(output_depths))
        
    else:
        next_path = paths[depth+1]
        assert os.path.isdir(next_path)
        try:
            i = dirs.index(next_path) # fix me : what if deleted while processing ?
        except Exception as e:
            print(type(e), e, file=sys.stderr)
            print(paths, next_path)
            raise
        output_fnames.extend(dirs[:i+1])
        output_depths += [depth] * (len(output_fnames) - len(output_depths))
        
        _get_entries(output_fnames, output_depths, paths, depth+1, is_close)
        output_fnames.extend(dirs[i+1:])
        # no: output.extend(files)
        output_depths += [depth] * (len(output_fnames) - len(output_depths))
    return


class _CountImageTkPhotoImage(ImageTk.PhotoImage):
    count = 0
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _CountImageTkPhotoImage.count += 1
        print('count id', id(self.count))
        print('after open:', self.count)
    def __del__(self):
        super().__del__()
        _CountImageTkPhotoImage.count -= 1
        print('after close:', self.count)

# no problem with PIL;
# it was caused by enlarge too many picture at one time.
_CountImageTkPhotoImage = ImageTk.PhotoImage


def calc_new_size(size, new_width):
    # new_width may be float
    width, height = size
    scale =  new_width / float(width)
    new_fheight = height * scale
    new_size = int(new_width), int(new_fheight)
    return new_size

def get_img_size(fname):
    try:
        with Image.open(fname) as img:
            return img.size
    except IOError as e:
        #print(type(e), e, file=sys.stderr)
        return None
    
    pass
    
def open_tk_img(fname, new_width = None):
    with Image.open(fname) as img:
        if new_width is not None:
            new_size = calc_new_size(img.size, new_width)
            img = img.resize(new_size)
        tk_img = _CountImageTkPhotoImage(img)
    return tk_img

def try_open_tk_img(path, new_width = None):
    try:
        tk_img = open_tk_img(path, new_width)
    except IOError as e:
        #print(type(e), e, file=sys.stderr)
        return None
    return tk_img



    
    
def make_entries(selected_path, paths):
    assert os.path.isdir(selected_path)
    
    is_close = (selected_path in paths)
    if is_close:
        i = paths.index(selected_path)
        del paths[i:]
        assert selected_path not in paths
    else:
        parent = os.path.abspath(os.path.dirname(selected_path))
        assert len(parent) < len(selected_path)
        dirs, _ = ls_all(parent)
        assert selected_path in dirs
        
        i = paths.index(parent)
        assert parent == paths[i]
        del paths[i+1:]
        assert parent == paths[-1]
        
        paths.append(selected_path)

    fnames, depths = get_entries(paths, is_close=False) # never close
    return fnames, depths



'''
<Destroy>
print(dir(cs))

        # serial field: valid vor all events
        # number of button: ButtonPress and ButtonRelease events only
        # height field: Configure, ConfigureRequest, Create,
        # ResizeRequest, and Expose events only
        # keycode field: KeyPress and KeyRelease events only
        # time field: "valid for events that contain a time field"
        # width field: Configure, ConfigureRequest, Create, ResizeRequest,
        # and Expose events only
        # x field: "valid for events that contain a x field"
        # y field: "valid for events that contain a y field"
        # keysym as decimal: KeyPress and KeyRelease events only
        # x_root, y_root fields: ButtonPress, ButtonRelease, KeyPress,
        # KeyRelease,and Motion events
        
class Event:
    """Container for the properties of an event.

    Instances of this type are generated if one of the following events occurs:

    KeyPress, KeyRelease - for keyboard events
    ButtonPress, ButtonRelease, Motion, Enter, Leave, MouseWheel - for mouse events
    Visibility, Unmap, Map, Expose, FocusIn, FocusOut, Circulate,
    Colormap, Gravity, Reparent, Property, Destroy, Activate,
    Deactivate - for window events.

    If a callback function for one of these events is registered
    using bind, bind_all, bind_class, or tag_bind, the callback is
    called with an Event as first argument. It will have the
    following attributes (in braces are the event types for which
    the attribute is valid):

        serial - serial number of event
    num - mouse button pressed (ButtonPress, ButtonRelease)
    focus - whether the window has the focus (Enter, Leave)
    height - height of the exposed window (Configure, Expose)
    width - width of the exposed window (Configure, Expose)
    keycode - keycode of the pressed key (KeyPress, KeyRelease)
    state - state of the event as a number (ButtonPress, ButtonRelease,
                            Enter, KeyPress, KeyRelease,
                            Leave, Motion)
    state - state as a string (Visibility)
    time - when the event occurred
    x - x-position of the mouse
    y - y-position of the mouse
    x_root - x-position of the mouse on the screen
             (ButtonPress, ButtonRelease, KeyPress, KeyRelease, Motion)
    y_root - y-position of the mouse on the screen
             (ButtonPress, ButtonRelease, KeyPress, KeyRelease, Motion)
    char - pressed character (KeyPress, KeyRelease)
    send_event - see X/Windows documentation
    keysym - keysym of the event as a string (KeyPress, KeyRelease)
    keysym_num - keysym of the event as a number (KeyPress, KeyRelease)
    type - type of the event as a number
    widget - widget in which the event occurred
    delta - delta of wheel movement (MouseWheel)
    """



    def bind(self, sequence=None, func=None, add=None):
        """Bind to this widget at event SEQUENCE a call to function FUNC.

        SEQUENCE is a string of concatenated event
        patterns. An event pattern is of the form
        <MODIFIER-MODIFIER-TYPE-DETAIL> where MODIFIER is one
        of Control, Mod2, M2, Shift, Mod3, M3, Lock, Mod4, M4,
        Button1, B1, Mod5, M5 Button2, B2, Meta, M, Button3,
        B3, Alt, Button4, B4, Double, Button5, B5 Triple,
        Mod1, M1. TYPE is one of Activate, Enter, Map,
        ButtonPress, Button, Expose, Motion, ButtonRelease
        FocusIn, MouseWheel, Circulate, FocusOut, Property,
        Colormap, Gravity Reparent, Configure, KeyPress, Key,
        Unmap, Deactivate, KeyRelease Visibility, Destroy,
        Leave and DETAIL is the button number for ButtonPress,
        ButtonRelease and DETAIL is the Keysym for KeyPress and
        KeyRelease. Examples are
        <Control-Button-1> for pressing Control and mouse button 1 or
        <Alt-A> for pressing A and the Alt key (KeyPress can be omitted).
        An event pattern can also be a virtual event of the form
        <<AString>> where AString can be arbitrary. This
        event can be generated by event_generate.
        If events are concatenated they must appear shortly
        after each other.

        FUNC will be called if the event sequence occurs with an
        instance of Event as argument. If the return value of FUNC is
        "break" no further bound function is invoked.

        An additional boolean parameter ADD specifies whether FUNC will
        be called additionally to the other bound function or whether
        it will replace the previous function.

        Bind will return an identifier to allow deletion of the bound function with
        unbind without memory leak.

        If FUNC or SEQUENCE is omitted the bound function or list
        of bound events are returned."""


        return self._bind(('bind', self._w), sequence, func, add)
    def unbind(self, sequence, funcid=None):
        """Unbind for this widget for event SEQUENCE  the
        function identified with FUNCID."""
        self.tk.call('bind', self._w, sequence, '')
        if funcid:
            self.deletecommand(funcid)
    def bind_all(self, sequence=None, func=None, add=None):
        """Bind to all widgets at an event SEQUENCE a call to function FUNC.
        An additional boolean parameter ADD specifies whether FUNC will
        be called additionally to the other bound function or whether
        it will replace the previous function. See bind for the return value."""
        return self._bind(('bind', 'all'), sequence, func, add, 0)
    def unbind_all(self, sequence):
        """Unbind for all widgets for event SEQUENCE all functions."""
        self.tk.call('bind', 'all' , sequence, '')
    def bind_class(self, className, sequence=None, func=None, add=None):

        """Bind to widgets with bindtag CLASSNAME at event
        SEQUENCE a call of function FUNC. An additional
        boolean parameter ADD specifies whether FUNC will be
        called additionally to the other bound function or
        whether it will replace the previous function. See bind for
        the return value."""

        return self._bind(('bind', className), sequence, func, add, 0)
    def unbind_class(self, className, sequence):
        """Unbind for a all widgets with bindtag CLASSNAME for event SEQUENCE
        all functions."""






    def event_add(self, virtual, *sequences):
        """Bind a virtual event VIRTUAL (of the form <<Name>>)
        to an event SEQUENCE such that the virtual event is triggered
        whenever SEQUENCE occurs."""

    def event_delete(self, virtual, *sequences):
        """Unbind a virtual event VIRTUAL from SEQUENCE."""
        
    def event_generate(self, sequence, **kw):
        """Generate an event SEQUENCE. Additional
        keyword arguments specify parameter of the event
        (e.g. x, y, rootx, rooty)."""
        
'''




'''

    def configure(self, cnf=None, **kw):
        """Configure resources of a widget.

        The values for resources are specified as keyword
        arguments. To get an overview about
        the allowed keyword arguments call the method keys.
        """
    config = configure
    def cget(self, key):
        """Return the resource value for a KEY given as string."""
    def keys(self):
        """Return a list of all resource names of this widget."""
'''


'''

    def after_idle(self, func, *args):
        """Call FUNC once if the Tcl main loop has no event to
        process.

        Return an identifier to cancel the scheduling with
        after_cancel."""
        
    def after_cancel(self, id):
        """Cancel scheduling of function identified with ID.

        Identifier returned by after or after_idle must be
        given as first parameter."""
        
'''



class Msgbox(tk_ask.Dialog):
    def __init__(self, msg, parent, title = None, **subwidget_options):
        self.__msg = msg
        self.__subwidget_options = subwidget_options
        
        super().__init__(parent, title)

    def get_subwidget_options(self):
        return self.__subwidget_options
    def get_message(self):
        return self.__msg
    def buttonbox(self):
        box = tk.Frame(self)
        w = tk.Button(box, text="BACK", width=10, command=self.cancel, default=tk.ACTIVE)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w.focus_set()
        self.bind("<Return>", self.cancel)
        self.bind("<Escape>", self.cancel)
        self.bind("<space>", self.cancel)
        box.pack()
        

        
    def body(self, master):
        label = tk.Label(master, text = self.get_message(),
                         **self.get_subwidget_options())
        #print((sorted(label.config().keys())))
        label.pack()
        return label
        
class ScrolledTextDialog(Msgbox):
    def __init__(self, text, parent, title = None, **text_kw):
        super().__init__(text, parent, title)
        
    def body(self, master):
        stext = tk_ScrolledText(master, **self.get_subwidget_options())
        stext.insert(tk.END, self.get_message())
        stext.pack()
        return stext



class BaseConfigDialog(tk_ask.Dialog):
    def __init__(self, parent, title = None):
        self.__output = None
        super().__init__(parent, title)

    def get_result(self):
        return self.__output

    def set_result(self, result):
        self.__output = result

    def __error(self, msg, title='error'):
        tk_msgbox.showerror('error', msg, parent=self)

    def __except(self, e):
        msg = '{} : {}'.format(type(e), e)
        #print(msg, file=sys.stderr)
        print_exc(file=sys.stderr)
        self.__error(msg, 'except')
        
    def validate(self):
        try:
            msg = self._validate()
        except BaseException as e:
            self.__except(e)
            return False

        
        
        if msg is None:
            return True
        self.__error(msg)
        return False
    
    def apply(self):
        try:
            self._apply()
        except BaseException as e:
            self.__except(e)
            pass
        return

    def _validate(self):
        raise NotImplementedError()
        return True
    
    def _apply(self):
        raise NotImplementedError()
    


class OthersConfigDialog(BaseConfigDialog):
    def __init__(self, wheel_rate, auto_move_dt, auto_move_dy,
                 picture_width, num_tmp_images, 
                 parent, title = None):
        self.__args = wheel_rate, auto_move_dt, auto_move_dy, \
                      picture_width, num_tmp_images

        # at last : run...
        super().__init__(parent, title)
        
    def body(self, master):
        texts = ['wheel_rate: ', 'auto_move_dt (ms): ', 'auto_move_dy (pix): ',
                 'picture_width (pix): ', 'num_tmp_images: ']
        initials = self.__args

        w = EntriesFrame(texts, initials, master)
        w.pack(side=tk.TOP,padx=5,pady=5,expand=tk.TRUE,fill=tk.BOTH)
        self.__w = w
        return w



    def _validate(self):
        msg = self.__calc()
        if isinstance(msg, str):
            return msg
        return None
    
    def __calc(self):
        w = self.__w
        values = w.get_entry_values()
        rate, dt, dy, width, num = values
        try:
            msg = 'wheel_rate should be a positive real number'
            wheel_rate = float(rate.get())
            if wheel_rate <= 0:
                raise ValueError()
            
            msg = 'auto_move_dt (ms) should be a positive integer'
            auto_move_dt = int(dt.get())
            if auto_move_dt <= 0:
                raise ValueError()
            
            msg = 'auto_move_dy (pix) should be a integer'
            auto_move_dy = int(dy.get())
            
            msg = 'picture_width (pix) should be a positive integer'
            picture_width = int(width.get())
            if picture_width <= 0:
                raise ValueError()
            
            msg = 'num_tmp_images should be a nonnegative integer'
            num_tmp_images = int(num.get())
            if num_tmp_images < 0:
                raise ValueError()
        except ValueError:
            return msg
        
        return wheel_rate, auto_move_dt, auto_move_dy, \
               picture_width, num_tmp_images

    def _apply(self):
        r = self.__calc()
        if isinstance(r, tuple):
            self.set_result(r)
            return
        raise ValueError('logic error??')

        
class EntriesFrame(tk.Frame):
    def __init__(self, texts, initials, *args, **kwargs):
        super().__init__(*args, **kwargs)

        main_frame = self
        self.__texts = texts = tuple(texts)
        self.__values = values = [tk.StringVar(main_frame, v) for v in initials]
        L = len(texts)
        if len(texts) != len(values):
            raise ValueError('len(texts) != len(initials)')
        
        for i, (text, value) in enumerate(zip(texts, values)):
            label = tk.Label(main_frame, text = text)
            label.grid(row = i, column = 0, sticky='e')
            entry = tk.Entry(main_frame, textvariable = value)
            entry.grid(row = i, column = 1)
            
    def get_entry_values(self):
        return self.__values
    def get_label_texts(self):
        return self.__texts
    
    
class FontConfigDialog(BaseConfigDialog):
    def __init__(self, font_name, size, is_bold, font_families,
                 parent, title = None, **font_kw):
        self.__font = font_name, size, is_bold, font_families
        self.__font_kw = font_kw
        self.__w = None

        # at last : run...
        super().__init__(parent, title)
        
    def body(self, master):
        w = FontFrame(*self.__font, parent=master, **self.__font_kw)
        w.pack(side=tk.TOP,padx=5,pady=5,expand=tk.TRUE,fill=tk.BOTH)
        self.__w = w
        return w

    
    
    def _validate(self):
        w = self.__w
        try:
            size = w.size.get()
            if size <= 0:
                raise ValueError()
        except ValueError:
            return 'size should be a positive integer'
        
        return None

    def _apply(self):
        w = self.__w
        size = w.size.get()
        is_bold = w.is_bold.get()
        font_name = w.font_name.get()
        output = (font_name, size, is_bold)
        self.set_result(output)
        
    
class FontFrame(tk.LabelFrame):
    def __init__(self, font_name, size, is_bold, font_families, parent = None):
        super().__init__(parent, borderwidth=2, text=' Font Families ')
        #main_frame = tk.LabelFrame(parent, borderwidth=2, text=' Font Families ')
        main_frame = self

        self.is_bold = tk.BooleanVar(self, is_bold)
        self.size = tk.IntVar(self, size)
        self.font_name = tk.StringVar(self, font_name)
        
        font_name_frame = tk.Frame(main_frame)
        list_font_names = tk.Listbox(font_name_frame, height=25)
        list_font_names.bind('<ButtonRelease-1>',self.OnListFontButtonRelease)
        
        font_scroll = tk.Scrollbar(font_name_frame)
        font_scroll.config(command=list_font_names.yview)
        list_font_names.config(yscrollcommand=font_scroll.set)


        font_args_frame = tk.Frame(main_frame)
        font_size_title = tk.Label(font_args_frame, text='Size :')

        # invalidcommand, textvariable, validate, validatecommand width
        # validate : all, key, focus, focusin, focusout, or none
        font_size_box = tk.Entry(font_args_frame, width = 5, textvariable = self.size)
        font_bold_flag = tk.Checkbutton(font_args_frame, variable=self.is_bold,
            onvalue=True, offvalue=False, text='Bold')


        
        #widget packing
        #main_frame.pack(side=LEFT,padx=5,pady=5,expand=TRUE,fill=BOTH)
        #frameFont
        TOP = tk.TOP
        X = tk.X
        Y = tk.Y
        LEFT = tk.LEFT
        TRUE = tk.TRUE
        W = tk.W
        
        font_name_frame.pack(side=TOP,padx=5,pady=5,fill=X)
        list_font_names.pack(side=LEFT,expand=TRUE,fill=X)
        font_scroll.pack(side=LEFT,fill=Y)
        
        font_args_frame.pack(side=TOP,padx=5,pady=5,fill=X)
        font_size_title.pack(side=LEFT,anchor=W)
        font_size_box.pack(side=LEFT,anchor=W)
        font_bold_flag.pack(side=LEFT,anchor=W,padx=20)


        # set
        self.is_bold.set(is_bold)
        for name in font_families:
            list_font_names.insert(tk.END, name)
        
        if font_name in font_families:
            idx = font_families.index(font_name)
            list_font_names.see(idx)
            list_font_names.select_set(idx)
            list_font_names.select_anchor(idx)
        
    def OnListFontButtonRelease(self, event):
        list_font_names = event.widget
        font_name = list_font_names.get(tk.ANCHOR)
        self.font_name.set(font_name)


                
class KeyPressHandlerMixin:
    def __init__(self, auto_move_dt=1000, auto_move_dy=100):
        self.__auto_move_id = None
        self.__auto_move_flag = False
        self.set_auto_move_dtdy((auto_move_dt, auto_move_dy))

    def get_auto_move_dtdy(self):
        return self.__auto_move_dt, self.__auto_move_dy
    def set_auto_move_dtdy(self, dtdy):
        dt, dy = dtdy
        if not isinstance(dt, int) or dt <= 0:
            raise ValueError('not isinstance(auto_move_dt, int) or auto_move_dt <= 0')
        if not isinstance(dy, int):
            raise ValueError('not isinstance(auto_move_dy, int)')
        self.__auto_move_dt, self.__auto_move_dy = dtdy
        
    def bind_keys(self):
        self.bind('<KeyPress-space>', self.page_down, '+')
        self.bind('<KeyPress-Next>', self.page_down, '+') # PgDn
        self.bind('<KeyPress-Down>', self.page_down, '+')
        self.bind('<KeyPress-Prior>', self.page_up, '+') # PgUp
        self.bind('<KeyPress-Up>', self.page_up, '+')

        
        self.bind('<KeyPress-Left>', self.page_left, '+')
        self.bind('<KeyPress-Right>', self.page_right, '+')
        
        self.bind('<KeyPress-BackSpace>', self.close_curr_dir, '+')
        
        #self.bind('<KeyPress-w>', self.config_picture_width, '+')
        self.bind('<KeyPress-o>', self.config_base_path, '+')
        self.bind('<KeyPress-h>', self.show_help, '+')
        self.bind('<KeyPress-F1>', self.show_help, '+')
        self.bind('<KeyPress-f>', self.config_font, '+')
        self.bind('<KeyPress-a>', self.auto_move, '+')
        #self.bind('<KeyPress-m>', self.config_auto_move_dtdy, '+')
        self.bind('<KeyPress-g>', self.config_general, '+')
        self.bind('<KeyPress-c>', self.show_options, '+')


        return
        # to find out the key name
        self.bind('<KeyPress>', self.onKeyPress, '+')

        
        self.bind('<ButtonPress-1>', self.page_down, '+')
        self.bind('<Configure>', self.bind_config, '+')
        _root = self._root()
        _root = self.winfo_toplevel()
        print(_root.wm_protocol('WM_DELETE_WINDOW'))
        self.bind('<Configure>', self.bind_config, '+')
        self.bind('<Visibility>', self.bind_config, '+')


        
    def bind_config(self, event):
        print(event.__dict__)

    def onKeyPress(self, event):
        print(event.__dict__)
        
    def page_down(self, event=None):
        self.cv.yview_scroll(1, 'page')
    def page_up(self, event=None):
        self.cv.yview_scroll(-1, 'page')
    def page_left(self, event=None):
        self.cv.xview_scroll(-1, 'page')
    def page_right(self, event=None):
        self.cv.xview_scroll(1, 'page')


    def config_general(self, event=None):
        dt, dy = self.get_auto_move_dtdy()
        rate = self.get_wheel_rate()
        width = self.get_picture_width()
        numtmp = self.get_num_tmp_images()
        d = OthersConfigDialog(rate, dt, dy, width, numtmp,
                               self, 'general config')
        output = d.get_result()
        if output is not None:
            #print('ok', output)
            wheel_rate, auto_move_dt, auto_move_dy, \
                        picture_width, num_tmp_images = output
            self.set_auto_move_dtdy((auto_move_dt, auto_move_dy))
            self.set_wheel_rate(wheel_rate)
            self.set_picture_width(picture_width)
            self.set_num_tmp_images(num_tmp_images)
            self._update_title()
        else:
            #print('cancel')
            pass
            
        self.focus_set()
        #raise NotImplementedError()
    
            


    def config_base_path(self, event = None):
        base_dir = tk_fdlg.askdirectory(parent=self,
                                        title='select top-most directory',
                                        initialdir = self._get_base_path(),
                                        mustexist=1)
        
        self.focus_set()

        # return '' if cancel, not None!!
        # print('base_dir: {!r}'.format(base_dir))
        if base_dir is None or base_dir == '':
            # cancel
            pass
        else:
            self._set_base_path_and_draw(base_dir)
            self.focus_set()
        
        
    def show_help(self, event=None):
        #tk_msgbox.showinfo('help', self.HELP, parent=self)
        Msgbox(self.HELP, parent=self, title='help', justify=tk.LEFT, width=70, wraplength=0)
        #raise NotImplementedError()
        self.focus_set()

    def show_options(self, event=None):
        msg = self.get_cmd_options()
        title = 'command line options for current configure'
        d = ScrolledTextDialog(msg, self, title)
        
    def config_font(self, event=None):
        families = tkfont_families(self)
        #msg = '\n'.join(families)
        #title = 'all available font families'
        #d = ScrolledTextDialog(msg, self, title, font=self.font)
        #print(self.font.actual())
        d = FontConfigDialog(*font2args(self.font),
                         font_families = families,
                         parent = self,
                         title = 'font config')
        
        output = d.get_result()
        if output is not None:
            #print('ok', output)
            font_name, size, is_bold = output
            self.font = args2font(font_name, size, is_bold)
            self._update_title()
        else:
            #print('cancel')
            pass
            
        self.focus_set()
    
    def close_curr_dir(self, event=None):
        paths = self.paths
        if len(paths) == 1:
            return
        clicked_path = paths[-1]
        self.redraw_cv(clicked_path)
        
    def auto_move(self, event=None):
        self.__auto_move_flag = not self.__auto_move_flag
        self.__auto_move()
        
    def __auto_move_cancel(self):
        if self.__auto_move_id is not None:
            self.after_cancel(self.__auto_move_id)
            self.__auto_move_id = None


    def __auto_move(self):
        self.__auto_move_cancel()
        if not self.__auto_move_flag:
            return
        
        self.__auto_move_id = self.after(self.__auto_move_dt, self.__auto_move)

        dx, dy = 0, -self.__auto_move_dy
        self._move_cv_view(dx, dy)
        
class IdleHandlerMixin:
    def __init__(self):
        self.__idle_iter = None
        self.__idle_id = None
        
    def _register_idle_func(self, idle_iter):
        self._cancel_idle_func()
        
        self.__idle_id = self.after_idle(self.__at_idle)
        self.__idle_iter = idle_iter

    def _register_idle_func_after(self, idle_iter, after=2000):
        self.__cancel_idle_func()
        
        self.__idle_id = self.after(after, self.__at_idle)
        self.__idle_iter = idle_iter
        
    def _cancel_idle_func(self):
        if self.__idle_id is not None:
            self.after_cancel(self.__idle_id)
            self.__idle_iter = None
            self.__idle_id = None
            
    def __at_idle(self):
        #print('__at_idle')
        idle_iter = self.__idle_iter
        if idle_iter is not None:
            for _ in idle_iter:
                # it just run once ! we should continue to register it
                self._register_idle_func(idle_iter)
                # self._register_idle_func_after(idle_func)
                #print('__at_idle exit')
                return
            else:
                # cancel
                self._cancel_idle_func()
                #print('__at_idle cancel and exit')
        return
    


class ButtonHandlerMixin:
    def __init__(self, wheel_rate = 1.0):
        
        self.__dragging = False
        self.__old_xy_for_drag = None
        self.set_wheel_rate(wheel_rate)
    def get_wheel_rate(self):
        return self.__wheel_rate
    def set_wheel_rate(self, wheel_rate):
        if wheel_rate <= 0:
            raise ValueError('wheel_rate <= 0')
        self.__wheel_rate = wheel_rate
        
        
    

    def __img_click_zoomin2(self, event):
        self.__img_click_zoom(event, 2)
    def __img_click_zoomout2(self, event):
        self.__img_click_zoom(event, 0.5)
    def __img_click_zoom(self, event, scale):
        cv = self.cv
        
        #tag = self._get_cv_tag_from_eventxy(event)
        tag = self.__get_img_tag(event)
        if tag is None:
            return
        
        idx, data = self.get_cvtag_idx_data(tag)
        assert data.tag == tag

        old_width, old_height = old_size = data.width, data.height
        new_width = old_width * scale
        assert new_width >= 0
        if new_width == 0:
            new_width = 1
            
        new_size = calc_new_size(old_size, new_width)
        new_width, new_height = data.width, data.height = new_size

        
        #print('move by', data.path)
        for _data in self.tag_path_data_ls[idx+1:]:
            _tag = _data.tag
            cv.move(_tag, 0, new_height - old_height)
            #print('move', _data.path)
        self.refresh_tag_y_ls()

        self.tmp_showing_tags.discard(tag)
        del self.tmp_path2tk_img[data.path]
        self._update_cv()
        
        assert tag != data.tag or data.path in self.tmp_bad_img_path
        self._auto_set_cv_view_region()
        self._move_cvtag_to_top(data.tag)
        #
        return


    def __get_img_tag(self, event):
        cv = self.cv
        tags = self._get_cv_tags_from_eventxy(event)
        assert len(tags) <= 1
        if tags and 'image' == cv.type(tags[0]):
            tag, = tags
            #print('_cv_click cv.type(tag)', cv.type(tag))
            return tag
        return None
            
        
    def _cv_click(self, event):
        if self.__dragging:
            # end dragging
            self.__dragging = False
            self.__old_xy_for_drag = None
            return
        
        cv = self.cv
        tags = self._get_cv_tags_from_eventxy(event)
        assert len(tags) <= 1
        if tags and 'text' == cv.type(tags[0]):
            tag, = tags
            #print('_cv_click cv.type(tag)', cv.type(tag))
            self._txt_click(event)
        else:
            #print('_cv_click click on nothing or image')
            self._img_click(event)
        return
    
    def bind_cv(self):
        cv = self.cv
        self.bind('<MouseWheel>', self.__wheel, '+')
        cv.bind('<ButtonPress-2><ButtonRelease-2>', self.close_curr_dir, '+')
        
        cv.bind('<ButtonPress-1><ButtonRelease-1>', self._cv_click, '+')
        cv.bind('<ButtonPress-3>', self.page_up, '+')
        cv.bind('<Button1-Motion>', self._img_drag, '')
        cv.bind('<Shift-ButtonPress-1><Shift-ButtonRelease-1>',
                self.__img_click_zoomin2, '')
        cv.bind('<Control-ButtonPress-1><Control-ButtonRelease-1>',
                self.__img_click_zoomout2, '')


    def __wheel(self, event):
        #self.bind_config(event)
        dx = 0
        dy = event.delta * self.__wheel_rate
        dy = int(dy)
        self._move_cv_view(0, dy)


        
    def _img_click(self, event):
        self.page_down(event)
        
    def _img_drag(self, event):
        #print(event.__dict__)

        if not self.__dragging:
            # begin dragging
            self.__dragging = True
            self.__old_xy_for_drag = (event.x, event.y)
            return
        old_xy = self.__old_xy_for_drag
        new_xy = self.__old_xy_for_drag = (event.x, event.y)
        dx, dy = ((u-v) for u, v in zip(new_xy, old_xy))
        
        self._move_cv_view(dx, dy)
        
    def _txt_click(self, event):
        cv = self.cv

        # find out the clicked tag and update cv
        tag = self._get_cv_tag_from_eventxy(event)
        idx, data = self.get_cvtag_idx_data(tag)
        clicked_path = data.path
        #print(tag, clicked_path)
        assert os.path.isdir(clicked_path)

        self.redraw_cv(clicked_path)


class CvToolsMixin:
    def __init__(self):pass
    

    def _set_cv_view_region(self, W, H):
        self.cv.config(scrollregion=(0, 0, W, H))
        
    def _auto_set_cv_view_region(self):
        cv = self.cv
        tags = cv.find_all()
        if tags:
            #print('cv.bbox(*tags)', cv.bbox(*tags))
            cv.config(scrollregion=cv.bbox(*tags))
    def _move_cv_view(self, dx, dy, xview = None, yview = None):
        cv = self.cv
        if yview is None:
            yview = cv.yview()
        if xview is None:
            xview = cv.xview()
            
        # move the view
        W, H = self._get_cv_wh()
        
        ftop, fbot = yview
        yoffset = int(ftop * H)
        y = yoffset - dy

        
        fleft, fright = xview
        xoffset = int(fleft * W)
        x = xoffset - dx
        
        cv.yview_moveto(y/H)
        cv.xview_moveto(x/W)
        return
        

        
    def _get_cv_wh(self):
        cv = self.cv
        x, y, w, h = cv.bbox(*cv.find_all())
        assert abs(x) < 2
        assert abs(y) < 2
        return w-x, h-y
    
        _, _, w, h = self.cv["scrollregion"].split()
        return int(w), int(h)
    
    def _get_cv_tags_from_eventxy(self, event):
        cv = self.cv
        #w=event.widget;print('widget', type(w), w, w.__dict__, dir(w))
        assert event.widget is cv
        y = cv.canvasy(event.y)
        x = cv.canvasx(event.x)
        #tags = cv.find_closest(x, y)
        tags = cv.find_overlapping(x, y, x, y)
        
        return tags
    def _get_cv_tag_from_eventxy(self, event):
        tag, = self._get_cv_tags_from_eventxy(event) # if only one tag...
        return tag

        #  what value of X, Y???????????
        #  virtual-height = cv.winfo_height()/(fbot-ftop) where ftop, fbot = cv.yview()
        #  virtual-height = int(cv["scrollregion"].split()[-1]) - int(cv["scrollregion"].split()[1])
        #  yoffset = int(ftop * virtual_height)
        #  y = yoffset + event.y
        #  y = cv.canvasy(event.y)

    def clear_cv(self):
        cv = self.cv
        cv.delete(*cv.find_all())
        cv.yview_moveto(0.0)

    def _move_cvtag_to_top(self, tag):
        cv = self.cv
        tag_x, tag_y = cv.coords(tag)
        _, cv_virtual_height = self._get_cv_wh()
        cv.yview_moveto(tag_y/cv_virtual_height)
        return


class TagData:
    def __init__(self, tag, path, width, height, img_or_txt):
        assert isinstance(tag, int)
        assert isinstance(width, int)
        assert isinstance(height, int)
        assert isinstance(path, str)
        assert img_or_txt is None or isinstance(img_or_txt, str)
        
        self.tag = tag
        self.path = path
        self.width = width
        self.height = height
        self.img_or_txt = img_or_txt

    def is_img(self):
        return not isinstance(self.img_or_txt, str)
    def get_tk_img(self):
        return try_open_tk_img(self.path, self.width)

    
class App(tk.Frame, KeyPressHandlerMixin, IdleHandlerMixin, ButtonHandlerMixin, CvToolsMixin):
    
    def __init__(self, base_path, picture_width, font, master=None,
                 *, opened_paths = (), num_tmp_images = 10,
                 wheel_rate = 1.0, auto_move_dt=1000, auto_move_dy=100):
        # the following statements should be placed at beginning
        # if failed, self.opened_paths holds the data
        self.opened_paths = opened_paths
        if hasattr(opened_paths, '__next__'):
            opened_paths = list(opened_paths)
        self.opened_paths = opened_paths

        ####################
        self.opened_paths = set(os.path.abspath(path) for path in opened_paths)
        
        if not isinstance(num_tmp_images, int) or num_tmp_images < 0:
            raise ValueError('not isinstance(num_tmp_images, int) or num_tmp_images < 0')
        
        IdleHandlerMixin.__init__(self)
        ButtonHandlerMixin.__init__(self, wheel_rate)
        KeyPressHandlerMixin.__init__(self,
                                      auto_move_dt=auto_move_dt,
                                      auto_move_dy=auto_move_dy)
        tk.Frame.__init__(self, master)
        self.pack(fill = tk.BOTH, expand=1)
        self.set_picture_width(picture_width)
        self.set_font(font)
        self.scrollY = None
        self.tmp_path2tk_img = collections.OrderedDict()
        self.set_num_tmp_images(num_tmp_images)
        self._update_cv_idle_id = None
        self.tmp_showing_tags = set()
        self.tmp_bad_img_path = set()

        self.__make_cv()

        self._set_base_path_and_draw(base_path)
        self.bind_keys()
        self.bind_cv()
        return

    def get_font(self):
        return self.font
    def set_font(self, font):
        self.font = font
    def get_config(self):
        font = self.get_font()
        picture_width = self.get_picture_width()
        num_tmp_images = self.get_num_tmp_images()
        auto_move_dt, auto_move_dy = self.get_auto_move_dtdy()
        wheel_rate = self.get_wheel_rate()

        family, size, is_bold = font2args(font)

        cnf = dict(picture_width = picture_width,
                   num_tmp_images = num_tmp_images,
                   auto_move_dt = auto_move_dt,
                   auto_move_dy = auto_move_dy,
                   wheel_rate = wheel_rate,
                   family = family,
                   size = size,
                   is_bold = is_bold)
        return cnf

    def get_cmd_options(self):
        cnf = self.get_config()
        ls = []
        for key, value in cnf.items():
            if key == 'is_bold':
                if value:
                    opt = '--BOLD'
                else:
                    opt = ''
            else:
                if key == 'family':
                    value = shell_quote(value)
                opt = '--{!s} {!s}'.format(key, value)
            ls.append(opt)

        options = ' '.join(ls)
        return options
        
    def clear_tmp(self):
        self.tmp_path2tk_img.clear()
        self.tmp_showing_tags.clear()
        self.tmp_bad_img_path.clear()
        
    def get_cvtag_idx_data(self, tag):
        idx = self.tag2ls_idx[tag]
        data = self.tag_path_data_ls[idx]
        assert data.tag == tag
        return idx, data
    def refresh_tag_y_ls(self):
        self.tag_y_ls.clear()
        ys = [0]
        ys.extend(data.height for data in self.tag_path_data_ls)
        ys.pop()
        
        self.tag_y_ls.extend(itertools.accumulate(ys))
        return
    def _set_base_path(self, base_path):
        base_path = os.path.abspath(base_path)
        self.base_path = base_path
        self.paths = [base_path]

        
        self.tag2ls_idx = None
        # [tag, path, width, height, img/txt]
        self.tag_path_data_ls = None
        self.tag_y_ls = None
        
        

    def _get_base_path(self):
        return self.paths[0]
    def _set_base_path_and_draw(self, base_path):
        #print('__set_base_path_and_draw')
        self._set_base_path(base_path)
        self._update_title()

        fnames, depths = get_entries(self.paths, is_close = False)
        self.tag2ls_idx, self.tag_path_data_ls, self.tag_y_ls = self.draw_cv(fnames, depths)
        #self._update_cv()
##        self.clear_cv()
##        fnames, depths = get_entries(self.paths, is_close = False)
##        self.tag2path = self.draw_cv(fnames, depths)

        self.focus_set()

    def get_num_tmp_images(self):
        return self.num_tmp_images
    def set_num_tmp_images(self, num_tmp_images):
        if not isinstance(num_tmp_images, int) or num_tmp_images < 0:
            raise ValueError('not isinstance(num_tmp_images, int) or num_tmp_images < 0')
        self.num_tmp_images = num_tmp_images
    def get_picture_width(self):
        return self.picture_width
    def set_picture_width(self, width):
        if not isinstance(width, int) or width <= 0:
            raise ValueError('not isinstance(picture_width, int) or picture_width <= 0')
        self.picture_width = width
        #self._update_title()
    def _update_title(self):
        base_path = self._get_base_path()
        
        dt, dy = self.get_auto_move_dtdy()
        rate = self.get_wheel_rate()
        
        title = 'base=[{base_path}] font=[{family!r} {size} {weight!r}] '\
                'width={width} num_tmp={num_tmp} '\
                'rate={rate} dt={dt}(ms) dy={dy}(pix)'.format(
            base_path = base_path,
            family = self.font.actual('family'),
            size = self.font['size'],
            weight = self.font.actual('weight'),
            width = self.picture_width,
            num_tmp = self.num_tmp_images,
            rate = rate, dt = dt, dy = dy)
        
        self.winfo_toplevel().title(title)
        
    HELP = r'''GUI HELP

MOVE:
    left-drag           - move by drag
    left/right-click    - page up/down
    Up/Down/PgUp/PgDn   - page up/down
    Space               - page down
    Left/Right          - page left/right
    wheel-up/down       - move by wheel
    A                   - auto move or stop
    
ZOOM:
    Shift + left-click on image
                        - enlarge image by double its size
    Ctrl + left-click on image
                        - shrink the size

CONFIG:
    G                   - general configure
    F                   - set font family/size/weight
    C                   - show command line options
                          for current configure

PATH:
    BackSpace/wheel-click
                        - back to parent folder
    left-click on tag   - open/close the clicked folder
    O                   - set the top folder

HELP:
    F1/H                - show this help
    
HAVE FUN!
'''

        
        
        
    def __cv_yview(self, *args, **kwargs):
        #print('__cv_yview', args, kwargs)
        self.cv.yview(*args, **kwargs)
    def __scrollY_set(self, *args, **kwargs):
        #print('__scrollY_set', args, kwargs)
        self.scrollY.set(*args, **kwargs)

        #self._update_cv();return
        if self._update_cv_idle_id is not None:
            self.after_cancel(self._update_cv_idle_id)
        self._update_cv_idle_id = self.after_idle(self._update_cv)
        
    def __make_cv(self):
        top_frame = tk.Frame(self)
        top_frame.pack(fill = tk.BOTH, expand=1)
        cv = self.cv = tk.Canvas(top_frame, bg = 'white')
        cv.pack(side = tk.LEFT, fill = tk.BOTH, expand=1)
        
        scrollY = self.scrollY = tk.Scrollbar(top_frame, orient=tk.VERTICAL,
                                              command=self.__cv_yview)#cv.yview)
        scrollY.pack(side = tk.RIGHT, fill=tk.Y)
        cv['yscrollcommand'] = self.__scrollY_set #scrollY.set
        
        scrollX = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=cv.xview)
        scrollX.pack(side = tk.BOTTOM, fill=tk.X, anchor = 'se', expand=0)
        cv['xscrollcommand'] = scrollX.set
        

    def _cvtag2path(self, tag):
        return self.get_cvtag_idx_data(tag)[-1].path
    def _tags2img_paths(self, tags):
        paths = (self._cvtag2path(tag) for tag in tags)
        img_paths = list(path for path in paths if not os.path.isdir(path))
        return img_paths
    
    def _update_cv(self):
        cv = self.cv
        #print('_update_cv self.scrollY.get()', self.scrollY.get())
        upper, lower = list(self.scrollY.get())[:2]
        assert 0 <= upper <= lower <= 1
        W, H = self._get_cv_wh()
        showing_tags = cv.find_overlapping(0, H*upper, W, H*lower)
        showing_tags = set(showing_tags)
        self.tmp_showing_tags &= showing_tags # remain
        new_tags = self._del_redraw_and_bind_cvtags(showing_tags - self.tmp_showing_tags)
        
        new_tags = set(new_tags)
        new_tags.discard(None)
        if not new_tags:
            return
        
        remaining_img_paths = self._tags2img_paths(self.tmp_showing_tags)
        self.tmp_showing_tags.update(new_tags)
        for path in remaining_img_paths:
            self.tmp_path2tk_img.move_to_end(path)


        showing_img_paths = set(self._tags2img_paths(self.tmp_showing_tags))
        tmp_paths = list(self.tmp_path2tk_img.keys())
        
        sL = len(showing_img_paths)
        tL = len(tmp_paths)
##        if not set(tmp_paths[tL-sL:]) == showing_img_paths:
##            print(tmp_paths)
##            print(showing_img_paths)
        assert set(tmp_paths[tL-sL:]) == showing_img_paths

        num_unused_tmp_paths = tL - sL
        assert num_unused_tmp_paths >= 0
        for _ in range(num_unused_tmp_paths - self.num_tmp_images):
            pop_path, _ = self.tmp_path2tk_img.popitem(last=False)
            assert pop_path not in showing_img_paths
        
        
        

    def _del_redraw_and_bind_cvtags(self, tags):
        assert not isinstance(tags, str)
        #print('_del_redraw_and_bind_cvtags', tags)

        ls = []
        for tag in tags:
            new = self._del_redraw_and_bind_cvtag(tag)
            ls.append(new)
        return ls
            
    def _del_redraw_and_bind_cvtag(self, tag):
        idx, data = self.get_cvtag_idx_data(tag)
        path = data.path
        y = self.tag_y_ls[idx]
        cv = self.cv
        if data.is_img():
            if path in self.tmp_bad_img_path:
                return None
            
            tk_img = self.tmp_path2tk_img.get(path, None)
            if tk_img is None:
                tk_img = data.get_tk_img()
            else:
                self.tmp_path2tk_img.move_to_end(path) # to put img at last
                
            if tk_img is None:
                #print('error ?? image deleted? or bad format?', file=sys.stderr)
                if not os.path.exists(path) or os.path.isdir(path):
                    msg = 'error ?? image deleted? {!r}'.format(path)
                else:
                    msg = 'error ?? image bad format? {!r}'.format(path)

                print(msg, file=sys.stderr)
                #return tag # nothing changes
                self.tmp_bad_img_path.add(path)
                return None

            self.tmp_path2tk_img[path] = tk_img
                
            new_tag = cv.create_image((0,y), image = tk_img, anchor = 'nw')

        else:
            text = data.img_or_txt
            
            if path in self.opened_paths:
                txt_color = 'red'
            else:
                txt_color = 'black'
            new_tag = cv.create_text((0, y), text=text, anchor = 'nw', font=self.font, fill=txt_color)


        cv.delete(tag)
        del self.tag2ls_idx[tag]
        self.tag2ls_idx[new_tag] = idx
        data.tag = new_tag
        return new_tag

        
            
            
        

    def redraw_cv(self, clicked_path):
        assert os.path.isdir(clicked_path)
        self.opened_paths.add(clicked_path)
        self.clear_tmp()
        fnames, depths = make_entries(clicked_path, self.paths)
        self.tag2ls_idx, self.tag_path_data_ls, self.tag_y_ls = self.draw_cv(fnames, depths)


        


        # let the clicked_path at top-most
        for data in self.tag_path_data_ls:
            if data.path == clicked_path:
                tag = data.tag
                assert data is self.tag_path_data_ls[self.tag2ls_idx[tag]]
                break
        else:
            raise logic-error
        self._move_cvtag_to_top(tag)
        return




    

    def draw_cv(self, fnames, depths):
        self.clear_cv()
        idle_iter = self.__draw_cv(fnames, depths)
        
        # let the clicked tag be shown on cv
        for tag2ls_idx, tag_path_data_ls, tag_y_ls in idle_iter:
            break
        else:
            raise logic-error
            
        self._register_idle_func(idle_iter)
        return tag2ls_idx, tag_path_data_ls, tag_y_ls



    def __draw_cv(self, fnames, depths):
        cv = self.cv




        # y = 0 # increaseing height of cv
        tag2ls_idx = {}
        # tag, path, width, height, img/txt
        tag_path_data_ls = []
        tag_y_ls = []
        openning_paths = frozenset(self.paths)
        self.tag2ls_idx, self.tag_path_data_ls, self.tag_y_ls = tag2ls_idx, tag_path_data_ls, tag_y_ls
        color = '#808080'

        # NOTE: 'bind' should not happen before updating tag2ls_idx
        for path, depth in zip(fnames, depths):
            assert len(tag_y_ls) == len(tag_path_data_ls)
            if not tag_y_ls:
                y = 0
            else:
                y = tag_y_ls[-1] + tag_path_data_ls[-1].height
                
            #print(path)
            if os.path.isdir(path):
                basename = os.path.basename(path)
                text = '>' * depth + basename
                if path in openning_paths:
                    text += ' ->'
                tag = cv.create_text((0, y), text=text, anchor = 'nw', font=self.font)
                #print('itemconfigure', cv.itemconfigure(tag))

                cv.itemconfigure(tag, fill='grey')
                _, _old_y, width, _new_y = cv.bbox(tag)
                assert _old_y == y
                # cv.delete(tag)
                height = _new_y - _old_y
                img_or_txt = text
                

            else:
                size = get_img_size(path)
                #print(path)
                if size is None:
                    continue

                width, height = calc_new_size(size, self.picture_width)
                #tag = cv.create_text((0,y), text = 'place holder: cannot see me', anchor = 'nw')
                tag = cv.create_rectangle(0, y, width, y+height, fill='grey')
                #tag = cv.create_window(0, y, width, y+height)
                #print('itemconfigure', cv.itemconfigure(tag))
                #cv.itemconfigure(tag, width=width)
                img_or_txt = None

            data = TagData(tag, path, width, height, img_or_txt)
            tag2ls_idx[tag] = len(tag_path_data_ls)
            tag_path_data_ls.append(data)
            tag_y_ls.append(y)

            if not os.path.isdir(path):
                # each time added a img, we pause.
                self._auto_set_cv_view_region()
                yield tag2ls_idx, tag_path_data_ls, tag_y_ls

        self._auto_set_cv_view_region()
        yield tag2ls_idx, tag_path_data_ls, tag_y_ls

def font2args(font):
    a = font.actual
    return a('family'), a('size'), a('weight').lower() == 'bold'

def args2font(font_name, size, is_bold):
    weight = tkfont.BOLD if is_bold else tkfont.NORMAL
    font = tkfont.Font(family=font_name, size=size, weight=weight)
    return font

def show_pic(path, size=30, family="times", weight=tkfont.NORMAL,
             *, picture_width=None, parent = None,
             opened_paths = (), num_tmp_images = 10,
             wheel_rate = 1.0, auto_move_dt=1000, auto_move_dy=100):

    if parent == None:
        xroot = tk.Tk()
    else:
        xroot = parent
    font = tkfont.Font(family=family, size=size, weight=weight)
    
    H = xroot.winfo_screenheight()
    W = xroot.winfo_screenwidth()
    VH = xroot.winfo_vrootheight()
    RH = xroot.winfo_reqheight()

    dW = 16
    dH = 40
    if picture_width == None:
        s = tk.Scrollbar()
        #print(s.configure())
        dW = int(s.cget('width'))
        #print(dW)
        picture_width = W-dW
    elif not isinstance(picture_width, int) or picture_width <= 0:
        raise ValueError('not isinstance(picture_width, int) or picture_width <= 0')
        
    app = App(path, picture_width, font, xroot,
              opened_paths = opened_paths,
              num_tmp_images = num_tmp_images,
              wheel_rate = wheel_rate,
              auto_move_dt = auto_move_dt,
              auto_move_dy = auto_move_dy)
    assert app.winfo_toplevel() is xroot

    
    xroot.wm_geometry('{}x{}+0+0'.format(W, H-dH))
    #xroot.wm_withdraw()
    
    # The following three commands are needed so the window pops
    # up on top on Windows...
    xroot.iconify()
    xroot.update()
    xroot.deiconify()
    xroot.focus()
    try:    pass; xroot.wm_state('zoomed')
    except: pass

    try:
        xroot.mainloop()
    finally:
        return app.opened_paths




def tkfont_families(root = None):
    xxxx = root
    if root == None:
        xxxx = tk.Tk()
        
    fonts=list(tkfont.families(xxxx))
    fonts.sort()
    if root == None:
        xxxx.destroy()
        
    return fonts


def my_askdirectory(title):
    xxxx = tk.Tk()
    
    """Query or set the state of this widget as one of normal, icon,
    iconic (see wm_iconwindow), withdrawn, or zoomed (Windows only)."""
    xxxx.wm_state('withdrawn')
    path = tk_fdlg.askdirectory(title=title,
                                mustexist=1,
                                parent = xxxx)
    xxxx.destroy()
    if not path:
        path = None
    return path

def nonnegative_integer(s):
    try:
        n = int(s)
        if n < 0:
            raise ValueError()
        return n
    except:
        msg = '{!r} is not nonnegative integer.'
        raise argparse.ArgumentTypeError(msg)




def positive_integer(s):
    try:
        n = int(s)
        if n <= 0:
            raise ValueError()
        return n
    except:
        msg = '{!r} is not positive integer.'
        raise argparse.ArgumentTypeError(msg)

def positive_float(s):
    try:
        n = float(s)
        if n <= 0:
            raise ValueError()
        return n
    except:
        msg = '{!r} is not positive real number.'
        raise argparse.ArgumentTypeError(msg)


def to_sys_printable(msg):
    encoding = sys.stdout.encoding
    bs = msg.encode(encoding=encoding, errors='backslashreplace')
    msg = bs.decode(encoding=encoding)
    return msg

    
def main(args=None):
    import argparse
    parser = argparse.ArgumentParser(
        #add_help = True,
        description = 'Show pictures under the given path.',
        epilog = '(press F1 or H on the window to get more information.)')
    
    parser.add_argument('path', type=str, nargs = '?',
                        default = None,
                        help='top folder of pictures to be shown')

    parser.add_argument('-s', '--size', type=int,
                        default = 30,
                        help='size of font')
    
    parser.add_argument('-B', '--BOLD', action='store_const',
                        default = tkfont.NORMAL, const=tkfont.BOLD,
                        help='let font be bold')


    parser.add_argument('-f', '--family', type=str,
                        default = 'times',
                        help='font family')
    
    parser.add_argument('-l', '--list_font_families', action='store_true',
                        default = False,
                        help='list all available font families and exit')
    
    parser.add_argument('-G', '--gui_help', action='store_true',
                        default = False,
                        help='print GUI help and exit')
    
    parser.add_argument('-W', '--picture_width', type=int,
                        default = None,
                        help='picture width to which every image was scaled')
    
    parser.add_argument('-H', '--history_file', type=str,
                        default = None,
                        help='history_file who records which folder you have visited')
    
    parser.add_argument('-TN', '--num_tmp_images', type=nonnegative_integer,
                        default = 5,
                        help='number of images which are not shown at screen but loaded in memory')
    


    parser.add_argument('-dt', '--auto_move_dt', type=positive_integer,
                        default = 1000,
                        help='time step of each move; unit: millisecond')
    
    parser.add_argument('-dy', '--auto_move_dy', type=int,
                        default = 100,
                        help='y-axis step of each move; unit: pix')
     
    parser.add_argument('-wr', '--wheel_rate', type=positive_float,
                        default = 1.0,
                        help='control the scroll speed by wheel')
    


    args = parser.parse_args(args)

    if args.list_font_families:
        msg = '\n'.join(tkfont_families())
        msg = to_sys_printable(msg)
        print(msg)
        parser.exit(0)
    if args.gui_help:
        msg = App.HELP
        msg = to_sys_printable(msg)
        print(msg)
        parser.exit(0)
    
    hfile = args.history_file
    opened_paths = ()
    if hfile is not None and os.path.exists(hfile):
        with open(hfile, encoding='utf8') as fin:
            txt = fin.read()
        opened_paths = ast.literal_eval(txt)
        
        
    

    if args.path is None:
        args.path = my_askdirectory('select top-most directory')
        if not args.path:
            # cancel
            parser.exit(0)
            return

    #config = dict()
    opened_paths = show_pic(
        path=args.path,
        size=args.size, family=args.family, weight=args.BOLD,
        picture_width = args.picture_width,
        opened_paths = opened_paths, num_tmp_images = args.num_tmp_images,
        wheel_rate = args.wheel_rate,
        auto_move_dt=args.auto_move_dt, auto_move_dy=args.auto_move_dy)

    
    if hfile is not None:
        with open(hfile, 'w', encoding='utf8') as fout:
            fout.write(repr(opened_paths))
    parser.exit(0)
    
if __name__ == "__main__":
    main()

    





