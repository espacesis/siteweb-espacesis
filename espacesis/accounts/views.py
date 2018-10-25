from django.views.generic import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserModel
from .forms import UserSignUpForm


class Profile( LoginRequiredMixin,View):
    """
    user Profile Page
    """

    login_url = reverse_lazy('login')

    def get(self, request):
        return render(request,'accounts/profile.html')


class Signup(View):
    """
    Create View For Signing Up
    """

    def post(self, request):
        forms = UserSignUpForm(request.POST)

        if forms.is_valid() :
            username = forms.cleaned_data['username']
            email = forms.cleaned_data['email']
            password = forms.cleaned_data['password']
            User.objects.create_user(username = username, email=email, password=password)
            user = authenticate(username = username, password=password)
            login(request, user)

            return redirect(reverse_lazy('home'))

        else :

            return render(request,'accounts/signup.html',{'forms': forms })

    def get(self, request):
        return render(request,'accounts/signup.html',{'forms': UserSignUpForm()})
