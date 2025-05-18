from django.contrib import admin
from django.utils.translation import gettext as _
from .models import Scout, SocialMediaProfile


@admin.register(Scout)
class ScoutAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'first_name',
        'last_name',
        'phone_number',
        'country',
        'state',
    ]
    search_fields = [
        'user__email', 'first_name', 'last_name', 'phone_number',
    ]
    readonly_fields = ['created_at', 'updated_at']
    ordering = ('-created_at',)

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'user',
                    'first_name',
                    'last_name',
                    'phone_number',
                    'photo',
                    'website',
                    'organization',
                    'bio',
                )
            }
        ),
        (
            _('Address Information'),
            {
                'fields': (
                    'address',
                    'country',
                    'city',
                    'state',
                )
            }
        ),
        (
            _('Timestamps'),
            {
                'fields': (
                    'created_at',
                    'updated_at',
                )
            }
        ),
    )


@admin.register(SocialMediaProfile)
class SocialMedisProfileAdmin(admin.ModelAdmin):
    list_display = (
        'scout',
        'name',
        'link',
    )
    search_fields = [
        'scout__user__email', 'name', 'link',
    ]
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        (
            _('Scout'),
            {
                'fields': (
                    'scout',
                )
            }
        ),
        (
            _('Social Media Profile'),
            {
                'fields': (
                    'name',
                    'link',
                )
            }
        ),
        (
            _('Timestamps'),
            {
                'fields': (
                    'created_at',
                    'updated_at',
                )
            }
        ),
    )

