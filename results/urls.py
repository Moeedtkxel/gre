from django.urls import re_path

from results import views

urlpatterns = [
    re_path(r'^results/$', views.AddResult.as_view(), name='result-list'),
    re_path(r'^getresults/$', views.GetResult.as_view(), name='result-list-get'),
    re_path(r'^timeremaining/$', views.GetTime.as_view(), name='time-list-get'),

]
