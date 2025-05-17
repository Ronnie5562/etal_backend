from django.contrib import admin
from django.utils.translation import gettext as _
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'title', 'type', 'is_read', 'timestamp'
    ]
    search_fields = [
        'user__email', 'title', 'message'
    ]
    readonly_fields = ['timestamp']
    ordering = ('-timestamp',)
    list_filter = ('type', 'is_read')

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'user',
                    'title',
                    'message',
                    'type',
                    'is_read',
                )
            }
        ),
        (
            _('Timestamp'),
            {
                'fields': (
                    'timestamp',
                )
            }
        ),
    )
