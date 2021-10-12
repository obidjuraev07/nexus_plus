from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserForm


def register_user(request):
	form = UserForm
	if request.POST:
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			messages.success(request,'Good!')
			return redirect('login')
		else:
			messages.error(request,'error')

	ctx = {
	'form':form,
	'search_bar':'true'
	}
	return render(request,'register.html',ctx)
def login_user(request):
	form = AuthenticationForm
	if request.POST:
		form = AuthenticationForm(request,data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username,password=password)
			if user:
				login(request,user)
				return redirect('home')
			else:
				messages.error(request,'error')
		else:
			messages.error(request,'error')
	ctx = {
	'form':form,
	'search_bar':'true'
	}
	return render(request,'login.html',ctx)
def logout_user(request):
	logout(request)
	return redirect('home')