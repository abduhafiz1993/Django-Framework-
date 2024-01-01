from django.contrib import admin
from .models import AuctionListing, Comment, Bid, User


class AuctionListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'current_price', 'end_time', 'seller', 'closed')
    list_filter = ('category', 'closed')
    search_fields = ('title', 'description', 'seller__username')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('commenter', 'auction_listing', 'comment_time')
    list_filter = ('auction_listing__category',)
    search_fields = ('text', 'commenter__username')

class BidAdmin(admin.ModelAdmin):
    list_display = ('bidder', 'auction_listing', 'amount', 'bid_time')
    list_filter = ('auction_listing__category',)
    search_fields = ('bidder__username', 'auction_listing__title')


admin.site.register(AuctionListing, AuctionListingAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(User)