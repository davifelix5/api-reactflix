from rest_framework import serializers
from .models import Category
from videos.serializers import VideoViewSerializer


class CategoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ['priority']

    def create(self, validated_data):
        category = Category(**validated_data)
        category.priority = Category.objects.all().count() + 1
        category.save()
        return category


class CategoryUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ['id']

    def validate_priority(self, priority):
        count = Category.objects.all().count()
        if priority and priority > count:
                raise serializers.ValidationError('Prioridade inválida')
        return priority

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance


class CategoryViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CategoryWithVideosSerializer(serializers.ModelSerializer):
    videos = VideoViewSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
