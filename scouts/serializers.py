from rest_framework import serializers
from .models import Scout


class ScoutListSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Scout
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'country',
            'website',
            'photo',
            'organization',
        ]

        read_only_fields = [
            'id',
            'email',
        ]


class ScoutDetailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
    social_media_profiles = serializers.SerializerMethodField()

    class Meta:
        model = Scout
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'website',
            'photo',
            'address',
            'country',
            'state',
            'city',
            'social_media_profiles',
            'bio',
            'organization',
        ]

        read_only_fields = [
            'id',
            'user',
            'created_at',
            'updated_at'
        ]

    def get_social_media_profiles(self, obj):
        return obj.social_media_profiles.values('name', 'link')
