from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from .models import Task

# Create your views here.
def HelloWorld(request):
    return HttpResponse('OLa Mundo')

def SeuNome(request,name):
    return render(request,'tasks/seunome.html',{'name':name})


# Views do ToDo
def taskList(request):
    tasks = Task.objects.all()

    return render (request,'tasks/list.html',{'tasks':tasks})

def taskView(request,id):
                            #model , id
    task = get_object_or_404(Task,pk=id)
    return render (request,'tasks/task.html',{'task':task})