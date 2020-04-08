from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)
from results.models import Results
from questions_detail.models import Questions_detail


class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = '__all__'
        # list_serializer_class = BulkListSerializer

    def create(self, validated_data):
        request = self.context.get('request')
        test_id = request.data.get('test_id', None)
        questions = self._kwargs['data']['questions']
        for question in questions:
            question['question_detail'] = Questions_detail.objects.get(id=question['question_detail'])
            results = Results.objects.create(test_taker=request.user, test_id=test_id, **question)
        return results
