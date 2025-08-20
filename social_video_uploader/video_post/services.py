import threading
from .uploaders import UPLOADERS

def process_video_post(video_post):
    def _task():
        platform = video_post.platforms.lower()
        uploader = UPLOADERS.get(platform)

        if uploader:
            success = uploader.upload(video_post)
            video_post.upload_status = "success" if success else "failed"
        else:
            video_post.upload_status = "failed"

        video_post.save(update_fields=["upload_status"])

    # run in background
    threading.Thread(target=_task, daemon=True).start()
