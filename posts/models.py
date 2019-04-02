from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from taggit.managers import TaggableManager


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts')
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=200)
    text = models.TextField(verbose_name=_('Text'))
    published_date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(
        verbose_name=_('Tags'),
        blank=True,
        help_text=_('A comma-separated list of tags'))

    class Meta:
        ordering = ('-published_date', )
