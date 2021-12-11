from . import views
from django.urls.conf import path


urlpatterns = [
    path('', views.apiOverview, name="api_overview")
]