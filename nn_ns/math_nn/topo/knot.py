
'''
TODO: knot -> link
TODO: knot diagram -> multiedged planar graph -> planar graph (add vertices)


A polygonal knot is a knot whose image in R3 is the union of a finite set of line segments.
A tame knot is any knot equivalent to a polygonal knot.

Point3D a = (Fractional a, Fractional a, Fractional a)
PolygonalKnot a = [Point3D a]
    -- orientation of knot is p[i]->p[i+1]; len < 4 is unknot


KnotDiagram crossing = ([[crossing]], Map crossing is_overpass_x_arrow)
    -- orientation of knot is p[i]->p[i+1]
    -- crossing presents twice
    -- begin with an overpass which contains overcrossings
    -- over-/under-pass alternative ==>> [2 | len(passes)]
    -- end with an underpass
    -- allow no passes but not allow pass with no crossing
    -- each crossing assigned 2 arrows, form O-x'y'z with z-axis arrow
    -- arrow is required to draw diagram into plane
    -- is right handed crossing <==> is overpass x_arrow
KnotPlanarGraph crossing vertex = Map point neighbors
    -- without vertex, grahp be multi-edged
    -- point = crossing | vertex
    -- neighors :: [point] # counter-clockwise
    -- p_vertex -> (prev_undercrossing, succ_overcrossing)
    -- n_vertex -> (prev_overcrossing, succ_undercrossing)
    -- right_handed_crossing -> (over_prev, under_prev, over_succ, under_succ)
    -- left_handed_crossing -> (over_prev, under_succ, over_succ, under_prev)
    -- 

Relator = [(i, exp)] # II x[i][j]^exp[j] {j}
GroupPresentation = (N, [Relator])





each crossing of the diagram
overcrossing
undercrossing
over-strand
under-strand
arc
handedness
right handed crossing
    for arbitrary orientation,
    rotate under-strand to over-strand in clockwise
    over-strand as x-axis, under-strand as y-axis, z-axis points to reader
    
from wiki: Knot (mathematics)
    Peter Tait in 1877
    knot diagram ==>> labeled multi-edged planar graph embedding
        -> multi-edged planar graph embedding
        -> color each face white or black s.t.
            unbounded face (external face) be black
            any two faces that share a boundary edge have opposite colors
            (<<== Jordan curve theorem implies that there is exactly one such coloring.)
        -> new planar graph embedding <<== white face as vertex, crossing as edge
        -> label edge with +/-1
            underpass -> new edge -> overpass is
                clockwise ==>> left edge (solid) ==>> +1
                counter-clockwise ==>> right edge (dashed) ==>> -1
    
    labeled multi-edged planar graph embedding ==>> knot diagram
        -> medial graph embedding <<== middle point of edge as vertex, each face generates a cycle as subgraph
        -> color vertex with old edge label
        -> knot diagram <<== vertex as crossing, s.t.
            +1 ==>> underpass -> old edge -> overpass is clockwise
            -1 ==>> underpass -> old edge -> overpass is counter-clockwise

mine:
    knot diagram ==>> colored multi-edged planar graph embedding with an overpass
    -> multi-edged planar graph embedding
    -> color each crossing with +/-1
        right_handed_crossing ==>> +1
        left_handed_crossing ==>> -1
    -> split edge which connects overcrossing and undercrossing by a vertex
    -> give an overpass = vertex->overcrossing
'''

from collections import defaultdict
from itertools import chain, cycle, count
from fractions import Fraction

def is_right_hand_xy(x_arrow, y_arrow):
    xx, xy = x_arrow
    yx, yy = y_arrow
    return is_right_hand_xyz((xx,xy,0), (yx,yy,0), (0,0,1))
def is_right_hand_xyz(x_arrow, y_arrow, z_arrow):
    return calc_volume(x_arrow, y_arrow, z_arrow) > 0

def calc_volume(x_arrow, y_arrow, z_arrow):
    x0, y0, z0 = x_arrow
    x1, y1, z1 = y_arrow
    x2, y2, z2 = z_arrow

    return x0*(y1*z2-z1*y2) - y0*(x1*z2-z1*x2) + z0*(x1*y2-y1*x2)

def is_point(p):
    return type(p) is tuple and all(type(x) is Fraction for x in p)
def is_point_dim(p, n):
    return is_point(p) and len(p) == n
