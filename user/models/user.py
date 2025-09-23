import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """Custom user with UUID primary key."""
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # AbstractUser já inclui:
    # username, first_name, last_name, email, is_staff, is_active, etc.

    def __str__(self):
        return self.username
