from django.conf.urls import patterns, url

from carrier_pigeon.views import InboxListView

urlpatterns = patterns('',
    url(r"^$", InboxListView.as_view(), name="home")
)
