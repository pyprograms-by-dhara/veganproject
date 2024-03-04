from django.db import models

# Create your models here.
class book(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    person=models.CharField(max_length=10)
    date=models.CharField(max_length=20)
    class Meta:
        db_table='book'
