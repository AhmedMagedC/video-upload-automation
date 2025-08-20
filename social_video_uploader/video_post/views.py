from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import VideoPost
from .serializers import VideoPostSerializer
from .tasks import process_video_task

class VideoPostViewSet(viewsets.ModelViewSet):
    queryset = VideoPost.objects.all()
    serializer_class = VideoPostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        video_post = serializer.save(upload_status="pending")
        
        process_video_task.delay(video_post.id)

        return Response(
            self.get_serializer(video_post).data,
            status=status.HTTP_201_CREATED,
        )
