

'''
transform to
transform topo_to

transform in {truncate, mid_truncate, snub3}
snub3 means snub on a solid whose num_faces_per_vtx == 3



truncate([A]*t)) ==>> [t, 2*A, 2*A]
mid_truncate([A]*t)) ==>> [t, A, t, A]

truncate_topo([A,B]*(t/2)) ==>> [t, 2*A, 2*B]
mid_truncate_topo([A,B]*(t/2)) ==>> [t, A, t, B] = [4, A, 4, B] = (3, 4, 4, 4)
snub3_topo([A]*3) ==>> [3,3,3,3,A]
'''

truncate_to = {
    (3, 3, 3):(3, 6, 6),
    (4, 4, 4):(3, 8, 8),
    (5, 5, 5):(3, 10, 10),
    (3, 3, 3, 3):(4, 6, 6),
    (3, 3, 3, 3, 3):(5, 6, 6),
    }
assert len(truncate_to) == 5 == len(set(truncate_to.values()))



mid_truncate_to = {
    (3, 3, 3):(3, 3, 3, 3),
    (4, 4, 4):(3, 4, 3, 4),
    (5, 5, 5):(3, 5, 3, 5),
    (3, 3, 3, 3):(3, 4, 3, 4),
    (3, 3, 3, 3, 3):(3, 5, 3, 5),
    }
assert len(mid_truncate_to) == 5
assert len(set(mid_truncate_to.values())) == 3


truncate_topo_to = {
    (3, 4, 3, 4):(4, 6, 8),
    (3, 5, 3, 5):(4, 6, 10),
    }
mid_truncate_topo = {
    (3, 4, 3, 4):(3, 4, 4, 4)
    }
snub3_topo_to = {
    (3, 3, 3):(3, 3, 3, 3, 3),
    (4, 4, 4):(3, 3, 3, 3, 4),
    (5, 5, 5):(3, 3, 3, 3, 5),
    }

'''

transform_to = {
    (3, 3, 3):,
    (3, 6, 6):,
    (3, 8, 8):,
    (3, 10, 10):,
    (4, 4, 4):,
    (4, 6, 6):,
    (4, 6, 8):,
    (4, 6, 10):,
    (5, 5, 5):,
    (5, 6, 6):,
    (3, 3, 3, 3):,
    (3, 4, 3, 4):,
    (3, 4, 4, 4):,
    (3, 4, 5, 4):,
    (3, 5, 3, 5):,
    (3, 3, 3, 3, 3):,
    (3, 3, 3, 3, 4):,
    (3, 3, 3, 3, 5):,
    }
'''
