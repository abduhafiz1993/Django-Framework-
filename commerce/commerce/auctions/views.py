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
        form = CreateListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.seller = request.user
            listing.current_price = form.cleaned_data["starting_price"]
            listing.save()
            return HttpResponseRedirect(reverse('index'))        
        
        else:
            return render(request, "auctions/create.html", {
                "form": form
            })

    return render(request, "auctions/create.html",{
        "form": CreateListingForm()
    })



def listing_detail(request, pk):
    listing = AuctionListing.objects.get(pk=pk)
    bids = Bid.objects.filter(auction_listing=listing).order_by('-amount')
    comments = Comment.objects.filter(auction_listing=listing).order_by('comment_time')

    if request.method == 'POST':
        # Handle bid submission
        bid_form = BidForm(request.POST)
        if bid_form.is_valid():
            bid_amount = bid_form.cleaned_data['bid_price']
            if bid_amount >= listing.starting_bid and (not bids or bid_amount > bids[0].amount):
                bid = bid_form.save(commit=False)
                bid.bidder = request.user
                bid.auction_listing = listing
                bid.amount = bid_form.cleaned_data["bid_price"]
                bid.save()
                listing.current_price = bid_amount
                listing.save()
            else:
                # Present an error to the user
                pass
                
    else:
        bid_form = BidForm()

    '''
    # Handle adding/removing from watchlist
    watchlist_status = False
    if request.user.is_authenticated:
        watchlist_status = request.user.watchlist.filter(pk=listing.pk).exists()

        if request.method == 'POST':
            if watchlist_status:
                request.user.watchlist.remove(listing)
            else:
                request.user.watchlist.add(listing)
            return redirect('listing_detail', pk=pk)
    '''
    # Handle closing the auction if the user is the seller
    if request.user == listing.seller and not listing.closed:
        if request.method == 'POST' and 'close_auction' in request.POST:
            listing.winner = bids[0].bidder if bids else None
            listing.closed = True
            listing.save()

    # Display winner status if the auction is closed and the user won
    won_auction = listing.closed and request.user == listing.winner

    # Handle adding comments
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.commenter = request.user
            comment.auction_listing = listing
            comment.save()
            return redirect('listing_detail', pk=pk)
    else:
        comment_form = CommentForm()

    return render(request, 'auctions/list.html', {'listing': listing, 'bids': bids, 'comments': comments,
                                                   'bid_form': bid_form,'won_auction': won_auction, 
                                                   'comment_form': comment_form})



def watchlist(request):
    user_watchlist = UserProfile.objects.filter(user = request.user)
    return render(request, 'aucations/watchlist.html', {'user_watchlist': user_watchlist})                                             