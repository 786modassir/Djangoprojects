from django.db import models

# Create your models here.
class Customer(models.Model):
    Customer_Name = models.CharField(max_length=50 ,primary_key=True)
    Address = models.CharField(max_length=50)

def __str__(self):
        return self.name
class Food(models.Model):
    Food_Name = models.CharField(max_length=50 ,primary_key=True)
    Price = models.IntegerField()

class Reviews(models.Model):
    Customer_Name = models.ForeignKey(Customer ,on_delete=models.CASCADE)
    Food_Name = models.ForeignKey(Food ,on_delete=models.CASCADE)
    Review_Name = models.CharField(max_length=50)
    Rating = models.IntegerField()