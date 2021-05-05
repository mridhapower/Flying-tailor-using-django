from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        db_table:"customer"