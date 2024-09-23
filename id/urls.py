from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="id-login"),
    path("logout/", views.logout_view, name="id-logout"),
    path("register/", views.register_view, name="id-register"),
]
