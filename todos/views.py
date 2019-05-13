from django.shortcuts import render
from .models import TodoList


def todos_list(request):
    lists = TodoList.objects.all()
    context = {'lists': lists}

    return render(request, 'pages/todos-list.html', context)
