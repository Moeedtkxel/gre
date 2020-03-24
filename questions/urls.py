from django.urls import path, re_path

from questions import views

urlpatterns = [
    re_path(r'^questions/$', views.QuestionList.as_view(), name='question-list'),
]
