import uuid
from django.db import models
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    # User information
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    first_name = models.CharField(
        max_length=255,
        blank=True,
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
    )
    website = models.URLField(
        blank=True,
        null=True
    )

    photo = CloudinaryField(
        'photo',
        blank=True,
        null=True,
        folder="users/profile/photos/",
    )

    bio = models.TextField(
        blank=True,
        null=True
    )

    # Address information
    address = models.CharField(
        max_length=255,
        blank=True,
    )
    country = models.CharField(
        max_length=100,
        help_text='Country'
    )
    city = models.CharField(
        max_length=100,
        blank=True,
        help_text='City or Town'
    )
    state = models.CharField(
        max_length=100,
        help_text='State or Province'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

