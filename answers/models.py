from django.db import models


# Create your models here.
class Answers(models.Model):
    text_answer = models.CharField(max_length=255, null=True)
    multiple_answer = models.ForeignKey('answers.MultipleAnswers', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "answers"

    def __str__(self):
        return str(self.id)


class MultipleAnswers(models.Model):
    choiceA = models.BooleanField(null=True)
    choiceB = models.BooleanField(null=True)
    choiceC = models.BooleanField(null=True)
    choiceD = models.BooleanField(null=True)
    choiceE = models.BooleanField(null=True)
    choiceF = models.BooleanField(null=True)
    choiceG = models.BooleanField(null=True)
    choiceH = models.BooleanField(null=True)
    choiceI = models.BooleanField(null=True)

    class Meta:
        db_table = "multipleanswers"
