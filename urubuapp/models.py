from django.db import models
import datetime
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Wallet(models.Model):
    amount = models.CharField(max_length=30)
    owner = models.ForeignKey("User", on_delete=models.CASCADE,)
    last_updated = models.DateTimeField("last updated")

    def last_transaction(self):
        return self.last_updated