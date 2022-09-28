from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


class AppCustomer(models.Model):
    names = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=200, null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.names)