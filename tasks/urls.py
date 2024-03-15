from django.urls import path
from . import views

urlpatterns = [
    #nome de url / função de views
    path('hello/',views.HelloWorld),

    #caminho , view , name.
    path('',views.taskList,name='task-list'),
    path('seunome/<str:name>',views.SeuNome,name='seu-nome'),
]
