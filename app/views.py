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

    template = loader.get_template("app/user.html.tpl")
    # I don't like django.shortcuts.render.
    return HttpResponse(template.render({
        "user": user,
        "sleeps": models.TimeOfSleep.objects.filter(id_str=user.id_str)
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


def user_addneru(request, username):
    try:
        user = models.TwitterUser.objects.filter(username=username)[0]
    except IndexError:
        raise Http404("User {} not found".format(username))

    try:
        note = request.POST["note"]
    except KeyError:
        template = loader.get_template("app/user.html.tpl")
        return HttpResponse(
            template.render({
                "sleeps": [],
                "error_message": "note not given",
                "user": user
            })
        )

    now = timezone.now()

    models.TimeOfSleep(
        id_str=user.id_str,
        datetime=now,
        time_of_sleep=now,
        note=note
    ).save()
    return HttpResponseRedirect(reverse("app:user", args=(username,)))
