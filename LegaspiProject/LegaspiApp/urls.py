from django.contrib import path
from django.urls import admin
from . import views


urlpatterns = [
    path ("", views.helloworld, name = "helloWorld"),
     path ("testpath/", views.testPath, name = "testPath")
]
