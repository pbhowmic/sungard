## The models module. Contains all models to be used by the projetc

from django.db import models

class Car(models.Model):
    ## The model representing a car.
    # The four fields are:
    # created: Date/Time when the car is entered into database. If not provided, the field value is autogenerated to now()
    # vin: The VIN identifier of the car
    # make: The "make" of the car eg. "Bugatti"
    # carmodel: The model of the car eg: "Veyron"
    # There is a fifth autogenerated field called 'id' which is an autoincremented integer which acts as the primary key for a Car object in the DB

    created = models.DateTimeField(auto_now_add=True)
    vin = models.CharField(max_length=100, blank=False)
    make = models.CharField(max_length=100, blank=False)
    carmodel  = models.CharField(max_length=100, blank=False)
    
    class Meta:
        ordering = ('created',)

