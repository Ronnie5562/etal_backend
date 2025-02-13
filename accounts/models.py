import uuid
from django.db import models
from accounts.choices import USER_ROLES
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from cloudinary.models import CloudinaryField
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):
    """
    Custom UserManager model that manages Accounts
    """
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(f'Input a valid Email: {email} is not valid')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.role = 'admin'
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        # Create Admin profile
        AdminProfile.objects.create(user=user)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model.
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    email = models.EmailField(
        max_length=255, unique=True, validators=[validate_email])
    role = models.CharField(
        max_length=50, choices=USER_ROLES, default='athlete')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        try:
            self.full_clean()
        except Exception as e:
            raise e

        super(User, self).save(*args, **kwargs)

    @property
    def profile(self):
        profile_attr = f"{self.role}_profile"
        return getattr(self, profile_attr, None)

    def __str__(self):
        """String representation of a user"""
        return f"{self.email} - {self.role}"

    class Meta:
        ordering = ("-date_joined",)


class AdminProfile(models.Model):
    # User information
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        related_name='admin_profile'
    )
    name = models.CharField(
        max_length=255,
        blank=True,
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
    )
    photo = CloudinaryField(
        'photo',
        blank=True,
        null=True,
        folder="users/profile/photos/",
    )

    class Meta:
        verbose_name_plural = "Admin Profiles"
