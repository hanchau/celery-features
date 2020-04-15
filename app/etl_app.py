import pdb; pdb.set_trace()
from celery import Celery

etl_app = Celery('tasks', broker='amqp://hanchau:hanchau@localhost/vhost1'
,backend='amqp://hanchau:hanchau@localhost/vhost1'
,include=['workers.all_tasks', 'callbacks.all_callbacks']
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
