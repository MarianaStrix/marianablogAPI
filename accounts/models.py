from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from blogAPI.settings import AVATAR_SIZE

from easy_thumbnails.fields import ThumbnailerImageField


class Account(AbstractUser):
    avatar = ThumbnailerImageField(default='default.png',
                                   upload_to='profile_pics/%Y/%m/%d',
                                   resize_source=dict(size=(AVATAR_SIZE, AVATAR_SIZE),
                                                      sharpen=True,
                                                      crop='smart'))

    def __str__(self):
        return self.username
