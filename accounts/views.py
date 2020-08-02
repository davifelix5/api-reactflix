from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from . import serializers


class RegisterUser(CreateAPIView):
    serializer_class = serializers.RegistrationSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokens = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(tokens, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        refresh_token = str(refresh)
        access_tokes = str(refresh.access_token)
        return {'access': access_tokes, 'refresh': refresh_token}
