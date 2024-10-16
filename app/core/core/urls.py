from django.contrib import admin
from django.urls import path

# Just test
from django.shortcuts import render

def tst(request):
    return render(request, "index.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tst)
]
