from django.db import models
from django.contrib.auth.models import User
from django.utils.text import truncate_words


class Message(models.Model):
    """
    """
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sender = models.ForeignKey(User, blank=True, null=True,
        related_name="sent_messages")
    recipient = models.ForeignKey(User, related_name="received_messages")
    name = models.CharField(max_length=75, blank=True)
    email = models.EmailField(blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(blank=True, null=True)
    replied_at = models.DateTimeField(blank=True, null=True)
    sender_archived = models.BooleanField(default=False)
    recipient_archived = models.BooleanField(default=False)


    class Meta:
        ordering = ["-sent_at", "-id"]

    def __unicode__(self):
        return truncate_words(self.subject, 5)

    @property
    def is_unread(self):
        return self.read_at is None

    @property
    def is_replied(self):
        return self.replied_at is not None

    @property
    def anonymous_message_display(self):
        return u"%s &lt;%s&gt;" % (self.name, self.email)
