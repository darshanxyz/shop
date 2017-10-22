from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib import auth
from forms import RegistrationForm, LoginForm

class RegistrationFormView(View):
    form_class = RegistrationForm
    template = 'reg_home.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('user_account:login')
        else:
            return render(request, self.template, {'form': form})

class LoginFormView(View):
	form_class = LoginForm
	template = 'login.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('items:items')

def logout(request):
    auth.logout(request)
    return redirect('items:items')

def index(request):
    return redirect('items:items')
