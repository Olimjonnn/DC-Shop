from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    type = models.IntegerField(choices=(
        (1, 'Director'),
        (2, 'Manager'),
        (3, 'User'),
    ), default=3)
    phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
    
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Info(models.Model):
    logo = models.ImageField(upload_to='Info/')
    in_link = models.CharField(max_length=500)
    tw_link = models.CharField(max_length=500)
    fa_link = models.CharField(max_length=500)
    insta_link = models.CharField(max_length=500)
    text = models.CharField(max_length=255, blank=True, null=True)

class Email(models.Model):
    email = models.EmailField()

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to="Product/")
    image2 = models.ImageField(upload_to="Product/")
    image3 = models.ImageField(upload_to="Product/")
    image4 = models.ImageField(upload_to="Product/")
    image5 = models.ImageField(upload_to="Product/")
    price = models.IntegerField()
    reyting = models.IntegerField(choices=(
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
    ), default=0)
    review = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    SKU = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


# class Slider(models.Model):
