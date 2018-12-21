
'''
fake_aedge
    like fface, fvertex
'''

def make_hedge2fake_aedge(*, num_hedges, hedge2another_hedge):
    # -> hedge2fake_aedge
    assert callable(hedge2another_hedge)
    assert num_hedges & 1 == 0 # even

    #num_aedges = num_hedges//2
    hedge2fake_aedge = [None]*num_hedges
    fake_aedge = 0
    for hedge in range(num_hedges):
        other = hedge2another_hedge(hedge)
        assert hedge != other
        assert hedge2another_hedge(other) == hedge
        if hedge2fake_aedge[hedge] is None:
            hedge2fake_aedge[hedge] = fake_aedge
            hedge2fake_aedge[other] = fake_aedge
            fake_aedge += 1

    num_aedges = fake_aedge; del fake_aedge
    assert 2*num_aedges == num_hedges
    return hedge2fake_aedge

