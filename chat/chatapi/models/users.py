from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class UserManager(BaseUserManager):
    def create_user(self, email, password, nickname):
        if not email:
            raise ValueError('No hay un email')

        if not password or len(password) < 6:
            raise ValueError('La contraseña es invalida')

        if not nickname or len(nickname) < 6:
            raise ValueError('El nickname es invalido')

        email = self.normalize_email(email)
        user = self.model(email=email, password=password, nickname=nickname)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, nickname):
        user = self.create_user(email, password, nickname)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=50, unique=True, blank=False, editable=False)
    password = models.CharField(max_length=50, blank=False)
    nickname = models.CharField(max_length=25, unique=True, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    created_at = models.DateField(auto_now=True, editable=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'nickname']

    objects = UserManager()

    def __str__(self):
        return self.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
