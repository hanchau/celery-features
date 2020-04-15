import pdb; pdb.set_trace()

from celery import chord
from workers.all_tasks import *


chord_ = chord(add.s(i, i) for i in range(10))
agg_applied = chord_(sum_list.s())
res = agg_applied.get()
print(res)

# callback = sum_list.s()
# header = [add.s(i, i) for i in range(100)]
# result = chord(header)(callback)
# result.get()


## Think of a way to implement chords without using chord
