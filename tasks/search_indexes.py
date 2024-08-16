from elasticsearch_dsl import Document, Text, Date
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=['http://localhost:9200'])

class TaskIndex(Document):
    title = Text()
    description = Text()
    created_at = Date()

    class Index:
        name = 'tasks'

    def save(self, **kwargs):
        return super().save(**kwargs)

    @classmethod
    def from_task(cls, task):
        return cls(
            meta={'id': task.id},
            title=task.title,
            description=task.description,
            created_at=task.created_at
        )
    