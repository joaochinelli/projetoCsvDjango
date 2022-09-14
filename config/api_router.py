from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from projeto.users.api.views import UserViewSet
from csv.api.views import CsvViewSet


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router.register("users", UserViewSet)
# router.register("csv", CsvViewSet, basename="csv")

app_name = "api"
urlpatterns = [
    path(r'csv/upload', include(router.urls)),
    # router.urls
]
