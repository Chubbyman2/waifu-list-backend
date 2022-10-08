from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path('api', WaifuApiView.as_view()),
    path('api/all', WaifuApiAll.as_view()),
]