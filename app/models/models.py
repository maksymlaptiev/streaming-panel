from django.db import models
from django.db.models import Sum, Count, Case, When,Q
from random import randint,choice
import hashlib
from datetime import *
import string

# Create your models here.
class Stream(models.Model):
       id                   = models.AutoField(primary_key=True)
       name                 = models.CharField(max_length=20)
       type                 = models.CharField(max_length=200)
       address              = models.CharField(max_length=200)
       lastpubdate          = models.DateTimeField(default=datetime.now)
       status               = models.IntegerField(default=0)
       createdate           = models.DateTimeField(default=datetime.now)

