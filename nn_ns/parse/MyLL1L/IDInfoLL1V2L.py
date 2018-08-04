
'''
is this shift-reduce?
just forbids conflicts ?
'''

'''
topID
refID is a topID owned by item

tID = trueID = (topID, ID..., idx) idx for each item in a list


vtID = virtual_tID = (topID, ID..., (idx, 0/1))
(topID, ID..., (idx, 0)) for item[(topID, ID..., idx)].refID {min, min} # {0,0} means skip; empty vtID
(topID, ID..., (idx, 1)) for item[(topID, ID..., idx)].refID {1, max-min} if max > min
if items: prev -> curr -> next, then .../prev0/1 -> curr0; curr0->curr1; curr0/curr1->next0


rID = realID = nonempty vtID # vtID which not with {0,0}
using single-linked list to represent RIGHT relationship.
nID = nullID : a guard for this single-linked list, one for each topID
add edges of topID -> [rID], make these single-linked lists a DAG. call it RG.
it begins with one source topID, and ends with one sink nID.



the FIRST relationship topID -> [rID] and rID -> refID(that is topID) make up a directed graph too.
call it FG.

we expect FG is a DAG too. otherwise signals error.
for any vertex v in FG, for two different children x y of v, assert distinguishable(x,y)




'''


from itertools import chain
class IDInfo_top_layer:
    def __init__(self, filter_actions, defs, default_action={}):
        self.block = IDInfo_block(default_action, None, filter_actions, defs)
        self.default_action = default_action
        return
    def get_args(self):
        ls = self.block.get_args()
        ls.append(self.default_action)
        return ls
    def __repr__(self):
        return 'IDInfo_top_layer{!r}'.format(tuple(self.get_args()))
    pass

class IDInfo_block:
    def __init__(self, default_action, tID, filter_actions, defs):
        self.filter_action = IDInfo_filter_action(default_action, filter_actions)
        self.defs = [build_IDInfo_def(\
            self.filter_action.child_action, tID, def_data) for def_data in defs]
        
        return
    def __iter__(self):
        return iter(self.defs)
    def get_args(self):
        defs = []
        ls = [self.filter_action.get_args(), defs]
        for d in self:
            args = [_get_pure_name_of_IDInfo_def(d)]
            args.extend(d.get_args())
            args[:2] = args[1::-1]
            defs.append(args)
            
        return ls
    
    pass



class IDInfo_def:
    def __init__(self, parent_tID, id):
        if parent_tID == None:
            parent_tID = ()
        self.tID = chain(parent_tID, [id])
        self.id = id
        return
    pass

def build_IDInfo_def(default_action, parent_tID, def_data):
    id, type, *args = def_data
    #print(id, type)
    if type == 'token':
        return IDInfo_token_def(parent_tID, id, *args)
    elif type == 'filter':
        return IDInfo_filter_def(default_action, parent_tID, id, *args)
    elif type == 'assign':
        return IDInfo_assign_def(default_action, parent_tID, id, *args)
    else:
        print(def_data)
        raise

def _get_pure_name_of_IDInfo_def(idInfo_def):
    assert isinstance(idInfo_def, IDInfo_def)
    name = type(idInfo_def).__name__
    assert name[:7] == 'IDInfo_'
    assert name[-4:] == '_def'
    return name[7:-4]

class IDInfo_token_def(IDInfo_def):
    def __init__(self, parent_tID, id, token_type, token_value=None):
        super().__init__(parent_tID, id)
        self.token_type = token_type
        self.token_value = token_value
        return
    def get_args(self):
        ls = [self.id, self.token_type, self.token_value]
        return ls
    pass

class IDInfo_filter_def(IDInfo_def):
    def __init__(self, default_action, parent_tID, id, filter_actions, defs):
        super().__init__(parent_tID, id)
        self.block = IDInfo_block(default_action, self.tID, filter_actions, defs)
        return
    def __iter__(self):
        return iter(self.block)
    def get_args(self):
        filter_actions, defs = self.block.get_args()
        ls = [self.id, filter_actions, defs]
        return ls
    pass


class IDInfo_assign_def(IDInfo_def):
    def __init__(self, default_action, parent_tID, id, unpack, item_defs, assign_actions):
        super().__init__(parent_tID, id)
        self.unpack = unpack
        self.assign_action = IDInfo_assign_action(default_action, assign_actions)
        self.items = [IDInfo_item_def(self.assign_action.child_action, self.tID, i, *args) \
                      for i, args in enumerate(item_defs)]
        return
    def __iter__(self):
        return iter(self.items)
    def get_args(self):
        ls = [self.id, self.unpack]
        ls.append([d.get_args() for d in self])
        ls.append(self.assign_action.get_args())
        return ls
    pass


class IDInfo_item_def(IDInfo_def):
    def __init__(self, default_action, parent_tID, id, tags, unpack, refID, min_max, item_actions):
        super().__init__(parent_tID, id)
        self.tags = tags
        self.unpack = unpack
        self.refID = refID
        self.min, self.max = min_max
        self.item_action = IDInfo_item_action(default_action, item_actions)


        if self.max == None:
            self.max = float('inf')
            
        self.none_max = self.max
        if self.none_max == float('inf'):
            self.none_max = None

        assert self.max != None
        assert self.none_max != float('inf') # it seems like a bug for repr(float('inf')) == 'inf'
        self.min_max = self.min, self.none_max
        return
    def get_args(self):
        ls = self.tags, self.unpack, self.refID, self.min_max, \
             self.item_action.get_args()
        return ls
    pass

class IDInfo_action:
    def __init__(self, default_action, new_actions):
        self.new_actions = new_actions
        self.self_action = default_action.copy() #collections.defaultdict(list)
        self.child_action = default_action.copy()
        
        self.objname_map = {'self':self.self_action, 'child':self.child_action}
        for a in new_actions:
            self.set_action(*a)
        return
    def set_action(self, what_fix , object_names, action_names, method_names):
        for object_name in object_names:
            obj = self.objname_map[object_name]
            for a in action_names:
                obj[(what_fix, a)] = tuple(method_names)
        return
    def get_args(self):
        return self.new_actions
    pass


class IDInfo_filter_action(IDInfo_action):pass
class IDInfo_assign_action(IDInfo_action):pass
class IDInfo_item_action(IDInfo_action):pass







