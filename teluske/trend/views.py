from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")

def service(request):
    return render(request, "service.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact-us.html")

def project(request):
    return render(request, "project.html")
    
def team(request):
    return render(request, "team.html")    


def male_service(request):
    return render(request, "team.html") 

