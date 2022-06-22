from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


class Car(models.Model):
    name = models.CharField(max_length=100)
    madein = models.CharField(max_length=100)
    speed = models.IntegerField()

class Result(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
        
