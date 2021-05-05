from django.db import models

# Create your models here.
class Location(models.Model):
    loc = models.CharField(max_length=255)
    class Meta:
        db_table:"location"

    

class Shop(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    loc = models.ForeignKey(Location, on_delete=models.CASCADE)
    class Meta:
        db_table:'shop'
    