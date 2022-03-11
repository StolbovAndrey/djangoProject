from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from users.forms import UserLoginForm, UserRegistrationForm, UserUpdateForm
from baskets.models import Basket


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'title': 'Авторизация', 'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрированы')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'GeekShop - Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)


@login_required()
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required()
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно обновлены')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserUpdateForm(instance=request.user)

    baskets = Basket.objects.filter(user=request.user)

    context = {
        'title': 'Профиль - geekshop',
        'form': form,
        'baskets': baskets
    }
    return render(request, 'users/profile.html', context)
