from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView, RedirectView, UpdateView, TemplateView, View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .forms import *
from .models import *


class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('company:Home')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(email=email, password=password)
        if user:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return render(self.request, 'users/login.html', context={
                'error': 'Don`t correct email or password.',
                'form': LoginForm
            })


class SignUpView(FormView):
    template_name = 'users/signup.html'
    form_class = SignUpForm
    form_class.fields = ['username', 'last_name', 'first_name', 'email', 'sex', 'password']
    success_url = reverse_lazy('company:Home')

    def form_valid(self, form):
        data = form.cleaned_data
        email = data.pop('email')
        password = data.pop('password')
        CustomUser.objects.create_user(email=email, password=password, **data)
        return super(SignUpView, self).form_valid(form)


class LogoutView(RedirectView):
    pattern_name = 'company:Home'
    
    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)


class ProfileView(UpdateView):
    template_name = 'users/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('users:Profile')

    def get_object(self, queryset=None):
        username = self.request.user.username
        self.user = get_object_or_404(CustomUser, username=username)
        return self.user

    def get_initial(self):
        initial = {
            'username': self.user.username,
            'last_name': self.user.last_name,
            'first_name': self.user.first_name,
            'email': self.user.email,
            'sex': self.user.sex
        }

        return initial


class SendingSuccessFul(TemplateView):
    template_name = 'users/reset_password/success.html'


class AjaxSignUpViews(FormView):
    form_class = SignUpForm
    template_name = 'users/signup.html'

    def form_invalid(self, form):
        response = {}
        for field, error in form.errors.items():
            response[field] = error
        return JsonResponse({'response': response, 'result': 'Error'})


# class AjaxShowOrder(View):
#     def get(self, request, *args, **kwargs):
#         response = Product.objects.filter(orders__user=self.request.user).values()
#         return JsonResponse({'response': list(response)})


