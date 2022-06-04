from django.urls import path
from .views import ListDrone, DetailDrone, ListDroneLoading, DispatchDrone

urlpatterns = [
    path('<int:pk>/', DetailDrone.as_view()), # details drone
    path('', ListDrone.as_view()), # all drone list
    path('loading', ListDroneLoading.as_view()), # drone list loading
    path('dispatch', DispatchDrone.as_view()),
    ]
