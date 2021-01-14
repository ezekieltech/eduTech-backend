from django.utils import timezone
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django.dispatch import receiver
from django.db.models.signals import post_save

from profiles.models import MentorProfile, MenteeProfile, EduconsultantProfile

# Create your models here.

MENTOR = 'Mentor'
MENTEE = 'Mentee'
EDUCONSULTANT = 'Edu-Consultant'

ROLES = [
    (MENTOR, 'Mentor'),
    (MENTEE, 'Mentee'),
    (EDUCONSULTANT, 'Edu-Consultant')
    ]

class CustomUserManager (BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email account")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            email = self.normalize_email(email),
            username = username, 
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password 
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email           = models.EmailField(verbose_name="email", max_length=60,unique=True)
    username        = models.CharField(max_length=30, unique=True)
    role            = models.CharField(max_length=20,  choices=ROLES, default=MENTEE)
    date_joined     = models.DateTimeField(verbose_name="date joined", default=timezone.now)
    last_login      = models.DateTimeField(verbose_name="last login", default=timezone.now)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD = "email"  # i want you to log in with email
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """A signal that creates either mentor or mentee or
    educonsultant profile depending on theinstance.role value

    Arguments:
        sender {cls} -- The model that send the signal
        instance {obj} -- instance of the custom user model
        created {bol} -- returns true if custom user is created
    """

    if created and instance.role == "Mentors":
        MentorsProfile.objects.create(user=instance)
    elif created and instance.role == "Mentee":
        MenteeProfile.objects.create(user=instance)
    elif created and instance.role == "Edu-Consultant":
        EduconsultantProfile.objects.create(user=instance)
