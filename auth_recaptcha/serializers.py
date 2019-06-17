from recaptcha.fields import ReCaptchaField

from rest_auth.registration.serializers import RegisterSerializer


class ReCaptchaRegisterSerializer (RegisterSerializer):
    recaptcha = ReCaptchaField(write_only=True)
