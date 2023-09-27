import uuid
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)

class Wallet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.DecimalField
    last_update = models.DateTimeField("last update")
    
    
    def __str__(self):
        return self.id
