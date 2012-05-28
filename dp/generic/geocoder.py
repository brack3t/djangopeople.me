from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils import simplejson as json
from django.utils.http import urlquote

import requests


class Geocoder(object):
    def __init__(self):
        self.mapquest_api_url = getattr(settings, "MAPQUEST_API_URL", None)

        if not self.mapquest_api_url:
            raise ImproperlyConfigured("MAPQUEST_API_URL does not exist in "
                "the settings file.")

    def mapquest_geocode(self, location=None):
        """
        MapQuest specific geocoder API call.
        """
        if not location:
            return {"error": "No location was received.", "status": False}

        result = requests.get(self.mapquest_api_url + "&location=%s" % (
            urlquote(location)))

        if result.status_code == 200:
            data = json.loads(result.content)

            try:
                lat = data["results"][0]["locations"][0]["displayLatLng"]["lat"]
                lng = data["results"][0]["locations"][0]["displayLatLng"]["lng"]
                return {
                    "point": u"POINT(%s %s)" % (lng, lat),
                    "status": True
                }
            except KeyError:
                return {"error": "MapQuest could not find data for the "
                    "location you entered.",
                    "status": False
                }

        return {
            "error": "There was a problem communicating with MapQuest. Please "
                "try again in a few minutes.",
            "status": False
        }
