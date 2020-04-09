from rest_framework import serializers
from results.models import Results, Time
from questions_detail.models import Questions_detail


class GetTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ('total_time', 'time_left')


class GetResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = '__all__'

class CreateResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = '__all__'

    def create(self, validated_data):
        # Getting Query Params from request object
        request = self.context.get('request')
        test_id = request.data.get('test_id', None)
        questions = request.data.get('questions', None)
        total_time = request.data.get('total_time', None)
        time_left = request.data.get('time_left', None)

        # Store/update time left and time remaining
        try:
            t1 = Time.objects.get(test_taker=request.user, test_id=test_id)
            t1.time_left = time_left
            t1.save()
        except Time.DoesNotExist:
            Time.objects.create(total_time=total_time, time_left=time_left, test_taker=request.user, test_id=test_id)

        # Store/update Questions
        for question in questions:
            question['question_detail'] = Questions_detail.objects.get(id=question['question_detail'])
            try:
                r1 = Results.objects.get(test_taker=request.user, test_id=test_id,
                                         question_detail=question['question_detail'])
                r1.answer = question['answer'];
                r1.custom_answer = question['custom_answer'];
                r1.isActive = question['isActive'];
                r1.save()
            except Results.DoesNotExist:
                Results.objects.create(test_taker=request.user, test_id=test_id, **question)

        return Results.objects.get(test_taker=request.user, test_id=test_id,
                                   question_detail=questions[0]['question_detail'])
