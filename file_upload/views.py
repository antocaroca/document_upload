from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView

from .forms import DocumentForm
from .models import Document


class HomeView(TemplateView):
    template_name = "home.html"

class DocumentListView(ListView):
    model = Document
    template_name = "document_list.html"
    context_object_name= 'docs'

class DocumentCreateView(CreateView):
    model = Document
    template_name = "document_new.html"
    form_class = DocumentForm
    success_url = reverse_lazy('document_list')

class DocumentDeleteView(DeleteView):
    model = Document
    template_name = "delete_document.html"
    success_url = reverse_lazy('document_list')
