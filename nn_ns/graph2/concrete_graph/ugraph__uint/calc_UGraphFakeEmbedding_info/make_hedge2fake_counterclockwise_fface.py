
def make_hedge2fake_counterclockwise_fface(*
    ,hedge2fake_clockwise_fface
    ,hedge2fake_clockwise_prev_hedge_around_vertex
    ):
    num_hedges = len(hedge2fake_clockwise_fface)
    return tuple(hedge2fake_clockwise_fface[
            hedge2fake_clockwise_prev_hedge_around_vertex[hedge]]
            for hedge in range(num_hedges)
            )

