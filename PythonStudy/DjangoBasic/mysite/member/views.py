import contextlib
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password

from .models import Member
# Create your views here.


def login(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        password = request.POST.get("user_password")

        if user_id and password:
            with contextlib.suppress(Member.DoesNotExist):
                member = Member.objects.get(user_id=user_id)
                if check_password(password, member.password):
                    request.session["member_id"] = member.member.id
                    return redirect("/polls/detail/")

    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        password = request.POST.get("user_password")

        if user_id and password:
            member = Member()
            member.user_id = user_id
            member.password = make_password(password)
            member.save()

            return redirect("/member/login/")
    
    return render(request, 'signup.html')