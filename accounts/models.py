from django.contrib.auth.models import AbstractUser
from django.conf import settings

from easy_thumbnails.fields import ThumbnailerImageField


class Account(AbstractUser):
    avatar = ThumbnailerImageField(default='default.png',
                                   upload_to='profile_pics/%Y/%m/%d',
                                   resize_source=dict(size=(settings.AVATAR_SIZE, settings.AVATAR_SIZE),
                                                      sharpen=True,
                                                      crop='smart'))

    def __str__(self):
        return self.username
