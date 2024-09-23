from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from . import forms


def login_view(request):
    next_url = request.GET.get("next", "/")

    if request.user.is_authenticated:
        return redirect(next_url)

    if request.method == "POST":
        next_url = request.POST.get("next", next_url)
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            login(request, user=form.user)
            return redirect("home")

    else:
        form = forms.LoginForm()

    return render(
        request,
        "id/login-page.html",
        {"form_title": "Login", "form": form, "next": next_url},
    )


def logout_view(request):
    logout(request)
    return redirect("id-login")


def register_view(request):
    next_url = request.GET.get("next", "/")

    if request.user.is_authenticated:
        return redirect(next_url)

    if request.method == "POST":
        next_url = request.POST.get("next", next_url)
        form = forms.CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user=user)
            return redirect("home")

    else:
        form = forms.CreateUserForm()

    return render(
        request,
        "id/register-page.html",
        {"form_title": "Create an account", "next": next_url, "form": form},
    )
