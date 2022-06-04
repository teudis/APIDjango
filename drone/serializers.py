from rest_framework import serializers
from .models import Drone, DispacherDrone

class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = ('serial_number', 'weight', 'battery_capacity', 'model_drone', 'state',)

    def validate_weight(self, value):
        if int(value) < 1 or int(value) > 500:
            raise serializers.ValidationError('Your weigth must be between 1 to 500 gr.')
        return value

    def validate_battery_capacity(self, value):
        if int(value) < 1 or int(value) > 100:
            raise serializers.ValidationError('Your Battery capacity must be between 1 to 10 percentage.')
        if int(value) < 25:
            raise serializers.ValidationError('Your Battery capacity cannot below 25%')
        return value


class DispatcherDroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispacherDrone
        fields = ('drone', 'medications',)