from django.conf.urls import patterns, include, url
from django.contrib import admin

from generic.views import HomePageView
from profiles.views import ProfileView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include("social_auth.urls")),
    url(r"^$", HomePageView.as_view(), name="home"),
    url(r"^profile/$", ProfileView.as_view(), name="profile"),
    url(r"^admin/", include(admin.site.urls)),
)
