
import pdb; pdb.set_trace()
from workers.all_tasks import add, sub, mul, div
from callbacks.all_callbacks import type_error
from celery import signature

# .s ~~ signature

# s = signature(add, args=(2, 2), countdown=10, link=type_error.s())

# s = signature(add, args=(2, '2'), countdown=10, link_error=type_error.s())

# s = signature(add, args=(2, '2'), countdown=10, link_error=type_error.s())

s = signature(add, args=(2,2), link=add.s(10))

res = s.apply_async()

# partial = add.s(2)
#
# res = partial.apply_async((10,))

print(res.parent.get())
