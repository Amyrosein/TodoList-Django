from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError



def register_user(request):
	if request.method == 'POST':
		try:
			user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
			user.save()
			return HttpResponseRedirect("/accounts/login")
		except IntegrityError:
			error_message = "یوزرنیم موجود است. یک یوزرنیم دیگه انتخاب کنید!"
			return render(request, "profiles/register.html", {'error_message': error_message})
	return render(request, "profiles/register.html")


def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/accounts/login/')
	return render(request, "profiles/login.html")