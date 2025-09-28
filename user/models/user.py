from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """Custom user model based on Django AbstractUser."""
    # Add extra fields when needed
    pass
