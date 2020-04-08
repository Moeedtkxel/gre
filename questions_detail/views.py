from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

from questions_detail.question_detail_filters import QuestionFilter
from .serializers import QuestionDetailSerializer
from .models import Questions_detail


class QuestionDetailList(generics.ListAPIView):
    queryset = Questions_detail.objects.all()
    serializer_class = QuestionDetailSerializer
    filter_backends = (filters.DjangoFilterBackend,)

    # filter_backends = (DjangoFilterBackend,)
    filter_class = QuestionFilter

    def get_queryset(self):
        return Questions_detail.objects.all().filter()
