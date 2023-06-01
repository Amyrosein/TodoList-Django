from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Todo
from .forms import TodoForm, UpdateTodoForm


@login_required(login_url="/accounts/login/")
def todo_view(request):
	user = request.user
	if request.method == "GET":
		todos = Todo.objects.filter(user=user)
		form = TodoForm()
		context = {"todos": todos, 'form': form}
		return render(request, "todos/todos.html", context=context)
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			task = form.cleaned_data['add_todo']
			todo = Todo.objects.create(user=user, description=task)
			todo.save()
			return HttpResponseRedirect("/")
	return HttpResponse("Invalid request")

@login_required
def todo_delete(request, id):
	todo = Todo.objects.get(pk=id).delete()
	return HttpResponseRedirect('/')


@login_required
def update_todo(request, id):
	if request.method == "POST":
		todo = Todo.objects.filter(pk=id).update(description=request.POST['todo'])
		return HttpResponseRedirect("/")


def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")