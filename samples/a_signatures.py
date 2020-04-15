import pdb; pdb.set_trace()

from app.etl_app import etl_app

# @etl_app.task
# def add(x, y):
#     return x + y
# s = add.signature((2, 2), countdown=10)
# print(s())
# print(dir(s))
# print(s.options)


from workers.all_tasks import add, sub, mul, div
from celery import signature

s = signature(add, args=(2, 2), countdown=10)
res = s.apply_async()

s = signature(sub, args=(2, 2))
res = s.apply_async()

s = signature(mul, args=(2, 2))
res = s.apply_async()

s = signature(div, args=(2, 2))
res = s.apply_async()

# cloning signatures

s = signature(add, args=(2))
s_ = s.clone(args=(4,))
res = s_.apply_async()

print(s)
print(dir(s))
print(s.options)
