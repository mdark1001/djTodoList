from django.contrib.auth import views as auth_view
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import SignupForm


def home(request):
    return render(request, 'base.html', {})


class LoginView(auth_view.LoginView):
    """
        Login View,  Class based view
    """
    template_name = 'login.html'
    redirect_authenticated_user = True


class LogoutView(LoginRequiredMixin, auth_view.LogoutView):
    """
        Logout view,  class based view
    """
    template_name = 'login.html'


class SignupView(FormView):
    """
        Singout class based view
    """

    template_name = 'singout.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')
    redirect_authenticated_user = True

    def form_valid(self, form):
        """ save form"""
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users:login') + '?register'
