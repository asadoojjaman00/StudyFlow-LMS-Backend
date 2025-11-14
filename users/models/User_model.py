from users.manager import UserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser,PermissionsMixin):
    class RoleChoice(models.TextChoices):
        student = 'student', 'Student'
        instructor = 'instructor', 'Instructor'
        admin = 'admin', 'Admin'

    full_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    role = models.CharField(
        max_length=15,
        choices=RoleChoice.choices,
        default=RoleChoice.student
    )
    
    join_date = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone_number']

    def __str__(self):
        return self.username
