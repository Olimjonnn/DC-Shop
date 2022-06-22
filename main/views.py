from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .task import *


@api_view(['GET'])
def Resultt(request):
    all = Result.objects.all()
    a = []
    for i in all:
        dat = {
            "Name": i.driver.name,
            "Age": i.driver.age,
            "Car"  
                "Car": i.car.name,
                "Made in": i.car.madein,
                "Speed": i.car.name,
                
        }
        a.append(dat)
    print(a)
    return Response(a)    

