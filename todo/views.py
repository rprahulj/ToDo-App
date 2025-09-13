from django.shortcuts import render, redirect, get_object_or_404
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
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('home')

def mark_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = True
    task.save()
    return redirect('home')

def unmark_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = False
    task.save()
    return redirect('home')

def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        task_description = request.POST.get('task_description')

        task.title = title
        task.task_description = task_description

        task.save()
        return redirect('home')
    
    context = {'task': task}
    return render(request, 'update_task.html', context)