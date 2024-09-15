from django.db import models


# Create your models here.
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    booking_date = models.DateTimeField()
    number_of_people = models.IntegerField()

    def __str__(self):
        return f"{self.customer_name} - {self.booking_date}"
