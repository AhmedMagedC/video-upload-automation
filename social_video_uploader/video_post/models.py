from django.db import models
from multiselectfield import MultiSelectField

class VideoPost(models.Model):
    PLATFORM_CHOICES = [
        ('youtube', 'YouTube'),
        ('vimeo', 'Vimeo'),
        ('dailymotion', 'Dailymotion'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    platforms = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    upload_status = models.CharField(max_length=10, choices=[
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
