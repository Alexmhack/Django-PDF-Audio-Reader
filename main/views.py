import os

from django.views.generic import CreateView, DetailView
from django.http import HttpResponseRedirect
from django.core.files import File

from .models import PDFAudio
from .utils import convert_pdf_to_audio


class CreatePDFView(CreateView):
    model = PDFAudio
    fields = ('pdf', 'audio_rate', 'volume_level',
        'audio_voice')

    def form_valid(self, form):
        # access inmemory file using - form.cleaned_data.get('file').read() / .file.getvalue()
        # tensorflow needs a path to file, create a temp file and use its path
        self.object = form.save()
        file_path, text = convert_pdf_to_audio(self.object)
        self.object.text = text.strip()
        with open(file_path, 'rb') as fi:
            self.object.audio_file = File(fi, name=os.path.basename(fi.name))
            self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class PDFDetailView(DetailView):
    model = PDFAudio
    queryset = PDFAudio.objects.all()
