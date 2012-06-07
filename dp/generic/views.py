from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.contrib.gis.geos import *
from django.contrib.gis.measure import D
from django.views.generic import RedirectView, TemplateView, FormView

from braces.views import LoginRequiredMixin, SelectRelatedMixin

from generic.forms import SearchForm
from generic.geocoder import Geocoder
from profiles.models import UserProfile


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


class SearchView(FormView):
    form_class = SearchForm
    template_name = "generic/search.html"
    point = u"POINT(%s %s)" % (-115.300516,36.136818)

    def form_valid(self, form):
        location = form.cleaned_data["location"]
        distance = form.cleaned_data["distance"]
        units = form.cleaned_data["units"]
        skills = form.cleaned_data.get("skills", None)
        skills = [s.strip() for s in skills.split(",")]
        point = Geocoder().mapquest_geocode(location)

        if point["status"]:
            qs = UserProfile.objects.select_related("user").exclude(
                point__isnull=True).distance(point["point"])

            if units == "km":
                qs = qs.filter(point__distance_lte=(
                    point["point"], D(km=distance)
                ))
            else:
                qs = qs.filter(point__distance_lte=(
                    point["point"], D(mi=distance)
                ))

            qs = qs.order_by("distance")
            qs = self._filter_by_skills(qs, skills)

        return self.render_to_response({"users": qs, "form": form,
            "units": units})

    def _filter_by_skills(self, queryset, skills):
        """
        If we have skills to pay tha billz, filter queryset yo.
        """
        if skills:
            return queryset.filter(tags__name__in=skills).distinct()
        return queryset
