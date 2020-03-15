from django.db import models


# Create your models here.
class Questions(models.Model):
    text = models.CharField(max_length=255, null=False)
    image = models.ForeignKey('images.Images', null=False, related_name='imageId', on_delete=models.CASCADE)
    answer = models.ForeignKey('answers.Answers', null=False, related_name='answersId', on_delete=models.CASCADE)
    custom_answer = models.ForeignKey('custom_answers.Custom_answers', null=False, related_name='custom_answersId',
                                      on_delete=models.CASCADE)
    question_type = models.IntegerField(null=False)
