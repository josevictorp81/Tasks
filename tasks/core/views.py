from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import datetime

from .models import Task
from .forms import TaskModelForm


@login_required
def taskList(request):
    search = request.GET.get('search')
    task_done_recently = Task.objects.filter(done='Done', updated__gt=datetime.datetime.now()-datetime.timedelta(days=30), user=request.user).count()
    task_done = Task.objects.filter(done='Done', user=request.user).count()
    task_doing = Task.objects.filter(done='Doing', user=request.user).count()
    #filter = request.GET.get('filter')
    if search:
        task = Task.objects.filter(title__icontains=search, user=request.user)
    #elif filter:
        #task = Task.objects.filter(done=filter, user=request.user)
    else:
        task_list = Task.objects.all().order_by('-created').filter(user=request.user)
        paginator = Paginator(task_list, 4)

        page = request.GET.get('page')

        task = paginator.get_page(page)

    data = {
        'task': task,
        'task_done_recently': task_done_recently,
        'task_done': task_done,
        'task_doing': task_doing,
    }
    return render(request, 'task/list.html', data)


@login_required
def taskDetail(request, id):
    task = get_object_or_404(Task, pk=id)
    
    data = {
        'task': task,
    }
    return render(request, 'task/detail.html', data)


@login_required
def newTask(request):
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'Doing'
            task.user = request.user
            task.save()
            return redirect('taskList')
    else:
        form = TaskModelForm()
        data = {
            'form': form,
        }
        return render(request, 'task/newTask.html', data)


@login_required
def editeTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskModelForm(instance=task)

    if request.method == 'POST':
        form = TaskModelForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('taskList')
    
    data = {
        'form': form, 
        'task': task,
    }
    return render(request, 'task/editeTask.html', data)


@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('taskList')


@login_required
def changeStatus(request, id):
    task = get_object_or_404(Task, pk=id)

    if task.done == 'Doing':
        task.done = 'Done'
    else:
        task.done = 'Doing'
    
    task.save()
    return redirect('taskList')
