from basic_dist.structs import Query

def dist(x: Query, y: Query):
    return (x.data - y.data) ** 2
