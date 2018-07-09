# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime

# Create your models here.

class User(AbstractBaseUser):
    user = models.EmailField(unique=True)
    last_accessed = models.DateTimeField(default=datetime.datetime.utcnow)
    last_ordered = models.DateTimeField(default=datetime.datetime.utcnow)
    total_ordered = models.IntegerField(default=0)
    total_delivered = models.IntegerField(default=0)

class UserAddress(models.Model):
    user = models.ForeignKey(User)
    state = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    address_line1 = models.CharField(max_length=254)
    address_line2 = models.CharField(max_length=254)
    pincode = models.CharField(max_length=254)

class UserPhone(models.Model):
    user = models.ForeignKey(User)
    phone_number = models.CharField(max_length=12)
    phone_type = models.CharField(max_length=6, default='A')
    is_reachable = models.BooleanField(default=False)
