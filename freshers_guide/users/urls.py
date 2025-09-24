from django.urls import path
from django.contrib.auth import views as auth_views   # ✅ add this
from .views import register_view, home
from .views import RegisterUserView, UserListView

urlpatterns = [
    # Frontend (HTML form)
    path("register/", register_view, name="register"),
    path("home/", home, name="home"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),  # ✅ redirect to login

    # API endpoints
    path("api/register/", RegisterUserView.as_view(), name="api-register"),
    path("api/users/", UserListView.as_view(), name="api-user-list"),
]
