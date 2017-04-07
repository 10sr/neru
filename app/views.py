from django.http import HttpResponse
from django.template import loader

from app import models


def index(request):
    return HttpResponse("hell, world!")


def user(request, username):
    sleeps = models.TimeOfSleep.objects.filter(username=username)
    template = loader.get_template("app/index.html")
    return HttpResponse(
        template.render({
            "sleeps": sleeps
        }, request)
    )
