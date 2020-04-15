import pdb; pdb.set_trace()
from celery import chain

from workers.all_tasks import *


# mutable signatures
res = chain(add.s(2, 2), add.s(4), add.s(8), mul.s(4), sub.s(20))()
# res = add.s(2, 2) | add.s(4) | add.s(8) | mul.s(4) | sub.s(20)

# Immutable signatures
# res = add.si(2, 2) | add.si(4,10) | add.si(8,8) | mul.si(40,21) | sub.si(20,23)

# res = res.apply_async()


print(res.get(),
res.parent.get(),
res.parent.parent.get(),
res.parent.parent.parent.get(),
res.parent.parent.parent.parent.get()
)

import pdb; pdb.set_trace()
# with open('graphs/chain.dot', 'w') as fh:
#     res.parent.parent.parent.graph.to_dot(fh)
