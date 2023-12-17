from django.shortcuts import render, redirect
from django.views.generic import CreateView, RedirectView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib import messages
from . import forms
from auto_bazaar.models import Order
from django.contrib.auth.models import User
from django.urls import reverse_lazy


# Create your views here.
class UserCreateView(CreateView):
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
        return reverse_lazy('homepage')
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
    
class LogoutView(RedirectView):
    """
    A view that logs out a user and redirects to the homepage.
    """
    permanent = False
    query_string = True
    pattern_name = 'homepage'  # Replace with the actual name of your homepage URL

    def get_redirect_url(self, *args, **kwargs):
        """
        Log out the user and redirect to the target URL.
        """
        if self.request.user.is_authenticated:
            messages.success(self.request, 'Logged out Successful')
            logout(self.request)
            
        return super().get_redirect_url()
    
class ProfileView(DetailView):
    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        return render(request, 'profile.html', {'orders': orders})

class EditProfileView(UpdateView):
    template_name = 'edit_profile.html'

    def get(self, request, *args, **kwargs):
        profile_form = forms.ChangeUserForm(instance=request.user)
        return render(request, self.template_name, {'form': profile_form})

    def post(self, request, *args, **kwargs):
        profile_form = forms.ChangeUserForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('user_profile')

        return render(request, self.template_name, {'form': profile_form})