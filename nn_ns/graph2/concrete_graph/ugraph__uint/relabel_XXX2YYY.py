

__all__ = '''
    relabel_XXX2YYY
    '''.split()


def relabel_XXX2YYY(*
    ,old_XXX2old_YYY

    ,new_XXX2old_XXX
    ,old_YYY2new_YYY
    ):
    '-> new_XXX2new_YYY'
    num_XXXs = len(new_XXX2old_XXX)
    assert num_XXXs == len(old_XXX2old_YYY)
    num_YYYs = len(old_YYY2new_YYY)

    new_XXX2new_YYY = [
        old_YYY2new_YYY[old_XXX2old_YYY[old_XXX]]
        for old_XXX in new_XXX2old_XXX
        ]
    return tuple(new_XXX2new_YYY)


