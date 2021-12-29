from django.urls import path, include, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^create/?$', views.create, name="create_view"),
    re_path(r"^/?$", views.view, name="home_view"),
    re_path(r'^api/?$', views.apiOverview, name="api_overview"),
    re_path(r"^api/people-names/?$", views.peopleNames, name="people-names")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
