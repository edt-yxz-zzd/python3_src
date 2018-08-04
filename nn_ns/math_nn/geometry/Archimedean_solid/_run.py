



from nn_ns.math_nn.geometry.Archimedean_solid.\
     Archimedean_solid__using_sympy__calc_coordinate import *


skips = {(3, 8, 8), (3, 10, 10), (5, 6, 6), # truncate
         (3, 4, 5, 4), (3, 5, 3, 5), # mid_truncate
         
         (4, 6, 8), (4, 6, 10), (3, 4, 4, 4),
         (3,3,3,3,3), (3, 3, 3, 3, 4), (3, 3, 3, 3, 5)}
try:
    for solid in solids:#[solids.index():]:
        print(solid)
        if solid in skips:
            print('skip...')
            continue
        cs = ASRP_solid2coordinates(solid, solid2g[solid])
        print(cs)

except:
    raise


