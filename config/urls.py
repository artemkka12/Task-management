from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings
from helpers import schema_view

urlpatterns = [
                  path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('admin/', admin.site.urls),
                  path('user/', include('apps.users.urls')),
                  path('', include('apps.tasks.urls')),
                  path('comment/', include('apps.comments.urls')),
                  path('gallery/', include('apps.gallery.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
