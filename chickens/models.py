from django.db import models

# Create your models here.
class Chicken(models.Model):
    breed = models.CharField(max_length=100)
    weight = models.PositiveSmallIntegerField()
    life_expectancy = models.PositiveSmallIntegerField()
    cuteness_level = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")