# Create your models here.
import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.timezone import now



class UserManager(BaseUserManager):

    def create_user(self, email, password, **all_fields):
        """
        Create and return a `User` with an email, username and password.
        """

        email = self.normalize_email(email)
        user = self.model(email=email, **all_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user



    def create_superuser(self, email, password, **all_fields):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        all_fields.setdefault('is_staff', True)
        all_fields.setdefault('is_superuser', True)
        all_fields.setdefault('is_active', True)
        user = self.create_user(email, password, **all_fields)

        return user

class MtAdminUser(AbstractBaseUser, PermissionsMixin):
    admin_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=255, default='first name')
    last_name = models.CharField(max_length=255, default='second name')
    role = models.CharField(max_length=100, default='default')
    date_created = models.DateTimeField(auto_now=now ,blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=now ,blank=True, null=True)
    ip_address = models.CharField(max_length=50, default='0.0.0.0')
    user_lang = models.IntegerField(default=0)
    email = models.CharField(max_length=255, unique=True)
    lost_password_code = models.CharField(max_length=255, default='default')
    session_token = models.CharField(max_length=255, default='default')
    last_login = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    user_access = models.TextField(blank=True, null=True, default='[]')
    status = models.CharField(max_length=100, default='active')
    contact_number = models.CharField(max_length=50, default='xxxxxxxxxx')
    inventory_role_id = models.IntegerField(default=0)
    inventory_enabled = models.IntegerField(default=1)
    #is_active = models.IntegerField(blank=True, null=True)
    #is_staff = models.IntegerField(blank=True, null=True)
    #is_superuser = models.IntegerField(blank=True, null=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []

    objects = UserManager()

    class Meta:
        managed = True
        db_table = 'mt_admin_user'

    def __str__(self):
        return self.email
