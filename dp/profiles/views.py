from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import (HttpResponse, HttpResponseRedirect,
                        HttpResponseForbidden)
from django.utils import simplejson as json
from django.views.generic import DetailView, UpdateView, View

from braces.views import LoginRequiredMixin, SelectRelatedMixin

from carrier_pigeon.forms import ContactForm
from generic.geocoder import Geocoder
from profiles.forms import UserProfileForm, LocationSearchForm
from profiles.models import UserProfile


class ProfileView(SelectRelatedMixin, DetailView):
    model = UserProfile
    select_related = ["user"]
    slug_field = "user__username"
    template_name = "profiles/detail.html"

    def get_context_data(self, **kwargs):
        """
        Authenticated users can message anyone. If anonymous messages
        are enabled and user is not authenticated add form.
        """
        context = super(ProfileView, self).get_context_data(**kwargs)
        obj = self.get_object()

        if self.request.user != obj.user:
            if self.request.user.is_authenticated():
                context.update({"form": ContactForm(self.request.POST or None,
                    initial={"recipient": obj.user_id,
                    "sender": self.request.user.pk}, user=self.request.user)})

            if not self.request.user.is_authenticated() and obj.anonymous_messages:
                context.update({"form": ContactForm(self.request.POST or None,
                    initial={"recipient": obj.user_id})})

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send Email!
            form.save()
            messages.success(request, u"Woo!")
            return HttpResponseRedirect(reverse("profile:detail",
                kwargs={"slug": self.object.user.username}))

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserProfileForm
    model = UserProfile
    template_name = "profiles/form.html"

    def get_object(self, queryset=None):
        return self.request.user.userprofile

    def get_success_url(self):
        return reverse("profile:edit")

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        context.update({"location_form": LocationSearchForm()})
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        user = self.request.user
        user.first_name = data.get("first_name", user.first_name)
        user.username = data.get("username", user.username)
        user.email = data.get("email", None)
        user.save()

        messages.success(self.request, "Your profile has been updated.")

        return super(ProfileUpdateView, self).form_valid(form)


class LocationSearchView(LoginRequiredMixin, View):
    """
    Returns a lat, lng response if a valid search string came through.
    """

    def post(self, request, *args, **kwargs):
        form = LocationSearchForm(request.POST or None)
        if form.is_valid():
            point = Geocoder().mapquest_geocode(form.cleaned_data["location"])
            response = {"success": True, "lat": point["lat"],
                "lng": point["lng"]}
            return HttpResponse(json.dumps(response),
                mimetype="application/json")
        else:
            return HttpResponseForbidden()
