from django.db import models


# Create your models here.

class Results(models.Model):
    test_taker = models.ForeignKey('users.User', null=True, related_name='testtakerId', on_delete=models.CASCADE)
    question_detail = models.ForeignKey('questions_detail.Questions_detail', null=True, related_name='answersId',
                                        on_delete=models.CASCADE)
    test_id = models.IntegerField(null=True)
    answer = models.CharField(max_length=255, null=True)
    text_answer = models.CharField(max_length=255, null=True)
    isActive = models.BooleanField(default=True, null=False)

    class Meta:
        db_table = "results"

    def __str__(self):
        return str(self.test_taker.username)


class Time(models.Model):
    total_time = models.IntegerField(choices=((1, "Normal TIme"),
                                              (2, "1.5x time"),
                                              (3, "Double Time"),
                                              (4, "Full time"),),
                                     default=1)
    time_left = models.FloatField(max_length=255, )
    test_id = models.IntegerField()
    test_taker = models.ForeignKey('users.User', null=True, related_name='timerId', on_delete=models.CASCADE)

    class Meta:
        db_table = "time"


class Marks(models.Model):
    test_taker = models.ForeignKey('users.User', null=True, related_name='testtakerIdforMarks',
                                   on_delete=models.CASCADE)
    test_id = models.IntegerField(null=False)
    marks = models.IntegerField(null=False)

    class Meta:
        db_table = "marks"

    def __str__(self):
        return str(self.test_taker.username)
