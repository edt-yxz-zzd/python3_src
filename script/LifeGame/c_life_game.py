from ._life_game import life_game

def life_game_steps(xys, n):
    assert n >= 0
    ls = [(int(x), int(y)) for x, y in xys]
    #print(len(ls), ls[0], n)
    return set(life_game(ls, n))
