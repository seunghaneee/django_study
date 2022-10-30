from django.shortcuts import render, redirect
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm # 필요없음
from django.contrib.auth.forms import PasswordChangeForm

from .forms import CustomUserCreationForm, CustomUserChangeForm

from django.contrib.auth import update_session_auth_hash

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.method =="POST":
        # form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            # 회원가입 후 곧바로 로그인
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        # form = UserCreationForm()
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def delete(request):
    request.user.delete()
    # 탈퇴하면서 해당 유저의 세션도 지우고 싶은경우
    # 먼저 로그아웃을 해버리면 해당 요청 객체의 정보가 없어지기때문에
    # 삭제후 로그아웃
    auth_logout(request)
    return redirect('articles:index')

def update(request):
    if request.method == 'POST':
        # pass
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/change_password.html', context)
