from django.urls import path
import index.views as views
import index.api as api
from tools import (
    driver_functions,
    tracking_post
)

urlpatterns = [
    path('', views.index),
]