# import pdb; pdb.set_trace()
from celery import Celery

etl_app = Celery('tasks', broker='redis://127.0.0.1:6379/'
,backend='redis://127.0.0.1:6379/1'
,include=['workers.celery_tasks', 'callbacks.all_callbacks']
)


# from kombu import Queue
#
# etl_app.conf.task_default_queue = 'default'
# etl_app.conf.task_queues = (
#     Queue('sum_list_only'),
#     Queue('default'),
# )
#
# etl_app.conf.task_routes = {'workers.all_tasks.sum_list': {'queue': 'sum_list_only'}}
