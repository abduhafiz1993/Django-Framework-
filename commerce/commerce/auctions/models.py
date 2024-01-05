from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass



class AuctionListing(models.Model):

    MOTORS = "MOT"
    FASHINON = "FAS"
    ELECTRONICS = "ELE"
    COLLECTIBLES_ARTS = "ART"
    HOME_GARDES = "HGA"
    SPORTING_GOODS = "SPO"
    TOYS = "TOY"
    BUSSINES_INDUSTRIAL = "BUS"
    MUSIC = "MUS"

    CATEGORY = [
        (MOTORS, "Motors"),
        (FASHINON, "Fashion"),
        (ELECTRONICS, "Electronics"),
        (COLLECTIBLES_ARTS, "Collectibles & Art"),
        (HOME_GARDES, "Home & Garden"),
        (SPORTING_GOODS, "Sporting Goods"),
        (TOYS, "Toys"),
        (BUSSINES_INDUSTRIAL, "Business & Industrial"),
        (MUSIC, "Music"),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    end_time = models.DateTimeField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='auctions/static/image', blank=True, null=True)
    category = models.CharField(max_length=3, choices = CATEGORY, default = MOTORS)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='won_auctions', null=True, blank=True)
    closed = models.BooleanField(default=False)


    def __str__(self):
        return f"Auction id: {self.id}, title: {self.title} Description:{self.description} Starting_price: {self.starting_price} Current_price:{self.current_price} End_time:{self.end_time} Seller:{self.seller} Image:{self.image}  Category:{self.category} Starting_bid: {self.starting_bid} winner: {self.winner} closed:{self.closed}" 


class Bid(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_time = models.DateTimeField(auto_now_add=True)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    bid_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Amount:{self.amount} Bid_time:{self.bid_time} Bidder: {self.bidder} Acution_listing:{self.auction_listing}"



class Comment(models.Model):
    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Text: {self.text} comment_time: {self.comment_time} commenter:{self.commenter} auction_listing: {self.auction_listing}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    watchlist = models.ManyToManyField('AuctionListing', blank=True)


    def __str__(self):
        return f"{self.user} wathinglist {self.watchlist}"


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
