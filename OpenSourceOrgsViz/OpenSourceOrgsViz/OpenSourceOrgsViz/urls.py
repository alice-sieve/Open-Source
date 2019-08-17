from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.conf.urls import url, include

from .views import (
    home_page
)

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', home_page, name='home_page'),
    url(r'^projects/', include('projects.urls', namespace='projects')),
    url(r'^search/', include('search.urls', namespace='search')),
]


if settings.DEBUG:

    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)