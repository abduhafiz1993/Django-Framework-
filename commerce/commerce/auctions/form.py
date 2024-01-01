# forms.py

from django import forms
from .models import AuctionListing

class CreateListingForm(forms.ModelForm):
    class Meta:
        model = AuctionListing
        fields = ['title', 'description', 'starting_price', 'image', 'category']

    # Add additional fields if needed, such as URL for an image

