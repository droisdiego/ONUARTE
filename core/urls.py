from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from home.views import *

urlpatterns = [
    path('admin', admin.site.urls),
    path('',ListaPublicacoes.as_view(),name='index'),
    path('accounts/', include('allauth.urls')),
]

urlpatterns = urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
