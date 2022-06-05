from rest_framework import generics
from .models import Drone, DispacherDrone
from .serializers import DroneSerializer, DispatcherDroneSerializer

class CreateDrone(generics.CreateAPIView):
    serializer_class = DroneSerializer

#Show Drone List And Add Drone
class ListDrone(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

# Details about a Drone
class DetailDrone(generics.RetrieveAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

class BatteryDrone(generics.RetrieveAPIView):
    queryset = Drone.objects.only('battery_capacity')
    serializer_class = DroneSerializer

#Drone LIST STATE LOADING
class ListDroneLoading(generics.ListAPIView):
    queryset = Drone.objects.filter(state="LOADING")
    serializer_class = DroneSerializer

#Dispacher DRONE
class DispatchDrone(generics.CreateAPIView):
    serializer_class = DispatcherDroneSerializer


#Dispacher DRONE
class ListDispatchDrone(generics.ListAPIView):
    queryset = DispacherDrone.objects.all()
    serializer_class = DispatcherDroneSerializer