from django.db import models


AUDIO_VOICES = (
    (0, 'Male'),
    (1, 'Female')
)


class PDFAudio(models.Model):
    text = models.TextField()
    pdf = models.FileField(upload_to='pdfs')
    audio_rate = models.IntegerField(blank=True, null=True)
    volume_level = models.DecimalField(
        decimal_places=1, max_digits=2,
        blank=True, null=True)
    audio_voice = models.CharField(max_length=1, choices=AUDIO_VOICES,
        default=1)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pdf.name
