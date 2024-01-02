

from django import forms
from .models import *

class CreateListingForm(forms.ModelForm):
    class Meta:
        model = AuctionListing
        exclude = ["winner", "closed", "seller", "current_price"]

class BidForm(forms.ModelForm):
    """Creates form for Bid model."""
    class Meta:
        model = Bid
        fields = ["bid_price"]

        

class CommentForm(forms.ModelForm):
    """Creates form for Comment model."""
    class Meta:
        model = Comment
        fields = ["text"]

