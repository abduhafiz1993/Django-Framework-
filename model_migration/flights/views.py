from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.
def index(request):
    return render(request, "flights/index.html",{
        "flights": Flight.objects.all()
    })

def flight(request, number):
    flight = Flight.objects.get(pk=number)
    passengers = flight.passengers.all()
    non_passenger = Passanger.objects.exclude(flights=flight).all()
    return render(request, "flights/flight.html",{
        "flight": flight,
        "passengers": passengers
        "non_passengers": non_passenger
    })

def book(request, number ):
    if request.method == "POST":

        flight = Flight.objects.get(pk=number)

        passanger_id = int(request.POST["passenger"])

        passenger = Passanger.objects.get(pk=passanger_id)

        passenger.flights.add(flight)

        return HttpResponseRedirect(reverse('flight', args=(number,)))
