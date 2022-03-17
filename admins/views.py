from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from admins.forms import UserAdminRegForm, UserAdminProfileForm
from users.models import User


@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='/')
def index(request):
    context = {
        'title': 'Админ-панель',
    }
    return render(request, 'admins/index.html', context)


@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='/')
def admin_users(request):
    users = User.objects.all()
    context = {
        'title': 'Админ-панель',
        'users': users
    }
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='/')
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь зарегистрирован')
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminRegForm()

    context = {
        'title': 'Админ-панель',
        'form': form
    }
    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='/')
def admin_users_update(request, pk):
    selected_user = User.objects.get(id=pk)

    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно обновлены')
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)

    context = {
        'title': 'Админ-панель',
        'form': form,
        'selected_user': selected_user
    }

    return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='/')
def admin_users_delete(request, pk):
    selected_user = User.objects.get(id=pk)
    selected_user.safe_delete()
    messages.warning(request, f'Пользователь {selected_user.username} удален')
    return HttpResponseRedirect(reverse('admin_staff:admin_users'))
