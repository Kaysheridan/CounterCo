from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


class AppCustomer(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    names = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.names)


class Foodoptions(models.Model):
    name = models.CharField(max_length=150)
    food_group = models.ManyToManyField(Category)
    calories = models.DecimalField(decimal_places=1, max_digits=5, default=0,
    blank=True)
    protein = models.DecimalField(decimal_places=1, max_digits=5, default=0)
    carbs = models.DecimalField(decimal_places=1, max_digits=5, default=0)
    fats = models.DecimalField(decimal_places=1, max_digits=5, default=0)
    amount = models.IntegerField(default=1, blank=True, null=True)

    def __str__(self):
        return str(self.names)


