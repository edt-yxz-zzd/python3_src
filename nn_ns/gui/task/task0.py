

import itertools, collections

def to_tuple(iterable):
    if type(iterable) == tuple:
        return iterable
    return tuple(iterable)

class TaskInfo:
    work_states = frozenset(['wait', 'work', 'finish'])
    @staticmethod
    def is_work_state(state):
        return state in TaskInfo.work_states
    @staticmethod
    def check_work_state(state):
        if not TaskInfo.is_work_state(state):
            raise ValueError('work_state should be one of {}, but not {!r}'\
                             .format(TaskInfo.work_states, state))
        return True
    
    def __init__(self, f, task_workstates_ls,
                 concepts, work_state = 'wait', free_state = False,
                 ref_count = 1):
        self.check_work_state(work_state)
        if type(free_state) != bool:
            raise ValueError('type(free_state) != bool')
        if type(ref_count) != int or ref_count < 0:
            raise ValueError('type(ref_count) != int or ref_count < 0')
        self.f = f
        self.task_workstates_ls = task_workstates_ls
        self.concepts = concepts
        self.work_state = work_state
        self.free_state = free_state
        self.ref_count = ref_count
        self.check()

    def check(self):
        if not self.ref_count >= (not self.free_state) + (self.work_state == 'work'):
            raise logic-error
        return True
    
    def is_dead(self):
        return self.ref_count == 0
        
class Task:
    '''FIFO task manager

public method:
__init__
new/free - each task should be freed
next/wait/finish - 'next' marks the task to be in 'work' state, should call wait/finish

other methods are all private.
'''



    def __init__(self):
        self.task2info = {}
        self.tasks = collections.deque()
        
    def new(self, f, task_workstates_ls,
            concepts, overwrite_concepts_ls):
        '''allocate a new task ID

task_workstates_ls:
    before 'next()' return, we will check whether all tasks' states agree with this list
overwrite_concepts_ls:
    all previous tasks will be cancel if their concepts match this list
    '''
        ts = []
        ls = []
        for task, workstates in task_workstates_ls:
            ts.append(task)
            workstates = to_tuple(workstates)
            for state in workstates:
                TaskInfo.chech_work_state(state)
            ls.append((task, workstates))
    
        if False == self.inc_ref_count_tasks(ts):
            return None

        task_workstates_ls = tuple(ls)

        concepts = frozenset(concepts)
        overwrite_concepts_ls = tuple(frozenset(cs)
                                      for cs in overwrite_concepts_ls)
        to_kill = []
        for task, info in task2info.items():
            if self.is_free(task):
                continue
            
            cs = self.get_concepts(task)
            for sub in overwrite_concepts_ls:
                if sub <= cs:
                    to_kill.append(i)
                    break
        self.free_task_idc(to_kill)
        task = self.add(f, task_workstates_ls, concepts)
        return task

    def free_task_idc(self, idc):
        if not idc:
            return
        tasks = list(self.tasks)
        for idx in idc:
            t = tasks[idx]
            assert t is not None
            tasks[idx] = None
            self.free(t)
            
        self.tasks.clear()
        self.tasks.extend(t for t in tasks if t is not None)
        
    def add(self, f, task_workstates_ls, concepts):
        task = self.new_task()
        info = TaskInfo(f, task_workstates_ls, concepts)

        assert task not in self.task2info

        self.task2info[task] = info
        return task
    def remove(self, task):
        del self.task2info[task]
        self.del_task(task)
        
        
    def free(self, task):
        assert not self.is_free(task)
        self.set_state_free(task)
        if self.is_dead(task):
            self.remove(task)
        
##
##    def empty(self):
##        return bool(self.tasks)
    def next(self):
        while True:
            task = self.tasks.popleft()
            if self.get_work_state(task) == 'wait':
                self.set_state_work(task)
                return task
        return None
    

    def wait(self, task):
        assert self.is_work(task)
        
        self.set_state_wait(task)
        if self.is_dead(task):
            self.remove(task)
        else:
            self.tasks.append(task)

    def finish(self, task):
        assert self.is_work(task)
        self.set_state_finish(task)
        if self.is_dead(task):
            self.remove(task)
    
        
        
        
        

        
