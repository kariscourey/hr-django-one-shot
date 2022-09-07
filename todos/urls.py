from django.urls import path

from todos.views import (
    show_todolist,
)

urlpatterns = [
    path("", show_todolist, name="todo_list_list")
]
