from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from admins.forms import UserAdminRegForm, UserAdminProfileForm
from users.models import User


class TitleMixin:
    title = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TitleMixin, self).get_context_data(object_list=None, **kwargs)
        context['title'] = self.title
        return context


class IndexAdminListView(TitleMixin, ListView):
    model = User
    template_name = 'admins/index.html'
    title = "Главная страница"

    @method_decorator(user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(IndexAdminListView, self).dispatch(request, *args, **kwargs)


class UserAdminListView(TitleMixin, SuccessMessageMixin, ListView):
    model = User
    template_name = 'admins/admin-users-read.html'
    title = 'Админка - пользователи'

    @method_decorator(user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UserAdminListView, self).dispatch(request, *args, **kwargs)


class UserAdminCreateView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserAdminRegForm
    template_name = 'admins/admin-users-create.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    success_message = 'Пользователь создан'
    title = "Создание пользователя"

    @method_decorator(user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UserAdminCreateView, self).dispatch(request, *args, **kwargs)


class UserAdminUpdateView(TitleMixin, UpdateView):
    model = User
    form_class = UserAdminProfileForm
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    title = "Обновление информации о пользователе"

    @method_decorator(user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UserAdminUpdateView, self).dispatch(request, *args, **kwargs)


class UserAdminDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.safe_delete()
        return HttpResponseRedirect(self.success_url)

    @method_decorator(user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UserAdminDeleteView, self).dispatch(request, *args, **kwargs)
