from django.db import models
from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, default="", null=True)
    position = models.CharField(max_length=50, null=True)
    nation = models.CharField(max_length=50, null=True)
    team = models.CharField(max_length=100, null=True)
