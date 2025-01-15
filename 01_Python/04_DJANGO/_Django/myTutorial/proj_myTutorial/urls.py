"""
URL configuration for proj_myTutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_myTutorial import views 


urlpatterns = [
    path('admin/', admin.site.urls),
	path('', views.home, name='login'),
	path('home/', views.home, name='home'),
	path('app_myTutorial/<str:category>/', views.tutorial_detail, name = 'tutorial_detail'),
	path('personal-login/', views.parsonal_login, name='personal_login'),
    path('accounts/', include('django.contrib.auth.urls')), 
]
