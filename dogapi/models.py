from django.db import models

# Create your models here.
class Breed(models.Model):
    name=models.CharField(max_length=50)
    
class Dog(models.Model):
    fullname=models.CharField(max_length=50)
    image_url=models.CharField(max_length=500)
    breedId=models.ForeignKey("Breed",on_delete=models.CASCADE,null=True)
    