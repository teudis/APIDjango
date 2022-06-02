from django.db import models

# Create your models here.
class Drone(models.Model):
    MODEL_DRONE = (
        ('Lightweight', 'Lightweight'),
        ('Middleweight', 'Middleweight'),
        ('Cruiserweight', 'Cruiserweight'),
        ('Heavyweight', 'Heavyweight'),
    )
    DRONE_STATUS = (
        ('IDLE', 'IDLE'),
        ('LOADING', 'LOADING'),
        ('LOADED', 'LOADED'),
        ('DELIVERING', 'DELIVERING'),
        ('DELIVERED', 'DELIVERED'),
        ('RETURNING', 'RETURNING'),
    )

    serial_number = models.CharField(max_length=100)
    weight = models.CharField(max_length=4)
    battery_capacity = models.CharField(max_length=3)
    model_drone = models.CharField(max_length=20, choices=MODEL_DRONE)
    state = models.CharField(max_length=20, choices=DRONE_STATUS)

    def __str__(self):
        return self.serial_number

class Medication(models.Model):
    name = models.CharField(max_length=50)
    weight = models.CharField(max_length=30)
    code = models.CharField(max_length=5)
    picture = models.CharField(max_length=200)

    def __str__(self):
        return self.name