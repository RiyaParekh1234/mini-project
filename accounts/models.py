from django.db import models
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your models here.

class registration(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    phone = models.IntegerField()
    class Meta:
        db_table = "accounts_registration"


