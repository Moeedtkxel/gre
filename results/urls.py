from django.urls import  re_path

from results import views

urlpatterns = [
    re_path(r'^results/$', views.AddResult.as_view(), name='result-list'),
]
