import time
from .base import BaseUploader

class VimeoUploader(BaseUploader):
    def upload(self, video_post):
        # Simulate upload delay
        time.sleep(2)
        # Return success
        return True
