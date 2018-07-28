
from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User

class Token(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    token = models.CharField(max_length=48)
    def __unicode__(self):
        return "{}_token".format(self.user)



class Expensee(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.BigIntegerField(default=0)
    user = models.ForeignKey(User)
    #amount1 = models.BigIntegerField(default=0)
    #amount3 = models.BigIntegerField(default=0)
    def __unicode__(self):
        return self.title

class income(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()#auto_now_add=True
    amount = models.BigIntegerField(default=0)
    user = models.ForeignKey(User)
    #amount1 = models.BigIntegerField(default=0)
    #amount3 = models.BigIntegerField(default=0)
    def __unicode__(self):
        return self.title
