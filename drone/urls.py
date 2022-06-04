from django.urls import path
from .views import ListDrone, DetailDrone, ListDroneLoading

urlpatterns = [
    path('<int:pk>/', DetailDrone.as_view()),
    path('', ListDrone.as_view()),
    path('loading', ListDroneLoading.as_view()),
    ]