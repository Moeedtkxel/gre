from django.shortcuts import render

# Create your views here.
from rest_framework import generics
# from django_filters.rest_framework import DjangoFilterBackend
from questions.serializers import QuestionsSerializer
from .models import Questions


class QuestionList(generics.ListCreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

    # filter_backends = [DjangoFilterBackend]
    filter_class = QuestionsSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return Questions.objects.all().filter()
