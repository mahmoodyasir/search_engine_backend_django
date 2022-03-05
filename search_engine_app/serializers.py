from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
from rest_framework.authtoken.models import Token


class EveryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EveryData
        fields = "__all__"


class SearchRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchRecord
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')
        extra_kwargs = {"password": {"write_only": True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')
        extra_kwargs = {"password": {"write_only": True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_superuser(**validated_data)
        Token.objects.create(user=user)
        return user

