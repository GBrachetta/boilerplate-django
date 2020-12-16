from django.urls import path
from . import views


# This is your first, dummy url pattern.
# Please edit it to your own needs.

urlpatterns = [
    path("", views.home, name="home"),
]
