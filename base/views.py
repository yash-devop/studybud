from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

rooms = [
    {
        "id": 1,
        "name": "yash",
    },
    {
        "id": 2,
        "name": "pratik",
    }
]

def home(request):
    return render(request,"base/home.html", {"rooms" : rooms} )

def room(request , id):
    room = None
    for i in rooms:
        if i["id"] == int(id):
            room = i;
    print(room)
    context = {"room" : room}
    return render(request,"base/room.html", context)