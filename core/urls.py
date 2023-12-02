from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from home.views import index
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index')
]

urlpatterns = urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
