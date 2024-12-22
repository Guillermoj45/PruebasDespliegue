# Create your models here.
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Usuario(User):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ultimo_login = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.username

    def was_registered_recently(self):
        return self.fecha_registro >= timezone.now() - datetime.timedelta(days=1)

    def is_active(self):
        return self.activo

    def get_avatar(self):
        return self.avatar

    class Meta:
        verbose_name_plural = "Usuarios"
        verbose_name = "Usuario"
        ordering = ['fecha_registro']
        db_table = 'usuarios'
        managed = True