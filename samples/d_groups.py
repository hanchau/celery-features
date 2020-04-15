import pdb; pdb.set_trace()

from celery import group
from workers.all_tasks import *

import time

# res = group(add.s(2, 2), mul.s(4,10), sub.s(2,3))
# res = res.apply_async()
#
# res = group(add.s(2, 2), mul.s(4,10), sub.si(2,3))
# res = res()

# 4 CORE MACHINE, 8 GIGS MEMORY, 1000 addition jobs
# for 1 worker, 72.92983603477478 seconds

# 1 worker 4 concurrency, 57.861945152282715 seconds
# 1 worker 8 concurrency, 53.10987687110901 seconds
# 1 worker 16 concurrency, 51.780194997787476 seconds
# 1 worker 32 concurrency, 48.15121579170227 seconds

# 2 worker 1 concurrency, 64.37082004547119 seconds
# 2 worker 2 concurrency, 57.25886797904968 seconds
# 4 worker 1 concurrency, 59.34687900543213 seconds

# 1 worker 10000 eventlets, 56.01543688774109 seconds

start_time = time.time()


g = group([ add.s(i, i) for i in range(1000)] )

# g = group( [add.s(i,i) for i in range(10)])


res = g.apply_async()

# while not res.successful():
#     print("not successful yet")
# print('successful',res.successful())
# print('failed', res.failed())
# print('waiting', res.waiting())
# print('ready', res.ready())
# print('completed_count', res.completed_count())
# print('join', res.join())

a = res.get()
print("TOTAL TIME TAKEN:", time.time() - start_time)

import pdb; pdb.set_trace()
