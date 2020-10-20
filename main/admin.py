from django.contrib import admin

from .models import PDFAudio


@admin.register(PDFAudio)
class PDFAudioAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'get_text', 'pdf', 'audio_rate', 'volume_level',
        'audio_voice',)
    list_filter = ('timestamp', 'audio_rate', 'audio_voice',
        'volume_level')

    def get_text(self, obj):
        return obj.text[:30]

    get_text.short_description = 'Text'
