from django.urls import path
from .views import ListDrone, DetailDrone
urlpatterns = [
    path('<int:pk>/', DetailDrone.as_view()),
    path('', ListDrone.as_view()),
    ]