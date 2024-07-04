from django.db import models
from django.contrib.auth.models import User
import datetime
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Sub_Category(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Color(models.Model):
    color = models.CharField(max_length=225)

    def __str__(self):
        return self.color


class Product(models.Model):
    Availability = (('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock'))
    Condition = (('New', 'New'), ('Old', 'Old'))

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos')
    name = models.CharField(max_length=200)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    price = models.IntegerField()
    availability = models.CharField(choices=Availability, null=True, max_length=225)
    condition = models.CharField(choices=Condition, null=True, max_length=225)
    information = RichTextField(null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class signup(models.Model):
    firstname = models.CharField(max_length=225)
    username = models.CharField(max_length=225)
    email = models.EmailField(max_length=200)
    password = models.IntegerField()


class Contact_us(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    email = models.EmailField(max_length=200)
    address = models.TextField(max_length=225)
    phone = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    zip = models.IntegerField(null=True, blank=True)
    amount = models.CharField(max_length=200)
    payment_id = models.CharField(max_length=300, null=True, blank=True)
    paid = models.BooleanField(default=False,null=True)
    date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return self.user.username


class FinalOrder(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    total = models.FloatField()



ORDERSTATUS = (("Pending", "Pending"), ("On the way", "On the way"),
               ("Delivered", "Delivered"), ("Cancel", "Cancel"), ("return", "return"))
class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    final = models.ForeignKey(FinalOrder, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos2')
    quantity = models.CharField(max_length=225)
    price = models.CharField(max_length=225)
    total = models.CharField(max_length=1000)
    status = models.CharField(choices=ORDERSTATUS, max_length=225)

    def __str__(self):
        return self.order.user.username