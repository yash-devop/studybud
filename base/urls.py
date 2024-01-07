from django.urls import path
from . import views
# or   from django.views import views

urlpatterns = [
    path("",views.home, name="Home"),
    path("room/<str:id>/",views.room, name="Room")
]
