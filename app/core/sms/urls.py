from django.urls import path
import sms.views as views

urlpatterns = [
    path('', views.index),
]