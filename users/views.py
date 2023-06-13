from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from users.forms import UserForm, UserRegisterForm
from users.models import User


class ProfileUpdateView(generic.UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class RegisterView(generic.CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('blog:home')