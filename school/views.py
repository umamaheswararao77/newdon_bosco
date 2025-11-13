from django.shortcuts import render , redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.template import loader
from .models import Members

# Create your views here.
def index(request):
	return render(request,'index.html',locals())

def register(request):
	return render(request,'register.html',locals())

def register_form(request):
	if request.method == "POST":
		r = Members.objects.create(
			firstname = request.POST['firstname'],
			lastname = request.POST['lastname'],
			email = request.POST['email'],
			mobile = request.POST['mobile'],
			password = request.POST['password']
			)
		r.save()
		return HttpResponseRedirect('/')
	return render(request, 'register.html',locals())

def login(request):
	if request.method == "POST":
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			auth_login(request, user)
			return HttpResponseRedirect("/")
		else:
			msg = 'Invalid Credentials'
	return render(request,'login.html',locals())

def logout_don_bosco(request):
	logout(request)
	return HttpResponseRedirect("/")


