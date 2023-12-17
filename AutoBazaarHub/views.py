from django.shortcuts import render
from auto_bazaar import models

def home(request):
    brands = models.Brand.objects.all()
    cars = models.Car.objects.all()
    return render(request, 'home.html', {"brands": brands, "cars": cars})