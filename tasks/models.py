from django.db import models
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry



class Task(models.Model):
    STATUS_CHOICES = [
        ('queued', 'В очереди...'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершена')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='queued')
    created_at = models.DateTimeField(auto_now_add=True)

@registry.register_document
class TaskDocument(Document):
    class Index:
        name = 'tasks'
    
    class Django:
        model = Task
        fields = [
            'title',
            'description',
            'status',
        ]
