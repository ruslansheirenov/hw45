from django.shortcuts import render

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
        date_of_completion = request.POST.get('date_of_completion')
        new_task = Task.objects.create(title=title, status=status, description=description, date_of_completion=date_of_completion)
        context = {'task': new_task}

        return render(request, 'task_view.html', context)

def task_view(request):
    task_id = request.GET.get('pk')
    task = Task.objects.get(pk=task_id)
    context = {'task': task}
    return render(request, 'task_view.html', context)