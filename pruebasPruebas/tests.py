import json

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Usuario, Grupos, Chat
import datetime

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


class UsuarioModelTests(TestCase):
    def test_was_registered_recently_with_recent_user(self):
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_user = Usuario(fecha_registro=time)
        self.assertIs(recent_user.was_registered_recently(), True)

    def test_was_registered_recently_with_old_user(self):
        time = timezone.now() - datetime.timedelta(days=2)
        old_user = Usuario(fecha_registro=time)
        self.assertIs(old_user.was_registered_recently(), False)

    def test_is_active_with_active_user(self):
        active_user = Usuario(activo=True)
        self.assertTrue(active_user.activo)

    def test_is_active_with_inactive_user(self):
        inactive_user = Usuario(activo=False)
        self.assertFalse(inactive_user.activo)

    def test_get_avatar_with_avatar(self):
        user_with_avatar = Usuario(avatar='avatars/test.jpg')
        self.assertEqual(user_with_avatar.get_avatar(), 'avatars/test.jpg')

    def test_get_avatar_without_avatar(self):
        user_without_avatar = Usuario()
        self.assertIsNone(user_without_avatar.get_avatar().name)


class ChatModelTests(TestCase):

    def test_str_returns_message(self):
        chat = Chat(mensaje="Test Message")
        self.assertEqual(str(chat), "Test Message")

class GruposModelTests(TestCase):
    def test_str_returns_group_name(self):
        group = Grupos(nombre="Test Group")
        self.assertEqual(str(group), "Test Group")


class HomeViewTests(TestCase):
    def test_home_view_returns_200(self):
        response = self.client.get(reverse('home'), follow=True)
        self.assertEqual(response.status_code, 200)

    #def test_home_view_returns_all_users(self):
    #    Usuario.objects.create(username="User1")
    #    Usuario.objects.create(username="User2")
    #    response = self.client.get(reverse('home'))
    #    self.assertEqual(len(json.loads(response.content)['usuarios']), 2)
#
    #def test_home_view_returns_empty_list_when_no_users(self):
    #    response = self.client.get(reverse('home'))
    #    self.assertEqual(len(json.loads(response.content)['usuarios']), 0)