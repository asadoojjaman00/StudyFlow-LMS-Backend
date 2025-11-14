from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, full_name, email, phone_number, password=None,**extra_fields):

        if not full_name:
            raise ValueError("user must have full name")
        
        if not email:
            raise ValueError("User must have an Email Address")
        
        if not phone_number:
            raise ValueError("User must have an phone number")
        
        email = self.normalize_email(email)
        username = email.split('@')[0]

        
        user = self.model(
            full_name=full_name,
            email=email,
            username=username,
            phone_number=phone_number,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,full_name, email, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')

        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("superuser must have is_staff = True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("superuser must have is_superuser = True")
        
        return self.create_user(full_name, email, phone_number, password, **extra_fields)
    