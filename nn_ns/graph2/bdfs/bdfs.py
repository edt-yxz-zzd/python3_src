
'''
iterative deepening depth-first search
iterative deepening breadth-depth-first search
width/depth/
'''

from itertools import islice

def bdfs(ops, implicit_graph):
    # ops will raise StopIteration to end
    # depth == 0: search root level only
    # width == 0: search nothing
    # prefix order

    g = implicit_graph
    dataG = ops.bdfs_init(g)
    ls = []
    def push(vs):
        ls.append(islice(vs, width))
    try:
        while True:
            # not ls
            roots, width, depth = \
                ops.args_for_new_round(dataG, g) # raise StopIteration
            push(roots)
            while ls:
                for v in ls[-1]:
                    break
                else:
                    ls.pop()
                    continue
                ops.test(dataG, g, v) # raise StopIteration

                if len(ls) > depth: continue
                cs = ops.iter_children(dataG, g, v)
                push(cs)
            # not ls
    except StopIteration:
        return dataG


