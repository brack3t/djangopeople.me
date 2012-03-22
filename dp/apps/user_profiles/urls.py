from django.conf.urls.defaults import patterns, url

from user_profiles.views import ProfileView

urlpatterns = patterns('',
    url(r"^$", ProfileView.as_view(), name="detail"),
)
