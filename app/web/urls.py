from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('on_publish',on_publish,name='on_publish'),
    path('on_publish_done',on_publish_done,name='on_publish_done'),
    path('record_done',record_done,name='record_done'),
]