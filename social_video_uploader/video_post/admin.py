from django.contrib import admin
from .models import VideoPost
from .tasks import process_video_task

@admin.register(VideoPost)
class VideoPostAdmin(admin.ModelAdmin):
    list_display = ("title", "upload_status", "created_at", "platforms")
    list_filter = ("upload_status", "platforms")
    search_fields = ("title", "description")
    readonly_fields = ("upload_status", "created_at")

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        process_video_task.delay(obj.id)