from django.db import models

# Create your models here.

class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(6)
    Booking_date = models.DateField()

class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()
        
    def __str__(self):
        return f'{self.Title} : ${self.Price}'


