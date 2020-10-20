from django.conf import settings

import PyPDF2
import pyttsx3

from uuid import uuid4


def extract_text(filename):
    """
    function to extract text from pdf at given filename
    """
    pdfFileObj = open(filename, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    mytext = ""

    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        mytext += pageObj.extractText()

    pdfFileObj.close()

    return mytext


def store_audio_file(filepath, text):
    """
    function to invoke TTS engine to speak the pdf text
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('voice', 'en+m7')
    engine.save_to_file(text, filepath)
    # engine.say(text)
    engine.runAndWait()
    engine.stop()
    # return filepath


def convert_pdf_to_audio(instance):
    text = extract_text(instance.pdf.path)
    import os
    filepath = os.path.join(settings.BASE_DIR, f'media/recs/{uuid4()}.wav')
    store_audio_file(filepath, text)
    return filepath, text
