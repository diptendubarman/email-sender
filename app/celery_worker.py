# celery_worker.py

from celery import Celery
import os

redis_url = os.getenv("REDIS_URL", "redis://redis:6379/0")
celery = Celery("worker", broker=redis_url, backend=redis_url, include=["app.tasks"])

celery.conf.update(
    task_routes={
        "app.tasks.send_email_task": {"queue": "send_mail"},
    },
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)
