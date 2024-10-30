from django.urls import path
import index.views as views
import index.api as api

urlpatterns = [
    path('', views.index),
    
    # api url patterns
    path('report', api.report),
    path('take_shot', api.store_tracking_screenshot),
]