
from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User


class Expensee(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.BigIntegerField(default=0)
    user = models.ForeignKey(User)
    amount1 = models.BigIntegerField(default=0)  
    amount3 = models.BigIntegerField(default=0)

class income(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.BigIntegerField(default=0)
    user = models.ForeignKey(User)
    amount1 = models.BigIntegerField(default=0)  
    amount3 = models.BigIntegerField(default=0)

