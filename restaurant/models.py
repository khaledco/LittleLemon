from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=300)
    number_of_guests = models.SmallIntegerField()
    booking_date = models.DateTimeField(auto_now=True)

class Menu(models.Model):
    title = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()
    
    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'