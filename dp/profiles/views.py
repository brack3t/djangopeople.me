from django.http import Http404
from django.views.generic import DetailView, UpdateView

from braces.views import LoginRequiredMixin

from profiles.forms import UserProfileForm
from profiles.models import UserProfile


class ProfileView(DetailView):
    model = UserProfile
    slug_field = "user__username"
    template_name = "profiles/detail.html"


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserProfileForm
    model = UserProfile
    template_name = "profiles/form.html"

    def get_object(self, queryset=None):
        try:
            obj = UserProfile.objects.select_related("user").get(
                user__username=self.kwargs["slug"])
        except UserProfile.DoesNotExist:
            raise Http404
        return obj
