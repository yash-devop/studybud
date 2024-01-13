from django.urls import path
from . import views
# or   from django.views import views

urlpatterns = [
    path("login/",views.LoginPage , name="login"),
    path("logout/",views.logoutUser , name="logout"),
    path("register/",views.registerUser , name="register"),
    path("",views.home, name="home"),
    path("room/<str:id>/",views.room, name="room"),
    path("create-form" , views.createRoom , name="create-room"),
    path("update-form/<str:id>/" , views.updateRoom , name="update-room"),
    path("delete-room/<str:id>/" , views.deleteRoom , name="delete-room")

]
