from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    new_email = models.EmailField(null=True,
                                  help_text=_('Enter a new email address'),
                                  verbose_name=_('New email'))

    def __str__(self):
        return self.username
