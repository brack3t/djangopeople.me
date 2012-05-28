from django.views.generic import TemplateView

class ProfileView(TemplateView):
    template_name = "profiles/mine.html"

    def get(self, request, *args, **kwargs):
        return self.render_to_response({"object": request.user})
