from django.contrib import admin
from django.urls import path, include
from id import urls as id_urls

# from basic_views import urls as bv_urls
from basic_views.views import home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("id/", include(id_urls)),
    path("", home_view, name="home"),
]
