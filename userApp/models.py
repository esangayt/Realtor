from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import Group, Permission


# Create your models here.
class AccountManager(BaseUserManager):
    def _create_user(self, username, email, first_name, last_name, password, is_staff, is_superuser, **extra_fields):

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, first_name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, first_name, last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, first_name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, first_name, last_name, password, True, True, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(unique=True, max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    phone_number = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = AccountManager()
