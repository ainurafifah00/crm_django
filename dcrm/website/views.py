from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


# 3 steps process:
# view
# function thing
# url

def home(request):
	#check if user is logged in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		#Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, 'You Have Been Logged In!')
			return redirect('home')
		else:
			messages.success(request, 'There Was An Error Logging In, Please Try Again')
			return redirect('home')
	else:
		return render(request, 'home.html', {})

def login_user(request):
	#our login function is under the home function
	pass

def logout_user(request):
	logout(request)
	messages.success(request, "You Have Successfully Logged Out")
	return redirect('home')

def register_user(request):
	return render(request, 'register.html', {})

