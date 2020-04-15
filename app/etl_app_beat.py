# import pdb; pdb.set_trace()
from celery import Celery
from celery.schedules import crontab

etl_app = Celery('beat_tasks', broker='amqp://hanchau:hanchau@localhost/vhost1'
,backend='amqp://hanchau:hanchau@localhost/vhost1'
,include=['workers.all_tasks', 'callbacks.all_callbacks']
)


# etl_app.conf.beat_schedule = {
#     'add-every-seconds': {
#         'task': 'workers.all_tasks.add',
#         'schedule': 1.0,
#         'args': (16, 16)
#     },
#     'mul-4-seconds': {
#         'task': 'workers.all_tasks.mul',
#         'schedule': 4.0,
#         'args': (20, 9)
#     }
# }


etl_app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'every_minute': {
        'task': 'workers.all_tasks.add',
        'schedule': crontab(minute='*/1'),
        'args': (2, 123),
    },
}

etl_app.conf.timezone = 'UTC'
