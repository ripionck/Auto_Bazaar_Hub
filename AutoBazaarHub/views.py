from django.shortcuts import render
from auto_bazaar import models

def home(request):
    brands = models.Brand.objects.all()
    cars = models.Car.objects.all()
    print(brands)
    return render(request, 'home.html', {"banrds": brands, "cars": cars})