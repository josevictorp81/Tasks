from django.shortcuts import render, get_object_or_404

from .models import Task

def taskList(request):
    task = Task.objects.all()

    data = {
        'task': task,
    }
    return render(request, 'task/list.html', data)

def taskDetail(request, id):
    task = get_object_or_404(Task, pk=id)
    
    data = {
        'task': task,
    }
    return render(request, 'task/detail.html', data)  
