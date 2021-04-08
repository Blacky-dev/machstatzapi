from django.urls import path

from . import views

urlpatterns=[
    path('apithree/start_time=<str:start_date> and end_time=<str:end_date>',views.apithree,name='apithree')
]