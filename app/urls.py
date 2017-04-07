from django.conf.urls import url

from app import views

app_name = "app"
urlpatterns = [
    url(r"^$", views.index, name="index"),
    # TODO: Fix URL to use
    url(r"^user/(?P<username>[_0-9a-zA-Z]+)$", views.user, name="user"),
    url(r"^user/(?P<username>[_0-9a-zA-Z]+)/post$", views.user_post,
        name="user_post")
]
