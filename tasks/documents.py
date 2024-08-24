# tasks/documents.py
from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from .models import Task

# Определяем индекс для Elasticsearch
tasks_index = Index('tasks')

# Настройки индекса, например, количество реплик и шардов
tasks_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@tasks_index.document
class TaskDocument(Document):
    title = fields.TextField(
        fields={
            'raw': fields.KeywordField(),
        }
    )
    description = fields.TextField()

    class Django:
        model = Task  # Указываем модель, которую нужно индексировать
        fields = [
            'id',
            'status',
        ]
