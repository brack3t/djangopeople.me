from django.conf.urls import patterns, url

from profiles.views import ProfileView, ProfileUpdateView, LocationSearchView

urlpatterns = patterns('',
    url(r"^location/search/$", LocationSearchView.as_view(),
        name="location_search"),
    url(r"^(?P<slug>[\w.@+-]+)/$", ProfileView.as_view(), name="detail"),
    url(r"^$", ProfileUpdateView.as_view(), name="edit"),
)
