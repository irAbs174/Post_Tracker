from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import (
    path,
    include
)

urlpatterns = [
    path('unique/', admin.site.urls),
    path('', include('index.urls')),
    path('upload_code', include('sms.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
