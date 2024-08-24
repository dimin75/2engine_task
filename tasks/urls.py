from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import TaskViewSet
from .views import search_tasks
from .views import search_tasks, task_list, task_detail, task_create, task_edit
# from . import views

# router = DefaultRouter()
# router.register(r'tasks', TaskViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.task_list, name='task_list'),
#     path('task/<int:pk>/', views.task_detail, name='task_detail'),
#     path('task/new/', views.task_create, name='task_create'),
#     path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
# ]

# urlpatterns = [
#     path('', include(router.urls)),
#     path('search/', search_tasks, name='search_tasks'),
#     path('tasks', views.task_list, name='task_list'),
#     path('task/<int:pk>/', views.task_detail, name='task_detail'),
#     path('task/new/', views.task_create, name='task_create'),
#     path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
# ]

# urlpatterns = [
#     path('', include(router.urls)),  # пути для API
#     path('search/', search_tasks, name='search_tasks'),
#     path('tasks/', task_list, name='task_list'),  #нужен слэш после 'tasks/'
#     path('task/<int:pk>/', task_detail, name='task_detail'),
#     path('task/new/', task_create, name='task_create'),
#     path('task/<int:pk>/edit/', task_edit, name='task_edit'),
# ]

urlpatterns = [
    path('', task_list, name='task_list'),  # Главная страница
    path('tasks/', task_list, name='task_list'),  #нужен слэш после 'tasks/'
    path('task/<int:pk>/', task_detail, name='task_detail'),
    path('task/new/', task_create, name='task_create'),
    path('task/<int:pk>/edit/', task_edit, name='task_edit'),
    path('search/', search_tasks, name='search_tasks'),
]
