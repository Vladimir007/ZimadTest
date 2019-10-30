from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from rest_framework.authtoken.models import Token


class User(AbstractUser):
    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)
    parent_name = models.CharField(_('parent name'), max_length=150)
    image_origin = models.ImageField(upload_to='origin', verbose_name=_('Your photo'))
    image_compressed = models.ImageField(null=True, upload_to='compressed')

    REQUIRED_FIELDS = ['first_name', 'last_name', 'parent_name', 'image_origin']

    def get_full_name(self):
        full_name = '%s %s %s' % (self.last_name, self.first_name, self.parent_name)
        return full_name.strip()

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        db_table = 'users'
        ordering = ('username',)
