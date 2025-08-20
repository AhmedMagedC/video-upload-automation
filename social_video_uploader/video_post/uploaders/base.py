from abc import ABC, abstractmethod

class BaseUploader(ABC):
    @abstractmethod
    def upload(self, video_post):
        """
        Simulates uploading a video to a platform.
        Should be overridden by subclasses.
        """
        pass
