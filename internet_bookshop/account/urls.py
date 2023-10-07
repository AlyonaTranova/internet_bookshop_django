from django.urls import path
from django.conf.urls import url
from .views import RegistrationView, UsersLoginView, UsersLogoutView, PassChangeView, PassResetView, AccountDetailView
from django.contrib.auth.views import (
	PasswordResetDoneView,
	PasswordResetConfirmView,
	PasswordResetCompleteView,
	PasswordChangeView,
	PasswordChangeDoneView,

)

urlpatterns = [
	path('registration', RegistrationView.as_view(), name='registration'),
	path('login', UsersLoginView.as_view(), name='login'),
	path('logout', UsersLogoutView.as_view(), name='logout'),

	path('password_change/', PassChangeView.as_view(), name='password_change'),
	path(
		'password_change/done/', PasswordChangeDoneView.as_view(template_name='password/password_change_success.html'),
		name='password_change_done'),

	path('password_reset', PassResetView.as_view(), name='password_reset'),
	path('password_reset/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})',
	     PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset/done', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

	path('account/<int:pk>/', AccountDetailView.as_view()),
]
