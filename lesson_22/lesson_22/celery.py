import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lesson_22.settings')
celery_app = Celery('lesson_22')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
