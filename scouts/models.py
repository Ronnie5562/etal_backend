from django.db import models
from profiles.models import Profile
from django.contrib.auth import get_user_model


User = get_user_model()


class Scout(Profile):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="scout_profile"
    )
    organization = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'scout'
        verbose_name_plural = 'scouts'


class SocialMediaProfile(models.Model):
    scout = models.ForeignKey(
        Scout,
        on_delete=models.CASCADE,
        related_name="social_media_profiles"
    )
    name = models.CharField(max_length=255)
    link = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
