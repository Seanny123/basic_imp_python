from basic_dist.structs import Query
from basic_dist.mod_dist.half import halve

def mid_dist(x: Query, y: Query):
    return halve((x.data - y.data) ** 2)
