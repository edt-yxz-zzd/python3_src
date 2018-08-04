
from Task2 import Task, Association
import tkinter as tk
import tkinter.font as tkfont

class Config:
    def __init__(self):
        font = tkfont.font(family = 'romans', size = 30, weight = 'bold')
        self.base_paths = []
        self.colors = {}
        self.font = font
        self.bind = {}
        self.scale_func = lambda width, height: 1350/width
        self.num_tmp_images = 0
        self.opened_paths = set()
        self.wheel_rate = 1.0
        #self.auto_move_script_idx = 0
        self.auto_move_script_table = [[]] # list of list of dtdxdy


class Face(tk.Toplevel):
    def __init__(self, ass, parent=None):
        super().__init__(parent)
        
        self.ass = ass
        cv = self.cv = tk.Canvas(self)
        self.scrollY = None
        self.__make_cv()
        self.__ass()

    

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
        cv = self.cv = tk.Canvas(top_frame, bg = 'black')
        cv.pack(side = tk.LEFT, fill = tk.BOTH, expand=1)
        
        scrollY = tk.Scrollbar(top_frame, orient=tk.VERTICAL,
                               command=self.__cv_yview)
        self.scrollY = scrollY
        scrollY.pack(side = tk.RIGHT, fill=tk.Y)
        cv['yscrollcommand'] = self.__scrollY_set #scrollY.set
        
        scrollX = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=cv.xview)
        scrollX.pack(side = tk.BOTTOM, fill=tk.X, anchor = 'se', expand=0)
        cv['xscrollcommand'] = scrollX.set
        
    def __ass(self):
        self.ass.new('cv', self.cv)
        self.ass.new('cv bg', 'white')
        self.ass.new_association(['set cv bg', ('cv', 'cv bg')],
                                 lambda cv, bg: cv.config(bg=bg))

        
    def draw(self, fnames, depths, top_most_path):
        pass
    def move_to(self, path):
        pass
                                 

class ViewImages:
    def __init__(self, cnf):
        self.cnf = cnf
        self.ass = Association()
        bindings = {
            'page up': ['<KeyPress-Prior>', '<KeyPress-Up>'],
            'page down': ['<KeyPress-space>', '<KeyPress-Next>', '<KeyPress-Down>'],
            'page left': ['<KeyPress-Left>'],
            'page right': ['<KeyPress-Right>'],
            'close this folder': ['<KeyPress-BackSpace>']
            }
        for name, seqs in bindings:
            ass.new('event ' + name, tuple(seqs))

        
        
        
