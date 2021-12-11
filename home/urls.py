from django.urls import path, include, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('create/', views.create, name="create_view"),
    path("", views.view, name="home_view"),
    path('api/', views.apiOverview, name="api_overview"),
    path("api/people-names", views.peopleNames, name="people-names")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
