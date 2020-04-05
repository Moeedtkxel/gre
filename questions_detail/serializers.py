from rest_framework import serializers
from .models import Questions_detail


class QuestionDetailSerializer(serializers.ModelSerializer):
    text = serializers.CharField(source="question.text", read_only=True)
    question_type = serializers.CharField(source="question.question_type", read_only=True)
    # image = serializers.CharField(source="question.image.image", read_only=True)
    optionA = serializers.CharField(source="question.optionA", read_only=True)
    optionB = serializers.CharField(source="question.optionB", read_only=True)
    optionC = serializers.CharField(source="question.optionC", read_only=True)
    optionD = serializers.CharField(source="question.optionD", read_only=True)
    class Meta:
        model = Questions_detail
        fields = '__all__'
        read_only_fields = ('text','question_type',)