from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    # return HttpResponse("This is HomePage.")
    context = {
        'variable1' : "Sonal is amazing",
        'variable2' : "Hehehehe"

    }
    return render(request, 'index.html', context)
    
def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is About Page.")

def service(request):
    return render(request, 'services.html')
    # return HttpResponse("This is service Page.")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        date = request.POST.get('date')

        contact = Contact(name=name, email=email, phone=phone, subject=subject, message=message, date=datetime.today())
        contact.save()
        messages.success(request, "Your Message has been sent!!!")


    return render(request, 'contact.html') 
    # return HttpResponse("This is Contact Page.")

