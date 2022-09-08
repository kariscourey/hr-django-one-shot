from django.urls import path

from todos.views import (
    list_todolist,
    detail_todolist,
    create_todolist,
    edit_todolist,
    delete_todolist,
    create_todoitem,
    edit_todoitem,

)

urlpatterns = [
    path("", list_todolist, name="todo_list_list"),
    path("<int:pk>", detail_todolist, name="todo_list_detail"),
    path("create/", create_todolist, name="todo_list_create"),
    path("<int:pk>/edit/", edit_todolist, name="todo_list_edit"),
    path("<int:pk>/delete/", delete_todolist, name="todo_list_delete"),
    path("items/create/", create_todoitem, name="todo_item_create"),
    path("items/<int:pk>/edit/", edit_todoitem, name="todo_item_edit"),
]
