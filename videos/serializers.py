from rest_framework import serializers
from .models import Video
import re

youtube_link = re.compile(r'^https://\w{0,3}.?youtube+\.\w{2,3}/watch\?v=([\w-]{11})')


class VideoCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        exclude = ['youtube_image']

    def validate_url(self, url):
        if not youtube_link.fullmatch(url):
            raise serializers.ValidationError('O Link informado não é de um vídeo do Youtube')
        return url

    def create(self, validated_data):
        video = Video(**validated_data)
        match = youtube_link.findall(validated_data['url'])
        if match:
            yt_id = match[0]
            video.youtube_image = f'http://i1.ytimg.com/vi/{yt_id}/0.jpg'
        video.save()
        return video


class VideoViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'
