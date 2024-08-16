# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import TaskViewSet
# from . import views

# router = DefaultRouter()
# router.register(r'tasks', TaskViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/new/', views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
]