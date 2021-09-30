from django.db import models


class Order(models.Model):
    pickup = models.CharField(max_length=50)
    drop = models.CharField(max_length=50)
    when = models.CharField(max_length=70)
    price = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)


class YandexCar(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=15)
    numbers = models.IntegerField()
    size = models.CharField(max_length=10)
    tip = models.CharField(max_length=20)
    image = models.ImageField(upload_to='pics')


class JorgoCar(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=15)
    numbers = models.IntegerField()
    size = models.CharField(max_length=10)
    timestamp = models.CharField(max_length=20)
    image = models.ImageField(upload_to='pics')



class NambaCar(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=15)
    numbers = models.IntegerField()
    size = models.CharField(max_length=10)
    timestamp = models.CharField(max_length=20)
    image = models.ImageField(upload_to='pics')



class Client(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    card = models.CharField(max_length=20)
    phone = models.CharField(max_length=50)
    pay = models.CharField(max_length=10)
