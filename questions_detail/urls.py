from django.urls import path, re_path

from questions_detail import views

urlpatterns = [
    re_path(r'^questions2/$', views.QuestionDetailList.as_view(), name='question-list'),
]
