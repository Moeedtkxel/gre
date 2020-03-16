from django.db import models


# Create your models here.
class Images(models.Model):
    image = models.BinaryField(null=False)

    def __str__(self):
        return str(self.id)
