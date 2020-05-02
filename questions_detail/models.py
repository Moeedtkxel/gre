from django.db import models


# Create your models here.
class Questions_detail(models.Model):
    difficulty_level = models.IntegerField(null=False)
    test_id = models.IntegerField(null=False)
    question = models.ForeignKey('questions_detail.Questions', null=False, related_name='questionId',
                                 on_delete=models.CASCADE)

    class Meta:
        db_table = "question_details"

    def __str__(self):
        return str(self.id)


class Questions(models.Model):
    text = models.CharField(max_length=255, null=False)
    options = models.ForeignKey('questions_detail.Options', on_delete=models.CASCADE, null=True)
    image = models.ForeignKey('images.Images', null=True, blank=True, related_name='imageId', on_delete=models.CASCADE)
    answer = models.ForeignKey('answers.Answers', null=True, blank=True, related_name='answersId',
                               on_delete=models.CASCADE)
    # custom_answer = models.ForeignKey('custom_answers.Custom_answers', null=True, blank=True,
    #                                   related_name='custom_answersId',
    #                                   on_delete=models.CASCADE)
    # Question type is a reference k front end me isy kese display krwana hai
    question_type = models.IntegerField(null=False)

    class Meta:
        db_table = "questions"

    def __str__(self):
        return str(self.text)


class Options(models.Model):
    optionA = models.CharField(max_length=255, null=True, blank=True, default=' ')
    optionB = models.CharField(max_length=255, null=True, blank=True, default=' ')
    optionC = models.CharField(max_length=255, null=True, blank=True, default=' ')
    optionD = models.CharField(max_length=255, null=True, blank=True, default=' ')
    optionE = models.CharField(max_length=255, null=True, blank=True, default=' ')
    optionF = models.CharField(max_length=255, null=True, blank=True, default=' ')
    optionG = models.CharField(max_length=255, null=True, blank=True, default=' ')
    optionH = models.CharField(max_length=255, null=True, blank=True, default=' ')
    optionI = models.CharField(max_length=255, null=True, blank=True, default=' ')

    class Meta:
        db_table = "options"
