from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def homePage(request):
    data = {
        'title': 'My Home',
        'bdata': 'Welcome to Wscubetech',
        'clist': ['PHP', 'Java', 'Python', 'Django'],
        'numbers': [],
        'student_details': [
            {'name': 'Sayed Mahfuze', 'phone': 9692392243},
            {'name': 'Sabiha', 'phone': 7799876552}
        ]
    }
    return render(request, "index.html", data)

def aboutus(request):
    return HttpResponse('Welcome to Wscubetech')

def course(request):
    return HttpResponse('Welcome to Wscubetech')

def courseDetails(request, courseid):
    return HttpResponse(courseid)

