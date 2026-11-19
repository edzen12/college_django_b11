from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.base.urls')),
    path('about/', include('apps.about.urls')),
    path('contacts/', include('apps.contacts.urls')),
    path('orientation/', include('apps.orientation.urls')),
    path('projects/', include('apps.projects.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)