def is_point3D(p):
    return is_point_dim(p, 3)
def is_point2D(p):
    return is_point_dim(p, 2)


def to_fraction_points(points):
    return tuple(tuple(map(Fraction, p)) for p in points)


def maybe_region_interset(region0, region1):
    # return region or None
    minp0, maxp0 = region0
    minp1, maxp1 = region1
    minp = tuple(map(max, minp0, minp1))
    maxp = tuple(map(min, maxp0, maxp1))
    maybe_region = minp, maxp
    region = line_segment2D_to_region(maybe_region)
    if maybe_region != region:
        return None
    return region

def line_segment2D_to_region(line_segment):
    # ((p,p), (p,p)) -> ((p,p), (p,p))
    (x0, y0), (x1, y1) = line_segment
    minx, maxx = sorted([x0, x1])
    miny, maxy = sorted([y0, y1])
    return (minx, miny), (maxx, maxy)

def point_in_region2D(point, region):
    x, y = point
    (minx, miny), (maxx, maxy) = region
    return minx <= x <= maxx and miny <= y <= maxy






def line_segment2vector(line_segment):
    # ((p...), (p...)) -> (p...)
    assert len(line_segment[0]) == len(line_segment[1])
    return tuple(b-a for a, b in zip(*line_segment))
def vector_scale(scale, v):
    return tuple(scale*x for x in v)
def is_scaled_vector_ex(target, source):
    # exists scale, s.t. target = scale * source??
    # return None | (scale,)
    assert len(target) == len(source)
    abs_src = tuple(map(abs, source))
    i = abs_src.index(max(abs_src))
    d = source[i]
    c = target[i]
    scale = c/d
    if vector_scale(scale, source) == target:
        return (scale,)
    return None
    
def vector_div(big, small):
    # result * small == big
    assert len(big) == len(small)
    r = is_scaled_vector_ex(big, small)
    if not r:
        raise ValueError('not parallel vectors')
    scale, = r
    return scale
    
def vector_add(v0, v1):
    assert len(v0) == len(v1)
    return tuple(a+b for a, b in zip(v0, v1))

def make_line_segment(point, vector):
    assert len(point) == len(vector)
    end = vector_add(point, vector)
    return point, end
def line_segment_scale(scale, line_segment):
    v = line_segment2vector(line_segment)
    v = vector_scale(scale, v)
    base, _ = line_segment
    return make_line_segment(base, v)


    


def line_segment2D_to_line_arguments(line_segment):
    # ((p, p), (p,p)) -> (a, b, c) s.t. ax+by=c
    (x0, y0), (x1, y1) = line_segment
    # a dx + b dy = 0
    dx = x1 - x0
    dy = y1 - y0
    b = -dx
    a = dy
    c = a*x0 + b*y0

    assert all(c == a*x+b*y for x, y in line_segment)
    return a, b, c

def is_parallel_lines(line0, line1):
    # (a, b, c) -> (a', b', c') -> bool ; where ax+by=c
    a0, b0, c0 = line0
    a1, b1, c1 = line1
    D = (b0*a1 - b1*a0)
    return not bool(D)


def calc_line_crossing2D(line0, line1):
    # (a, b, c) -> (a', b', c') -> (x, y) ; where ax+by=c
    r = calc_line_crossing2D_ex(line0, line1)
    if not is_point2D(r):
        raise ValueError('calc crossing of parallel lines')
    return r

def calc_line_crossing2D_ex(line0, line1):
    # (a, b, c) -> (a', b', c') -> None|(x, y)|line0 ; where ax+by=c
    a0, b0, c0 = line0
    a1, b1, c1 = line1
    D = (b0*a1 - b1*a0)
    if not D:
        if is_scaled_vector_ex(line0, line1):
            return line0
        else:
            return None
    # (b0 a1 - b1 a0)x + 0 = b0 c1 - b1 c0
    # 0 + (a0 b1 - a1 b0)y = a0 c1 - a1 c0
    x = (b0*c1 - b1*c0)/D
    y = (a0*c1 - a1*c0)/-D
    return x, y

assert calc_line_crossing2D_ex(*to_fraction_points([[1,2,4], [2,4,8]])) == (1,2,4)
assert calc_line_crossing2D_ex(*to_fraction_points([[1,2,4], [2,4,0]])) == None
assert calc_line_crossing2D_ex(*to_fraction_points([[1,0,0], [0,1,0]])) == (0, 0)


