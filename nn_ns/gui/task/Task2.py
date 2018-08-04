from collections import OrderedDict

class TaskInfo:
    def __init__(self, generator, concepts, filter_taskstate_ls):
        self.generator = generator
        self.concepts = concepts
        self.filter_taskstate_ls = filter_taskstate_ls

class Task:
    def __init__(self):
        self.new_id = 1
        self.tasks = OrderedDict()

    def __new_task(self):
        task = self.new_id
        self.new_id += 1
        return task

    def __std_concepts(self, concepts):
        return frozenset(concepts)
    def __std_overwrite_concepts_ls(self, overwrite_concepts_ls):
        return tuple(self.__std_concepts(cs) for cs in overwrite_concepts_ls)
    def __std_filter_taskstate_ls(self, filter_taskstate_ls):
        return tuple(self.__std_taskstate(ts) for ts in filter_taskstate_ls)
    def __std_taskstate(self, taskstate):
        task, state = taskstate
        self.check_task(task)
        if type(state) != bool:
            raise TypeError('state should be bool, indicating whether task is not finish')
        
    
    def new(self, generator, concepts,
            overwrite_concepts_ls, filter_taskstate_ls):

        
        for cs in overwrite_concepts_ls:
            to_del = []
            for task, info in self.tasks.items():
                if cs <= info.concepts:
                    to_del.append(task)
                    break
            for task in to_del:
                del self.tasks[task]

        info = TaskInfo(generator, concepts, filter_taskstate_ls)
        task = self.__new_task()
        self.tasks[task] = info
        return task

    def check_task(self, task):
        if not type(task) == int or not 0 < task < self.new_id:
            raise ValueError('unknown task: {!r}'.format(task))
        
    def delete(self, task):
        self.check_task(task)
        self.tasks.pop(task, None)

    def __is_good(self, filter_taskstate_ls):
        for task, state in filter_taskstate_ls:
            if (task in self.tasks) != state:
                return False
        return True
    
    def step(self):
        tasks = self.tasks
        while tasks:
            task, info = tasks.popitem(last=False)
            if not self.__is_good(info.filter_taskstate_ls):
                continue # delete
            
            g = info.generator
            for _ in g: break
            else:
                # end/delete
                continue
            tasks[task] = info # move to end
            return True
        return False

    def __iter__(self):
        while self.step():
            yield







class Association:
    def __init__(self):
        self.item2value = {}
        self.item2associations = {} # association is (name, items)
        self.association2function = {}
        self.item2new_value = {}
        self.new_associations = set()

    def check(self):
        if len(self.item2value) != len(self.item2associations):
            raise logic-error
        
    def exists(self, item):
        return item in self.item2value
    def check_item(self, item):
        if not self.exists(item):
            raise ValueError('unknown item: {!r}'.format(item))
        
    def set(self, item, value):
        self.check_item(item)
        self.item2new_value[item] = value

    def new(self, item, value):
        if self.exists(item):
            raise ValueError('item exists')
        self.item2value[item] = value
        self.item2associations[item] = set()
    def delete(self, item):
        self.check_item(item)
        ls = list(self.item2associations[item])
        for a in ls:
            self.delete_association(a)

        assert not self.item2associations[item]
        del self.item2associations[item]
        del self.item2value[item]
        self.item2new_value.pop(item, None)
        
        

    def __std_association(self, association):
        name, items = association
        items = tuple(items)
        for item in items:
            self.check_item(item)
        return name, items
    
    def new_association(self, association, f):
        association = self.__std_association(association)
        if association in self.association2function:
            raise ValueError('association exists: {}'.format(association))
        
        name, items = association
        for item in items:
            self.item2associations[item].add(association)
        self.association2function[association] = f
        self.new_associations.add(association)
        
        
    def delete_association(self, association):
        if association not in self.association2function:
            raise ValueError('association not exists: {!r}'.format(association))
        del self.association2function[association]

        name, items = association
        for item in items:
            self.item2associations[item].remove(association)
        self.new_associations.discard(association)

    def update_ls(self):
        ls = []
        while True:
            for item, value in self.item2new_value:
                if value != self.item2value[item]:
                    self.new_associations.update(self.item2associations[item])
                    self.item2value[item] = value
            self.item2new_value.clear()

            if not self.new_associations:
                break

            ass, self.new_associations = self.new_associations, set()
            assert not self.item2new_value
            assert not self.new_associations
            
            for a in ass:
                if a not in self.association2function:
                    # may be deleted in this loop
                    continue
                f = self.association2function[a]
                name, items = a
                args = tuple(self.item2value[item] for item in items)
                #f(*args)
                ls.append((f, args))

        return ls
    

    
                
        
        













        
