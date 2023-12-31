from django.urls import path
from . import views

app_name = "flights"

urlpatterns = [
    path('', views.index, name="index"),
    path('flight/<int:number>', views.flight, name="flight"),

]