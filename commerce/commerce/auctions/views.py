from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .form import *
from django.contrib.auth.models import User

# @login_required

from .models import User, AuctionListing


def index(request):
    AuctionListings = AuctionListing.objects.filter(closed=False).order_by("end_time")
    return render(request, "auctions/index.html",{
        "Acution_listings": AuctionListings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required(login_url="login")
def create_listing(request):

    if request.method == "POST":
        form = CreateListingForm(request.POST)
        
        if form.is_valid():

            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            category = form.cleaned_data["category"]
            image = form.cleaned_data["image"]
            starting_price = form.cleaned_data["starting_price"]
            current_price = form.cleaned_data["starting_price"]
            starting_bid = form.cleaned_data["starting_bid"]
            end_time = form.cleaned_data['end_time']

            au = AuctionListing(
                seller = User.objects.get(pk=request.user.id),
                title = title,
                description = description,
                category = category,
                image = image,
                starting_price = starting_price,
                current_price = current_price,
                starting_bid =starting_bid,
                end_time = end_time
            )
            au.save()

            return HttpResponseRedirect(reverse('index'))
        
        else:
            return render(request, "auctions/create.html", {
                "form": form
            })

    return render(request, "auctions/create.html",{
        "form": CreateListingForm()
    })


