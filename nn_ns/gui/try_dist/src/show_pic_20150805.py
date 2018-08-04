


from PIL import Image, ImageTk

import tkinter as tk
import tkinter.font as tkfont
#import tkinter.constants as cs
import tkinter.messagebox as tk_msgbox
import tkinter.simpledialog as tk_ask
import tkinter.filedialog as tk_fdlg

import os, os.path
import sys

r'''
images should be hold by myself, otherwise it would be deleted.
pack/hold-img-myself/
bind/focus_set/wm_protocol/
config/keys/cget/
winfo_screenwidth/winfo_toplevel/wm_geometry/winfo_y/winfo_height
Canvas:
    canvasy/find_closest/coords/["scrollregion"]
    yview_moveto/yview_scroll/yview/bbox/find_all/coords



slow where too many images under a folder: fixed by 'dynamic load when idle'
fail at:
    火凤燎原/第10卷/
        total 190 jpg 16.1 MB (16,952,408 字节)
        each one: 512 x 768 x 8 bit ~ upzipped: 384 KB => total unzipped 72960 KB
        resize width to 1350 => 72960 KB * (1350/512)**2 ~ 507238.7 KB
        may be convert to RGB 24 bit => 1521716.3 KB ~ 1486 MB
        use up all my 2GB memory.

        how ?
        1) decrease the picture_width argument
            before load images: python 19916 KB
            set width 512 => python 533208 KB    dmem = 513292
            set width 768 => python 1171872 KB   dmem = 1151956   /(9/4)= 511980
            set width 1024 => python 2069012 KB  dmem = 2049096   /4 = 512274
            1.3 KB per pix ?????????
        2) decrease the number of pictures each folder
        3) reimplement this App 'load when show'

'''
xbase_path2 = r'E:\multimedia\picture\beauty\wallpaper'
xbase_path = r'E:\multimedia\picture\something'
#base_path = r'E:\multimedia\picture\funny'






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

def open_tk_img(fname, to_width = None):
    with Image.open(fname) as img:
        if to_width is not None:
            width, height = img.size
            scale =  to_width / float(width)
            to_fheight = height * scale
            img = img.resize((to_width, int(to_fheight)))
        pic = _CountImageTkPhotoImage(img)
    return pic

def try_open_tk_img(path, to_width = None):
    try:
        img = open_tk_img(path, to_width)
    except IOError as e:
        #print(type(e), e, file=sys.stderr)
        return None
    return img



    
    
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

class KeyPressHandlerMixin:
    def __init__(self):pass
    
    def bind_keys(self):
        self.bind('<KeyPress-space>', self.page_down, '+')
        self.bind('<KeyPress-Next>', self.page_down, '+') # PgDn
        self.bind('<KeyPress-Down>', self.page_down, '+')
        self.bind('<KeyPress-Prior>', self.page_up, '+') # PgUp
        self.bind('<KeyPress-Up>', self.page_up, '+')

        
        self.bind('<KeyPress-Left>', self.page_left, '+')
        self.bind('<KeyPress-Right>', self.page_right, '+')
        
        self.bind('<KeyPress-BackSpace>', self.close_curr_dir, '+')
        
        self.bind('<KeyPress-w>', self.set_picture_width, '+')
        self.bind('<KeyPress-o>', self.set_base_path, '+')
        self.bind('<KeyPress-h>', self.show_help, '+')
        self.bind('<KeyPress-F1>', self.show_help, '+')


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
    


