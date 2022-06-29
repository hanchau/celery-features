# import pdb; pdb.set_trace()

from celery import group, chord
from tasks.funcs import MainCode
from workers.celery_tasks import *

import time


chunks = [chunk for chunk in [ [i for i in range(0, 100000000)]                            ]]

start_time = time.time()

chord_ = chord(process_chunk.s(chunk) for chunk in chunks)
agg_applied = chord_(sum_list.s())
a = agg_applied.get()

print("Parallel | TOTAL TIME TAKEN: ", time.time() - start_time)

del chunks
del chord_
del agg_applied
del a




start_time = time.time()
g = [ MainCode.add(i,i) for i in range(100000000) ]
a = MainCode.sum_list(g)
print("Linear | TOTAL TIME TAKEN: ", time.time() - start_time)

del g
del a



