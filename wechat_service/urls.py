from django.urls import path
from services.test import test_api

urlpatterns = [
    path('test', test_api, name='test_api'),
]
