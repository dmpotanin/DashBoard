import os
from celery import Celery
from celery.schedules import crontab

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Callboard.settings')
#
# app = Celery('Callboard')
# app.config_from_object('django.conf:settings', namespace='CELERY')
#
# app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'send_weekly_posts': {
#         'task': 'board.tasks.send_email_weekly_posts',
#         'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
#         'args': (),
#     },
# }
