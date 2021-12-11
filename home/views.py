from django.shortcuts import render
from .models import People
from .forms import Peopleform
from django.contrib import messages
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PeopleSerializer


# Create your views here.
def create(request, *args, **kwargs):
    if request.method == "GET":
        form = Peopleform()
        context = {"form":form}
        return render(request, "create.html", context)
    if request.method == "POST":
        form = Peopleform(request.POST or None)
        if request.POST['email'].split("@")[1] == "srmist.edu.in":
            pass
        else:
            messages.error(request, "Please use only SRM email.")
            return render(request, "create.html", {"form": form})
        if form.is_valid():
            form.save()
            form = Peopleform()
            context = {"form" : form}
            messages.success(request, "Successfully sent!")
        else:
            messages.error("Something went wrong, please try again.")
        return render(request, "create.html", context)

    
def view(request, *args, **kwargs):

    # Arrays and Variables 
    
    objects = People.objects.all()
    names = []
    items = []

    # Algorithm to remove repeating submitted form

    for i in objects:
        if i.name.lower() in names:
            index = names.index(i.name.lower())
            People.objects.filter(pk=items[index].id).delete()
        else:
            names.append(i.name.lower())
            items.append(i)
##        People.objects.filter(name="Ananmay").delete()
    context = {'objects': objects}
    return render(request, "view.html", context)

# API's
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "Names" : "/people-names/",
        "Details" : "/people-details/<str:pk>/",
        "Create": "/people-create/",
        "Update" : "/people-update/<str:pk>",
        "Delete" : "/people-delete/<str:pk>"
    }
    return Response(api_urls)

@api_view(['GET'])
def peopleNames(request):
    people = People.objects.all()
    serializer = PeopleSerializer(people, many=True)
    return Response(serializer.data)