class App(tk.Frame, KeyPressHandlerMixin, IdleHandlerMixin):
    
    def __init__(self, base_path, picture_width, font, master=None):
        IdleHandlerMixin.__init__(self)
        tk.Frame.__init__(self, master)
        self.pack(fill = tk.BOTH, expand=1)
        self.picture_width = picture_width
        self.font = font

        self.__make_cv()

        self.__set_base_path_and_draw(base_path)
        self.__dragging = False
        self.__old_xy_for_drag = None
        self.bind_keys()
        return
    
    def __set_base_path(self, base_path):
        base_path = os.path.abspath(base_path)
        self.base_path = base_path
        self.paths = [base_path]
        self.imgs = []
        self.tags = []
        self.tag2path = None

    def __get_base_path(self):
        return self.paths[0]
    def __set_base_path_and_draw(self, base_path):
        #print('__set_base_path_and_draw')
        self.__set_base_path(base_path)
        base_path = self.__get_base_path()
        title = '[{base_path}] font: {family!r} {size}'.format(
            base_path = base_path,
            family = self.font.actual('family'),
            size=self.font['size'])
        
        self.winfo_toplevel().title(title)
        
        self.clear_cv()
        fnames, depths = get_entries(self.paths, is_close = False)
        self.tag2path = self.draw_cv(fnames, depths)

        self.focus_set()
        
    HELP = r'''HELP:
    MOVE:
        left-drag on image        - move by drag
        left/right-click on image - page up/down
        Up/Down/PgUp/PgDn         - page up/down
        Space                     - page down
        Left/Right                - page left/right
        
    ZOOM:
        Shift + left-click on image  - enlarge image by double its size
        Ctrl + left-click on image   - back to the original size

    CONFIG:
        W                  - set the picture width

    PATH:
        BackSpace          - back to parent folder
        left-click on tag  - open/close the clicked folder
        O                  - set the top folder

    HELP:
        F1/H               - show this help
    
HAVE FUN!
'''
    def set_picture_width(self, event=None):
        w = tk_ask.askinteger('set picture width',
                              'input a integer as the width:',
                              parent=self,
                              initialvalue=self.picture_width,
                              minvalue=1)
        self.focus_set()
        if w is None:
            # cancel
            pass
        else:
            assert type(w) is int
            if w <= 0:
                tk_msgbox.showerror('error', 'picture width should be an positive integer.')
            else:
                self.picture_width = w
            


    def set_base_path(self, event = None):
        base_dir = tk_fdlg.askdirectory(parent=self,
                                        title='select top-most directory',
                                        initialdir = self.__get_base_path(),
                                        mustexist=1)
        
        self.focus_set()

        # return '' if cancel, not None!!
        # print('base_dir: {!r}'.format(base_dir))
        if base_dir is None or base_dir == '':
            # cancel
            pass
        else:
            self.__set_base_path_and_draw(base_dir)
            self.focus_set()
        
        
    def show_help(self, event=None):
        tk_msgbox.showinfo('help', self.HELP, parent=self)
        #raise NotImplementedError()
        self.focus_set()
    
    def close_curr_dir(self, event=None):
        paths = self.paths
        if len(paths) == 1:
            return
        clicked_path = paths[-1]
        self.redraw_cv(self.cv, clicked_path)


    def __img_click_zoomin2(self, event):
        self.__img_click_zoom(event, 2)
    def __img_click_zoomin1(self, event):
        self.__img_click_zoom(event, 1)
    def __img_click_zoom(self, event, scale):
        cv = self.cv
        new_width = int(self.picture_width * scale)
        assert new_width > 0
        
        I = self.__get_cv_tag_from_eventxy(cv, event)
        img_path = self.tag2path[I]
        img = try_open_tk_img(img_path, new_width)
        if img is None:
            print('error??')
            return
        new_tag = self.__swap_tag_for_newimg(I, img)
        self.__move_cvtag_to_top(new_tag)
        return

    def __img_click(self, event):
        if self.__dragging:
            # end dragging
            self.__dragging = False
            self.__old_xy_for_drag = None
            return
        self.page_down(event)
        
    def __img_drag(self, event):
        #print(event.__dict__)

        if not self.__dragging:
            # begin dragging
            self.__dragging = True
            self.__old_xy_for_drag = (event.x, event.y)
            return
        old_xy = self.__old_xy_for_drag
        new_xy = self.__old_xy_for_drag = (event.x, event.y)
        dx, dy = ((u-v) for u, v in zip(new_xy, old_xy))
        
        self.__move_cv_view(self.cv, dx, dy)
        

    def __move_cv_view(self, cv, dx, dy):
        # move the view
        W, H = self.__get_cv_wh()
        
        ftop, fbot = cv.yview()
        yoffset = int(ftop * H)
        y = yoffset - dy

        
        fleft, fright = cv.xview()
        xoffset = int(fleft * W)
        x = xoffset - dx
        
        cv.yview_moveto(y/H)
        cv.xview_moveto(x/W)
        return
        

    def __swap_tag_for_newimg(self, old_tag, new_img, img_path=None):
        cv = self.cv
        I = old_tag
        if img_path is None:
            img_path = self.tag2path[I]
        
        #print('itemconfigure', cv.itemconfigure(I))
        _, y, _, _ = cv.bbox(I)
        i = self.tags.index(I)
        cv.delete(I)
        del self.tag2path[I]
        idx = cv.create_image((0,y), image = new_img, anchor = 'nw')
        self.tags[i] = idx
        self.tag2path[idx] = img_path
        self.imgs[i] = new_img
        self.__bind_img(idx)

        if 0:
            W, H = self.__get_cv_wh()
            self.__set_cv_view_region(max(W, new_img.width()), max(H, y+new_img.height()))
        else:
            self.__auto_set_cv_view_region()

        new_tag = idx
        return new_tag
    
        
        
        
