from django.shortcuts import render

from django.http import HttpResponse

from .models import Course

# Create your views here.


def index(request):
    # return HttpResponse("Hello World")
    courses = Course.objects
    return render(request,'courses/index.html',{'courses' : courses})
