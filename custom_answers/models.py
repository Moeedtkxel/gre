from django.db import models


# Create your models here.
class Custom_answers(models.Model):
    choice = models.CharField(max_length=255, null=False)
