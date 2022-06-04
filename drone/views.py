from rest_framework import generics
from .models import Drone ,DispacherDrone
from .serializers import DroneSerializer, DispatcherDroneSerializer

#Show Drone List And Add Drone
class ListDrone(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

# Details about a Drone
class DetailDrone(generics.RetrieveAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

#Drone LIST STATE LOADING
class ListDroneLoading(generics.ListAPIView):
    queryset = Drone.objects.filter(state="LOADING")
    serializer_class = DroneSerializer


#Dispacher DRONE
class DispatchDrone(generics.ListCreateAPIView):
    queryset = DispacherDrone.objects.all()
    serializer_class = DispatcherDroneSerializer