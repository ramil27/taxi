from django.db import models


class Order(models.Model):
    name = models.TextField()
    address = models.TextField()
    phone = models.TextField()


class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=20)
    image = models.ImageField(upload_to='pics')

