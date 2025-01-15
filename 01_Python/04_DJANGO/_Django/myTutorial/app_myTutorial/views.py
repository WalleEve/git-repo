from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required 
from app_myTutorial.models import PersonalUser

# Create your views here.

# Login view 

def user_login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		
		if user is not None:
			login(request, user)
			return redirect('home') # redirect to the home page 
	return render(request, 'login.html')
	
# home page with menu options 
	
def home(request):
    return render(request, 'home.html')
	
# Menu detais view 

@login_required 
def tutorial_detail(request, category):
	return render(request, 'tutorial_detail.html', {'category': category})
	
# Personal login view 

def parsonal_login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		
		if PersonalUser.objects.filter(username = username, password = password).exists():
			return render(request, 'Personal_home.html') # Redirect to personal home 
			
	return render(request, 'personal_login.html')
	





