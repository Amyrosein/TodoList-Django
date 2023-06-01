from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Todo
from .forms import TodoForm, UpdateTodoForm


def todo_view(request):
	if request.method == "GET":
		todos = Todo.objects.all()
		form = TodoForm()
		context = {"todos": todos, 'form': form}
		return render(request, "todos/todos.html", context=context)
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			todo = Todo.objects.create(description=form.data['add_todo'])
			todo.save()
			return HttpResponseRedirect("/")


def todo_delete(request, id):
	todo = Todo.objects.get(pk=id).delete()
	return HttpResponseRedirect('/')


def update_todo(request, id):
	if request.method == "POST":
		todo = request.POST['todo']
		todo = Todo.objects.filter(pk=id).update(description=todo)
		return HttpResponseRedirect("/")