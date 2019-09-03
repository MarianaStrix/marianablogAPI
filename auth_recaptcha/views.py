from rest_auth.registration.views import RegisterView

from .serializers import ReCaptchaRegisterSerializer


class ReCaptchaRegisterView(RegisterView):
    serializer_class = ReCaptchaRegisterSerializer
