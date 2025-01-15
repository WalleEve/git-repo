""" Defines URL patterns for app_learning_logs."""

from django.urls import include, path
from . import views

urlpatterns = [
    # Home page
    path(r'^$', views.index, name = 'index'),
]
