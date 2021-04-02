from django.urls import path

from . import views

urlpatterns = [
    path('', views.taskList, name='taskList'),
    path('task/<int:id>/', views.taskDetail, name='taskDetail'),
    path('new-task/', views.newTask, name='newTask'),
    path('edit/<int:id>/', views.editeTask, name='editeTask'),
    path('delete/<int:id>/', views.deleteTask, name='deleteTask'),
]