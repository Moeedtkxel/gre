from collections import OrderedDict

from rest_framework import serializers
from rest_framework.fields import SkipField

from results.models import Results, Time
from questions_detail.models import Questions_detail
from questions_detail import lookupanswerId

class GetTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ('total_time', 'time_left')


class GetResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = '__all__'

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue
            if field.field_name == 'answer':
                attribute = lookupanswerId.getstring(attribute)
            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                    # Do not serialize empty lists
                    continue
                ret[field.field_name] = represenation

        return ret


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
        isActive = request.data.get('isActive', None);

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
            question['answer'] = lookupanswerId.getid(question['answer'])
            try:
                r1 = Results.objects.get(test_taker=request.user, test_id=test_id,
                                         question_detail=question['question_detail'], isActive=isActive)
                r1.answer = question['answer'];
                r1.save()
            except Results.DoesNotExist:
                Results.objects.create(test_taker=request.user, test_id=test_id, isActive=isActive, **question)

        return Results.objects.get(test_taker=request.user, test_id=test_id,
                                   question_detail=questions[0]['question_detail'])


class GetMarksSerializer(serializers.ModelSerializer):
    ActualAnswer = serializers.IntegerField(source='question_detail.question.id', read_only=True)

    # questions_detail__answer_id = serializers.ReadOnlyField()

    class Meta:
        model = Results
        fields = '__all__'
        read_only_fields = ('ActualAnswer',)
