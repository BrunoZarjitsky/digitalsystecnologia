import os

from celery import Celery
from celery.utils.log import get_task_logger
from django.conf import settings

logger = get_task_logger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "settings.settings")

app = Celery("settings")
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
