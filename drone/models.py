from django.db import models
from django.core.exceptions import ValidationError
import re


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

    serial_number = models.CharField(unique=True, max_length=100)
    weight = models.CharField(max_length=4)
    battery_capacity = models.CharField(max_length=3)
    model_drone = models.CharField(max_length=20, choices=MODEL_DRONE)
    state = models.CharField(max_length=20, choices=DRONE_STATUS)

    def __str__(self):
        return "Serial Number:" + self.serial_number + "---" + "Weigth:" + self.weight


class Medication(models.Model):
    name = models.CharField(max_length=50)
    weight = models.CharField(max_length=30)
    code = models.CharField(unique=True, max_length=5)
    picture = models.ImageField(upload_to='medications/photos')

    def __str__(self):
        return "Name:" + self.name + "---" + "Weigth:" + self.weight

    def clean(self):
        if not re.match("^[A-Za-z0-9_-]*$", self.name):
            raise ValidationError(
                {'name': "Name should have only letters, numbers, ‘-‘, ‘_’"})
        if not re.match("^[A-Z0-9_]*$", self.code):
            raise ValidationError(
                {'code': "Code should have  only upper case letters, underscore and numbers"})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class DispacherDrone(models.Model):
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    medications = models.ManyToManyField(Medication)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    total = models.FloatField(editable=False, blank=True, default=0)

    def __str__(self):
        return self.drone.serial_number + "--" + str(self.created) + "--" + str(self.total)

    def clean(self):
        self.total = 0
        if not self.pk is None:
            for med in self.medications.all():
                self.total += float(med.weight)
            if self.total > int(self.drone.weight):
                raise ValidationError({'medications': "The weight of the medication not be upper to the drone weight limit"})

    def save(self, *args, **kwargs):
        self.total = 0
        if self.pk is None:
            super(DispacherDrone, self).save(*args, **kwargs)
        for med in self.medications.all():
            self.total += float(med.weight)
        self.full_clean()
        super(DispacherDrone, self).save(*args, **kwargs)
