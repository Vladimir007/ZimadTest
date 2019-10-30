from rest_framework import serializers, fields

from users.models import User


class UserSerialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'parent_name',
            'image_origin', 'image_compressed', 'date_joined'
        )
