import email
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator,  MinValueValidator

class User(AbstractUser):
    type = models.IntegerField(choices=(
        (1, 'Director'),
        (2, 'Manager'),
        (3, 'User'),
    ), default=3)
    phone = models.IntegerField(null=True, blank=True)
    email = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.username
    
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Info(models.Model):
    logo = models.ImageField(upload_to='Info/')
    in_link = models.URLField()
    tw_link = models.URLField()
    fa_link = models.URLField()
    insta_link = models.URLField()

class Newsletter(models.Model):
    email = models.EmailField()

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to="Product/")
    image2 = models.ImageField(upload_to="Product/")
    image3 = models.ImageField(upload_to="Product/")
    image4 = models.ImageField(upload_to="Product/")
    image5 = models.ImageField(upload_to="Product/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date =  models.DateField(auto_now_add=True)
    text = models.TextField()
    discount = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ], default=0
    )
    rating = models.FloatField(default=0)
    reviews = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    SKU = models.IntegerField(default=1)
    description = models.TextField()
    weight = models.FloatField()
    dimentions = models.CharField(max_length=100)
    colours = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Slider(models.Model):
    title = models.CharField(max_length=90)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.FloatField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    date =  models.DateField(auto_now_add=True)

class ContactUs(models.Model):
    first_name = models.CharField(max_length=199)
    last_name = models.CharField(max_length=199)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()


class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title

class Card(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.title

class Blog(models.Model):
    img = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=255)
    mintext = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    blogtext = models.ManyToManyField('Blogtext', blank=True, null=True)

class Reply(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    website = models.CharField(max_length=255)
    comment = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Blogtext(models.Model):
    text = models.CharField(max_length=100)

    

class About(models.Model):
    img = models.ImageField(upload_to='About/')
    title = models.CharField(max_length=255)
    mintext = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    blogtext = models.ManyToManyField('Abouttext', blank=True, null=True)


class Abouttext(models.Model):
    text = models.CharField(max_length=100) 