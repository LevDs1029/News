
from django.contrib import admin
from django.urls import path, include
from newslist.views import index, test

urlpatterns = [
    path('admin/', admin.site.urls),
    path("newslist/", include("newslist.urls"))
]
