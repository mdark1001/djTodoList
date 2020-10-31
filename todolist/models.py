from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Tags(models.Model):
    class Meta:
        verbose_name_plural = 'Tags'

    name = models.CharField(
        verbose_name='Nombre',
        max_length=120
    )
    color = models.IntegerField(
        verbose_name='Color',
        default=1
    )

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(
        verbose_name='Tarea',
        max_length=120
    )
    user = models.ForeignKey(
        User,
        verbose_name='Usuario',
        on_delete=models.CASCADE,
    )
    tag = models.ForeignKey(
        Tags,
        verbose_name='Etiqueta',
        on_delete=models.CASCADE,
    )
    descrripcion = models.TextField(
        verbose_name='Descripción',
        blank=True,
        null=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    state = models.BooleanField(
        default=True,
        verbose_name='Estatus',
    )

    @property
    def first_name(self):
        return self.user.first_name

    def __str__(self):
        return self.name
