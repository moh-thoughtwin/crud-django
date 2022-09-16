from crypt import methods
from urllib import request
from django.shortcuts import render, redirect,HttpResponse
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import  render, redirect

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
# Create your views here.

    
#from demo.core.forms import SignUpForm

def Index(request):
    return render(request,'users/index.html')

def Register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request,"User created ")
            return redirect('login')
        messages.error(request,"Unsuccessfull")
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', {'form': form})


def Login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="users/login.html", context={"login_form":form})