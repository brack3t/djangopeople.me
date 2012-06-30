from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, UpdateView

from braces.views import LoginRequiredMixin, SelectRelatedMixin

from carrier_pigeon.forms import ContactForm
from profiles.forms import UserProfileForm
from profiles.models import UserProfile


class ProfileView(SelectRelatedMixin, DetailView):
    model = UserProfile
    select_related = ["user"]
    slug_field = "user__username"
    template_name = "profiles/detail.html"

    def get_context_data(self, **kwargs):
        """
        Authenticated users can message anyone. If anonymous messages
        are enabled and user is not authenticated add form.
        """
        context = super(ProfileView, self).get_context_data(**kwargs)
        obj = self.get_object()

        if self.request.user.is_authenticated():
            context.update({"form": ContactForm(initial={
                "recipient": obj.user_id, "sender": self.request.user.pk},
                user=self.request.user)})

        if not self.request.user.is_authenticated() and obj.anonymous_messages:
            context.update({"form": ContactForm(initial={
                "recipient": obj.user_id})})

        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserProfileForm
    model = UserProfile
    template_name = "profiles/form.html"

    def get_object(self, queryset=None):
        return self.request.user.userprofile

    def get_success_url(self):
        return reverse("profile:edit")

    def form_valid(self, form):
        data = form.cleaned_data
        user = self.request.user
        user.first_name = data.get("first_name", user.first_name)
        user.username = data.get("username", user.username)
        user.email = data.get("email", None)
        user.save()

        messages.success(self.request, "Your profile has been updated.")

        return super(ProfileUpdateView, self).form_valid(form)
