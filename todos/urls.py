from django.urls import path

from todos.views import (
    list_todolist,
    detail_todolist,
)

urlpatterns = [
    path("", list_todolist, name="todo_list_list"),
    path("<int:pk>", detail_todolist, name="todo_list_detail")
]
