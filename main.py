from structs import Query
from utils import dist

a = Query("a", 1)
b = Query("b", -1)

print(dist(a, b))
