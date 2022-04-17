from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    business_name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    account_owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.business_name
