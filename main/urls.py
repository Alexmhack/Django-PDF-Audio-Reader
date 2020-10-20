from django.urls import path

from .views import CreatePDFView, PDFDetailView

app_name = 'main'

urlpatterns = [
    path('', CreatePDFView.as_view(), name='create-pdf'),
    path('<int:pk>/details/', PDFDetailView.as_view(), name='pdf-detail')
]