def calc_line_segment_crossing2D_ex(line_segment0, line_segment1):
    # return (x,y) | None | common_line_segment (same direction as line_segment0)
    line0 = line_segment2D_to_line_arguments(line_segment0)
    line1 = line_segment2D_to_line_arguments(line_segment1)
    r = calc_line_crossing2D_ex(line0, line1)
    if r is None:
        # parallel, no crossing
        return None
    if r is not line0:
        # one crossing, but may not on both line_segments
        xy = crossing = r
        if not all(point_in_region2D(xy, line_segment2D_to_region(seg))
                   for seg in [line_segment0, line_segment1]):
            return None
        return xy
    
    assert r is line0
    # both line_segments are on same line

    p0, p1 = line_segment0
    if p0 == p1:
        region1 = line_segment2D_to_region(line_segment1)
        if point_in_region2D(p0, region1):
            return p0

    # line_segment0 is not a point
    # map line0 -> x-axis by line_segment0->[0,1]
    #    ==>> line_segment1->[s0, s1]
    q0, q1 = line_segment1

    u = line_segment2vector(line_segment0)
    v0 = line_segment2vector((p0, q0))
    v1 = line_segment2vector((p0, q1))
    s0 = vector_div(v0, u)
    s1 = vector_div(v1, u)

    # intersect [0,1] and [s0,s1]; note: s1 may < s0
    a0, a1 = sorted([s0, s1])
    c0 = max(0, a0)
    c1 = min(1, a1)
    
    # common [c0, c1]
    if c0 > c1:
        # not overlap
        return None
    def scale2point(s):
        v = vector_scale(s, u)
        return vector_add(p0, v)

    r0, r1 = map(scale2point, [c0, c1])
    if r0 == r1:
        return r0
    return r0, r1


assert calc_line_segment_crossing2D_ex(to_fraction_points([(0,0), (1,0)]), to_fraction_points([(0,0), (0,1)])) == (0,0)
assert calc_line_segment_crossing2D_ex(to_fraction_points([(0,0), (1,0)]), to_fraction_points([(0,1), (0,2)])) == None
assert calc_line_segment_crossing2D_ex(to_fraction_points([(0,0), (1,0)]), to_fraction_points([(0,1), (1,1)])) == None
assert calc_line_segment_crossing2D_ex(to_fraction_points([(0,0), (1,0)]), to_fraction_points([(1,0), (2,0)])) == (1,0)
assert calc_line_segment_crossing2D_ex(to_fraction_points([(0,0), (2,0)]), to_fraction_points([(1,0), (2,0)])) == ((1,0), (2,0))

def calc_maybe_crossing2D(line_segment0, line_segment1):
    # None | (x,y)
    maybe_xy = calc_line_segment_crossing2D_ex(line_segment0, line_segment1)
    if not is_point2D(maybe_xy):
        return None

    return maybe_xy
def calc_crossing2D(line_segment0, line_segment1):
    xy = calc_maybe_crossing2D(line_segment0, line_segment1)
    if xy is None:
        raise ValueError('line_segments not connected')
    return xy
                                 

def point2D_to_height(point2D, line_segment3D):
    line_segment2D = tuple((x,y) for x,y,_ in line_segment3D)
    new_line_segment2D = line_segment2D[0], point2D
    scale = vector_div(line_segment2vector(new_line_segment2D), line_segment2vector(line_segment2D))
    new_line_segment3D = line_segment_scale(scale, line_segment3D)
    _, point3D = new_line_segment3D
    _, _, z = point3D
    return z








def find_connected_line_segments__2D(line_segments):
    # LineSegment = (Point, Point)
    # line_segments :: Iter LineSegment
    # return [[LineSegment]]
    # input[i] -> output[i]
    #    output[i] sorted from u->v if input[i]=(u,v)
    # TODO: improve performence; current O(n^2)

    
    line_segments = tuple(line_segments)
    lineargss = tuple(map(line_segment2D_to_line_arguments, line_segments))
    
    N = len(line_segments)
    data = [[] for _ in range(N)] # [[(this_line_segment, crossing, other_line_segment)]]
    for i, line in enumerate(line_segments):
        for j, other in enumerate(line_segments[i+1:], i+1):
            crossing = calc_maybe_crossing2D(line, other)
            if crossing is None:
                continue
            data[i].append((line, crossing, other))
            data[j].append((other, crossing, line))

    def key(info):
        line, crossing, other = info
        base, _ = line
        new_line = base, crossing
        v = line_segment2vector(line)
        new_v = line_segment2vector(new_line)
        scale = vector_div(new_v, v)
        return scale
    for infos in data:
        infos.sort(key=key)

    result = [[other for _, _, other in infos] for infos in data]
    return result









