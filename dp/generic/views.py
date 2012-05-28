from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "generic/index.html"

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})
