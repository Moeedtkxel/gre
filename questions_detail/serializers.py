from rest_framework import serializers
from .models import Questions_detail


class QuestionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions_detail
        fields = '__all__'
