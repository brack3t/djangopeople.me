from django.conf.urls import patterns, url

from profiles.views import ProfileView

urlpatterns = patterns('',
    url(r"^(?P<slug>[\w.@+-]+)/$", ProfileView.as_view(), name="detail"),
)
