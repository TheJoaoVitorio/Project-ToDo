from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm

# Create your views here.
def HelloWorld(request):
    return HttpResponse('OLa Mundo')

def SeuNome(request,name):
    return render(request,'tasks/seunome.html',{'name':name})


# Views do ToDo
def taskList(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render (request,'tasks/list.html',{'tasks':tasks})

def taskView(request,id):
                            #model , id
    task = get_object_or_404(Task,pk=id)
    return render (request,'tasks/task.html',{'task':task})

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render (request, 'tasks/addtask.html',{'form':form})
