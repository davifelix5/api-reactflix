from rest_framework import generics
from . import serializers
from videos.serializers import VideoViewSerializer
from .models import Category
from videos.models import Video
from rest_framework.response import Response


class ListCreateCategories(generics.ListCreateAPIView):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.CategoryViewSerializer
        else:
            return serializers.CategoryCreateSerializer


class ListCategoriesWithVideos(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryWithVideosSerializer


class RetrieveUpdateDestroyCategories(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.request.method in ('PATCH', 'PUT'):
            return serializers.CategoryUpdateSerializer
        else:
            return serializers.CategoryViewSerializer


class ListCategorieVideos(generics.GenericAPIView):
    queryset = Category.objects.all()

    def get(self, request, pk):
        videos = Video.objects.filter(category__id=pk)
        if not videos:
            return Response({'message': 'Vídeos não encontados'})
        serializer = VideoViewSerializer(videos, many=True)
        return Response(serializer.data, status=200)
