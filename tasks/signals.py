from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task
from .search_indexes import TaskIndex

@receiver(post_save, sender=Task)
def index_task(sender, instance, **kwargs):
    TaskIndex.from_task(instance).save()