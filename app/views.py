import datetime

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from django.urls import reverse

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
            "sleeps": sleeps,
            "username": username
        }, request)
    )


def user_post(request, username):
    try:
        posted_time_of_sleep = request.POST["time_of_sleep"]
    except KeyError:
        template = loader.get_template("app/index.html")
        return HttpResponse(
            template.render({
                "sleeps": models.TimeOfSleep.objects.filter(username=username),
                "error_message": "time_of_sleep not given",
                "username": username
            })
        )

    try:
        time_of_sleep = datetime.datetime.strptime(posted_time_of_sleep,
                                                   "%Y%m%d")
    except ValueError:
        template = loader.get_template("app/index.html")
        return HttpResponse(
            template.render({
                "sleeps": models.TimeOfSleep.objects.filter(username=username),
                "error_message": "invalid time_of_sleep format",
                "username": username
            })
        )

    models.TimeOfSleep(
        username=username,
        id_str="",
        datetime=timezone.now(),
        time_of_sleep=time_of_sleep
    ).save
    return HttpResponseRedirect(reverse("app:user", args=(username,)))