##        img = cv.itemcget(I, 'image') a str name !!!
##        print('img', type(img), img)
        
    def __get_cv_wh(self):
        _, _, w, h = self.cv["scrollregion"].split()
        return int(w), int(h)
    
    def __get_cv_tag_from_eventxy(self, cv, event):
        #w=event.widget;print('widget', type(w), w, w.__dict__, dir(w))
        assert event.widget is cv
        y = cv.canvasy(event.y)
        x = cv.canvasx(event.x)
        I, = cv.find_closest(x, y) # if only one tag...
        return I

        #  what value of X, Y???????????
        #  virtual-height = cv.winfo_height()/(fbot-ftop) where ftop, fbot = cv.yview()
        #  virtual-height = int(cv["scrollregion"].split()[-1]) - int(cv["scrollregion"].split()[1])
        #  yoffset = int(ftop * virtual_height)
        #  y = yoffset + event.y
        #  y = cv.canvasy(event.y)
        
##        print('winfo_vrootx', cv.winfo_vrootx())
##        print('winfo_vrooty', cv.winfo_vrooty())
##        print('winfo_x', cv.winfo_x())
##        print('winfo_y', cv.winfo_y())
##        print('cv.yview', cv.yview())
##        print('cv.winfo_height', cv.winfo_height())
##        print('cv["scrollregion"].split()', cv["scrollregion"].split())
##        ftop, fbot = cv.yview()
##        virtual_height = cv.winfo_height()/(fbot-ftop)
##        print('cv["scrollregion"].split()[-1] == virtual_height',
##              cv["scrollregion"].split()[-1], virtual_height)
##
##        virtual_height = int(cv["scrollregion"].split()[-1])
##        yoffset = int(ftop * virtual_height)
##        y = yoffset + event.y
##        print('yoffset + event.y == cv.canvasy(event.y)', y, cv.canvasy(event.y))
        
    def __make_cv(self):
        top_frame = tk.Frame(self)
        top_frame.pack(fill = tk.BOTH, expand=1)
        cv = self.cv = tk.Canvas(top_frame, bg = 'white')
        cv.pack(side = tk.LEFT, fill = tk.BOTH, expand=1)
        
        scrollY = tk.Scrollbar(top_frame, orient=tk.VERTICAL, command=cv.yview)
        scrollY.pack(side = tk.RIGHT, fill=tk.Y)
        cv['yscrollcommand'] = scrollY.set
        
        scrollX = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=cv.xview)
        scrollX.pack(side = tk.BOTTOM, fill=tk.X, anchor = 'se', expand=0)
        cv['xscrollcommand'] = scrollX.set
        

    def text_click_handle(self, event):
