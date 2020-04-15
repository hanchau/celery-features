import pdb; pdb.set_trace()

from workers.all_tasks import *

# map
# f( [1,2,3,4,..,n] ) --> [ f(1), f(2), f(3), ..., f(n)]
a = [i for i in range(100)]
b = [i for i in range(1000)]

list_ = [a, b]

map_ = sum_list.map(list_)

res = map_.apply_async()
print(res.get())


# starmap
# f( zip([a,b,c], [d,e,f]) ) --> [ f(a,d), f(b,e), f(c,f) ]
#
# a = [i for i in range(1000,20000)]
# b = [i for i in range(4000,23000)]
#
# zip_lists = zip(a, b)
#
# star_map_ = mul.starmap(zip_lists)
#
# res = star_map_.apply_async()
#
# print(res.get())
#

# chunks
# f( zip([a,b,c], [d,e,f]) ) --> [ [f(a,d)], [f(b,e)], [f(c,f)] ]

a = [i for i in range(1000,20000)]
b = [i for i in range(4000,23000)]

zip_lists = zip(a, b)

chunk_ = mul.chunks(zip_lists, 100)
res = chunk_.apply_async()

# print(res.get())
