from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ListDrone, DetailDrone

urlpatterns = [
    path('<int:pk>/', DetailDrone.as_view()),
    path('', ListDrone.as_view()),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)