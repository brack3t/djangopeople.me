from django.views.generic import ListView, DetailView

from braces.views import LoginRequiredMixin, SetHeadlineMixin

from carrier_pigeon.models import Message


class InboxListView(LoginRequiredMixin, SetHeadlineMixin, ListView):
    headline = "Inbox"
    model = Message
    template_name = "carrier_pigeon/list.html"

    def get_queryset(self):
        """
        Return all inbox messages for this user.
        """
        return self.request.user.received_messages.filter(
            recipient_archived=False
        )


class ArchiveListView(InboxListView):
    headline = "Archive"

    def get_queryset(self):
        """
        Return all archived messages for this user.
        """
        return self.request.user.received_messages.filter(
            recipient_archived=True
        )


class MessageDetailView(LoginRequiredMixin, SetHeadlineMixin, DetailView):
    model = Message
    template_name = "carrier_pigeon/detail.html"

    def get_headline(self):
        return u"Set This Shit"
