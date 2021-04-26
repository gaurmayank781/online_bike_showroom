from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile = models.IntegerField(null=True)
    city = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    image = models.ImageField(null=True)
    def __str__(self):
        return self.user.username

class Bike_Type(models.Model):
    type = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.type

class Company(models.Model):
    name = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=30, null=True)
    email1 = models.EmailField(null=True)
    mobile = models.IntegerField(null=True)
    image = models.FileField(null=True)
    def __str__(self):
        return self.name

class Bike_detail(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(Bike_Type, on_delete=models.CASCADE, null=True)
    bike_name = models.CharField(max_length=100,null=True)
    number = models.CharField(max_length=100,null=True)
    price = models.IntegerField(max_length=100,null=True)
    fuel_type = models.CharField(max_length=100,null=True)
    displacement = models.CharField(max_length=100,null=True)
    max_power = models.CharField(max_length=100,null=True)
    max_torque = models.CharField(max_length=100,null=True)
    milage = models.CharField(max_length=100,null=True)
    gear = models.CharField(max_length=100,null=True)
    front_type = models.CharField(max_length=100,null=True)
    rear_type = models.CharField(max_length=100,null=True)
    length = models.CharField(max_length=100,null=True)
    width = models.CharField(max_length=100,null=True)
    height = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    img1 = models.FileField(null=True)
    img2 = models.FileField(null=True)
    img3 = models.FileField(null=True)
    img4 = models.FileField(null=True)
    img5 = models.FileField(null=True)
    def __str__(self):
        return self.company.name+" "+self.bike_name

class Status(models.Model):
    status = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.status

class Booking(models.Model):
    status = models.ForeignKey(Status,on_delete=models.CASCADE,null=True)
    signup = models.ForeignKey(Signup,on_delete=models.CASCADE,null=True)
    bike = models.ForeignKey(Bike_detail,on_delete=models.CASCADE,null=True)
    date1 = models.DateField(null=True)
    def __str__(self):
        return self.bike.bike_name+" "+self.signup.user.username

class Send_Feedback(models.Model):
    signup = models.ForeignKey(Signup,on_delete=models.CASCADE,null=True)
    date = models.DateField(null=True)
    message1 = models.TextField(null=True)
    def __str__(self):
        return self.signup.user.username
