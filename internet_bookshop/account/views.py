import os
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from .forms import RegistrationForm, ChangePasswordForm
from .models import WebsiteUser
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
	PasswordResetCompleteView, PasswordChangeForm, PasswordChangeView, PasswordChangeDoneView
from django_registration.forms import User


class UsersLoginView(LoginView):
	template_name = 'login.html'


class UsersLogoutView(LogoutView):
	next_page = '/'


class PassResetView(PasswordResetView):
	template_name = 'password/password_reset_form.html'


class PassResetDoneView(PasswordResetDoneView):
	template_name = 'password/password_reset_done'


class PassResetConfirmView(PasswordResetConfirmView):
	template_name = 'password/password_reset_confirm'


class PassResetCompleteView(PasswordResetCompleteView):
	template_name = 'password/password_reset_complete'


class PassChangeView(PasswordChangeView):
	form_class = ChangePasswordForm
	template_name = 'password/password_change.html'


class RegistrationView(View):

	def get(self, request):
		form = RegistrationForm()
		url = request.build_absolute_uri()
		con = os.path.basename(url)
		print(con)
		return render(request, 'registration.html', {'form': form})

	def post(self, request):
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			email = form.cleaned_data.get('email')
			WebsiteUser.objects.create(
				user=user,
				email=email,
			)
			user.save()
			login(request, user)
			return redirect('login')

		return render(request, 'registration.html', {'form': form})


class AccountDetailView(DetailView):
	model = User
	template_name = 'account.html'

	def get_context_data(self, *args, **kwargs):
		context = super(AccountDetailView, self).get_context_data(**kwargs)
		context['user_data'] = WebsiteUser.objects.filter(user=self.object).first()
		return context