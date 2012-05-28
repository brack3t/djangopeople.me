from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.views.generic import RedirectView, TemplateView

from braces.views import LoginRequiredMixin


class HomePageView(TemplateView):
    template_name = "generic/index.html"

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})


class LogoutView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, **kwargs):
        return reverse("home")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
