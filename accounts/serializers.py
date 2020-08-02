from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(min_length=8, write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(min_length=8, write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        if not password == password2:
            raise serializers.ValidationError({'password': 'As senhas não são iguais'})
        data.pop('password2')
        return data

    def create(self, validated_data):
        password = validated_data.get('password')
        validated_data['password'] = make_password(password)
        user = User(**validated_data)
        user.save()
        return user
