from django.shortcuts import render

def taskList(request):
    return render(request, 'task/list.html')
