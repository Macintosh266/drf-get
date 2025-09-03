from django.contrib.auth.base_user import *
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth import get_user_model


class CustomUserManager(BaseUserManager):
    def create_user(self,username,password=None,**extra_fields):
        if not username:
            return  ValueError('User kiritish shart!')
        user=self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,password,**extra_fields):
        extra_fields.setdefault('is_admin',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_admin') is not True:
            return ValueError("Sizda is_admin==True b'olishi kerak")
        if extra_fields.get('is_active') is not True:
            return ValueError()

        return  self.create_user(username,password,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=50,unique=True)
    email=models.CharField(max_length=50,null=True)
    is_admin=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)
    is_active =models.BooleanField(default=True)
    is_student=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)

    objects=CustomUserManager()

    USERNAME_FIELD='username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    @property
    def is_superuser(self):
        return self.is_admin



class Movie(models.Model):
    name=models.CharField(max_length=150)
    year=models.IntegerField()
    photo=models.ImageField(upload_to='photo/%Y/%m/%d/',null=True, blank=True)
    genre=models.CharField(max_length=50)
    actor=models.ManyToManyField('Actor')

    def __str__(self):
        return self.name


class Actor(models.Model):
    name=models.CharField(max_length=150)
    birthdate=models.DateField()

    def __str__(self):
        return self.name

class CommitMovie(models.Model):
    title=models.CharField(max_length=50)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    create_ed=models.DateField(auto_now_add=True)
    update_ed=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.create_ed}-{self.update_ed}"

