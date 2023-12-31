from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, "flights/index.html",{
        "flights": Flight.objects.all()
    })

def flight(request, number):
    flight = Flight.objects.get(pk=number)
    passengers = flight.passengers.all()
    return render(request, "flights/flight.html",{
        "flight": flight,
        "passengers": passengers
    })

def book(request, number):
    pass
