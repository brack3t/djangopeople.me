from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'', include("social_auth.urls")),
    (r'', include("generic.urls")),
    (r"^messages/", include("carrier_pigeon.urls", namespace="pigeon")),
    (r"^profile/", include("profiles.urls", namespace="profile")),
    (r"^admin/", include(admin.site.urls)),
)
