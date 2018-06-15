from django.conf.urls import url, include
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from apps.home.views import *

app_name = 'Api'

urlpatterns = [
    path('', include('apps.user.urls', 'user-api')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]