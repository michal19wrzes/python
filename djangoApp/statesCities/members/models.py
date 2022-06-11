from lib2to3.pytree import Base
from django.db import models
from django.apps import apps
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

#AUTH_USER_MODEL = members.UserAccount

class UserAccountManager(BaseUserManager):
    def _create_user(self,name,email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not name:
            raise ValueError("The given name must be set")
        if not email:
            raise ValueError("email must be set")
        email = self.normalize_email(email)
        if not password:
            raise ValueError("PASSWORD MUST BE SET")
        
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        
        name = GlobalUserModel.normalize_username(name)
        user = self.model(name=name, email=email,password=password, **extra_fields)
        user.password = make_password(password) #should be hasher by make_password
        
        user.save(using=self._db)
        return user

    def create_user(self,name,  email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user( name,email, password, **extra_fields)

    def create_superuser(self,name, email,password,**extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(name,email, password, **extra_fields)

class UserAccount(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)
    
    objects=UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['name']
    
    def get_full_name(self):
        return self.name
    def get_short_name(self):
        return self.name
    def __str__(self):
        return self.email