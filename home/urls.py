from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
 path('create/', views.create, name="create_view"),
 path("", views.view, name="home_view"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

