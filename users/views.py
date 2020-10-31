from django.contrib.auth import views as auth_view
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, UpdateView

from .forms import SignupForm
from .models import Profile

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


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """
        Udapte Profile View Class
    """
    template_name = 'update_profile.html'
    model = Profile
    fields = ['picture', 'biography']

    def get_object(self):
        """Return concurrent user's profile. """
        return self.request.user.profile

    def post(self, request, *args, **kwargs):
        user = request.user
        user.first_name = request.POST['user_first_name']
        user.last_name = request.POST['user_last_name']
        user.save()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('todolist:home')
