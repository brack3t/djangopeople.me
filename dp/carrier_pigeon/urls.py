from django.conf.urls import patterns, url

from carrier_pigeon.views import (InboxListView, ArchiveListView,
                                    MessageDetailView, ArchiveMessageView)

urlpatterns = patterns('',
    url(r"^$", InboxListView.as_view(), name="inbox"),
    url(r"^archive/$", ArchiveListView.as_view(), name="archive"),
    url(r"^view/(?P<pk>\d+)/$", MessageDetailView.as_view(), name="detail"),
    url(r"^action/archive/(?P<pk>\d+)/$", ArchiveMessageView.as_view(),
        name="action_archive"),
)
