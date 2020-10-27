from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    """
        Model for profile user
    """
    user = models.OneToOneField(
        User,
        verbose_name='Usuario',
        on_delete=models.CASCADE,
    )
    picture = models.ImageField(
        upload_to='store/users/picture',
        blank=True,
        null=True,
        verbose_name='Fotografía'
    )
    biography = models.TextField(
        verbose_name='Biografía',
        blank=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return str(self.user)
