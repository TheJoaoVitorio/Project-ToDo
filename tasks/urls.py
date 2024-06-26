from django.urls import path
from . import views

urlpatterns = [
    #nome de url / função de views
    path('hello/',views.HelloWorld),
    path('seunome/<str:name>',views.SeuNome,name='seu-nome'),

    #caminho , view , name.
    path('',views.taskList,name='task-list'),
    path('task/<int:id>',views.taskView,name='task-view'),
    path('newtask/', views.newTask,name='new-task'),
    path('edittask/<int:id>',views.editTask,name='edit-task'),
    path('deletetask/<int:id>',views.deleteTask,name='delete-task'),
]
