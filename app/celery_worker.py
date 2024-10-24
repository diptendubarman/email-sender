# celery_worker.py

from celery import Celery
import os

redis_url = os.getenv("REDIS_URL", "redis://redis:6379/0")
celery = Celery("worker", broker=redis_url, backend=redis_url, include=["app.tasks"])

celery.conf.update(
    task_routes={
        "app.tasks.send_email_task": {"queue": "send_mail"},
    },
    broker_connection_retry_on_startup=True,
    task_acks_late=True,  # Acknowledge tasks only after successful execution
    task_reject_on_worker_lost=True,  # Retry tasks if the worker crashes
    worker_prefetch_multiplier=1,  # Avoid over-fetching tasks by workers
    task_default_retry_delay=300,  # 5 minutes between task retries
    task_max_retries=3,  # Retry tasks 3 times on failure
    worker_max_tasks_per_child=100,  # Restart worker after processing 100 tasks (prevents memory leaks)
    result_expires=3600,  # Task results expire after 1 hour
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)
