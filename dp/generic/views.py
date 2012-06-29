from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.contrib.gis.geos import *
from django.contrib.gis.measure import D
from django.views.generic import RedirectView, TemplateView, FormView

from braces.views import LoginRequiredMixin

from generic.forms import SearchForm
from generic.geocoder import Geocoder
from profiles.models import UserProfile


class HomePageView(TemplateView):
    template_name = "generic/index.html"

    def get(self, request, *args, **kwargs):
        form = SearchForm()
        return self.render_to_response({"form": form})


class LogoutView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, **kwargs):
        return reverse("home")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class SearchView(FormView):
    form_class = SearchForm
    model = UserProfile
    template_name = "generic/search.html"

    def form_valid(self, form):
        location = form.cleaned_data["location"]
        distance = form.cleaned_data["distance"]
        units = form.cleaned_data["units"]
        skills = form.cleaned_data.get("skills", None)

        if skills:
            skills = [s.strip() for s in skills.split(",")]

        point = Geocoder().mapquest_geocode(location)

        if point["status"]:
            queryset = self.model.objects.select_related("user").exclude(
                point__isnull=True).distance(point["point"])

            if units == "km":
                queryset = queryset.filter(point__distance_lte=(
                    point["point"], D(km=distance)
                ))
            else:
                queryset = queryset.filter(point__distance_lte=(
                    point["point"], D(mi=distance)
                ))

            queryset = queryset.order_by("distance")
            queryset = self._filter_by_skills(queryset, skills)

        return self.render_to_response({"object_list": queryset, "form": form,
            "units": units})

    def _filter_by_skills(self, queryset, skills):
        """
        If we have skills to pay tha billz, filter queryset yo.
        """
        if skills:
            return queryset.filter(tags__name__in=skills).distinct()
        return queryset
