from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, "flights/index.html",{
        "flights": Flight.objects.all()
    })

def flight(request, number):
    flight = Flight.objects.get(pk=number)
    return render(request, "flights/flight.html",{
        "flight": flight
    })
