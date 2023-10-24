from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from .models import WebsiteUser


class AuthorizationForm(forms.Form):
	username = forms.CharField(
		label='username'
	)
	password = forms.CharField(
		widget=forms.PasswordInput,
		label='password'
	)


class RegistrationForm(UserCreationForm):
	username = UsernameField(
		required=True,
		label='login',
		widget=forms.TextInput(attrs={'class': 'form-input'}))
	# text = ['Пароль должен содержать минимум 8 символов', 'Пароль не может состоять только из цифр.']
	password1 = forms.CharField(
		label="enter password", strip=False,
		widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-input'}),
		help_text='Password should contain at least 8 symbols. You can not use numbers only')
	password2 = forms.CharField(
		label='repeat password',
		widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-input'}),
		strip=False,
		help_text='', )
	email = forms.EmailField(
		required=True,
		label='email',
		widget=forms.TextInput(attrs={'class': 'form-input'}))

	class Meta:
		model = User
		fields = [
			'username', 'password1', 'password2', 'email'
		]


class AvatarForm(forms.ModelForm):
	class Meta:
		model = WebsiteUser
		fields = ['avatar']

	def __init__(self, *args, **kwargs):
		super(AvatarForm, self).__init__(*args, **kwargs)
		self.fields['avatar'].widget = forms.FileInput(attrs={
			'class': 'Profile-file form-input Profile-fileLabel'})
		self.fields['avatar'].label = 'upload photo'


class ProfileForm(forms.ModelForm):
	class Meta:
		model = WebsiteUser
		fields = ['phone_number', 'email', 'first_name', 'last_name', 'patronymic']

	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		self.fields['phone_number'].widget = forms.TextInput(attrs={
			'id': 'id_phone_number',
			'class': 'form-input',
			'placeholder': '+7(___)-___-__-__'})
		self.fields['email'].widget = forms.TextInput(attrs={
			'class': 'form-input'})
		self.fields['first_name'].widget = forms.TextInput(attrs={
			'class': 'form-input'})
		self.fields['last_name'].widget = forms.TextInput(attrs={
			'class': 'form-input'})
		self.fields['patronymic'].widget = forms.TextInput(attrs={
			'class': 'form-input'})
		self.fields['email'].required = False
		self.fields['first_name'].required = False
		self.fields['last_name'].required = False
		self.fields['patronymic'].required = False
		self.fields['phone_number'].required = False


class ChangePasswordForm(PasswordChangeForm):
	class Meta:
		model = User
		fields = ['old_password', 'new_password1', 'new_password2']

	def __init__(self, *args, **kwargs):
		super(ChangePasswordForm, self).__init__(*args, **kwargs)
		self.fields['old_password'].label = 'old password'

	old_password = forms.CharField(
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'})
	),
	new_password1 = forms.CharField(
		max_length=100, label="new password",
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'})
	)
	new_password2 = forms.CharField(
		max_length=100,
		label="repeat new password",
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'})
	)
