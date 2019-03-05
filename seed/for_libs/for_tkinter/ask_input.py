
__all__ = '''
    ask_input
    IAskInput
    AskInput
    '''.split()

import PIL.Image, PIL.ImageTk
import tkinter.messagebox
from abc import ABC, abstractmethod

class IAskInput(ABC):
    __slots__ = ()
    def __init__(self, *, title, prompt, image_PIL, root=None):
        '''
input:
    title :: str
    prompt :: str
    image_PIL :: file_path | image_PIL
    root :: None|window_tk
output:
    result # from __button_callback__
'''
        if root is None:
            root = tkinter.Tk()

        image_path = image_PIL
        try:
            image_PIL = read_image__PIL(image_path)
        except:
            del image_path
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
            , command=self.button_callback, default=tkinter.ACTIVE)
        button_ok.pack()
        root.bind("<Return>", self.on_OK)


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
        self.result01 = []


    def on_OK(self, event=None):
        self.button_ok.invoke()
    def ask(self):
        #https://solarianprogrammer.com/2018/04/20/python-opencv-show-image-tkinter-window/
        self.result01.clear()
        self.root.wm_attributes("-topmost", 1)
        self.root.focus_force()
        self.root.mainloop() # ; root.destroy()
        [result] = self.result01
        return result

    @abstractmethod
    def __button_callback__(self, user_input):
        'user_input -> (stop::bool, result)'
        raise NotImplementedError
    def button_callback(self):
        #https://www.tutorialspoint.com/python/tk_button.htm
        user_input = self.box_input.get()
        stop, result = type(self).__button_callback__(self, user_input)
        if stop:
            self.root.destroy() # quit()
            self.result01.append(result)
        return
        tkinter.messagebox.showinfo("Hello", repr(box_input.get()), master=root)


def _default_button_callback(user_input):
    return (True, user_input)
class AskInput(IAskInput):
    def __init__(self, *, title, prompt, image_PIL, root=None, button_callback=None):
        '''
input:
    title :: str
    prompt :: str
    image_PIL :: file_path | image_PIL
    button_callback :: None | (user_input::str) -> (stop::bool, result)
    root :: None|window_tk
output:
    result # from button_callback
'''
        if button_callback is None:
            button_callback = _default_button_callback

        super().__init__(title=title, prompt=prompt, image_PIL=image_PIL, root=root)
        self._button_callback = button_callback


    def __button_callback__(self, user_input):
        'user_input -> (stop::bool, result)'
        stop, result = self._button_callback(user_input)
        return bool(stop), result

def ask_input(*, title, prompt, image_PIL, button_callback=None):
    '''
input:
    title :: str
    prompt :: str
    image_PIL :: file_path | image_PIL
    button_callback :: None | (user_input::str) -> (stop::bool, result)
output:
    result # from button_callback
'''

    ask_obj = AskInput(button_callback=button_callback
                    , title=title, prompt=prompt, image_PIL=image_PIL)
    return ask_obj.ask()




def read_image__tk(root, image_path):
    image_PIL = read_image__PIL(image_path)
    image_tk = image_PIL2image_tk(image_PIL)
    return image_tk
def image_PIL2image_tk(root, image_PIL):
    image_tk = PIL.ImageTk.PhotoImage(master=root, image=image_PIL)
    return image_tk
def read_image__PIL(root, image_path):
    image_PIL = PIL.Image.open(image_path)
    return image_PIL


if __name__ == '__main__':
    print(ask_input(
        title='haha'
        ,prompt='>>>'
        ,image_PIL=r'E:\my_data\program_source\github\edt-yxz-zzd\python3_src\nn_ns\app\Django\favicon.ico'
        ,button_callback=lambda user_input:(bool(user_input), repr(user_input))
        ))
