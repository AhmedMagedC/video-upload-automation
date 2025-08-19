from django.contrib import admin
from .models import VideoPost

@admin.register(VideoPost)
class VideoPostAdmin(admin.ModelAdmin):
    list_display = ("title", "upload_status", "created_at", "platforms")
    list_filter = ("upload_status", "platforms")
    search_fields = ("title", "description")
    readonly_fields = ("upload_status", "created_at")
