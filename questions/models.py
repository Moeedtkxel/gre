from django.db import models


# Create your models here.
class Questions(models.Model):
    text = models.CharField(max_length=255, null=False)
    optionA = models.CharField(max_length=255, null=True, blank=True,  default=' ')
    optionB = models.CharField(max_length=255, null=True, blank=True,  default=' ')
    optionC = models.CharField(max_length=255, null=True, blank=True,  default=' ')
    optionD = models.CharField(max_length=255, null=True, blank=True,  default=' ')
    image = models.ForeignKey('images.Images', null=True, blank=True, related_name='imageId', on_delete=models.CASCADE)
    answer = models.ForeignKey('answers.Answers', null=True, blank=True, related_name='answersId', on_delete=models.CASCADE)
    custom_answer = models.ForeignKey('custom_answers.Custom_answers', null=True, blank=True, related_name='custom_answersId',
                                      on_delete=models.CASCADE)
    question_type = models.IntegerField(null=False)

    def __str__(self):
        return str(self.text)
