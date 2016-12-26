from __future__ import unicode_literals

from django.db import models

class Size(models.Model):
    width = models.CharField(max_length=10)
    height = models.CharField(max_length=10)
