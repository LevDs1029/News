from .views import test, index
from django.urls import path

urlpatterns = [
    path('', index),
    path("test/", test)
]