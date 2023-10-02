from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)

class Wallet(models.Model):
    amount = models.CharField(max_length=30)
    owner = models.ForeignKey("User", on_delete=models.CASCADE,)
    last_updated = models.DateTimeField("last updated")