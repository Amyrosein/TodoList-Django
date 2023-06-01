from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User


def register_user(request):
	if request.method == 'POST':
		print(request.POST)
		user = User.objects.create(username=request.POST['username'], password=request.POST['password'])

		return HttpResponseRedirect('/accounts/login/')
	return render(request, "registration/register.html")
