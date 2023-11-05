from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Account(AbstractUser):
    balance = models.IntegerField("Баланс",  default=0)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Product(models.Model):
    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length = 100) 
    info  = models.CharField(max_length = 100, default = '')
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
   