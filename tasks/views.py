from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def HelloWorld(request):
    return HttpResponse('OLa Mundo')

def SeuNome(request,name):
    return render(request,'tasks/seunome.html',{'name':name})


# Views do ToDo
def taskList(request):
    return render (request,'tasks/list.html')