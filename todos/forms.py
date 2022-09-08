from django import forms
from todos.models import TodoList, TodoItem


class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ["name"]


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ["task"]
