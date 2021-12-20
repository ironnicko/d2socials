from django.shortcuts import render, redirect
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
        if request.POST['email'].split("@")[1] != "srmist.edu.in":
            messages.error(request, "Please use only SRM email.")
            return redirect("create_view")

        if form.is_valid():
            objects = People.objects.all()        
            form.save()
            messages.success(request, "Successfully sent!")
        else:
            messages.error("Something went wrong, please try again.")
        return redirect("create_view")

    
def view(request, *args, **kwargs):

    objects = People.objects.all()
    #  Validate insta accounts
    try:
        for i in objects:
            if "https" in i.instagram.split(":")[0]:
                i.instagram = i.instagram.split("/")[-1]
                i.save()
            if i.instagram[0] == "@":
                i.instagram = i.instagram[1:]
                i.save()
    except Exception as e:
        pass

    # Algorithm to remove repeating submitted form
    emails = {}
    for i in objects:
        if i.email in emails.keys() and i.email != "none":
            element = emails.get(i.email)
            People.objects.filter(pk=element.id).delete()
        else:
            emails[i.email]=i  
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

