from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'id', 'user', 'title', 'message', 'type',
            'is_read', 'timestamp'
        ]
        read_only_fields = ['user', 'timestamp']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['type'] = instance.get_type_display()  # Show human-readable type
        return ret
