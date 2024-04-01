#URlS DO projectTodo

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #aqui eu to pegando todas as urls do app task e incluindo no projetoTodo
    path('',include('tasks.urls')),
]