def polygonal_knot2knot_diagram(polygonal_knot):
    point3Ds = tuple(polygonal_knot)
    assert all(map(is_point3D, point3Ds))
    
    point2Ds = tuple((x, y) for x, y, z in point3Ds)
    line_segment3Ds = tuple(zip(point3Ds, point3Ds[1:]+point3Ds[:1]))
    line_segment2Ds = tuple(zip(point2Ds, point2Ds[1:]+point2Ds[:1]))
    line_segment2Dss = find_connected_line_segments__2D(line_segment2Ds)

    line_segment2D_to_3D = dict(zip(line_segment2Ds, line_segment3Ds))

    crossing_infoss = [] # [[(is_overcrossing, crossing2D, is_x_arrow)]]
    for line_segment3D, line_segment2D, connected_line_segment2Ds in zip(line_segment3Ds, line_segment2Ds, line_segment2Dss):
        assert len(connected_line_segment2Ds) >= 2
        assert connected_line_segment2Ds[0][1] == line_segment2D[0]
        assert connected_line_segment2Ds[-1][0] == line_segment2D[1]
        crossing_infos = [] # [(is_overcrossing, crossing2D, is_x_arrow)]
        crossing_infoss.append(crossing_infos)
        for connected_line_segment2D in connected_line_segment2Ds[1:-1]:
            crossing2D = calc_crossing2D(line_segment2D, connected_line_segment2D)
            this_z = point2D_to_height(crossing2D, line_segment3D)
            connected_line_segment3D = line_segment2D_to_3D[connected_line_segment2D]
            other_z = point2D_to_height(crossing2D, connected_line_segment3D)
            assert this_z != other_z
            is_overcrossing = this_z > other_z
            is_x_arrow = is_right_hand_xy(line_segment2vector(line_segment2D),
                                          line_segment2vector(connected_line_segment2D),
                                          )
            
            crossing_infos.append((is_overcrossing, crossing2D, is_x_arrow))

    double_num_crossings = sum(map(len, crossing_infoss))
    assert double_num_crossings % 2 == 0
    num_points = double_num_crossings//2 + len(point2Ds)
    assert num_points == len(set(point2Ds) | set(crossing for infos in crossing_infoss for is_over, crossing, is_x in infos if is_over))

    crossing_infos = list(chain.from_iterable(crossing_infoss)) # [(is_overcrossing, crossing2D, is_x_arrow)]
    if not crossing_infos:
        # no overcrossing ==>> unknot
        return ()

    # find first vertex s.t. from underpass to overpass
    prev__is_over = crossing_infos[-1][0]
    for i, (is_over, _, _) in enumerate(crossing_infos):
        if not prev__is_over and is_over:
            break
        prev__is_over = is_over
    else:
        raise ...

    
    crossing_infos = crossing_infos[i:] + crossing_infos[:i]
    crossing2id = {}
    diagram_passes = [] # [[crossing_id]]
    crossing2is_overpass_x_arrow = {}
    next_id = 0 # 0 will be the first vertex
    prev__is_over = crossing_infos[-1][0]
    assert not prev__is_over
    for is_over, crossing, is_x in crossing_infos:
        if prev__is_over != is_over:
            # requires a vertex
            # diagram_points.append(next_id)
            # next_id += 1

            diagram_passes.append([])
            prev__is_over = is_over
        if crossing not in crossing2id:
            crossing2id[crossing] = next_id
            next_id += 1
        diagram_passes[-1].append(crossing2id[crossing])
        if is_over:
            crossing2is_overpass_x_arrow[crossing] = is_x

    crossing_id2is_overpass_x_arrow = dict((crossing2id[c], is_x) for c, is_x in crossing2is_overpass_x_arrow.items())
    return tuple(map(tuple, diagram_passes)), crossing_id2is_overpass_x_arrow





