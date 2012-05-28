from django.http import HttpResponse
from django.views.generic import View


class InboxListView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hola Bitch!")