##        print('click', event)
##        print('widget', type(event.widget))
##        
##        print(event.__dict__)
##        print('x, y = ', event.x, event.y)
##        print('x_root, y_root = ', event.x_root, event.y_root)
        cv = self.cv

        # find out the clicked tag and update cv
        I = self.__get_cv_tag_from_eventxy(cv, event)
        clicked_path = self.tag2path[I]
        #print(I, clicked_path)
        assert os.path.isdir(clicked_path)

        self.redraw_cv(cv, clicked_path)

    def clear_cv(self):
        cv = self.cv
        cv.delete(*cv.find_all())
        cv.yview_moveto(0.0)
        
    def redraw_cv(self, cv, clicked_path):
        assert os.path.isdir(clicked_path)
        imgs = self.imgs
        tags = self.tags
        
        fnames, depths = make_entries(clicked_path, self.paths)
        self.clear_cv()
        imgs.clear()
        tags.clear()
        self.tag2path = self.draw_cv(fnames, depths)


        


        # let the clicked_path at top-most
        for tag, path in self.tag2path.items():
            if path == clicked_path:
                break
        else:
            raise logic-error
        self.__move_cvtag_to_top(tag)
        return


    def __move_cvtag_to_top(self, tag):
        cv = self.cv
        #print('tag, select_item', tag, cv.select_item())  always None
            
        #print('tag, cv.coords(tag)', tag, cv.coords(tag))
        tag_x, tag_y = cv.coords(tag)
        #print('cv.keys(), cv[state], cv[offset]', cv.keys(), cv['state'], cv['offset'])
        #cv.yview('moveto', tag_y)
        #return 
        _, cv_virtual_height = self.__get_cv_wh()
        cv.yview_moveto(tag_y/cv_virtual_height)
        return
##
##    def __scale(self, tag):
##        cv = self.cv
##        bbox = cv.bbox(tag)
##        print('bbox', bbox)
##        a, b, c, d = bbox
##        ls = [30,30,1,2]
##        print(ls)
##        cv.scale(tag, *ls)
##        bbox = cv.bbox(tag)
##        print('bbox', bbox)
##

    

    def draw_cv(self, fnames, depths):
        idle_iter = self.__draw_cv(fnames, depths)
        
        # let the clicked tag be shown on cv
        for tag2path in idle_iter:
            break
        else:
            raise logic-error
            
        self._register_idle_func(idle_iter)
        return tag2path


    def __bind_txt(self, idx):
        cv = self.cv
        cv.tag_bind(idx, '<ButtonPress-1>', self.text_click_handle, '+')
    
    def __bind_img(self, idx):
        cv = self.cv
        cv.tag_bind(idx, '<ButtonPress-1><ButtonRelease-1>', self.__img_click, '+')
        cv.tag_bind(idx, '<ButtonPress-3>', self.page_up, '+')
        cv.tag_bind(idx, '<Shift-ButtonPress-1>', self.__img_click_zoomin2, '+')
        cv.tag_bind(idx, '<Control-ButtonPress-1>', self.__img_click_zoomin1, '+')
        cv.tag_bind(idx, '<Button1-Motion>', self.__img_drag, '')
        


    def __draw_cv(self, fnames, depths):
        cv = self.cv
        imgs = self.imgs
        tags = self.tags
        assert not imgs
        assert not tags




        y = 0 # increaseing height of cv
        tag2path = {}
        heights = []
        widths = []
        openning_paths = frozenset(self.paths)

        # NOTE: 'bind' should not happen before updating tag2path
        for path, depth in zip(fnames, depths):
            #print(path)
            if os.path.isdir(path):
                basename = os.path.basename(path)
                text = '. ' * depth + basename
                if path in openning_paths:
                    text += ' ->'
                idx = cv.create_text((0, y), text=text, anchor = 'nw', font=self.font)
                bind = self.__bind_txt
                imgs.append('not image') # to index tag and img with same index num
                
    ##            print(cv.coords(idx))
    ##            print(cv.bbox(idx)) #X1,Y1,X2,Y2

            else:
                img = try_open_tk_img(path, self.picture_width)
                #print(path)
                if img is None:
                    continue
                idx = cv.create_image((0,y), image = img, anchor = 'nw')
                bind = self.__bind_img
                imgs.append(img)

            #print('y:', y)
            #print('cv.bbox(idx)', cv.bbox(idx))
            _, _old_y, width, _new_y = cv.bbox(idx)
            assert _old_y == y
            y = _new_y
            widths.append(width)
            tags.append(idx)
            assert idx not in tag2path
            tag2path[idx] = path
            bind(idx) # until now we can bind...

            if not os.path.isdir(path):
                # each time added a img, we pause.
                if tags:
                    #self.__set_cv_view_region(max(widths), y)
                    self.__auto_set_cv_view_region()
                #print('yield tag2path')
                yield tag2path

        if tags:
            # print("cv['height']", cv['height']) never change!!!
            # cv.config(scrollregion=cv.bbox(*tags))
            #self.__set_cv_view_region(max(widths), y)
            self.__auto_set_cv_view_region()
        yield tag2path

    def __set_cv_view_region(self, W, H):
        self.cv.config(scrollregion=(0, 0, W, H))
        
    def __auto_set_cv_view_region(self):
        cv = self.cv
        tags = cv.find_all()
        if tags:
            #print('cv.bbox(*tags)', cv.bbox(*tags))
            cv.config(scrollregion=cv.bbox(*tags))


