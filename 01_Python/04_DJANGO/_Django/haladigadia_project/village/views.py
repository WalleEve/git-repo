from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm

# Create your views here.
def home(request):
    return render(request, 'village/home.html')

def login_view(request):
    return render(request, 'village/login.html')


class CustomLoginView(LoginView):
    template_name = 'village/login.html'
    authentication_form = CustomLoginForm
