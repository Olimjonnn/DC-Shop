from django.shortcuts import render
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializer import *
from rest_framework import viewsets
from . import models
# HOME

class Slider(ListAPIView):
    http_method_names = ['get']
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        slider = Product.objects.all().order_by('-id')[0:6]
        ser = ProductSerializer(slider, many=True)
        return Response(ser.data)

class LatestProduct(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        product = Product.objects.all().order_by('-id')[0:6]
        ser = ProductSerializer(product, many=True)
        return Response(ser.data)

# SHOP

def Search(request):
    name = request.GET.get('name')
    product = Product.objects.get(name__icontains=name)
    ser = ProductSerializer(product, many=True)
    return Response(ser.data)

def Filter(request):
    firstprice = request.GET.get('firstprice')
    secondprice = request.GET.get('secondprice')
    product = Product.objects.filter(price__gte=firstprice, price__lte=secondprice)
    ser = ProductSerializer(product, many=True)
    return Response(ser.data)

class ProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductPk(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class WishlistView(ListAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

class CardView(ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

def Sortby(request, pk):
    products = Product.objects.get(category_id=pk)
    ser = ProductSerializer(products, many=True)
    return Response(ser.data)

def Shopby(request, pk):
    products = Product.objects.get(category_id=pk)
    ser = ProductSerializer(products, many=True)
    return Response(ser.data)

class ContactView(CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

class ReviewVw(APIView):

    def post(self, request, pk):
        product = Product.objects.get(id=pk),
        user = request.user
        a = Review.objects.create(
            product = product,
            raiting = request.data['raiting'],
            text = request.data['text'],
            message = request.data['message'],
            user = user,
        )
        b = ReviewSerializer(a)
        return Response(b.data)
    
    def get(self, request):
        review = Review.objects.all()
        ser = ReviewSerializer            

# LOGIN

# models.Product.objects.filter(is_active=False).order_by('-id')[:6]

User