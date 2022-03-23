from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('-id')

    return render(request, 'lybmvvsapp/index.html',{'title':'Главная страница сайта', 'tasks':tasks})

def about(request):
    return render(request, 'lybmvvsapp/about.html')

def create(request):
    error=''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            error = 'Плохие стихи'
    form = TaskForm()
    context = {'form': form,
               'error': error}
    return render(request, 'lybmvvsapp/create.html', context)


# Create your views here.
