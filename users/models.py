from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='user_images', null=True, blank=True)

    def safe_delete(self):
        self.is_active = False
        self.save()
