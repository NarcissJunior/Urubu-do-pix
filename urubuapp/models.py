from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "user"
    
class WalletModel(models.Model):
    amount = models.CharField(max_length=30)
    owner = models.ForeignKey("User", on_delete=models.CASCADE,)
    last_updated = models.DateTimeField("last updated")

    def last_transaction(self):
        return self.last_updated
    
    class Meta:
        db_table = "wallet"