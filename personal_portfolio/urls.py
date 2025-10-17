from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.views.static import serve as static_serve
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('blog.urls')),
    path('', include('about_me.urls')),
]

SERVE_MEDIA = os.getenv("SERVE_MEDIA", "False").strip().lower() in ("true","1","yes")

if SERVE_MEDIA:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', static_serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', static_serve, {'document_root': settings.STATIC_ROOT}),
    ]


admin.site.site_title = "Samim Osman"
admin.site.site_header = "Samim Osman's Portfolio"
admin.site.app_index = "Welcome to Dashboard"

