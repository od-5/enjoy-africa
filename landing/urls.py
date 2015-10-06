from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^about/', include('apps.about.urls', namespace='about'),),
    url(r'^travels/', include('apps.travel.urls', namespace='travel'),),
    url(r'^groups/', include('apps.groups.urls', namespace='groups'),),
    url(r'^forum/', include('apps.forum.urls', namespace='forum'),),
    url(r'^vk/', include('apps.vk.urls', namespace='vk'),),
    url(r'', include('core.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
