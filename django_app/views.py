from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from django_app.models import News


# Create your views here.

def index(request):
    task = News.objects.all()
    return render(request, 'django_app/first.html', {'task': task})


def login_f(request):
    if request.method == 'GET':
        return render(request, 'django_app/profile_login.html', context={})
    elif request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is None:
                return render(request, 'django_app/profile_login.html', context={"error": "User не найден"})
            login(request, user)
            return redirect('main')
        return render(request, 'django_app/profile_login.html', context={"error": "username or password пустые"})


def register_f(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "django_app/profile_register.html", context={})

    elif request.method == "POST":
        # todo чтение из формы
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        # todo чтение из формы

        # todo сравнение паролей
        if password1 != password2:
            return render(request, "django_app/profile_register.html", context={"error": "incorrect password1"})
        # todo сравнение паролей

        # todo регистрация пользователя
        User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        # todo регистрация пользователя

        # todo перенаправление пользователя
        return redirect("login")
        # todo перенаправление пользователя


def logout_f(request):
    logout(request)
    return redirect('main')
