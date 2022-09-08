from django.shortcuts import render, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm, TodoItemForm


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


def create_todolist(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            # TODO make it so form can't be submitted if empty!!
        return redirect("todo_list_list")
    else:
        form = TodoListForm()

    context = {
        "form": form,
    }

    return render(request, "todos/create.html", context)


def edit_todolist(request, pk):
    todolist_instance = TodoList.objects.get(pk=pk)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todolist_instance)
        if form.is_valid():
            form.save()
            # TODO make it so form can't be submitted if empty!!
            return redirect("todo_list_detail", pk=pk)
    else:
        form = TodoListForm(instance=todolist_instance)

    context = {
        "form": form,
    }

    return render(request, "todos/edit.html", context)


def delete_todolist(request, pk):
    todolist_instance = TodoList.objects.get(pk=pk)
    if request.method == "POST":
        todolist_instance.delete()
        return redirect("todo_list_list")

    return render(request, "todos/delete.html")


def create_todoitem(request):
    todolist_list = TodoList.objects.all()
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            # TODO make it so form can't be submitted if empty!!
        return redirect("todo_list_detail")
    else:
        form = TodoItemForm()

    context = {
        "form": form,
        "todolist_list": todolist_list,
    }

    return render(request, "items/create.html", context)


def edit_todoitem(request, pk):
    todolist_list = TodoList.objects.all()
    todoitem_instance = TodoItem.objects.get(pk=pk)
    if request.method == "POST":
        form = TodoItemForm(request.POST, instance=todoitem_instance)
        if form.is_valid():
            form.save()
            # TODO make it so form can't be submitted if empty!!
            return redirect("todo_list_edit", pk=pk)
    else:
        form = TodoListForm(instance=todoitem_instance)

    context = {
        "form": form,
        "todolist_list": todolist_list,
    }

    return render(request, "items/edit.html", context)
