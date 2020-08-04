from django.urls import path
from .views import index
from django.conf.urls.static import static
from name_spinner import settings

urlpatterns = [
    path('', index),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
