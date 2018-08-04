'''
strongly connected components
https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
Tarjan's strongly connected components algorithm


Stack invariant

Nodes are placed on a stack in the order in which they are visited. When the depth-first search recursively visits a node v and its descendants, those nodes are not all necessarily popped from the stack when this recursive call returns. The crucial invariant property is that a node remains on the stack after it has been visited if and only if there exists a path in the input graph from it to some node earlier on the stack.

At the end of the call that visits v and its descendants, we know whether v itself has a path to any node earlier on the stack. If so, the call returns, leaving v on the stack to preserve the invariant. If not, then v must be the root of its strongly connected component, which consists of v together with any nodes later on the stack than v (such nodes all have paths back to v but not to any earlier node, because if they had paths to earlier nodes then v would also have paths to earlier nodes which is false). The connected component rooted at v is then popped from the stack and returned, again preserving the invariant.


def strongly_connected_components(g):
    # directed_graph -> [[vertex]]
    #   extra output: low_pt, preorder
    #
    # postcondition:
    #   components list in reversed topological ordering
    #   preorder of vertices in each component is reversed
    #
    # preordering dfs
    unvisited = -1
    max_visiting = -2 # visiting <= -2
    preorder = {}
    stack = []
    low_pt = {}
    components = []
        # components in reversed topo order
        # preorder reversed in each component

    def pop_new_component(v):
        component = []
        components.append(component)
        while True:
            u = stack.pop()
            component.append(u)
            if u is v:
                return
        pass
    def is_unvisited(v):
        # -1
        return preorder.get(v, unvisited) == unvisited
    def is_visiting(v):
        # visiting = max_visiting - preorder[v]
        return preorder.get(v, unvisited) <= max_visiting
    def set_visited(v):
        preorder[v] = max_visiting - preorder[v]
    def get_preorder(v):
        order = preorder[v]
        if order < 0:
            return max_visiting - order
        return order
    def recur_preordering_dfs(may_parent, v):
        if is_unvisited(v):
            # tree_edge

            # set visiting
            order = len(preorder)
            preorder[v] = max_visiting - order
            low_pt[v] = order

            #
            # v enter
            stack.append(v)
            for u in g.vtx2iter_vertices(v):
                recur_preordering_dfs(v, u)
                # update low_pt[v]
                low_pt[v] = min(low_pt[v], low_pt[u])

            # v exit
            # is v component root?
            set_visited(v)
            if low_pt[v] < preorder[v]:
                # not component root
                # remain on stack
                pass
            else:
                pop_new_component(v)
            return
        elif is_visiting(v):
            # back_edge

            # update low_pt[may_parent]
            if may_parent is not None:
                low_pt[may_parent] = min(low_pt[may_parent], low_pt[v])
            else:
                # v is root
                pass
        else:
            # v is not root; may_parent is not None
            # cross_edge or forward_edge
            return
        return
    for v in g.vertices():
        recur_preordering_dfs(None, v)
    return components
'''



