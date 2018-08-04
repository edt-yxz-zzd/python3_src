

__all__ = '''
    def_id_nullable
    left_recur_detect
    left_recur_detect_ex
    '''.split()


def def_id_nullable(def_id2itemss, item_nullable):
    '''\
def_id_nullable :: (def_id2itemss, item_nullable) -> def_id2nullable
def_id2nullable :: {DefID : nullable}
def_id2itemss :: {DefID : [[items]]}
item_nullable :: (item, def_id2nullable) -> nullable
nullable = bool # False == DefID should consume token
'''
    L = len(def_id2itemss)
    def_id2itemss = dict(def_id2itemss)
    #def_id2nullable = defaultdict(lambda: False)
    def_id2nullable = {k:False for k in def_id2itemss}
    done = False
    while not done:
        done = True
        for def_id, itemss in list(def_id2itemss.items()):
            assert not def_id2nullable[def_id]
            # any(all(null...))
            for items in itemss:
                if all(map(lambda item:item_nullable(item, def_id2nullable),items)):
                    def_id2nullable[def_id] = True
                    del def_id2itemss[def_id]
                    done = False
                    break
    assert len(def_id2nullable) == L
    return def_id2nullable


def left_recur_detect_ex(
    def_id2itemss, item_nullable, item_heads, def_id2nullable = None):
    # like left_recur_detect, but return (left_recur_def_ids, def_id2nullable)
    if def_id2nullable is None:
        def_id2nullable = def_id_nullable(def_id2itemss, item_nullable)
    left_recur_def_ids = left_recur_detect(
        def_id2itemss, item_nullable, item_heads, def_id2nullable)
    return left_recur_def_ids, def_id2nullable

def left_recur_detect(
    def_id2itemss, item_nullable, item_heads, def_id2nullable = None):
    '''\
left_recur_detect
    :: (def_id2itemss, item_nullable, item_heads, def_id2nullable = None)
    -> [left_recur_def_id]
def_id2itemss :: {DefID : [[items]]}
item_nullable :: (item, def_id2nullable) -> nullable
item_heads :: (item, def_id2nullable) -> [def_id] # direct beginning def_ids
def_id2nullable :: {DefID : nullable}
nullable = bool # False == DefID should consume token
'''

    if def_id2nullable is None:
        def_id2nullable = def_id_nullable(def_id2itemss, item_nullable)
    # def_id2heads # direct heads
    def_ids = set(def_id2itemss.keys())
    def_id2heads = {k:set() for k in def_id2itemss.keys()}
    for def_id, itemss in def_id2itemss.items():
        def_id_heads = def_id2heads[def_id]
        for items in itemss:
            for item in items:
                heads = item_heads(item, def_id2nullable)
                def_id_heads.update(heads)
                if not item_nullable(item, def_id2nullable):
                    break

    # def_id2heads # all heads
    done = False
    while not done:
        done = True
        for heads in def_id2heads.values():
            assert heads <= def_ids
            L = len(heads)
            ls = list(heads)
            heads.update(*(def_id2heads[head] for head in ls))
            if len(heads) != L:
                done = False
    left_recur_def_ids = [def_id
        for def_id, heads in def_id2heads.items() if def_id in heads]
    return left_recur_def_ids



