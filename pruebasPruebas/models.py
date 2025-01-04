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


class Grupos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuarios = models.ManyToManyField(Usuario, related_name='grupos')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Grupos"
        verbose_name = "Grupo"
        ordering = ['fecha_creacion']
        db_table = 'grupos'
        managed = True


class Chat(models.Model):
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mensaje

    class Meta:
        verbose_name_plural = "Chats"
        verbose_name = "Chat"
        ordering = ['fecha_envio']
        db_table = 'chats'
        managed = True