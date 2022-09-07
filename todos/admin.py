from django.contrib import admin

from todos.models import TodoList


class TodoListAdmin(admin.ModelAdmin):
    pass


admin.site.register(TodoList, TodoListAdmin)
