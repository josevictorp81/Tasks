from django.shortcuts import render, get_object_or_404, redirect

from .models import Task
from .forms import TaskModelForm

def taskList(request):
    task = Task.objects.all().order_by('-created')

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

def newTask(request):
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'Doing'
            task.save()
            return redirect('taskList')
    else:
        form = TaskModelForm()
        data = {
            'form': form,
        }
        return render(request, 'task/newTask.html', data)
