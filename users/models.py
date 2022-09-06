from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, username,  password, **other):
        if not username:
            raise ValueError('Deve-se fornecer um nome de usuário')
        user = self.model(username=username, **other)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **other):
        other.setdefault('is_staff', True)
        other.setdefault('is_superuser', True)
        other.setdefault('is_active', True)

        if other.get('is_staff') is not True:
            raise ValueError('Superusers must to be assigned as is_staff=True')
        if other.get('is_superuser') is not True:
            raise ValueError('Superusers must to be assigned as is_superuser=True')
        
        return self.create_user(username, password, **other)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50,unique=True)
    email = None
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username



