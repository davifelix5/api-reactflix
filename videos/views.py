from rest_framework import generics
from . import serializers
from .models import Video


class ListCreateVideos(generics.ListCreateAPIView):
    serializer_class = serializers.VideoCreateUpdateSerializer
    queryset = Video.objects.all()


class RetrieveUpdateDeleteVideos(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()

    def get_serializer_class(self):
        if self.request.method in ('PATCH', 'PUT'):
            return serializers.VideoCreateUpdateSerializer
        else:
            return serializers.VideoViewSerializer