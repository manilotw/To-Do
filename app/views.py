from django.shortcuts import render
from .models import Task

def index(request):
    tasks = Task.objects.all()
    
    return render(request, 'index.html', {'tasks': tasks})

def login(request):
    return render(request, 'login.html')

def register(request):

    return render(request, 'register.html')

def task(request):

    return render(request, 'task-create.html')