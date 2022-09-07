from django.shortcuts import render
from todos.models import TodoList


def show_todolist(request):
    todolist_list = TodoList.objects.all()

    context = {
        "todolist_list": todolist_list
    }

    return render(request, "todos/list.html", context)
