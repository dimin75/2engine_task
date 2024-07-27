from django.db import models

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
