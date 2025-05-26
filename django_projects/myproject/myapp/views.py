from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("<h1>Hello this is home page")
    return render(request, "myapp/home.html")

def about(request):
    # return HttpResponse("<h1>Hello this is home page")
    return render(request, "myapp/about.html")

def contact(request):
    # return HttpResponse("<h1>Hello this is home page")
    return render(request, "contact/home.html")