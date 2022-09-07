from django.urls import path

from todos.views import (
    list_todolist,
    detail_todolist,
    create_todolist,
    edit_todolist,
)

urlpatterns = [
    path("", list_todolist, name="todo_list_list"),
    path("<int:pk>", detail_todolist, name="todo_list_detail"),
    path("create/", create_todolist, name="todo_list_create"),
    path("<int:pk>/edit/", edit_todolist, name="todo_list_edit"),
]
