from django.conf.urls import include, url
#from django.contrib.auth import views as auth_views

from app import views

app_name = "app"
urlpatterns = [
    url(r"^$", views.index, name="index"),
    #url(r"^login$", auth_views.login, name="login"),
    # Following names are imported from django.contrib.auth.urls
    # - login
    # - logout
    # - password_change
    # - password_reset
    # - password_reset_done
    # - password_reset_confirm
    # - password_reset_complete
    url(r"^", include("django.contrib.auth.urls")),
    url(r"^login_required_page$", views.login_required_page, name="login_required_page"),
    # TODO: Fix URL to use
    url(r"^user/(?P<username>[_0-9a-zA-Z]+)$", views.user, name="user"),
    url(r"^user/(?P<username>[_0-9a-zA-Z]+)/addneru$", views.user_addneru,
        name="user_addneru"),
    # pk is for primary key so URL like usesrview/10sr will fail
    # TODO: How to pass arbitrary parameter to DetailView?
    url(r"^userview/(?P<pk>[_0-9a-zA-Z]+)$", views.UserView.as_view(), name="userview"),
]
