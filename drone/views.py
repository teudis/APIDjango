from rest_framework import generics
from .models import Drone, DispacherDrone
from .serializers import DroneSerializer, DispatcherDroneSerializer, BatteryDroneSerializer, DispatcherDroneMedicationSerializer

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

#SHOW BATTERY LEVEL BY DRONE(ID)
class BatteryDrone(generics.RetrieveAPIView):
    queryset = Drone.objects.only('battery_capacity')
    serializer_class = BatteryDroneSerializer

#Drone LIST STATE LOADING
class ListDroneLoading(generics.ListAPIView):
    queryset = Drone.objects.filter(state="LOADING")
    serializer_class = DroneSerializer

#CREATE Dispatcher DRONE
class DispatchDrone(generics.CreateAPIView):
    serializer_class = DispatcherDroneSerializer


#LIST Dispatcher DRONE
class ListDispatchDrone(generics.ListAPIView):
    queryset = DispacherDrone.objects.all()
    serializer_class = DispatcherDroneSerializer

#LIST Medications from Dispatcher DRONE
class ListMedicationsDispatchDrone(generics.RetrieveAPIView):
    queryset = DispacherDrone.objects.all()
    serializer_class = DispatcherDroneMedicationSerializer