def show_pic(path, size=30, family="times", weight=tkfont.NORMAL,
             *, name = None, picture_width=None, parent = None):

    if parent == None:
        xroot = tk.Tk()
    else:
        xroot = parent
    H = xroot.winfo_screenheight()
    W = xroot.winfo_screenwidth()
    VH = xroot.winfo_vrootheight()
    RH = xroot.winfo_reqheight()

    dW = 16
    dH = 40
    #print(H, VH, RH)
    #H = 721
    #print(xroot.keys())
    xroot.config()
    font = tkfont.Font(family=family, name=name, size=size, weight=weight)

    if picture_width == None:
        s = tk.Scrollbar()
        #print(s.configure())
        dW = int(s.cget('width'))
        #print(dW)
        picture_width = W-dW
    elif not isinstance(picture_width, int) or picture_width <= 0:
        raise ValueError('not isinstance(picture_width, int) or picture_width <= 0')
        
    app = App(path, picture_width, font, xroot)
    assert app.winfo_toplevel() is xroot

    #xroot.title(path)
    #xroot.maxsize(1366, 768)
    #print('wm_geometry', xroot.wm_geometry())
    xroot.wm_geometry('{}x{}+0+0'.format(W, H-dH))
    #xroot.wm_positionfrom('user')
    #xroot.wm_sizefrom('user')
    #xroot.wm_withdraw()
    
    # The following three commands are needed so the window pops
    # up on top on Windows...
    xroot.iconify()
    xroot.update()
    xroot.deiconify()
    xroot.focus()
    try:    pass; xroot.wm_state('zoomed')
    except: pass
    #xroot.wm_focusmodel('passive')

    xroot.mainloop()

#show_pic(xbase_path, size=30, family="times")

def my_askdirectory(title):
    xxxx = tk.Tk()
##        print(xxxx.config())
##        xxxx.wm_geometry('0x0+0+0')
##        xxxx.wm_iconify()
##        print(xxxx.wm_state())
    
    """Query or set the state of this widget as one of normal, icon,
    iconic (see wm_iconwindow), withdrawn, or zoomed (Windows only)."""
    xxxx.wm_state('withdrawn')
    path = tk_fdlg.askdirectory(title=title,
                                mustexist=1,
                                parent = xxxx)
    xxxx.destroy();xxxx= None
    if not path: path = None
    return path

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
    
    parser.add_argument('-W', '--picture_width', type=int,
                        default = None,
                        help='font family')
    

    
    args = parser.parse_args(args)

    if args.path is None:
        args.path = my_askdirectory('select top-most directory')
        if not args.path:
            # cancel
            parser.exit(0)
            return


    show_pic(path=args.path, size=args.size, family=args.family,
             weight=args.BOLD, picture_width = args.picture_width)
    parser.exit(0)
    
if __name__ == "__main__":
    main()

    





