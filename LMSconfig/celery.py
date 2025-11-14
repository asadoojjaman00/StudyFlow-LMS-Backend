from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# 1) Django settings file declare 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LMSconfig.settings')

# 2) Celery App create
app = Celery('LMSconfig')

# 3) Celery settings auto load from Django settings 
app.config_from_object('django.conf:settings', namespace='CELERY')

# 4) Django installed apps 
app.autodiscover_tasks()
