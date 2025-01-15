from django.contrib import admin
from .models import PersonalUser  # Import the PersonalUser model


# Register your models here.

# Register the PersonalUser model with the admin site
admin.site.register(PersonalUser)
