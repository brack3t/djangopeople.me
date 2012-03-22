from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r"^admin/", include(admin.site.urls)),

    url(r"^profile/", include("user_profiles.urls", namespace="profiles",
        app_name="user_profiles")),
    url(r'', include("generic.urls")),
    url(r'', include("social_auth.urls")),
)

urlpatterns += staticfiles_urlpatterns()
