from django.urls import path
from .views import *

urlpatterns = [
    path('api', WaifuApiView.as_view()),
    path('api/all', WaifuApiGetAll.as_view()),
]