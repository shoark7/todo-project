from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .forms import TodoListForm
from .models import TodoList


@csrf_exempt
def todos_list(request):
    if request.GET:
        criteria = request.GET.get('criteria')
        ordering = request.GET.get('ordering')
        sign = '' if ordering == 'ascending' else '-'
        lists = TodoList.objects.order_by(sign + criteria)
        context = {'lists': lists, 'criteria': criteria, 'ordering': ordering}
    else:
        lists = TodoList.objects.all()
        context = {'lists': lists}

    return render(request, 'pages/todos-list.html', context)


@csrf_exempt
def todos_new(request):
    if request.method == 'GET':
        form = TodoListForm()
        context = {'form': form}
        return render(request, 'pages/todo-new.html',  context)
    elif request.method == 'POST':
        form = TodoListForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('todos-list')
        else:
            return render(request, 'pages/todo-new.html', context)


@csrf_exempt
def todos_update(request, pk):
    todo = get_object_or_404(TodoList, pk=pk)

    if request.method == 'GET':
        form = TodoListForm(instance=todo)
        context = {'form': form, 'pk': pk}
        return render(request, 'pages/todo-update.html', context)
    else:
        form = TodoListForm(request.POST, instance=todo)
        context = {'form': form, 'pk': pk}
        if form.is_valid():
            form.save()
            return redirect('todos-list')
        return render(request, 'pages/todo-update.html', context)


@csrf_exempt
def todos_delete(request, pk):
    todo = get_object_or_404(TodoList, pk=pk)
    todo.delete()
    return redirect('todos-list')
