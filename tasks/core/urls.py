from django.urls import path

from . import views

urlpatterns = [
    path('', views.taskList, name='taskList'),
    path('task/<int:id>/', views.taskDetail, name='taskDetail'),
    path('newTask/', views.newTask, name='newTask'),
]