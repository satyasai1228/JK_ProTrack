from django.contrib import admin
from django.urls import path
from data.views import *


urlpatterns = [
    path("Reportdata",Reportdata.as_view()),
]
