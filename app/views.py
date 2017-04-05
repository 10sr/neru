from django.http import HttpResponse


def index(request):
    return HttpResponse("hell, world!")


def user(request, user_id):
    return (HttpResponse("history of {}".format(user_id)))
