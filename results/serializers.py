from rest_framework import serializers
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)
from results.models import Results


class ResultsSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = '__all__'
        list_serializer_class = BulkListSerializer