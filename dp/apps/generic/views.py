from django.conf import settings
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        kwargs = super(IndexView, self).get_context_data(**kwargs)
        kwargs.update({"cloudmade_key": settings.CLOUDMADE_API_KEY})
        return kwargs
