from django.db import models
from django.contrib.auth.models import User



class brand(models.Model):
    Name=models.CharField(max_length=50)
    Image_field = models.ImageField(null=True,blank=True,upload_to='Brandpic/')

    def __str__(self):

        return self.Name

class Car(models.Model):
    car_image=models.ImageField(null=True,blank=True,upload_to='carpic/')
    Name=models.CharField(max_length=50)
    description=models.TextField()
    quantity=models.IntegerField()
    price=models.IntegerField()
    brand=models.ForeignKey(brand,on_delete=models.CASCADE)
    def __str__(self):

        return self.Name

class comment(models.Model):
    car=models.ForeignKey(Car,on_delete=models.CASCADE,related_name='comments')
    body=models.TextField()
    name=models.CharField(max_length=50)
    def __str__(self):

        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.user.username}"






    
