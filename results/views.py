from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView

from results.models import Results
from results.serializers import ResultsSerializer


class AddResult(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = ResultsSerializer

    def get_queryset(self):
        return Results.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response_data = {
            "success": "True",
            "message": "Successfully sent",
        }
        return Response(response_data, status=status.HTTP_201_CREATED,
                        headers=headers)
