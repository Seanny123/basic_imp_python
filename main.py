from basic_dist.structs import Query
from basic_dist.utils import dist
from basic_dist.mod_dist.mid import mid_dist

a = Query("a", 1)
b = Query("b", -1)

print(dist(a, b))
print(mid_dist(a, b))
