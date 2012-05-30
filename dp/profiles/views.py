from django.views.generic import DetailView

from profiles.models import UserProfile


class ProfileView(DetailView):
    model = UserProfile
    slug_field = "user__username"
    template_name = "profiles/detail.html"


#class ProfileView(TemplateView):
    #template_name = "profiles/mine.html"

    #def get(self, request, *args, **kwargs):
        #return self.render_to_response({"object": request.user})
