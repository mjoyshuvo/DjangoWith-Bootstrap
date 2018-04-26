from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path
from apps.home.views import *


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    # path('', include('django.contrib.auth.urls')),
    # path('/', LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    # path('accounts / login / [name='login']')
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
