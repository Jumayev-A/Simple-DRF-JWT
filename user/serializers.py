from asyncore import read
from imp import source_from_cache
from pyexpat import model
from rest_framework import serializers
from user.models import UserModel
from django.contrib.auth.models import User


class UserModelSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    user_password = serializers.CharField(source='user.password', read_only=True)
    class Meta:
        model = UserModel
        fields = ['id', 'phone', 'user_username', 'user_password']
