from django.shortcuts import render
from .models import Todo

def todo_view(request):
	todos = Todo.objects.all()
	context = {"todos": todos}
	return render(request, "todos/todos.html", context=context)
