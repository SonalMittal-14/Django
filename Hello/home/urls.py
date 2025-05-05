from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
    path("", views.index, name="home"), # ki koin bhi agar aata h toh use bhej do views.index mai or iska name rakh do home

    path("about", views.about, name="about"),
    path("service", views.service, name="service"),
    path("contact", views.contact, name="contact"),

]
