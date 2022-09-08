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
            entry = form.save(commit=False)
            last = TodoList.objects.last()
            if last:
                list_id = last.id + 1
            else:
                list_id = 1
            entry.id = list_id
            entry.save()
            # TODO make it so form can't be submitted if empty!!
        return redirect("todo_list_detail", pk=list_id)
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
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            list_name = form.cleaned_data["list"]
            list_id = TodoList.objects.get(name=list_name).id
            entry.list_id = list_id
            entry.save()
            # TODO make it so form can't be submitted if empty!!
        return redirect("todo_list_detail", pk=list_id)
    else:
        form = TodoItemForm()

    context = {
        "form": form,
    }

    return render(request, "items/create.html", context)


def edit_todoitem(request, pk):
    todoitem_instance = TodoItem.objects.get(pk=pk)
    if request.method == "POST":
        form = TodoItemForm(request.POST, instance=todoitem_instance)
        if form.is_valid():
            entry = form.save(commit=False)
            list_name = form.cleaned_data["list"]
            list_id = TodoList.objects.get(name=list_name).id
            entry.list_id = list_id
            entry.save()
            # TODO make it so form can't be submitted if empty!!
            return redirect("todo_list_detail", pk=list_id)
    else:
        form = TodoItemForm(instance=todoitem_instance)

    context = {
        "form": form,
    }

    return render(request, "items/edit.html", context)
