from django.urls import path
import index.views as views
import index.api as api

urlpatterns = [
    path('', views.index),
    path('test', api.test),
]