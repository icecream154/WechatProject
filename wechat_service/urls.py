from django.urls import path
from wechat_service.services.test import test_api, fetch_wx_user

urlpatterns = [
    path('test', test_api, name='test_api'),
    path('login', fetch_wx_user, name='fetch_wx_user')
]
