from django.contrib import admin
from .models import Drone, Medication, DispacherDrone

# Register your models here.
admin.site.register(Drone)
admin.site.register(Medication)
admin.site.register(DispacherDrone)