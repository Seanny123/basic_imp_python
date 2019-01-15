from basic_dist.structs import Query

def mid_dist(x: Query, y: Query):
    return ((x.data - y.data) ** 2) / 2
