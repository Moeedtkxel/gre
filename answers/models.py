from django.db import models


# Create your models here.
class Answers(models.Model):
    choice = models.CharField(max_length=255, null=False)
