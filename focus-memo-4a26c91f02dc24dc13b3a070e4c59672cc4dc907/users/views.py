from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "회원가입 완료! 로그인 해주세요.")
            return redirect("login")
        messages.error(request, "입력값을 확인해 주세요.")
    else:
        form = UserCreationForm()

    return render(request, "users/signup.html", {"form": form})