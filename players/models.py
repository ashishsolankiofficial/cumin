from django.db import models
from utils.model_utils import get_ext_id

from django.contrib.auth.models import AbstractUser
from .manager import UserManager


# Create your models here.
class Organisation(models.Model):
    ext_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        while not self.ext_id:
            new_id = get_ext_id()
            if not type(self).objects.filter(ext_id=new_id).exists():
                self.ext_id = new_id
        super().save(*args, **kwargs)

class BusinessUnit(models.Model):
    ext_id = models.CharField(max_length=10)
    organisation = models.ForeignKey(Organisation, related_name='units', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        while not self.ext_id:
            new_id = get_ext_id()
            if not type(self).objects.filter(ext_id=new_id).exists():
                self.ext_id = new_id
        super().save(*args, **kwargs)


class User(AbstractUser):
    ext_id = models.CharField(max_length=10)
    email = models.EmailField(max_length=254, unique=True)
    display_name = models.CharField(max_length=50, unique=True)
    business_unit = models.ForeignKey(BusinessUnit, related_name='bu_users', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'display_name']

    objects = UserManager()

    def save(self, *args, **kwargs):
        while not self.ext_id:
            new_id = get_ext_id()
            if not type(self).objects.filter(ext_id=new_id).exists():
                self.ext_id = new_id
        super().save(*args, **kwargs)
