from django.db import models


# Create your models here.
class Questions_detail(models.Model):
    difficulty_level = models.IntegerField(null=False)
    test_id = models.IntegerField(null=False)
    question = models.ForeignKey('questions.Questions', null=False, related_name='questionId', on_delete=models.CASCADE)

