from django.http import HttpResponse, Http404
from django.template import loader

from app import models


def index(request):
    return HttpResponse("hell, world!")


def user(request, username):
    sleeps = models.TimeOfSleep.objects.filter(username=username)
    if not sleeps:
        raise Http404("No sleep time record found for {}".format(username))
    template = loader.get_template("app/index.html")
    return HttpResponse(
        template.render({
            "sleeps": sleeps
        }, request)
    )
