from rest_framework import serializers
from .models import Drone

class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = ('serial_number', 'weight', 'battery_capacity', 'model_drone', 'state',)

    def validate_weight(self, value):
        if value < 1  or value > 500:
            raise serializers.ValidationError('Your weigth must be between 1 to 500 gr.')
        return value

    def validate(self, value):
        if value < 1  or value >100:
             raise serializers.ValidationError('Your Battery capacity must be between 1 to 10 percentage.')
        return value