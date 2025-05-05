from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("This is HomePage.")
    context = {
        'variable1' : "Sonal is amazing",
        'variable2' : "Hehehehe"

    }
    return render(request, 'index.html', context)
    
def about(request):
    return HttpResponse("This is About Page.")

def service(request):
    return HttpResponse("This is service Page.")

def contact(request):
    return HttpResponse("This is Contact Page.")

