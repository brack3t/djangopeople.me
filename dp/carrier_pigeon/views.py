from django.views.generic import ListView

from braces.views import LoginRequiredMixin

from carrier_pigeon.models import Message


class InboxListView(LoginRequiredMixin, ListView):
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

    def get_queryset(self):
        """
        Return all archived messages for this user.
        """
        return self.request.user.received_messages.filter(
            recipient_archived=True
        )
