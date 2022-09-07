from django.shortcuts import render
from todos.models import TodoList


def list_todolist(request):
    todolist_list = TodoList.objects.all()

    context = {
        "todolist_list": todolist_list,
    }
    return render(request, "todos/list.html", context)


def detail_todolist(request, pk):
    todolist_instance = TodoList.objects.get(pk=pk)
    context = {
        "todolist_instance": todolist_instance,
    }
    return render(request, "todos/detail.html", context)
