from __future__ import unicode_literals

from django.db import models

class Kitten_image(models.Model):
    image_name = models.CharField(max_length=100)
    width = models.CharField(max_length=10)
    height = models.CharField(max_length=10)
