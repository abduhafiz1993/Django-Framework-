from django.contrib import admin
from .models import *

# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

# Register your models here.
admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(Passanger )


