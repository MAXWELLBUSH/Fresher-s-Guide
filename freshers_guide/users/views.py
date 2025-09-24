from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


# Register endpoint
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# Get list of users (for testing)
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after register
            return redirect("/")  # redirect to homepage (you can change)
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def home(request):
    return render(request, "users/home.html", {"username": request.user.username})