from celery import shared_task
from .models import VideoPost
from .services import process_video_post

@shared_task
def process_video_task(video_post_id):
    post = VideoPost.objects.get(id=video_post_id)
    process_video_post(post)

@shared_task
def retry_failed_uploads():
    failed_posts = VideoPost.objects.filter(upload_status="failed")
    for post in failed_posts:
        process_video_post(post)
