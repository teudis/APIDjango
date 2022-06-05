from django.urls import path
from .views import ListDrone,CreateDrone, DetailDrone, ListDroneLoading, DispatchDrone

urlpatterns = [
    path('<int:pk>/', DetailDrone.as_view(), name='drone_detail'), # details drone
    path('drone/list', ListDrone.as_view(), name='list_drone'), # all drone list
    path('drone/loading', ListDroneLoading.as_view(), name='list_drone_loading'), # drone list loading
    path('drone/create', CreateDrone.as_view(), name='create_drone'), # create drone
    path('dispatch', DispatchDrone.as_view()),
    ]
