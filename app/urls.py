from django.conf.urls import url

from app import views

app_name = "app"
urlpatterns = [
    url(r"^$", views.index, name="index"),
    # TODO: Fix URL to use
    url(r"^user/(?P<username>[_0-9a-zA-Z]+)$", views.user, name="user"),
    url(r"^user/(?P<username>[_0-9a-zA-Z]+)/addneru$", views.user_addneru,
        name="user_addneru"),
    # pk is for primary key so URL like usesrview/10sr will fail
    # TODO: How to pass arbitrary parameter to DetailView?
    url(r"^userview/(?P<pk>[_0-9a-zA-Z]+)$", views.UserView.as_view(), name="userview"),
]
