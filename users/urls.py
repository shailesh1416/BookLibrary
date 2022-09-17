from users.views import register

from django.urls.conf import path, include

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),
]
