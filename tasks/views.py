from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from .tasks import process_task

from rest_framework.decorators import action
from rest_framework.response import Response
from .tasks import update_task_status

from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.db.models import Q

from django_elasticsearch_dsl.search import Search
from django.shortcuts import render
from .documents import TaskDocument
# from .models import Task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        process_task.delay(task.id, task.title, task.description) 

    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        task = self.get_object()
        new_status = request.data.get('status')
        update_task_status.delay(task.id, new_status)
        return Response({'status': 'Task status update initiated'})

def task_list(request):
    query = request.GET.get('q')
    if query:
        tasks = Task.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            # add task to celery
            process_task.delay(task.id, task.title, task.description)
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'tasks/task_edit.html', {'form': form})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            # add task to celery
            process_task.delay(task.id, task.title, task.description)
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_edit.html', {'form': form})
# search notes

def search_tasks(request):
    query = request.GET.get('q')
    search = Search(index='tasks').query("multi_match", query=query, fields=['title', 'description'])
    results = search.execute()
    return render(request, 'tasks/search_results.html', {'results': results})



