from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})


class ProfileView(TemplateView):
    template_name = "profile.html"

    def get(self, request, *args, **kwargs):
        return self.render_to_response({"user": request.user})
