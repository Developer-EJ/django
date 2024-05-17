from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoItem
from .forms import TodoForm

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    todos = TodoItem.objects.all()
    return render(request, 'todo/todo_detail.html', {'todo': todo, 'todos': todos})

def todo_new(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm()
    todos = TodoItem.objects.all()
    return render(request, 'todo/todo_edit.html', {'form': form, 'todos': todos})

def todo_edit(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm(instance=todo)
    todos = TodoItem.objects.all()
    return render(request, 'todo/todo_edit.html', {'form': form, 'todos': todos})

def todo_delete(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    todo.delete()
    return redirect('todo_list')