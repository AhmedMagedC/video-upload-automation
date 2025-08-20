from rest_framework import serializers
from .models import VideoPost

class VideoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPost
        fields = ["id", "title", "description", "platforms", "video_file", "upload_status", "created_at"]
        read_only_fields = ["upload_status", "created_at"]
