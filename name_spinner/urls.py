from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('', include('spinner.urls')),
    re_path(r'^celery-progress/', include('celery_progress.urls')),
    path('admin/', admin.site.urls),
]
