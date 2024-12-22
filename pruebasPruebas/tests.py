from time import sleep

from django.test import TestCase
from .models import *

# Create your tests here.

class CreateUsuario(TestCase):
    def test_create_usuario(self):
        usuario = Usuario(username='test', password='test', email='pedro@safareyes.es')
        usuario.save()
        self.assertEqual(usuario.username, 'test')
        self.assertEqual(Usuario.objects.get(username='test').username, 'test')

    def test_create_usuario2(self):
        usuario = Usuario(username='test', password='test', email='pedsad@safareyes.es')
        usuario.save()
        self.assertEqual(usuario.username, 'test')
