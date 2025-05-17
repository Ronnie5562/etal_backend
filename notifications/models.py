from django.db import models
from .choices import (
    NOTIFICATION_TYPES
)
from django.contrib.auth import get_user_model


User = get_user_model()


class Notification(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_notifications'
    )
    title = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    type = models.CharField(
        max_length=20,
        choices=NOTIFICATION_TYPES
    )
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.title}"

    class Meta:
        ordering = ('-timestamp',)
