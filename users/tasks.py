from __future__ import absolute_import, unicode_literals

import os
from celery import shared_task

from ZimadTest.utils import CompressedImage
from users.models import User


@shared_task()
def save_compressed(user_id):
    user = User.objects.get(pk=user_id)
    user.image_compressed.save(os.path.basename(user.image_origin.name), CompressedImage(user.image_origin), save=True)
