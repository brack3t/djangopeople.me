from django.views.generic import DetailView, UpdateView

from braces.views import LoginRequiredMixin, SelectRelatedMixin

from profiles.forms import UserProfileForm
from profiles.models import UserProfile

class ProfileView(SelectRelatedMixin, DetailView):
    model = UserProfile
    select_related = ["user"]
    slug_field = "user__username"
    template_name = "profiles/detail.html"


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserProfileForm
    model = UserProfile
    template_name = "profiles/form.html"

    def get_object(self, queryset=None):
        return self.request.user.userprofile
