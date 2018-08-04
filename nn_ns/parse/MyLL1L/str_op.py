

def join_children(parent, children, *, newline = '\n', indent = ' '*4):
    m = newline + indent
    lines = [parent]
    s = newline.join(children)
    lines.extend(s.split(newline))
    return m.join(lines)
