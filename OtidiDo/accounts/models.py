from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class AppUser(AbstractUser):
    is_admin_user = models.BooleanField(default=False)


class Traveler(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username