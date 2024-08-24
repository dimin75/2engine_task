import time
from celery import shared_task
from .models import Task
from celery import Task as CeleryTask

class BaseTask(CeleryTask):
    def on_success(self, retval, task_id, args, kwargs):
        task_id = kwargs.get('task_id')
        if task_id:
            try:
                task = Task.objects.get(id=task_id)
                task.status = 'completed'
                task.save()
            except Task.DoesNotExist:
                print(f"Task with id {task_id} does not exist.")
        super().on_success(retval, task_id, args, kwargs)

    # def on_success(self, retval, task_id, args, kwargs):
    #     task = Task.objects.get(id=kwargs.get('task_id'))
    #     task.status = 'completed'
    #     task.save()
    #     super().on_success(retval, task_id, args, kwargs)

@shared_task(bind=True, base=BaseTask)
def process_task(self, task_id, title, description):
    task = Task.objects.get(id=task_id)
    task.status = 'in_progress'
    task.save()
    
    # Pass task metadata
    self.update_state(
        state='PROGRESS',
        meta={
            'title': title,
            'description': description,
            'status': task.status,
        }
    )
    
    # Long time task simulation
    # import time
    time.sleep(10)
    
    task.status = 'completed'
    task.save()

    return {
        'task_id': task_id,
        'status': task.status,
        'title': title,
        'description': description
    }

@shared_task
def update_task_status(task_id, status):
    task = Task.objects.get(id=task_id)
    task.status = status
    task.save()

# @shared_task
# def process_task(task_id):
#     task = Task.objects.get(id=task_id)
#     task.status = 'in_progress'
#     task.save()
#     time.sleep(10)
#     task.status = 'completed'
#     task.save()