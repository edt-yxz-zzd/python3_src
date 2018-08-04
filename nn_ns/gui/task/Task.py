

from sand import index_manager_t as IndexManager

from collections import OrderedDict

class TaskFIFO:
    def __init__(self):
        self.tasks = OrderedDict()
        self.old_tasks = {}
        self.mngr = IndexManager()
        self.check()

    def is_finished(self, task):
        self.check()
        self.check_task(task)
        return task in self.old_tasks
    
    def check(self):
        assert len(self.mngr) == len(self.old_tasks) + len(self.tasks)
        
##    def __contain__(self, task):
##        return task in self.mngr
    def check_task(self, task):
        if task not in self.mngr:
            raise ValueError('unknown task')

    def get_data(self, task):
        self.check()
        self.check_task(task)
        if task in self.tasks:
            return self.tasks[task]
        return self.old_tasks[task]
    
        
        
    def new(self, data):
        self.check()
        
        task = self.mngr.new()
        assert task not in self.tasks
        self.tasks[task] = data
        
        self.check()
        return task

    def delete(self, task):
        self.check()

        self.check_task(task)
        self.mngr.delete(task)
        if task in self.old_tasks:
            assert task not in self.tasks
            del self.old_tasks[task]
        else:
            del self.tasks[task]

        
        self.check()

    def next(self):
        self.check()
        if not self.tasks:
            return None

        task, data = self.tasks.popitem(last=False)
        self.old_tasks[task] = data

        
        self.check()
        return task, data

        
    def update(self, task, data):
        self.check()
        self.check_task(task)
        if task in self.old_tasks:
            del self.old_tasks[task]
        else:
            self.tasks.move_to_end(task)

        self.tasks[task] = data
        self.check()


def to_tuple(ls):
    if type(ls) == tuple:
        return ls
    return tuple(ls)



class RefTaskFIFO:
    def __init__(self):
        self.tasks = TaskFIFO()
        self.task2ref_count = {}
        self.task2ref_tasks = {}
        self.deleted_tasks = set()
        

    def new(self, data, ref_tasks):
        ref_tasks = to_tuple(ref_tasks)
        for t in ref_tasks:
            self.check_task(t)
        for t in ref_tasks:
            self.task2ref_count[t] += 1

        task = self.tasks.new(data)
        self.task2ref_tasks[task] = ref_tasks
        self.task2ref_count[task] = 1

    def check_task(self, task):
        self.tasks.check_task(task)
        if task in self.deleted_tasks:
            raise ValueError('task has been deleted')
        
    def is_finished(self, task):
        self.check_task(task)
        return self.tasks.is_finished(task)
    
    
    def get_state(self, task):
        self.tasks.check_task(task)
        if task in self.deleted_tasks:
            return 'deleted-but-ref'
        if self.is_finish(task):
            return 'finished'
        return 'waiting'

    
    def get_data(self, task):
        self.check_task(task)
        return self.tasks.get_data(task)
    
    def delete(self, task):
        self.check_task(task)
        self.deleted_tasks.add(task)
        self.__dec_refcount(task)
    def __dec_refcount(self, task):
        if self.task2ref_count[task] < 1:
            raise ReferenceError('logic error')
        self.task2ref_count[task] -= 1
        if self.task2ref_count[task] == 0:
            # delete
            del self.task2ref_count[task]
            ref_tasks = self.task2ref_tasks.pop(task)
            self.tasks.delete(task)
            self.deleted_tasks.remove(task)
            for t in ref_tasks:
                self.__dec_refcount(t)

    

    def next(self):
        while True:
            taskdata = self.tasks.next()
            if taskdata is None:
                return None
            

            task, data = taskdata
            if task not in self.deleted_tasks:
                return task, data
        return None
    

        
    def update(self, task, data):
        self.check_task(task)
        self.tasks.update(task, data)



class FilterRefTaskFIFO:
    states = frozenset(['waiting', 'finished', 'deleted-but-ref'])
    def __init__(self, drop):
        self.tasks = RefTaskFIFO()
        self.drop = drop

    def check_states(self, states):
        for s in states:
            self.check_state(s)
    def check_state(self, state):
        if state not in self.states:
            raise ValueError('state should be {}; unknown state: {}'\
                             .format(self.states, state))
        

    def __std_ls(self, filter_taskstates_ls):
        taskstates_ls = tuple((task, tuple(states)) for task, states in filter_taskstates_ls)
        for task, states in taskstates_ls:
            self.check_task(task)
            self.check_states(states)
        return taskstates_ls
        
    def new(self, data, filter_taskstates_ls):
        taskstates_ls = self.__std_ls(filter_taskstates_ls)

        ref_tasks = tuple(task for task, _ in taskstates_ls)
        task = self.tasks.new((data, taskstates_ls), ref_tasks)
        return task

    def delete(self, task):
        self.check_task(task)
        self.tasks.delete(task)

    def check_task(self, task):
        self.tasks.check_task(task)
        
    def get_state(self, task):
        self.check_task(task)
        return self.tasks.get_state(task)
    
    def __is_good(self, taskstates_ls):
        for t, ss in taskstates_ls:
            state = self.get_state(t)
            if state not in ss:
                return False
        return True
    
    def get_data_filter(self, task):
        self.check_task(task)
        return self.tasks.get_data(task)
        
    def next(self):
        while True:
            taskdatals = self.tasks.next()
            if taskdatals is None:
                return None

            task, (data, taskstates_ls) = taskdatals
            if self.__is_good(taskstates_ls):
                return task, data
            #self.delete(task)
            self.drop(task, data)
            
        pass

    def update(self, task, data):
        __data, filterls = self.get_data_filter(task)
        self.task.update(task, (data, filterls))



class OverwriteFilterRefTaskFIFO:
    


                
                
    

        

        
    

