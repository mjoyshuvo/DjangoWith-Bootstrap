from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from django.urls import path
from apps.user.views import UserViewSet

app_name = 'user'

router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')

urlpatterns = [
    path('', include(router.urls))
]
