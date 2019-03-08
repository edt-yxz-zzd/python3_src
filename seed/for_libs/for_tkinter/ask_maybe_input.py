
'''
see:
    easygui
        buttonbox
        multenterbox



1. RuntimeError('Too early to create image',)
    # no Tk()
    cause:
        PIL.ImageTk.PhotoImage(image_PIL)
        where no tk_root
            requires Tk() first
    post:
        root = Tk()
        image_tk = PIL.ImageTk.PhotoImage(master=root, image=image_PIL)
2. _tkinter.TclError: image "pyimage1" doesn't exist
    # more than one Tk()
    cause:
        ___donot_destroy_me = tkinter.Tk() # global

        # local
        root = Tk()
        image_tk = PIL.ImageTk.PhotoImage(master=root, image=image_PIL)
            #there should not be more than 1 Tk object!!!!
    post:
        romove ___donot_destroy_me = ...
        def ...(..., root=None):
            if root is None:
                root = Tk()
            image_tk = PIL.ImageTk.PhotoImage(master=root, image=image_PIL)

3. AttributeError: 'PhotoImage' object has no attribute '_PhotoImage__photo'
    cause:
        image_tk = PIL.ImageTk.PhotoImage(img)
        where img is not a image_PIL
            e.g. img is a path, image_tk, ...
                once I use:
                    try:
                        image_PIL = ....(image_path) # miss arg "root"
                    except:
                        image_PIL = image_path
                    image_tk = ...(image_PIL)
                        # error!! image_PIL is image_path indeed!!!
    post:
        try:
            image_path = Path(image_PIL)
        except:
            image_PIL = image_PIL
        else:
            image_PIL = PIL.Image.open(image_path)
        image_tk = PIL.ImageTk.PhotoImage(master=root, image=image_PIL)



'''

__all__ = '''
    ask_maybe_input
    IAskMaybeInput
    AskMaybeInput
    '''.split()

import PIL.Image, PIL.ImageTk
import tkinter.messagebox
from abc import ABC, abstractmethod
from pathlib import Path

class IAskMaybeInput(ABC):
    __slots__ = ()
    def __init__(self, *, title, prompt, image_PIL, root=None):
        '''
input:
    title :: str
    prompt :: str
    image_PIL :: file_path | image_PIL
    root :: None|window_tk
output:
    () | (result,) # from __button_ok_callback__
'''
        if root is None:
            root = tkinter.Tk()

        #image_path = image_PIL
        #read_image__tk(root, image_path)
        try:
            image_path = Path(image_PIL)
        except Exception as e:
            #import traceback
            #traceback.print_exc()
            #del image_path
            image_PIL = image_PIL
        else:
            image_PIL = read_image__PIL(image_path)
        image_tk = image_PIL2image_tk(root, image_PIL)

        canvas = tkinter.Canvas(root, width=image_tk.width(), height=image_tk.height())
        #canvas = tkinter.Canvas(root, width=image_PIL.width, height=image_PIL.height)

        canvas.pack()
        canvas.create_image(0, 0, image=image_tk, anchor=tkinter.NW)


        #https://www.tutorialspoint.com/python/python_gui_programming.htm
        #https://www.tutorialspoint.com/python/tk_entry.htm
        label_prompt = tkinter.Label(root, text=prompt)
        label_prompt.pack()
        box_input = tkinter.Entry(root, bd=5)
        box_input.pack()
        box_input.focus_set()
        button_ok = tkinter.Button(root, text="OK"
            , command=self.button_ok_callback, default=tkinter.ACTIVE)
        button_cancel = tkinter.Button(root, text="cancel"
            , command=self.button_cancel_callback, default=tkinter.ACTIVE)
        button_ok.pack()
        root.bind("<Return>", self.on_OK)
        button_cancel.pack()
        root.bind("<Escape>", self.on_cancel)


        self.title = title
        self.prompt = prompt

        # SHOULD save image, otherwise auto deleted, and show nothing
        self.image_PIL = image_PIL
        self.image_tk = image_tk

        self.root = root
        self.canvas = canvas
        self.label_prompt = label_prompt
        self.box_input = box_input
        self.button_ok = button_ok
        self.button_cancel = button_cancel
        self.result01 = []


    def on_cancel(self, event=None):
        self.button_cancel.invoke()
    def on_OK(self, event=None):
        self.button_ok.invoke()
    def maybe_ask(self):
        #https://solarianprogrammer.com/2018/04/20/python-opencv-show-image-tkinter-window/
        self.result01.clear()
        self.root.wm_attributes("-topmost", 1)
        self.root.focus_force()
        self.root.mainloop() # ; root.destroy()
        maybe_result = tuple(self.result01)
        assert len(maybe_result) <= 1
        return maybe_result
        [result] = self.result01
        return result

    @abstractmethod
    def __button_ok_callback__(self, user_input):
        'user_input -> (stop::bool, result)'
        raise NotImplementedError
    def button_cancel_callback(self):
        self.root.destroy()     # quit()
        self.result01.clear()   # output nothing
        return
    def button_ok_callback(self):
        #https://www.tutorialspoint.com/python/tk_button.htm
        user_input = self.box_input.get()
        stop, result = type(self).__button_ok_callback__(self, user_input)
        if stop:
            self.root.destroy()             # quit()
            self.result01.append(result)    # output result
        return
        tkinter.messagebox.showinfo("Hello", repr(box_input.get()), master=root)


def _default_button_ok_callback(user_input):
    return (True, user_input)
class AskMaybeInput(IAskMaybeInput):
    def __init__(self, *, title, prompt, image_PIL, root=None, button_ok_callback=None):
        '''
input:
    title :: str
    prompt :: str
    image_PIL :: file_path | image_PIL
    button_ok_callback :: None | (user_input::str) -> (stop::bool, result)
    root :: None|window_tk
output:
    () | (result,) # from button_ok_callback
'''
        if button_ok_callback is None:
            button_ok_callback = _default_button_ok_callback

        super().__init__(title=title, prompt=prompt, image_PIL=image_PIL, root=root)
        self._button_ok_callback = button_ok_callback


    def __button_ok_callback__(self, user_input):
        'user_input -> (stop::bool, result)'
        stop, result = self._button_ok_callback(user_input)
        return bool(stop), result

def ask_maybe_input(*, title, prompt, image_PIL, button_ok_callback=None):
    '''
input:
    title :: str
    prompt :: str
    image_PIL :: file_path | image_PIL
    button_ok_callback :: None | (user_input::str) -> (stop::bool, result)
output:
    () | (result,) # from button_ok_callback
'''

    ask_obj = AskMaybeInput(button_ok_callback=button_ok_callback
                    , title=title, prompt=prompt, image_PIL=image_PIL)
    return ask_obj.maybe_ask()




def read_image__tk(root, image_path):
    image_PIL = read_image__PIL(image_path)
    image_tk = image_PIL2image_tk(root, image_PIL)
    return image_tk
def image_PIL2image_tk(root, image_PIL):
    #image_tk = PIL.ImageTk.PhotoImage(master=root, image=image_PIL)
    image_tk = PIL.ImageTk.PhotoImage(image_PIL, master=root)
    return image_tk
def read_image__PIL(image_path):
    image_PIL = PIL.Image.open(image_path)
    return image_PIL


if __name__ == '__main__':
    print(ask_maybe_input(
        title='haha'
        ,prompt='>>>'
        ,image_PIL=r'E:\my_data\program_source\github\edt-yxz-zzd\python3_src\nn_ns\app\Django\favicon.ico'
        ,button_ok_callback=lambda user_input:(bool(user_input), repr(user_input))
        ))
