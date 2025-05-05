from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is HomePage.")
    
def about(request):
    return HttpResponse("This is About Page.")

def service(request):
    return HttpResponse("This is service Page.")

def contact(request):
    return HttpResponse("This is Contact Page.")

