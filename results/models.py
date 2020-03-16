from django.db import models


# Create your models here.
class Results(models.Model):
    test_taker = models.ForeignKey('users.User', null=False, related_name='testtakerId', on_delete=models.CASCADE)
    question_detail = models.ForeignKey('questions_detail.Questions_detail', null=False, related_name='answersId',
                                        on_delete=models.CASCADE)
    answer = models.CharField(max_length=255, null=True)
    custom_answer = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.test_taker.username)
