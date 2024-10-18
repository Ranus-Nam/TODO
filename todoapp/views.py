from django.shortcuts import render,redirect
from.models import *

# Create your views here.
# main page function
def todo_list(request):
    todos = Todo.objects.order_by('-id')
    return render(request, 'todo/index.html', {'todos': todos})


# function which create_todo
def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Todo.objects.create(title=title, description=description)
    return redirect('/')


# function complete todo
def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('/')

# function delete todo
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('/')