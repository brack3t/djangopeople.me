from django.conf.urls import patterns, include, url
from django.contrib import admin

from profiles.views import ProfileView

admin.autodiscover()

urlpatterns = patterns('',
    (r'', include("social_auth.urls")),
    (r'', include("generic.urls")),

    url(r"^profile/$", ProfileView.as_view(), name="profile"),
    url(r"^admin/", include(admin.site.urls)),
)
