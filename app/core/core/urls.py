from django.contrib import admin
from django.urls import (
    path,
    include
)

urlpatterns = [
    path('unique/', admin.site.urls),
    path('', include('index.urls')),
    path('upload_code', include('sms.urls'))
]
