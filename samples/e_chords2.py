
# another implementation
import pdb; pdb.set_trace()

from celery import group
from celery import chain
from workers.all_tasks import *
from callbacks.all_callbacks import *

# list_ = [add.s(i, i) for i in range(10)]
#
# group_ = group(list_)
#
# chord = chain(group_, sum_list.s())
#
# # res = chord.apply_async()
# res = chord.delay()
#
# res = res.get()
# print(res)

# if one of the task raises an exception

# list_ = [add.s(i, '2').on_error(type_error.s()) for i in range(10)]
list_ = [add.s(1, 2), add.s('2','3')]

group_ = group(list_)

sum_sig = sum_list.s()

sum_sig_with_callback = sum_sig.on_error(on_chord_error.s())

chord = chain(group_, sum_sig_with_callback)

# res = chord.apply_async()
res = chord.delay()

res = res.get()
print(res)
