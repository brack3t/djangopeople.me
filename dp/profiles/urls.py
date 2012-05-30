from django.conf.urls import patterns, url

from profiles.views import ProfileView, ProfileUpdateView

urlpatterns = patterns('',
    url(r"^(?P<slug>[\w.@+-]+)/$", ProfileView.as_view(), name="detail"),
    url(r"^$", ProfileUpdateView.as_view(), name="edit"),
)
