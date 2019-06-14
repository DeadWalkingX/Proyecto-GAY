from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):

  def _create_user(self, email, rut,  password, is_staff, is_superuser, tipo):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        rut = rut,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser,
        last_login=now,
        tipo=tipo
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, rut, password, tipo):
    return self._create_user(email, rut, password, False, False, tipo)

  def create_superuser(self, email, rut, password):
    user=self._create_user(email, rut, password, True, True, 'super')
    user.save(using=self._db)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    rut = models.CharField(max_length=254, null=True, blank=True)
    tipo = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = [email]

    objects = UserManager()