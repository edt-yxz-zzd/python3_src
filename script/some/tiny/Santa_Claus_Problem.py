'''
Santa Claus Problem

Beautiful Code
Beautiful Concurrency

I want to show you a complete, runnable concurrent program using STM. A well-known example is the so-called Santa Claus problem, originally attributed to Trono:
Santa repeatedly sleeps until wakened by either all of his nine reindeer,
back from their holidays, or by a group of three of his ten elves.
If awakened by the reindeer, he harnesses each of them to his sleigh,
delivers toys with them and finally unharnesses them
(allowing them to go off on holiday). If awakened by a group of elves,
he shows each of the group into his study, consults with them on toy R&D
and finally shows them each out (allowing them to go back to work).
Santa should give priority to the reindeer in the case that there is both
a group of elves and a group of reindeer waiting.
'''

import threading
import queue
import time
import random
import sys

sleep = lambda t=2: time.sleep(random.triangular(0.3*t, 5*t, t))
new_cv = lambda: threading.Condition(threading.Lock())



class Print:
    lock = threading.Lock()
    old_print = print
    @staticmethod
    def __call__(*args, **kw):
        with Print.lock:
            Print.old_print(*args, **kw)

print = Print()


class Channel:
    #cv = new_cv()
    def __init__(self, batch_size, condition):
        assert batch_size > 0
        
        self.size = batch_size # const
        self.batchs = queue.Queue()
        self.batch = []
        self.lock = threading.Lock()
        self.cv = condition
        
    def add(self, promise):
        with self.lock:
            self.batch.append(promise)
            if len(self.batch) == self.size:
                self.batchs.put(self.batch)
                self.batch = []
                with self.cv:
                    self.cv.notify()

class Future:
    def __init__(self):
        self.data = None
        self.cv = new_cv()
    def get(self):
        with self.cv:
            while not self.data:
                self.cv.wait()
            data, self.data = self.data, ('dead',)
            if len(data) == 1:
                raise logic-error
            case, var = data
            if case == 'return':
                return var
            raise var

class Promise:
    def __init__(self, future):
        self.future = future
    def set_exc(self, exc):
        self.set('raise', exc)
    def set_var(self, var):
        self.set('return', var)
    def set(self, case, var):
        with self.future.cv:
            self.future.data = (case, var)
            self.future.cv.notify()

class Counter:
    def __init__(self, n=0, notify = lambda n:None):
        self.n = n
        self.lock = threading.Lock()
        self.notify = notify
        
    def transform(self, f):
        with self.lock:
            self.n = f(self.n)
            self.notify(self.n)
    def inc(self):
        self.transform(lambda n:n+1)
    
    def dec(self):
        self.transform(lambda n:n-1)

    def get(self):
        with self.lock:
            return self.n
        
    
def make_future():
    future = Future()
    promise = Promise(future)
    return future, promise


'''
class Task_NotifyMe:
    def __init__(self, condition, args=None, transform=None):
        self.cv = condition
        self.args = args
        self.transform = transform

    def get_args(self):
        return self.args
    def transform_args(self, *args, **kw):
        with self.cv:
            self.args = self.transform(self.args, *args, **kw)
            self.cv.notify()
        
    def __call__(self, args):
        with self.cv:
            self.args = args
            self.cv.notify()

    pass'''



class Life:
    def __init__(self, name, channel):
        self.name = name
        self.channel = channel
        
    def __call__(self):
        while True:
            self.holiday()
            self.work()
    def holiday(self):
        print(self.name, 'holiday')
        sleep(16)
    def do_work(self, f, task_arg):
        print(self.name, 'work')
        sleep(2)
        f(task_arg)
    def work(self):
        ear, promise = make_future()
        self.channel.add(promise)
        f, task_arg = ear.get()
        self.do_work(f, task_arg)
        
            
    
    
class Elf(Life): pass
class Reindeer(Life):pass


class Worker:
    def __init__(self, name, channels_cv, channels, task_arg_ls):
        assert len(channels) == len(task_arg_ls)
        self.channels = channels
        self.task_arg_ls = task_arg_ls
        self.cv = channels_cv
        self.name = name
    def run(self):
        while True:
            self.sleep()
            self.work()
    def sleep(self):
        print(self.name, 'sleep')
        with self.cv:
            self.cv.wait()
        
    def work(self):
        while self.do_work(): pass
    def do_work(self):
        with self.cv:
            #self.cv.wait()
            print(self.name, 'work')
            for channel, task_arg in zip(self.channels, self.task_arg_ls):
                batchs = channel.batchs
                #if len(batchs):
                if batchs.qsize():
                    try:
                        batch = batchs.get_nowait()
                        break
                    except queue.Empty:
                        print('logic error', file=sys.stderr)
                        raise
            else:
                # nothing to do; end the working loop
                return False

        print('--------begin--------')
        future, promise = make_future()
        def notify(n, promise=promise):
            if n == 0:
                promise.set_var(None)
                
        c = Counter(len(batch), notify)
        def task(s):
            print(s)
            c.dec()
            
        for promise in batch:
            promise.set_var((task, task_arg))

        future.get()
        
        batchs.task_done()
        print('-------- end --------')
        return True # continue working
            
            




def main():
    channels_cv = new_cv()
    channels = reindeer_channel, elf_channel = \
               [Channel(9, channels_cv), Channel(3, channels_cv)]
    task_arg_ls = ['delivering toys', 'meeting in the study']

    elves = [Elf('elf<{}>'.format(i), elf_channel) for i in range(10)]
    reindeer = [Reindeer('reindeer<{}>'.format(i), reindeer_channel) for i in range(9)]

    lives = elves + reindeer
    for life in lives:
        t = threading.Thread(target=life)
        t.daemon = True
        t.start()

    Santa = Worker('Santa Claus', channels_cv, channels, task_arg_ls)

    Santa.run()
main()










