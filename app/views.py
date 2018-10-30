import datetime

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from django.urls import reverse
from django.views import generic

from app import models


def index(request):
    return HttpResponse("""hell, world!
    <a href="admin">admin</a>
    <a href="user/10sr">10sr</a>
    <a href="userview/10sr">10sr view</a>
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


class UserView(generic.DetailView):
    model = models.TwitterUser
    template_name = "app/userview.html.tpl"


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
