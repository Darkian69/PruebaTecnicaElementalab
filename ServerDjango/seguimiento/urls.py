from django.urls import path
from . import views

urlpatterns = [
    path("redirect/", views.tracking_url, name="tracking_url"),
]
