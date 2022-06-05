from django.urls import path
from .views import ListDrone,CreateDrone, DetailDrone, ListDroneLoading, DispatchDrone,ListDispatchDrone , BatteryDrone, ListMedicationsDispatchDrone

urlpatterns = [
    path('<int:pk>/', DetailDrone.as_view(), name='drone_detail'), # details drone
    path('drone/list', ListDrone.as_view(), name='list_drone'), # all drone list
    path('drone/loading', ListDroneLoading.as_view(), name='list_drone_loading'), # drone list loading
    path('drone/create', CreateDrone.as_view(), name='create_drone'), # create drone
    path('drone/<int:pk>/check', BatteryDrone.as_view(), name='check_battery_drone'), # Check Battery drone
    path('dispatch/create', DispatchDrone.as_view(), name="create_dispatch"),
    path('dispatch/list', ListDispatchDrone.as_view(), name="list_dispatch"),
    path('dispatch/<int:pk>/med', ListMedicationsDispatchDrone.as_view(), name='list_medications_by_drone'), # List medicaction by drone
    ]
