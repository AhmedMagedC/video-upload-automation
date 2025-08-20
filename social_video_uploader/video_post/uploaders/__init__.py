from .youtube import YouTubeUploader
from .vimeo import VimeoUploader
from .dailymotion import DailymotionUploader

UPLOADERS = {
    "youtube": YouTubeUploader(),
    "vimeo": VimeoUploader(),
    "dailymotion": DailymotionUploader(),
}
