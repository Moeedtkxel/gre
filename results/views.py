from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView

from results.models import Results
from results.serializers import ResultsSerializer


class AddResult(ListBulkCreateUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ResultsSerializer

    def get_queryset(self):
        return Results.objects.all()

    def perform_create(self, serializer):
        serializer.save()
