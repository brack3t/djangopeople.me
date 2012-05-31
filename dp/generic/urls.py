from django.conf.urls import patterns, url

from generic.views import HomePageView, LogoutView, SearchView

urlpatterns = patterns('',
    url(r"^$", HomePageView.as_view(), name="home"),
    url(r"^search/$", SearchView.as_view(), name="search"),
    url(r"^accounts/logout/$", LogoutView.as_view(), name="logout"),
)
