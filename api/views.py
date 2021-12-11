from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "names" : "/task-names/",
        "details" : "/task-details/<str:pk>/",
        "create": "/task-create/",
        "update" : "/task-update/<str:pk>",
        "delete" : "/task-delete/<str:pk>"
    }
    return Response(api_urls)