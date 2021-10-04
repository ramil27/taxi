from django.shortcuts import render, redirect
from .models import *


def home(request):
    cars = Car.objects.all()
    return render(request, 'index.html', {'cars': cars})


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        print(name, phone, address)
        ins = Order(name=name, address=address, phone=phone)
        ins.save()
        print('data save in db')
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')
