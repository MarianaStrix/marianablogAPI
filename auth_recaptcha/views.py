from rest_auth.registration.views import RegisterView
from auth_recaptcha.serializers import ReCaptchaRegisterSerializer


class ReCaptchaRegisterView(RegisterView):
    serializer_class = ReCaptchaRegisterSerializer
