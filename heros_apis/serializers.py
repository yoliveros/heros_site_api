from rest_framework import serializers
from heros_apis.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "user_name", "password", "is_admin"]
