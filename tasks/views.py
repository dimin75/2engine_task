# from django.shortcuts import render

# Create your views here.
# from rest_framework import viewsets
# from .models import Task
# from .serializers import TaskSerializer

# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from .tasks import process_task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        process_task.delay(task.id)    