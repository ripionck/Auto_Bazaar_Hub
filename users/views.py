from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib import messages
from . import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy


# Create your views here.
class AddUserCreateView(CreateView):
    model = User
    form_class = forms.UserRegistrationForm
    template_name = 'register_user.html'
    success_url = reverse_lazy('register_user')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Registration'
        return context


class UserLoginView(LoginView):
    template_name = 'register_user.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context