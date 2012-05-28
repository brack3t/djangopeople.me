from django.conf.urls import patterns, url

from generic.views import HomePageView, LogoutView

urlpatterns = patterns('',
    url(r"^$", HomePageView.as_view(), name="home"),
    url(r"^accounts/logout/$", LogoutView.as_view(), name="logout"),
)
