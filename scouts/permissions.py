from rest_framework.permissions import BasePermission


class IsScoutProfileOrReadOnly(BasePermission):
    message = "You must be a the owner of this profile to perform this action."

    def has_object_permission(self, request, view, obj):
        return request.method in ['GET', 'HEAD', 'OPTIONS'] or (
            request.user.role == 'scout' and request.user == obj.user
        )
