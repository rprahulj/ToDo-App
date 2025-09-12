from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def task(request):
    tasks = Task.objects.all()
    context = {
        'tasks' : tasks
    }
    return render(request, 'tasks.html', context)

def add_task(request):
    if request.method == 'POST':
        tasks = request.POST
        title = tasks.get('title')
        task_description = tasks.get('task_description')

        Task.objects.create(
            title = title,
            task_description = task_description
        )
        return redirect('home')
    return render(request, 'add_task.html')

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home')