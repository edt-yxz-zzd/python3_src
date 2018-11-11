
def lnk2list(lnk):
    ls = []
    while lnk:
        lnk, last = lnk
        ls.append(last)
    ls.reverse()
    return ls


