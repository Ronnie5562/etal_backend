from django.contrib import admin
from django.utils.translation import gettext as _
from .models import Athlete, SocialMediaProfile


@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
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
                    'age',
                    'school',
                    'first_name',
                    'last_name',
                    'phone_number',
                    'photo',
                    'website',
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
        'athlete',
        'name',
        'link',
    )
    search_fields = [
        'athlete__user__email', 'name', 'link',
    ]
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        (
            _('Athlete'),
            {
                'fields': (
                    'athlete',
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

