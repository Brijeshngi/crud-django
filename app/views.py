from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpRequest

from .forms import todoform
from .forms import EditForm
from .models import todo
from django.utils import timezone
 #index function 
def index(request):
 
    item_list = todo.objects.order_by("date")
    if request.method == "POST":
        form = todoform(request.POST)
        if form.is_valid():
            form.save()
    form = todoform()
 
    page = {
             "forms" : form,
             "list" : item_list,
             "title" : "TODO LIST",
           }
    context = 'index.html'       
    return render(request, context , page)

def remove(request,todo_id):
    todo_to_delete = todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/app/list')

def updatetask(request, todo_id):
    if request.method == "GET":
        if todo_id == 0:
            form = EditForm()
        else:
            task = todo.objects.get(id=todo_id)
            form = EditForm(instance=task)
        return render(request, "app_edit.html", {'form': form})
    else:
        if todo_id == 0:
            form = EditForm(request.POST)
        else:
            task = todo.objects.get(id=todo_id)
            form = EditForm(request.POST,instance= task)
        if form.is_valid():
            form.save()
            return redirect('/app/list')
        


    