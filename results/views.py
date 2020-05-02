# Create your views here.
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from results.models import Results, Time
from results.serializers import CreateResultsSerializer, GetResultsSerializer, GetTimeSerializer, GetMarksSerializer


class AddResult(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = CreateResultsSerializer

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


class GetResult(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = GetResultsSerializer

    def get_queryset(self):
        return Results.objects.all().filter(test_taker=self.request.user, isActive=True)


class GetTime(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = GetTimeSerializer

    def get_queryset(self):
        return Time.objects.filter(test_taker=self.request.user, ).filter((~Q(time_left=0)))


class GetMarks(generics.ListAPIView):
    lookup_field = 'pk'

    serializer_class = GetMarksSerializer

    def get_queryset(self):
        R = Results.objects.filter(
            test_id=1)  # A.filter(ActualAnswer=answer)  # .values()  # return ValuesQuerySet object
        return R
