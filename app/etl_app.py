# import pdb; pdb.set_trace()
from celery import Celery

etl_app = Celery('tasks', broker='amqp://hanchau:hanchau@localhost/vhost1'
,backend='amqp://hanchau:hanchau@localhost/vhost1'
,include=['workers.all_tasks', 'callbacks.all_callbacks']
)
