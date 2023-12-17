from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Brand(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='car_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    
    def __str__(self):
        return self.text
