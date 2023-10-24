import os
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from .forms import RegistrationForm, ChangePasswordForm, ProfileForm, AvatarForm
from .models import WebsiteUser
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
	PasswordResetCompleteView, PasswordChangeForm, PasswordChangeView, PasswordChangeDoneView
from django_registration.forms import User
from django.contrib import messages


class UsersLoginView(LoginView):
	template_name = 'login.html'
	next_page = '/'


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


class ProfileView(View):
	def get(self, request):
		avatar_form = AvatarForm()
		profile_form = ProfileForm()
		return render(
			request, 'profile.html', context={'avatar_form': avatar_form, 'form': profile_form}
		)

	def post(self, request):
		try:
			profile = request.user.websiteuser
		except WebsiteUser.DoesNotExist:
			profile = WebsiteUser(user=request.user)

		avatar_form = AvatarForm(request.POST, request.FILES, instance=profile)
		profile_form = ProfileForm(request.POST, instance=profile)

		user = User.objects.filter(id=request.user.id).first()

		if 'avatar' in request.POST:
			if avatar_form.is_valid():
				avatar_form.save()
				messages.success(request, 'Photo has been uploaded')
				return redirect('profile')
			else:
				avatar_form = AvatarForm()
		elif 'profile' in request.POST:
			if profile_form.is_valid():
				# 	print(profile_form.cleaned_data)
				# 	for field in profile_form.cleaned_data:
				# 		if profile_form.cleaned_data[field] != '':
				# 			WebsiteUser.objects.update(field=profile_form[field])
				#
				# 	# WebsiteUser.objects.update(inf=inf)
				profile_form.save()
				messages.success(request, 'Profile has been changed')
				return redirect('profile')
		else:
			profile_form = ProfileForm()
		return render(
			request, 'profile.html', context={'avatar_form': avatar_form, 'form': profile_form}
		)
