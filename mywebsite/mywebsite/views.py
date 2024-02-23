from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    data={
        'title': 'Home Page',
        'home_page_body': 'Welcome to mywebsite'
    }
    return render(request,"index.html",data)

def aboutUs(request):
    return HttpResponse("Welcome to mywebsite")

def Course(request):
    return HttpResponse("Welcome to Courses")

def CourseDetails(request,courseid):
    return HttpResponse(courseid)