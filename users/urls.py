from django.urls import path
from users.views import login
from users.views import register
from users.views import logout

urlpatterns = [
    path("login", login, name='users_login'),
    path("register", register, name="users_register"),
    path("logout", logout, name="users_logout")
]
