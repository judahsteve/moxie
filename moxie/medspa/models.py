from django.db import models

# Create your models here.
class Medspa(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=13,unique=True)
    email = models.CharField(max_length=50,unique=True)

    class Meta:
        db_table = "medspas"