from django.http import HttpResponse
from django.shortcuts import render, redirect
# Get the todo objects
from .models import Todo
from .forms import TodoForm


# CRUD operation

# show all todos
def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todo_list': todos
    }
    # name the path of the folder/then the html file for render
    return render(request, 'todo/todo_list.html', context)


# read a todo
def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'todo/todo_detail.html', context)


# create a todo
def todo_create(request):
    # created a todo with django forms
    form = TodoForm(request.POST or None)
    if form.is_valid():
        # save data from form
        form.save()
        # redirect and see new todo
        return redirect('/')
    context = {'form': form}
    return render(request, 'todo/todo_create.html', context)


# update todo
def todo_update(request, id):
    # grabbing todo object
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'todo/todo_update.html', context)

# delete a todo


def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')
