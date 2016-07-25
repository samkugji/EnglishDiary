from django.views.generic.base import View
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib import messages


class SignupView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "users/signup.html",
            context={},
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        # Validate username
        if get_user_model().objects.filter(username=username).exists():
            messages.add_message(
                request,
                messages.ERROR,
                "이미 존재하는 닉네임입니다.",
            )
            return redirect(reverse("users:signup"))

        # Validate email
        if get_user_model().objects.filter(email=email).exists():
            messages.add_message(
                request,
                messages.ERROR,
                "이미 존재하는 이메일입니다.",
            )
            return redirect(reverse("users:signup"))

        user = get_user_model().objects.create_user(
            username=username,
            password=password,
            email=email,
        )
        messages.add_message(
            request,
            messages.SUCCESS,
            "회원가입이 성공적으로 되었습니다.",
        )
        return redirect(reverse("users:signin"))
