from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from django.urls import include, path, re_path

from apps.gallery.sitemap import sitemap

urlpatterns = [
    path("admin/", admin.site.urls),
    path("sitemap.xml", sitemap, name="sitemap"),
    path("api/v1/", include("apps.core.urls")),
    path("api/v1/", include("apps.accounts.urls")),
    path("api/v1/", include("apps.designs.urls")),
    path("api/v1/", include("apps.assets.urls")),
    path("api/v1/", include("apps.gallery.urls")),
    path("api/v1/", include("apps.elements.urls")),
    path("api/v1/", include("apps.fonts.urls")),
    path("api/v1/", include("apps.brand.urls")),
    path("api/v1/", include("apps.sharing.urls")),
    path("api/v1/", include("apps.exports.urls")),
    path("api/v1/", include("apps.collab.urls")),
    path("api/v1/", include("apps.presets.urls")),
    path("api/v1/", include("apps.apitokens.urls")),
    path("api/v1/ai/", include("apps.ai.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
elif settings.SERVE_MEDIA:
    # `static()` does nothing outside DEBUG, so serve the files explicitly.
    urlpatterns += [
        re_path(
            rf"^{settings.MEDIA_URL.lstrip('/')}(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}
        )
    ]

handler404 = "apps.core.views.not_found"
handler500 = "apps.core.views.server_failure"
