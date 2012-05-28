from django.conf.urls import patterns, url

from carrier_pigeon.views import (InboxListView, ArchiveListView)

urlpatterns = patterns('',
    url(r"^$", InboxListView.as_view(), name="inbox"),
    url(r"^archive/$", ArchiveListView.as_view(), name="archive"),
)
