from datetime import datetime

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import Http404
from django.views.generic import ListView, DetailView, RedirectView
from django.utils.timezone import utc

from braces.views import LoginRequiredMixin, SetHeadlineMixin

from carrier_pigeon.models import Message


class InboxListView(LoginRequiredMixin, SetHeadlineMixin, ListView):
    headline = "Inbox"
    model = Message
    paginate_by = 30
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


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = "carrier_pigeon/detail.html"

    def get_object(self):
        """
        Set read_at if this is the first time viewing a message.
        """
        obj = super(MessageDetailView, self).get_object()

        if not obj.read_at:
            obj.read_at = datetime.utcnow().replace(tzinfo=utc)
            obj.save()

        return obj


class ArchiveMessageView(LoginRequiredMixin, RedirectView):
    model = Message
    url = "pigeon:inbox"

    def get_redirect_url(self, **kwargs):
        return reverse(self.url)

    def get(self, request, pk, *args, **kwargs):
        try:
            message = self.model.objects.get(pk=pk, recipient=request.user)
        except self.model.DoesNotExist:
            return Http404

        message.recipient_archived = True
        message.save()
        messages.success(request, "Message archived.")
        return super(ArchiveMessageView, self).get(request, pk, *args, **kwargs)
