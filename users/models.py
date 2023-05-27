from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    balance = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    account_number = models.UUIDField(default=uuid.uuid4())
