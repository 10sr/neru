import datetime

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from django.urls import reverse

from app import models


def index(request):
    return HttpResponse("""hell, world!
    <a href="admin">admin</a>
    <a href="user/10sr">10sr</a>
    """)


def user(request, username):
    # TODO: Fix when username not found
    try:
        user = models.TwitterUser.objects.filter(username=username)[0]
    except IndexError:
        raise Http404("User {} not found".format(username))

    template = loader.get_template("app/index.html.tpl")
    # I don't like django.shortcuts.render.
    return HttpResponse(template.render({
        "user": user,
        "sleeps": []
    }, request))
    # sleeps = models.TimeOfSleep.objects.filter(username=username)
    # if not sleeps:
    #     raise Http404("No sleep time record found for {}".format(username))
    # template = loader.get_template("app/index.html")
    # return HttpResponse(
    #     template.render({
    #         "sleeps": sleeps,
    #         "username": username
    #     }, request)
    # )


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
    ).save()
    return HttpResponseRedirect(reverse("app:user", args=(username,)))