def knot_diagram2multiedged_graph(knot_diagram):
    # sorted neighbors in counter-clockwise
    # {crossing:(over_prev, underend, over_succ, underend)}
    # if overpass is x_arrow: (over_prev, under_prev, over_succ, under_succ)
    # else: (over_prev, under_succ, over_succ, under_prev)
    diagram_passes, crossing2is_overpass_x_arrow = knot_diagram
    assert len(diagram_passes) % 2 == 0
    assert all(diagram_passes)
    assert sum(map(len, diagram_passes)) == 2*len(crossing2is_overpass_x_arrow)
    
    u2vtc = {}
    double_crossinges = list(chain.from_iterable(diagram_passes))
    N2 = len(double_crossinges)
    i = -1
    for is_over, pass_crossinges in zip(cycle([True, False]), diagram_passes):
        for crossing in pass_crossinges:
            i += 1
            assert double_crossinges[i] is crossing
            if crossing not in u2vtc:
                u2vtc[crossing] = [None]*4

            neighbors = double_crossinges[(i-1)%N2], double_crossinges[(i+1)%N2]
            if not is_over:
                if not crossing2is_overpass_x_arrow[crossing]:
                    neighbors = neighbors[::-1]
            u2vtc[crossing][1-is_over::2] = neighbors

    
    return dict((key, tuple(value)) for key, value in u2vtc)

def diagram_passes_to_crossing2passes(diagram_passes):
    # {crossing: (pass_i, pass_j)}
    crossing2passes = defaultdict(list)
    for i, crossings in enumerate(diagram_passes):
        for crossing in crossings:
            crossing2passes[crossing].append(i)
    return dict(crossing2passes)
def is_overpass_idx(pass_idx):
    return pass_idx % 2 == 0

def knot_diagram2knot_group_over_presentation(knot_diagram):
    # group of knot K is the fundamental group of R^3-K
    # return (N, [[(i, exp)]])
    diagram_passes, crossing2is_overpass_x_arrow = knot_diagram
    crossing2passes = diagram_passes_to_crossing2passes(diagram_passes)

    # loop(underpass) - counter-clockwise
    # exp = +1 if loop(underpass) is x-arrow and overpass is y-arrow
    N2 = len(diagram_passes)
    N = N2//2 # rank of free group
    relators = []
    for i, underpass in zip(count(1, 2), diagram_passes[1::2]):
        prev_overpass_idx = (i-1)%N2 # will do [0,2..N2-1] -> [0..N-1]
        succ_overpass_idx = (i+1)%N2
        relator = [(prev_overpass_idx, +1)]
        for crossing in underpass:
            a, b = crossing2passes[crossing]
            overpass_idx = b if a == i else a # the crossing overpass
            exp = -1 if crossing2is_overpass_x_arrow[crossing] else +1
            relator.append((overpass_idx, exp))
        relator.append((succ_overpass_idx, -1))
        relator.extend((pass_idx, -exp) for pass_idx, exp in relator[1:-1])
        relators.append(relator)

    relators = [[(idx//2, exp) for idx, exp in relator] for relator in relators]
    relators = tuple(map(tuple, relators))
    return N, relators

right_handed_trefoil_knot_diagram = (tuple((i,) for i in range(3))*2, dict((i, True) for i in range(3)))
def make_right_handed_trefoil_polygonal_knot():
    a, b = 1, 4
    c, d = 4, -1
    e, f = 3, -2
    H, L = 2, -2
    p0, p1 = (-a, b, H), (a, b, L)
    p2, p3 = (c, d, H), (e, f, L)
    p4, p5 = (-e, f, H), (-c, d, L)


    right_handed_trefoil_polygonal_knot = to_fraction_points(
        [p0, p5, p2, p1, p4, p3])
    assert polygonal_knot2knot_diagram(right_handed_trefoil_polygonal_knot) ==\
           (((0,), (1,), (2,), (0,), (1,), (2,)), {0: True, 1: True, 2: True}) ==\
           right_handed_trefoil_knot_diagram
    return right_handed_trefoil_polygonal_knot
make_right_handed_trefoil_polygonal_knot()


r = knot_diagram2knot_group_over_presentation(right_handed_trefoil_knot_diagram)
assert r == (3, (((0, 1), (2, -1), (1, -1), (2, 1)), ((1, 1), (0, -1), (2, -1), (0, 1)), ((2, 1), (1, -1), (0, -1), (1, 1))))



        

    
