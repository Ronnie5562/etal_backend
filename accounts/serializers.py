# from typing import Optional
from django.conf import settings
from .choices import USER_ROLES
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer
)
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the user object
    """
    role = serializers.ChoiceField(choices=(
        # ('admin', 'Admin'),
        ('scout', 'Scout'),
        ('athlete', 'Athlete'),
    ))

    class Meta:
        model = get_user_model()
        exclude = (
            'groups',
            'is_staff',
            'is_active',
            'last_login',
            'is_superuser',
            'date_modified',
            'user_permissions',
        )
        required_fields = [
            'email', 'password', 'role',
        ]
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5},
        }

    def create(self, validated_data):
        """
        Create a user with encrypted password and returns the user instance
        """
        return get_user_model().objects.create_user(
            **validated_data, is_active=False
        )

    def update(self, instance, validated_data):
        """
        Update a user, setting the password correctly and return it
        """
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom serializer to include role-based validation for login
    and additional fields in the token response.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["role"] = serializers.CharField(write_only=True)
        self.fields["photo"] = serializers.CharField(read_only=True)
        self.fields["name"] = serializers.CharField(read_only=True)
        self.fields["email"] = serializers.CharField()

    def validate(self, attrs):
        input_role = attrs.pop("role", None)
        if not input_role:
            raise ValidationError({"role": "This field is required."})

        # Check if the user's account is active
        user_ = User.objects.filter(email=attrs["email"]).first()

        if not user_:
            raise ValidationError(
                {
                    "email": "User with this email does not exist.",
                    "code": "user_not_found"
                }
            )

        if not user_.is_active:
            raise ValidationError(
                {
                    "email": "Your account is not activated. You need to verify your email.",
                    "code": "account_not_activated"
                },
            )

        if not user_.check_password(attrs["password"]):
            raise ValidationError(
                {
                    "password": "Incorrect password.",
                    "code": "incorrect_password"
                }
            )

        # Validate email and password
        data = super().validate(attrs)

        if input_role not in list(zip(*USER_ROLES))[0]:
            raise ValidationError(
                {"role": f"{input_role} is an Invalid role."}
            )

        # Check if the user's role matches the provided role
        if self.user.role != input_role:
            raise ValidationError(
                {
                    "role": f"{self.user.role} cannot login on the {input_role} portal."
                }
            )

        if hasattr(self.user, "profile") and self.user.profile.photo:
            data["photo"] = self.user.profile.photo.url
        else:
            data["photo"] = ""

        data["email"] = self.user.email
        data["name"] = self.user.profile.name or self.user.email.split("@")[0]
        data["user_id"] = self.user.id
        data["role"] = self.user.role
        data["profile_id"] = self.user.profile.id
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["role"] = user.role
        return token


class JWTCookieTokenRefreshSerializer(TokenRefreshSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["refresh"] = serializers.CharField(write_only=True)

    refresh = None

    def validate(self, attrs):
        attrs["refresh"] = self.context["request"].COOKIES.get(
            settings.SIMPLE_JWT["REFRESH_TOKEN_NAME"])

        if attrs["refresh"]:
            return super().validate(attrs)
        else:
            raise InvalidToken("No valid refresh token found")


class AccountActivationSerializer(serializers.Serializer):
    pass


class LogOutSerializer(serializers.Serializer):
    pass
