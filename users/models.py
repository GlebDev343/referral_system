import string
import random

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

def generate_invite_code():
    """Генерирует уникальный 6-значный инвайт-код"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=15, unique=True)
    invite_code = models.CharField(max_length=6, unique=True, blank=True, null=True,
                                   default=generate_invite_code)
    activated_invite_code = models.CharField(max_length=6, blank=True, null=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["invite_code", "activated_invite_code"]


    def set_password(self, raw_password):
    # Переопределяем, чтобы ничего не делать с паролем
        pass

    def __str__(self):
        return f"User {self.phone_number}"
