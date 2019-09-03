from django.urls import path, re_path
from django.views.generic import TemplateView
from rest_auth.registration.views import VerifyEmailView

from .views import ReCaptchaRegisterView

urlpatterns = [
    path('', ReCaptchaRegisterView.as_view(), name='rest_register'),
    path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    re_path(
        r'^account-confirm-email/(?P<key>[-:\w]+)/', TemplateView.as_view(),
        name='account_confirm_email',
        ),
]
