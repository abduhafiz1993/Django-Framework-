# forms.py

from django import forms
from .models import AuctionListing

class CreateListingForm(forms.ModelForm):
    """Creates form for Auction model."""
    title = forms.CharField(label="Title", max_length=20, required=True, widget=forms.TextInput(attrs={
                                                                            "autocomplete": "off",
                                                                            "aria-label": "title",
                                                                            "class": "form-control"
                                                                        }))
    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={
                                    'placeholder': "Tell more about the product",
                                    'aria-label': "description",
                                    "class": "form-control"
                                    }))
    image_url = forms.URLField(label="Image URL", required=True, widget=forms.URLInput(attrs={
                                        "class": "form-control"
                                    }))

    category = forms.ChoiceField(required=True, choices=Auction.CATEGORY, widget=forms.Select(attrs={
                                        "class": "form-control"
                                    }))

    class Meta:
        model = Auction
        fields = ["title", "description", "category", "image_url"]

class BidForm(forms.ModelForm):
    """Creates form for Bid model."""
    class Meta:
        model = Bid
        fields = ["bid_price"]
        labels = {
            "bid_price": _("")
        }
        widgets = {
            "bid_price": forms.NumberInput(attrs={
                "placeholder": "Bid",
                "min": 0.01,
                "max": 100000000000,
                "class": "form-control"
            })
        }

class CommentForm(forms.ModelForm):
    """Creates form for Comment model."""
    class Meta:
        model = Comment
        fields = ["comment"]
        labels = {
            "comment": _("")
        }
        widgets = {
            "comment": forms.Textarea(attrs={
                "placeholder": "Comment here",
                "class": "form-control",
                "rows": 1
            })
        }

