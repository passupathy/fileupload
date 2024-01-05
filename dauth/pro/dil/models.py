from django.db import models

# Create your models here.

class honda(models.Model):

    uni=models.CharField(max_length=20)
    shine=models.FileField()
