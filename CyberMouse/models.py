'''from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    activation_token = models.UUIDField(default=uuid.uuid4, editable=False)
    reset_token = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username

    @classmethod
    def create_user(cls, username):
        return cls.objects.create_user(username=username)

    @classmethod
    def get_user_by_username(cls, username):
        return cls.objects.get(username = username)

    @classmethod
    def update_user_email(cls, username, email):
        user = cls.get_user_by_username()
        user.email = email
        user.save()
        return  user

    @classmethod
    def delete_user(cls, username):
        user = cls.get_user_by_username(username)
        user.delete()


'''