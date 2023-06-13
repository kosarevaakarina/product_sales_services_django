from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.views import generic

from users.forms import UserForm, UserRegisterForm
from users.models import User
from users.services import send_mail_for_verify


class ProfileUpdateView(generic.UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class RegisterView(generic.CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:confirm_email')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()

        send_mail_for_verify(self.request, user)
        return response


class EmailVerify(generic.View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and default_token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('blog:home')
        return redirect('users:invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist, ValidationError):
            user = None
        return user
