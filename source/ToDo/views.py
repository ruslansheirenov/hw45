from django.shortcuts import render, redirect, get_object_or_404

from .models import Task

# Create your views here.

def index_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context)

def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'task_create.html')
    else:
        title = request.POST.get('title')
        status = request.POST.get('status')
        description = request.POST.get('description')
        detailed_description = request.POST.get('detailed_description')
        date_of_completion = request.POST.get('date_of_completion')
        new_task = Task.objects.create(title=title, status=status, description=description, detailed_description=detailed_description, date_of_completion=date_of_completion)
        
        return redirect("task_view", pk=new_task.pk)

def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'task_view.html', context)